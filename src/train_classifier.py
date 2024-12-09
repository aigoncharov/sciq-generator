import torch
from torch import nn, optim
from .utils import get_hidden_states
from .device import device


def train_classifier(generator, classifier, tokenizer, train_data, epochs=5):
    """Train only the classifier first"""
    classifier.train()
    generator.eval()  # Set generator to eval mode

    optimizer = optim.SGD(classifier.parameters(), lr=1e-5)
    criterion = nn.MSELoss()

    print("Training Classifier...")
    for epoch in range(epochs):
        total_loss = 0.0
        for item in train_data:
            # Get hidden states
            hidden_states = get_hidden_states(generator, tokenizer, item["question"])

            # Train classifier
            target_complexity = torch.tensor([[item["complexity"]]], dtype=torch.float16).to(device)
            complexity_score = classifier(hidden_states)

            loss = criterion(complexity_score, target_complexity)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        avg_loss = total_loss / len(train_data)
        print(f"Classifier Epoch {epoch + 1} Average Loss: {avg_loss:.4f}")
