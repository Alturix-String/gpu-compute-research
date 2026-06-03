# Research Plan

## Objectives

1. Characterize compute-bound workload behavior on AMD GPUs
2. Characterize memory-bound workload behavior on AMD GPUs
3. Build a profiling harness for kernel analysis
4. Document findings for reproducibility

## Methodology

- Run experiments on ROCm 6.x with AMD Instinct GPUs
- Compare CPU baseline vs GPU execution
- Measure: runtime, throughput, bandwidth, utilization
- Store all results in structured JSON

## Timeline

- Phase 1: CPU baseline experiments
- Phase 2: HIP kernel experiments
- Phase 3: Profiling and analysis
- Phase 4: Cross-architecture comparison
