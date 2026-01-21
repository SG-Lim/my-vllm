import os
from huggingface_hub import snapshot_download

model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
local_dir = "./model_weights"
os.makedirs(local_dir, exist_ok=True)
snapshot_download(
    repo_id=model_id,
    local_dir=local_dir,
    local_dir_use_symlinks=False,  
    revision="main"  
)