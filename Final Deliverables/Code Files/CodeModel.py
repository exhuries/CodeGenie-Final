from llama_cpp import Llama
from functools import lru_cache
import time, pathlib

MODEL_PATH = pathlib.Path("codellama-7b-instruct.Q4_K_M.gguf")

@lru_cache(maxsize=1)
def _llm():
    # n_threads = logical CPU cores you want to use
    return Llama(model_path=str(MODEL_PATH),
                 n_ctx=4096,
                 n_threads=8)      # adjust if you have fewer / more cores

def generate_code(prompt, max_tokens: int = 256):
    start = time.time()
    resp = _llm().create_completion(prompt,
                                    max_tokens=max_tokens,
                                    temperature=0.1,
                                    top_p=0.9)
    end = time.time()
    return resp["choices"][0]["text"].strip(), start, end
