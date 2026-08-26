#!/usr/bin/env python3
"""
SecureCoding101 CLI — Secure coding lessons from the command line.

Usage:
    python cli.py lessons
    python cli.py lessons --category injection
    python cli.py lesson sql_injection
    python cli.py quiz sql_injection
    python cli.py quiz sql_injection --answer 1
    python cli.py check sql_injection --code "cursor.execute(query, (username,))"
    python cli.py progress
    python cli.py categories
"""

import argparse
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from course import SecureCoding


sc = SecureCoding()


def cmd_lessons(args):
    """List all lessons."""
    if args.category:
        lessons = sc.get_lessons_by_category(args.category)
        label = args.category
    elif args.difficulty:
        lessons = sc.get_lessons_by_difficulty(args.difficulty)
        label = args.difficulty
    else:
        lessons = sc.lessons
        label = "all"

    print(f"\n📚 Lessons ({label}) — {len(lessons)}\n{'='*60}")
    print(f"{'ID':<25} {'Title':<30} {'Lang':<10} {'Diff':<12} {'Pts'}")
    print("-" * 80)

    diff_icons = {"beginner": "🟢", "intermediate": "🟡", "advanced": "🔴"}
    for l in lessons:
        icon = diff_icons.get(l.difficulty, "⚪")
        done = "✅" if l.id in sc.completed else "  "
        print(f"{l.id:<25} {done} {l.title:<28} {l.language:<10} {icon} {l.difficulty:<10} {l.points}")


def cmd_lesson(args):
    """Show a lesson."""
    lesson = sc.get_lesson(args.id)
    if not lesson:
        print(f"\n❌ Lesson not found: {args.id}")
        return

    diff_icons = {"beginner": "🟢", "intermediate": "🟡", "advanced": "🔴"}
    icon = diff_icons.get(lesson.difficulty, "⚪")

    print(f"\n📖 {lesson.title}\n{'='*60}")
    print(f"  ID:         {lesson.id}")
    print(f"  Language:   {lesson.language}")
    print(f"  Category:   {lesson.category}")
    print(f"  Difficulty: {icon} {lesson.difficulty}")
    print(f"  Points:     {lesson.points}")
    print(f"  Status:     {'✅ Completed' if lesson.id in sc.completed else '⬜ Not completed'}")

    print(f"\n  📝 Description:")
    print(f"  {lesson.description}")

    print(f"\n  🔴 Vulnerable Code:")
    print(f"  {'-'*40}")
    for line in lesson.vulnerable_code.split("\n"):
        print(f"  {line}")

    print(f"\n  🟢 Secure Code:")
    print(f"  {'-'*40}")
    for line in lesson.secure_code.split("\n"):
        print(f"  {line}")

    print(f"\n  💡 Explanation:")
    print(f"  {lesson.explanation}")

    if lesson.key_points:
        print(f"\n  🎯 Key Points:")
        for point in lesson.key_points:
            print(f"    • {point}")

    if lesson.references:
        print(f"\n  📚 References:")
        for ref in lesson.references:
            print(f"    • {ref}")


def cmd_quiz(args):
    """Take a quiz."""
    quiz = sc.get_quiz(args.id)
    if not quiz:
        print(f"\n❌ No quiz available for: {args.id}")
        return

    if args.answer is not None:
        result = sc.answer_quiz(quiz.id, args.answer)
        if "error" in result:
            print(f"\n❌ {result['error']}")
            return

        icon = "✅" if result["correct"] else "❌"
        print(f"\n{icon} Quiz Result\n{'='*40}")
        print(f"  Question: {quiz.question}")
        print(f"  Your answer: {quiz.options[args.answer]}")
        print(f"  Correct: {result['correct_answer']}")
        print(f"  Explanation: {result['explanation']}")
    else:
        print(f"\n❓ Quiz: {quiz.question}\n{'='*40}")
        for i, option in enumerate(quiz.options):
            print(f"  {i}. {option}")
        print(f"\n  Usage: python cli.py quiz {args.id} --answer <0-3>")


def cmd_check(args):
    """Check if code is secure."""
    result = sc.check_fix(args.id, args.code)

    if "error" in result:
        print(f"\n❌ {result['error']}")
        return

    if result["is_secure"]:
        print(f"\n✅ Code is SECURE!")
        print(f"  +{result['points']} points earned!")
    else:
        print(f"\n❌ Code has vulnerabilities:")
        for issue in result["issues"]:
            print(f"    ⚠️  {issue}")

    print(f"\n  💡 {result['explanation']}")


def cmd_progress(args):
    """Show progress."""
    progress = sc.get_progress()

    bar_len = 20
    filled = int(progress["percentage"] / 100 * bar_len)
    bar = "█" * filled + "░" * (bar_len - filled)

    print(f"\n📊 Course Progress\n{'='*40}")
    print(f"  Lessons:   {bar} {progress['completed']}/{progress['total']} ({progress['percentage']:.0f}%)")
    print(f"  Points:    {progress['points']}/{progress['max_points']}")
    print(f"  Quizzes:   {progress['quizzes_passed']}/{progress['quizzes_taken']} passed")


def cmd_categories(args):
    """List categories."""
    cats = sc.get_categories()

    print(f"\n📁 Categories\n{'='*30}")
    for cat, count in sorted(cats.items()):
        print(f"  • {cat:<20} {count} lessons")


def main():
    parser = argparse.ArgumentParser(
        description="📚 SecureCoding101 — Secure Coding Course"
    )
    sub = parser.add_subparsers(dest="command")

    # lessons
    lessons_p = sub.add_parser("lessons", help="List lessons")
    lessons_p.add_argument("--category", "-c", default="")
    lessons_p.add_argument("--difficulty", "-d", default="")

    # lesson
    lesson_p = sub.add_parser("lesson", help="Show lesson")
    lesson_p.add_argument("id")

    # quiz
    quiz_p = sub.add_parser("quiz", help="Take quiz")
    quiz_p.add_argument("id")
    quiz_p.add_argument("--answer", "-a", type=int, default=None)

    # check
    check_p = sub.add_parser("check", help="Check code")
    check_p.add_argument("id")
    check_p.add_argument("--code", "-c", required=True)

    # progress
    sub.add_parser("progress", help="Show progress")

    # categories
    sub.add_parser("categories", help="List categories")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    commands = {
        "lessons": cmd_lessons, "lesson": cmd_lesson, "quiz": cmd_quiz,
        "check": cmd_check, "progress": cmd_progress, "categories": cmd_categories,
    }
    commands[args.command](args)


if __name__ == "__main__":
    main()
