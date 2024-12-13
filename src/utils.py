import torch
from contextlib import nullcontext
from .device import device


def get_hidden_states(generator, tokenizer, text, no_grad=True):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512).to(device)
    context = torch.no_grad() if no_grad else nullcontext()
    with context:
        outputs = generator(**inputs, output_hidden_states=True)
        hidden_states = outputs.hidden_states[-1]
        pooled_hidden_state = hidden_states.mean(dim=1)
    return pooled_hidden_state
