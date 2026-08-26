#!/usr/bin/env python3
"""
LLMFuzz CLI — Automated LLM Prompt Fuzzing Toolkit

Usage:
    python cli.py fuzz --target "You are helpful" --iterations 100
    python cli.py fuzz --target "You are helpful" --strategy homoglyph_swap
    python cli.py mutate --prompt "test prompt" --strategy hybrid --count 5
    python cli.py strategies
    python cli.py stats --results results.json
    python cli.py report --results results.json
"""

import argparse
import json
import sys
import time
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.fuzzer import Mutator, Fuzzer, FuzzResults


def cmd_fuzz(args):
    """Run the fuzzer against a target prompt."""
    mutator = Mutator(strategy=args.strategy, seed=args.seed)
    fuzzer = Fuzzer(
        target=args.target,
        mutator=mutator,
        max_iterations=args.iterations,
        mutations_per_seed=args.mutations,
    )

    print(f"🛡️  LLMFuzz — Automated Prompt Fuzzing")
    print(f"   Target: {args.target[:60]}...")
    print(f"   Strategy: {args.strategy}")
    print(f"   Iterations: {args.iterations}")
    print(f"   Mutations/seed: {args.mutations}")
    print(f"   Seed: {args.seed or 'random'}")
    print()

    start = time.time()
    results = fuzzer.run()
    elapsed = time.time() - start

    # Summary
    summary = results.summary()
    print(f"{'='*60}")
    print(f"📊 RESULTS")
    print(f"{'='*60}")
    print(f"   Total iterations:  {summary['total_iterations']}")
    print(f"   Interesting finds:  {summary['interesting_findings']}")
    print(f"   Crash rate:        {summary['crash_rate']}")
    print(f"   Time elapsed:      {elapsed:.2f}s")
    print()

    # Show interesting findings
    if results.crashes:
        print(f"🚨 INTERESTING FINDINGS ({len(results.crashes)}):")
        print(f"{'-'*60}")
        for i, crash in enumerate(results.crashes[:10], 1):
            print(f"  [{i}] Iteration #{crash.iteration}")
            print(f"      Mutations: {', '.join(m.strategy for m in crash.mutations)}")
            print(f"      Prompt: {crash.mutations[0].mutated[:80] if crash.mutations else 'N/A'}...")
            print(f"      Response: {crash.response[:100]}")
            print()
    else:
        print("✅ No interesting findings detected.")

    # Strategy breakdown
    strat_counts = {}
    for r in results.results:
        for m in r.mutations:
            strat_counts[m.strategy] = strat_counts.get(m.strategy, 0) + 1

    if strat_counts:
        print(f"📈 STRATEGY USAGE:")
        for strat, count in sorted(strat_counts.items(), key=lambda x: -x[1]):
            print(f"   {strat:25s} {count:4d}")

    # Export
    if args.output:
        export = {
            "summary": summary,
            "elapsed_seconds": elapsed,
            "config": {
                "target": args.target,
                "strategy": args.strategy,
                "iterations": args.iterations,
                "seed": args.seed,
            },
            "findings": [c.to_dict() for c in results.crashes],
            "strategy_usage": strat_counts,
        }
        with open(args.output, 'w') as f:
            json.dump(export, f, indent=2, ensure_ascii=False)
        print(f"\n📁 Results exported to {args.output}")


def cmd_mutate(args):
    """Apply mutations to a prompt."""
    mutator = Mutator(strategy=args.strategy, seed=args.seed)

    print(f"🔬 LLMFuzz — Prompt Mutation")
    print(f"   Original: {args.prompt}")
    print(f"   Strategy: {args.strategy}")
    print(f"   Count: {args.count}")
    print()

    for i in range(args.count):
        mutated, mutations = mutator.mutate(args.prompt, args.num_mutations)
        strats = ', '.join(m.strategy for m in mutations)
        print(f"  [{i+1}] {mutated}")
        print(f"      Strategies: {strats}")
        print()


def cmd_strategies(args):
    """List all available mutation strategies."""
    m = Mutator()

    print(f"🔬 LLMFuzz — Mutation Strategies ({len(m.STRATEGIES)} total)")
    print(f"{'='*60}")

    categories = {
        "Character-level": ["char_insert", "char_delete", "char_replace", "case_flip"],
        "Word-level": ["word_insert", "word_delete", "word_replace", "repeat_phrase"],
        "Whitespace/Unicode": ["whitespace_inject", "unicode_inject", "null_bytes",
                               "zero_width_inject", "rtl_override", "homoglyph_swap"],
        "Encoding": ["base64_wrap", "reverse_string", "escape_chars"],
        "Structural": ["nest_parens", "format_overflow", "delimiter_confusion",
                       "recursive_wrap"],
        "Injection": ["tag_inject", "instruction_premble", "token_boundary"],
        "Advanced": ["polyglot_payload", "entropy_bomb", "multi_language"],
    }

    for cat, strats in categories.items():
        print(f"\n  📦 {cat}:")
        for s in strats:
            print(f"     • {s}")

    print(f"\n  💡 Use --strategy hybrid to mix all strategies randomly.")


