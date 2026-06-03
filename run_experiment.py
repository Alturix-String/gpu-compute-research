#!/usr/bin/env python3
"""Main experiment runner."""
from __future__ import annotations

import argparse
import time
from pathlib import Path

from rich.console import Console
from rich.panel import Panel

console = Console()


def main():
    parser = argparse.ArgumentParser(description="gpu-compute-research")
    parser.add_argument("--experiment", choices=["compute_bound", "memory_bound", "all"], default="all")
    parser.add_argument("--output", "-o", default="results")
    args = parser.parse_args()

    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)

    console.print(Panel.fit(
        "[bold white]gpu-compute-research[/bold white]\n"
        f"Experiment: {args.experiment}",
        title="GPU Compute Research",
        border_style="cyan",
    ))

    t_start = time.time()

    if args.experiment in ("compute_bound", "all"):
        console.print("\n[bold]=== Compute-bound ===[/bold]")
        from experiments.compute_bound import run_compute_experiments, print_results, save_results
        r = run_compute_experiments()
        print_results(r)
        save_results(r, output / "compute_results.json")

    if args.experiment in ("memory_bound", "all"):
        console.print("\n[bold]=== Memory-bound ===[/bold]")
        from experiments.memory_bound import run_memory_experiments, print_results as pr, save_results as sr
        r = run_memory_experiments()
        pr(r)
        sr(r, output / "memory_results.json")

    console.print(f"\n[green]Done in {time.time() - t_start:.1f}s[/green]")


if __name__ == "__main__":
    main()
