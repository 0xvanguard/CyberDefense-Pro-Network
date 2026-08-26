"""Tests for SecureCoding101"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.course import SecureCoding, Lesson, QuizQuestion, LessonCategory


sc = SecureCoding()


def test_lesson_category_enum():
    assert LessonCategory.INJECTION.value == "injection"
    assert LessonCategory.WEB.value == "web"
    assert LessonCategory.AUTH.value == "auth"
    assert len(list(LessonCategory)) == 8
    print("✅ LessonCategory enum OK")


def test_lessons_loaded():
    assert len(sc.lessons) == 12
    print(f"✅ Lessons loaded: {len(sc.lessons)}")


def test_get_lesson():
    lesson = sc.get_lesson("sql_injection")
    assert lesson is not None
    assert lesson.title == "SQL Injection Prevention"
    assert lesson.language == "python"
    print("✅ Get lesson OK")


def test_get_lesson_nonexistent():
    assert sc.get_lesson("nonexistent") is None
    print("✅ Get nonexistent lesson OK")


def test_lessons_by_category():
    injection = sc.get_lessons_by_category("injection")
    assert len(injection) == 2
    assert all(l.category == "injection" for l in injection)
    print(f"✅ By category: {len(injection)} injection lessons")


def test_lessons_by_difficulty():
    beginner = sc.get_lessons_by_difficulty("beginner")
    assert len(beginner) > 0
    assert all(l.difficulty == "beginner" for l in beginner)
    print(f"✅ By difficulty: {len(beginner)} beginner lessons")


def test_lesson_to_dict():
    lesson = sc.get_lesson("xss_prevention")
    d = lesson.to_dict()
    assert d["id"] == "xss_prevention"
    assert "key_points" in d
    print("✅ Lesson to_dict OK")


def test_lesson_has_vulnerable_code():
    lesson = sc.get_lesson("sql_injection")
    assert "SELECT" in lesson.vulnerable_code
    assert "username" in lesson.vulnerable_code
    print("✅ Vulnerable code present OK")


def test_lesson_has_secure_code():
    lesson = sc.get_lesson("sql_injection")
    assert "%s" in lesson.secure_code
    assert "execute" in lesson.secure_code
    print("✅ Secure code present OK")


def test_quizzes_loaded():
    assert len(sc.quizzes) == 5
    print(f"✅ Quizzes loaded: {len(sc.quizzes)}")


def test_get_quiz():
    quiz = sc.get_quiz("sql_injection")
    assert quiz is not None
    assert quiz.question != ""
    assert len(quiz.options) == 4
    print("✅ Get quiz OK")


def test_answer_quiz_correct():
    result = sc.answer_quiz("q1", 1)
    assert result["correct"] is True
    assert "parameterized" in result["explanation"].lower()
    print("✅ Quiz correct answer OK")


def test_answer_quiz_incorrect():
    result = sc.answer_quiz("q1", 0)
    assert result["correct"] is False
    print("✅ Quiz incorrect answer OK")


def test_answer_quiz_nonexistent():
    result = sc.answer_quiz("q999", 0)
    assert "error" in result
    print("✅ Quiz nonexistent OK")


def test_check_fix_secure():
    code = 'query = "SELECT * FROM users WHERE username = %s"\ncursor.execute(query, (username,))'
    result = sc.check_fix("sql_injection", code)
    assert result["is_secure"] is True
    assert result["points"] > 0
    print("✅ Check fix secure OK")


def test_check_fix_insecure():
    code = 'query = "SELECT * FROM users WHERE username = \'" + username + "\'"\ncursor.execute(query)'
    result = sc.check_fix("sql_injection", code)
    assert result["is_secure"] is False
    assert len(result["issues"]) > 0
    print("✅ Check fix insecure OK")


def test_check_xss_secure():
    code = "const div = document.createElement('div');\ndiv.textContent = comment;"
    result = sc.check_fix("xss_prevention", code)
    assert result["is_secure"] is True
    print("✅ Check XSS secure OK")


def test_check_xss_insecure():
    code = "document.getElementById('comments').innerHTML += comment;"
    result = sc.check_fix("xss_prevention", code)
    assert result["is_secure"] is False
    print("✅ Check XSS insecure OK")


def test_check_crypto_insecure():
    code = 'return hashlib.md5(password.encode()).hexdigest()'
    result = sc.check_fix("crypto_basics", code)
    assert result["is_secure"] is False
    print("✅ Check crypto insecure OK")


def test_check_command_injection():
    code = 'os.system(f"ping -c 1 {host}")'
    result = sc.check_fix("command_injection", code)
    assert result["is_secure"] is False
    print("✅ Check command injection OK")


def test_check_pickle_insecure():
    code = 'return pickle.loads(data)'
    result = sc.check_fix("insecure_deserialization", code)
    assert result["is_secure"] is False
    print("✅ Check pickle insecure OK")


def test_check_nonexistent_lesson():
    result = sc.check_fix("nonexistent", "code")
    assert "error" in result
    print("✅ Check nonexistent lesson OK")


def test_progress_initial():
    sc2 = SecureCoding()
    progress = sc2.get_progress()
    assert progress["completed"] == 0
    assert progress["total"] == 12
    assert progress["percentage"] == 0.0
    print("✅ Initial progress OK")


def test_progress_after_completion():
    sc2 = SecureCoding()
    sc2.check_fix("sql_injection", "cursor.execute(query, (username,))")
    progress = sc2.get_progress()
    assert progress["completed"] == 1
    print("✅ Progress after completion OK")


def test_categories():
    cats = sc.get_categories()
    assert "injection" in cats
    assert "web" in cats
    assert "auth" in cats
    assert "crypto" in cats
    print(f"✅ Categories: {list(cats.keys())}")


def test_len():
    assert len(sc) == 12
    print("✅ Len OK")


def test_lesson_key_points():
    lesson = sc.get_lesson("sql_injection")
    assert len(lesson.key_points) > 0
    print("✅ Key points OK")


def test_lesson_references():
    lesson = sc.get_lesson("sql_injection")
    assert len(lesson.references) > 0
    print("✅ References OK")


def test_all_lessons_have_code():
    for lesson in sc.lessons:
        assert lesson.vulnerable_code != ""
        assert lesson.secure_code != ""
    print("✅ All lessons have code OK")


def test_all_lessons_have_explanation():
    for lesson in sc.lessons:
        assert lesson.explanation != ""
    print("✅ All lessons have explanation OK")


def test_quiz_to_dict():
    quiz = sc.quizzes[0]
    d = quiz.to_dict()
    assert "question" in d
    assert "options" in d
    print("✅ Quiz to_dict OK")


if __name__ == "__main__":
    test_lesson_category_enum()
    test_lessons_loaded()
    test_get_lesson()
    test_get_lesson_nonexistent()
    test_lessons_by_category()
    test_lessons_by_difficulty()
    test_lesson_to_dict()
    test_lesson_has_vulnerable_code()
    test_lesson_has_secure_code()
    test_quizzes_loaded()
    test_get_quiz()
    test_answer_quiz_correct()
    test_answer_quiz_incorrect()
    test_answer_quiz_nonexistent()
    test_check_fix_secure()
    test_check_fix_insecure()
    test_check_xss_secure()
    test_check_xss_insecure()
    test_check_crypto_insecure()
    test_check_command_injection()
    test_check_pickle_insecure()
    test_check_nonexistent_lesson()
    test_progress_initial()
    test_progress_after_completion()
    test_categories()
    test_len()
    test_lesson_key_points()
    test_lesson_references()
    test_all_lessons_have_code()
    test_all_lessons_have_explanation()
    test_quiz_to_dict()
    print("\n🎉 All 31 tests passed!")
