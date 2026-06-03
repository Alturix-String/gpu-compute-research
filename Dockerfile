FROM rocm/pytorch:rocm6.2_ubuntu22.04_py3.10_pytorch_release_2.3.0

LABEL maintainer="Alturix-String"
LABEL description="gpu-compute-research"

WORKDIR /workspace/gpu-compute-research

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "run_experiment.py", "--all"]