def cmd_report(args):
    """Generate a report from results."""
    if not os.path.exists(args.results):
        print(f"❌ Results file not found: {args.results}")
        return

    with open(args.results) as f:
        data = json.load(f)

    summary = data.get("summary", {})
    findings = data.get("findings", [])
    config = data.get("config", {})
    strat_usage = data.get("strategy_usage", {})

    print(f"{'='*60}")
    print(f"📋 LLMFUZZ REPORT")
    print(f"{'='*60}")
    print(f"  Target:        {config.get('target', 'N/A')[:60]}")
    print(f"  Strategy:      {config.get('strategy', 'N/A')}")
    print(f"  Iterations:    {summary.get('total_iterations', 0)}")
    print(f"  Findings:      {summary.get('interesting_findings', 0)}")
    print(f"  Crash Rate:    {summary.get('crash_rate', '0%')}")
    print()

    if findings:
        print(f"🚨 TOP FINDINGS:")
        for i, f in enumerate(findings[:5], 1):
            print(f"  {i}. {f.get('response', 'N/A')[:80]}")
            if f.get('mutations'):
                print(f"     Mutation: {f['mutations'][0].get('strategy', 'N/A')}")
        print()

    if strat_usage:
        print(f"📈 STRATEGY EFFECTIVENESS:")
        for strat, count in sorted(strat_usage.items(), key=lambda x: -x[1])[:10]:
            bar = "█" * min(count, 30)
            print(f"   {strat:25s} {bar} ({count})")


def cmd_stats(args):
    """Show statistics from results."""
    if not os.path.exists(args.results):
        print(f"❌ Results file not found: {args.results}")
        return

    with open(args.results) as f:
        data = json.load(f)

    findings = data.get("findings", [])
    strat_usage = data.get("strategy_usage", {})
    summary = data.get("summary", {})

    print(f"📊 LLMFUZZ STATISTICS")
    print(f"{'='*60}")
    print(f"  Total iterations:  {summary.get('total_iterations', 0)}")
    print(f"  Interesting finds:  {summary.get('interesting_findings', 0)}")
    print(f"  Crash rate:        {summary.get('crash_rate', '0%')}")
    print()

    # Severity breakdown
    sev_counts = {"critical": 0, "high": 0, "medium": 0, "low": 0}
    for f in findings:
        resp = f.get("response", "").lower()
        if any(w in resp for w in ["system prompt", "admin", "root"]):
            sev_counts["critical"] += 1
        elif any(w in resp for w in ["override", "bypass", "debug"]):
            sev_counts["high"] += 1
        else:
            sev_counts["medium"] += 1

    print(f"  SEVERITY BREAKDOWN:")
    for sev, count in sev_counts.items():
        bar = "█" * count
        print(f"   {sev:10s} {bar} ({count})")

    # Strategy effectiveness
    if strat_usage:
        print(f"\n  STRATEGY EFFECTIVENESS:")
        total = sum(strat_usage.values())
        for strat, count in sorted(strat_usage.items(), key=lambda x: -x[1]):
            pct = (count / total * 100) if total > 0 else 0
            bar = "█" * int(pct)
            print(f"   {strat:25s} {bar} {pct:.1f}%")


def main():
    parser = argparse.ArgumentParser(
        description="LLMFuzz — Automated LLM Prompt Fuzzing Toolkit",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python cli.py fuzz --target "You are helpful" --iterations 100
  python cli.py mutate --prompt "Hello world" --strategy homoglyph_swap
  python cli.py strategies
  python cli.py report --results results.json
        """
    )
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # fuzz
    p_fuzz = subparsers.add_parser("fuzz", help="Run fuzzer against target")
    p_fuzz.add_argument("--target", "-t", required=True, help="Target system prompt")
    p_fuzz.add_argument("--strategy", "-s", default="hybrid", help="Mutation strategy (default: hybrid)")
    p_fuzz.add_argument("--iterations", "-n", type=int, default=100, help="Max iterations (default: 100)")
    p_fuzz.add_argument("--mutations", "-m", type=int, default=3, help="Mutations per seed (default: 3)")
    p_fuzz.add_argument("--seed", type=int, default=None, help="Random seed for reproducibility")
    p_fuzz.add_argument("--output", "-o", help="Export results to JSON file")

    # mutate
    p_mut = subparsers.add_parser("mutate", help="Apply mutations to a prompt")
    p_mut.add_argument("--prompt", "-p", required=True, help="Prompt to mutate")
    p_mut.add_argument("--strategy", "-s", default="hybrid", help="Mutation strategy")
    p_mut.add_argument("--count", "-c", type=int, default=5, help="Number of mutations to generate")
    p_mut.add_argument("--num-mutations", type=int, default=2, help="Mutations per output")
    p_mut.add_argument("--seed", type=int, default=None, help="Random seed")

    # strategies
    subparsers.add_parser("strategies", help="List all mutation strategies")

    # report
    p_report = subparsers.add_parser("report", help="Generate report from results")
    p_report.add_argument("--results", "-r", required=True, help="Results JSON file")

    # stats
    p_stats = subparsers.add_parser("stats", help="Show statistics from results")
    p_stats.add_argument("--results", "-r", required=True, help="Results JSON file")

    args = parser.parse_args()

    if args.command == "fuzz":
        cmd_fuzz(args)
    elif args.command == "mutate":
        cmd_mutate(args)
    elif args.command == "strategies":
        cmd_strategies(args)
    elif args.command == "report":
        cmd_report(args)
    elif args.command == "stats":
        cmd_stats(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
