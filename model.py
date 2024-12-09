import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from device import device

generator_model_name = "mistralai/Mistral-7B-v0.1"
tokenizer = AutoTokenizer.from_pretrained(generator_model_name)
generator = AutoModelForCausalLM.from_pretrained(generator_model_name, torch_dtype=torch.float16, device_map="auto").to(
    device
)
