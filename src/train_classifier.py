import torch
from torch import nn, optim
from .device import device
from .estimate_question import estimate_question


def train_classifier(generator, classifier, train_data, epochs=50):
    """Train only the classifier first"""
    classifier.train()
    generator.eval()  # Set generator to eval mode

    optimizer = optim.SGD(classifier.parameters(), lr=1e-3)
    criterion = nn.MSELoss()

    print("Training Classifier...")
    for epoch in range(epochs):
        total_loss = 0.0
        for item in train_data:
            complexity_score = estimate_question(generator, classifier, item["topic"], item["question"])
            target_complexity = torch.tensor([[item["complexity"]]], dtype=torch.float16).to(device)

            loss = criterion(complexity_score, target_complexity)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        avg_loss = total_loss / len(train_data)
        print(f"Classifier Epoch {epoch + 1} Average Loss: {avg_loss:.6f}")
