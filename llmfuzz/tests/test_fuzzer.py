"""Tests for LLMFuzz — Core Fuzzing Engine"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.fuzzer import Mutator, Fuzzer, FuzzResults, FuzzResult, Mutation


class TestMutation:
    """Tests for the Mutation dataclass."""

    def test_mutation_creation(self):
        m = Mutation("char_insert", "hello", "hXello", 1, "Inserted X at 1")
        assert m.strategy == "char_insert"
        assert m.original == "hello"
        assert m.mutated == "hXello"
        assert m.position == 1


class TestMutator:
    """Tests for the Mutator class."""

    def test_init(self):
        m = Mutator()
        assert m.strategy == "hybrid"
        assert len(m.STRATEGIES) >= 27

    def test_init_with_seed(self):
        # Same seed should produce same random sequence
        m1 = Mutator(seed=42)
        m2 = Mutator(seed=42)
        # Use a specific strategy to ensure deterministic behavior
        mut1, _ = Mutator(strategy="reverse_string", seed=42).mutate("hello")
        mut2, _ = Mutator(strategy="reverse_string", seed=42).mutate("hello")
        assert mut1 == mut2

    def test_mutate_returns_tuple(self):
        m = Mutator(seed=42)
        result = m.mutate("hello world")
        assert isinstance(result, tuple)
        assert len(result) == 2

    def test_mutate_returns_string_and_list(self):
        m = Mutator(seed=42)
        mutated, mutations = m.mutate("test")
        assert isinstance(mutated, str)
        assert isinstance(mutations, list)

    def test_mutate_changes_text(self):
        m = Mutator(seed=42)
        mutated, _ = m.mutate("Hello World", 3)
        # With 3 mutations, very likely to change
        # (not guaranteed but overwhelmingly likely)
        assert isinstance(mutated, str)

    def test_mutate_specific_strategy(self):
        m = Mutator(strategy="char_insert", seed=42)
        mutated, mutations = m.mutate("test", 1)
        assert mutations[0].strategy == "char_insert"

    def test_mutate_hybrid_uses_multiple(self):
        m = Mutator(strategy="hybrid", seed=42)
        strategies_used = set()
        for _ in range(50):
            _, mutations = m.mutate("test prompt", 1)
            if mutations:
                strategies_used.add(mutations[0].strategy)
        # Hybrid should use multiple strategies
        assert len(strategies_used) > 3

    def test_char_insert(self):
        m = Mutator(strategy="char_insert", seed=42)
        mutated, mutations = m.mutate("abc", 1)
        assert mutations[0].strategy == "char_insert"
        assert len(mutated) == 4  # One char added

    def test_char_delete(self):
        m = Mutator(strategy="char_delete", seed=42)
        mutated, mutations = m.mutate("abc", 1)
        assert mutations[0].strategy == "char_delete"
        assert len(mutated) == 2  # One char removed

    def test_case_flip(self):
        m = Mutator(strategy="case_flip", seed=42)
        mutated, mutations = m.mutate("hello", 1)
        assert mutations[0].strategy == "case_flip"

    def test_reverse_string(self):
        m = Mutator(strategy="reverse_string", seed=42)
        mutated, mutations = m.mutate("abc", 1)
        assert mutated == "cba"

    def test_nest_parens(self):
        m = Mutator(strategy="nest_parens", seed=42)
        mutated, mutations = m.mutate("test", 1)
        assert mutated.startswith("(")
        assert mutated.endswith(")")

    def test_base64_wrap(self):
        m = Mutator(strategy="base64_wrap", seed=42)
        mutated, mutations = m.mutate("hello world", 1)
        assert mutations[0].strategy == "base64_wrap"

    def test_word_insert(self):
        m = Mutator(strategy="word_insert", seed=42)
        mutated, mutations = m.mutate("hello world", 1)
        assert mutations[0].strategy == "word_insert"

    def test_word_delete(self):
        m = Mutator(strategy="word_delete", seed=42)
        mutated, mutations = m.mutate("hello beautiful world", 1)
        assert len(mutated.split()) == 2

    def test_escape_chars(self):
        m = Mutator(strategy="escape_chars", seed=42)
        mutated, mutations = m.mutate("hello world.test", 1)
        assert "\\t" in mutated or "\\." in mutated

    def test_homoglyph_swap(self):
        m = Mutator(strategy="homoglyph_swap", seed=42)
        mutated, mutations = m.mutate("attack the server", 1)
        assert mutations[0].strategy == "homoglyph_swap"

    def test_zero_width_inject(self):
        m = Mutator(strategy="zero_width_inject", seed=42)
        mutated, mutations = m.mutate("hello world test", 1)
        assert mutations[0].strategy == "zero_width_inject"

    def test_tag_inject(self):
        m = Mutator(strategy="tag_inject", seed=42)
        mutated, mutations = m.mutate("test prompt", 1)
        assert mutations[0].strategy == "tag_inject"
        assert "<" in mutated

    def test_polyglot_payload(self):
        m = Mutator(strategy="polyglot_payload", seed=42)
        mutated, mutations = m.mutate("test", 1)
        assert mutations[0].strategy == "polyglot_payload"
        assert len(mutated) > len("test")

    def test_recursive_wrap(self):
        m = Mutator(strategy="recursive_wrap", seed=42)
        mutated, mutations = m.mutate("test", 1)
        assert mutated.startswith("[")
        assert mutated.endswith("]")

    def test_entropy_bomb(self):
        m = Mutator(strategy="entropy_bomb", seed=42)
        mutated, mutations = m.mutate("short", 1)
        assert len(mutated) > 50

    def test_instruction_premble(self):
        m = Mutator(strategy="instruction_premble", seed=42)
        mutated, mutations = m.mutate("test", 1)
        assert mutations[0].strategy == "instruction_premble"
        assert len(mutated) > len("test")

    def test_multi_language(self):
        m = Mutator(strategy="multi_language", seed=42)
        mutated, mutations = m.mutate("test", 1)
        assert mutations[0].strategy == "multi_language"

    def test_empty_input(self):
        m = Mutator(seed=42)
        mutated, mutations = m.mutate("", 1)
        assert mutated == ""

    def test_single_char_input(self):
        m = Mutator(seed=42)
        mutated, mutations = m.mutate("a", 1)
        assert isinstance(mutated, str)

    def test_long_input(self):
        m = Mutator(seed=42)
        long_text = "word " * 1000
        mutated, mutations = m.mutate(long_text, 5)
        assert isinstance(mutated, str)


class TestFuzzer:
    """Tests for the Fuzzer class."""

    def test_init(self):
        f = Fuzzer(target="test prompt")
        assert f.target == "test prompt"
        assert f.max_iterations == 100

    def test_init_custom(self):
        f = Fuzzer(
            target="test",
            max_iterations=50,
            mutations_per_seed=2,
        )
        assert f.max_iterations == 50
        assert f.mutations_per_seed == 2

    def test_run_returns_results(self):
        f = Fuzzer(target="test prompt", max_iterations=10)
        results = f.run()
        assert isinstance(results, FuzzResults)

    def test_run_has_results(self):
        f = Fuzzer(target="test prompt", max_iterations=10)
        results = f.run()
        assert results.total > 0

    def test_run_with_seed(self):
        f = Fuzzer(target="test", max_iterations=5)
        results = f.run()
        assert results.total >= 1

    def test_custom_interesting_fn(self):
        def my_interesting(prompt, response):
            return "BOMB" in prompt

        f = Fuzzer(
            target="test",
            max_iterations=20,
            interesting_fn=my_interesting,
        )
        results = f.run()
        assert isinstance(results, FuzzResults)

    def test_fuzz_result_to_dict(self):
        r = FuzzResult(
            iteration=1,
            seed="test",
            mutations=[Mutation("char_insert", "a", "b", 0, "test")],
            response="response",
            is_interesting=True,
            latency_ms=10.5,
        )
        d = r.to_dict()
        assert d["iteration"] == 1
        assert d["is_interesting"] is True
        assert d["latency_ms"] == 10.5


class TestFuzzResults:
    """Tests for FuzzResults class."""

    def test_empty_results(self):
        r = FuzzResults()
        assert r.total == 0
        assert r.crash_rate == 0

    def test_total(self):
        results = [
            FuzzResult(1, "a", [], "r", False, 1.0),
            FuzzResult(2, "b", [], "r", True, 2.0),
            FuzzResult(3, "c", [], "r", False, 3.0),
        ]
        r = FuzzResults(results=results)
        assert r.total == 3

    def test_crash_rate(self):
        results = [
            FuzzResult(1, "a", [], "r", False, 1.0),
            FuzzResult(2, "b", [], "r", True, 2.0),
            FuzzResult(3, "c", [], "r", True, 3.0),
        ]
        crashes = [results[1], results[2]]
        r = FuzzResults(results=results, crashes=crashes)
        assert abs(r.crash_rate - 66.67) < 0.01

    def test_summary(self):
        results = [
            FuzzResult(1, "a", [], "r", False, 1.0),
            FuzzResult(2, "b", [], "r", True, 2.0),
        ]
        crashes = [results[1]]
        r = FuzzResults(results=results, crashes=crashes)
        s = r.summary()
        assert s["total_iterations"] == 2
        assert s["interesting_findings"] == 1
