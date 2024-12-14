import torch
from contextlib import nullcontext
from .device import device


def get_hidden_states(generator, tokenizer, text, no_grad=True):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512).to(device)
    context = torch.no_grad() if no_grad else nullcontext()
    with context:
        outputs = generator(**inputs, output_hidden_states=True)
        hidden_states = torch.stack(outputs.hidden_states)
        # print("After stack:", hidden_states.shape)
        pooled_hidden_states = hidden_states.mean(dim=2)
        # print("After mean:", pooled_hidden_states.shape)
        pooled_hidden_states = pooled_hidden_states.transpose(0, 1)
        # print("After transpose:", pooled_hidden_states.shape)
    return pooled_hidden_states
