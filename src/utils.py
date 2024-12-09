import torch
from .device import device


def get_hidden_states(generator, tokenizer, text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512).to(device)
    with torch.no_grad():
        outputs = generator(**inputs, output_hidden_states=True)
        hidden_states = outputs.hidden_states[-1]
        pooled_hidden_state = hidden_states.mean(dim=1)
    return pooled_hidden_state
