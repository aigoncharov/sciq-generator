import torch
from torch import nn
from .model import generator
from .device import device


class ComplexityClassifier(nn.Module):
    def __init__(self, hidden_size: int):
        super().__init__()
        self.fc1 = nn.Linear(hidden_size, 512, dtype=torch.float16)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(512, 1, dtype=torch.float16)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = x.to(torch.float16)
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        complexity_score = torch.sigmoid(out)
        return complexity_score


hidden_size = generator.config.hidden_size
classifier = ComplexityClassifier(hidden_size=hidden_size).to(device)
