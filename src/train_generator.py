import torch
from torch import nn, optim
from .utils import get_hidden_states
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
            hidden_states = get_hidden_states(generator, tokenizer, question)

            complexity_score = classifier(hidden_states)

            # Train generator to match target complexity
            target_complexity = torch.tensor([[item["complexity"]]], dtype=torch.float16).to(device)
            loss = criterion(complexity_score, target_complexity)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        avg_loss = total_loss / len(train_data)
        print(f"Generator Epoch {epoch + 1} Average Loss: {avg_loss:.4f}")
