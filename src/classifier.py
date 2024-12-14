import torch
from torch import nn
from .model import generator
from .device import device


class ComplexityClassifier(nn.Module):
    def __init__(self, hidden_size: int, num_layers: int):
        super().__init__()
        # print(f"Classifier initialized with hidden_size: {hidden_size}, num_layers: {num_layers}")
        self.fc1 = nn.Linear(hidden_size * num_layers, 512, dtype=torch.float16)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(512, 1, dtype=torch.float16)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = x.to(torch.float16)
        # print("Input shape:", x.shape)
        x = x.reshape(x.size(0), -1)
        # print("After reshape:", x.shape)
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        complexity_score = torch.sigmoid(out)
        return complexity_score


hidden_size = generator.config.hidden_size
num_layers = generator.config.num_hidden_layers + 1
classifier = ComplexityClassifier(hidden_size=hidden_size, num_layers=num_layers).to(device)
