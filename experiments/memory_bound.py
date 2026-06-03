#!/usr/bin/env python3
"""Memory-bound workload experiments."""
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
class MemoryResult:
    workload: str
    size_mb: float
    time_ms: float
    bandwidth_gbps: float
    mode: str


def run_memory_experiments() -> list[MemoryResult]:
    results = []
    for size_mb in [1, 16, 64, 256, 1024]:
        nbytes = size_mb * 1024 * 1024
        data = np.ones(nbytes // 4, dtype=np.float32)
        times = []
        for _ in range(10):
            t0 = time.perf_counter()
            _ = data.copy()
            times.append(time.perf_counter() - t0)
        avg = np.mean(times)
        gbps = (nbytes / (avg * 1e9)) if avg > 0 else 0
        results.append(MemoryResult("memcpy", size_mb, round(avg*1000, 3), round(gbps, 2), "cpu"))
    return results


def print_results(results: list[MemoryResult]):
    table = Table(title="Memory-bound Experiments")
    table.add_column("Workload")
    table.add_column("Size (MB)", justify="right")
    table.add_column("Time (ms)", justify="right")
    table.add_column("BW (GB/s)", justify="right")
    table.add_column("Mode")
    for r in results:
        table.add_row(r.workload, str(r.size_mb), f"{r.time_ms:.3f}", str(r.bandwidth_gbps), r.mode)
    console.print(table)


def save_results(results: list[MemoryResult], path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps([asdict(r) for r in results], indent=2))
