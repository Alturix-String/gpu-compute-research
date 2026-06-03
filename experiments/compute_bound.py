#!/usr/bin/env python3
"""Compute-bound workload experiments."""
from __future__ import annotations

import json
import time
from dataclasses import dataclass, asdict
from pathlib import Path

import numpy as np
from rich.console import Console
from rich.table import Table

console = Console()


@dataclass
class ComputeResult:
    workload: str
    size: int
    time_ms: float
    gflops: float
    mode: str


def run_compute_experiments() -> list[ComputeResult]:
    results = []

    # GEMM
    for size in [256, 512, 1024, 2048]:
        a = np.random.randn(size, size).astype(np.float32)
        b = np.random.randn(size, size).astype(np.float32)
        times = []
        for _ in range(5):
            t0 = time.perf_counter()
            np.dot(a, b)
            times.append(time.perf_counter() - t0)
        avg = np.mean(times)
        gflops = (2 * size**3) / (avg * 1e9)
        results.append(ComputeResult("gemm", size, round(avg*1000, 3), round(gflops, 2), "cpu"))

    # Elementwise
    for size in [1000000, 5000000, 10000000]:
        a = np.random.randn(size).astype(np.float32)
        b = np.random.randn(size).astype(np.float32)
        times = []
        for _ in range(10):
            t0 = time.perf_counter()
            c = np.sqrt(a**2 + b**2)
            times.append(time.perf_counter() - t0)
        avg = np.mean(times)
        gflops = (3 * size) / (avg * 1e9)
        results.append(ComputeResult("elementwise", size, round(avg*1000, 3), round(gflops, 2), "cpu"))

    return results


def print_results(results: list[ComputeResult]):
    table = Table(title="Compute-bound Experiments")
    table.add_column("Workload")
    table.add_column("Size", justify="right")
    table.add_column("Time (ms)", justify="right")
    table.add_column("GFLOPS", justify="right")
    table.add_column("Mode")
    for r in results:
        table.add_row(r.workload, str(r.size), f"{r.time_ms:.3f}", str(r.gflops), r.mode)
    console.print(table)


def save_results(results: list[ComputeResult], path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps([asdict(r) for r in results], indent=2))
