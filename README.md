# gpu-compute-research

[![ROCm](https://img.shields.io/badge/ROCm-6.x-ED1C24?logo=amd&logoColor=white)](https://rocm.docs.amd.com/)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Research repository for GPU compute workload analysis — kernel profiling, memory behavior studies, and performance characterization on AMD GPUs.**

A structured research workspace for investigating compute-bound and memory-bound workload patterns.

---

## Research Areas

| Area | Focus | Status |
|:---|:---|:---:|
| **Compute-bound Kernels** | Matrix ops, reduction, convolution | Active |
| **Memory-bound Kernels** | Bandwidth, latency, transfer patterns | Active |
| **Kernel Profiling** | rocprof integration, hotspot analysis | Planned |
| **Cross-arch Comparison** | CDNA vs RDNA behavior | Planned |
| **Power Efficiency** | TFLOPS/watt measurement | Planned |

---

## Repository Layout

```
gpu-compute-research/
+-- experiments/
|   +-- compute_bound.py      # Compute-bound workload analysis
|   +-- memory_bound.py       # Memory-bound workload analysis
|   +-- kernel_profiling.py   # Kernel profiling harness
+-- kernels/
|   +-- vector_ops.py         # Vector operation kernels
|   +-- matrix_ops.py         # Matrix operation kernels
|   +-- reduction_ops.py      # Reduction kernels
+-- analysis/
|   +-- plot_results.py       # Result visualization
|   +-- compare_runs.py       # Run comparison
+-- docs/
|   +-- research-plan.md      # Research objectives
|   +-- architecture.md       # System architecture
|   +-- methodology.md        # Experimental methodology
+-- results/                  # Experiment outputs
+-- references/               # Technical references
+-- run_experiment.py         # Main entry point
+-- requirements.txt
+-- pyproject.toml
+-- LICENSE
```

---

## Quick Start

```bash
git clone https://github.com/Alturix-String/gpu-compute-research.git
cd gpu-compute-research
pip install -r requirements.txt

python run_experiment.py --experiment compute_bound
python run_experiment.py --experiment memory_bound
python run_experiment.py --all
```

---

## Experiments

### Compute-bound

Tests kernel performance where computation is the bottleneck:
- Matrix multiplication (GEMM)
- Element-wise math operations
- Reduction operations

### Memory-bound

Tests kernel performance where memory bandwidth is the bottleneck:
- Large array copy
- Strided access patterns
- H2D/D2H transfer rates

---

## Development

```bash
pip install -e ".[dev]"
ruff check .
pytest tests/ -v
```

---

## Roadmap

- [ ] rocprof v2 integration
- [ ] Roofline model analysis
- [ ] Multi-GPU scaling experiments
- [ ] Power efficiency benchmarking
- [ ] Cross-vendor comparison (AMD vs NVIDIA)

---

## License

MIT -- see [LICENSE](LICENSE).
