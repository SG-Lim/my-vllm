## Project Setup (uv)

This project uses **uv** for Python environment and dependency management.

### 1. Initialize the project

Remove the default configuration files that already exist:

```bash
rm pyproject.toml .python-version
```

Re-initialize the project with a custom name and pin python version:

```bash
uv init --name my-vllm
uv python pin 3.12
```

### 2. Install dependencies

Add the required libraries:

```bash
uv add vllm trl huggingface_hub
uv add flash-attn --no-build-isolation
```

### 3. Verify installed packages

Confirm that the key dependencies are installed correctly, and that the scripts run:

```bash
uv pip list | grep -E "torch|vllm|flash-attn|trl|transformers|accelerate"
uv run python model_download.py && CUDA_VISIBLE_DEVICES=0 uv run python main.py
```

### Notes

flash-attn is installed with --no-build-isolation to ensure compatibility with the local CUDA/PyTorch setup.

vllm will pull in torch and transformers as dependencies if they are not already present.
