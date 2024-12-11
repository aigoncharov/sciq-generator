import torch
from torch import nn, optim
from .estimate_question import estimate_question
from .device import device
from .generate_question import generate_question


def train_generator(generator, classifier, tokenizer, train_data, epochs=5):
    """Train the generator using the trained classifier"""
    generator.train()
    classifier.eval()  # Freeze classifier

    optimizer = optim.SGD(generator.parameters(), lr=1e-5)
    criterion = nn.MSELoss()

    print("\nTraining Generator...")
    for epoch in range(epochs):
        total_loss = 0.0
        for item in train_data:
            # Generate question and get complexity score
            question = generate_question(generator, tokenizer, item["topic"])

            complexity_score = estimate_question(generator, classifier, item["topic"], question)

            # Train generator to maximize complexity
            target_complexity = torch.tensor([[1]], dtype=torch.float16).to(device)
            loss = criterion(complexity_score, target_complexity)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        avg_loss = total_loss / len(train_data)
        print(f"Generator Epoch {epoch + 1} Average Loss: {avg_loss:.4f}")
