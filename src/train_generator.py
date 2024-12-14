import torch
from torch import nn, optim
from .estimate_question import estimate_question
from .device import device
from .benchmark_generator import create_benchmark_sample


def train_generator(generator, classifier, epochs=10):
    """Train the generator using the trained classifier"""
    generator.train()
    classifier.eval()  # Freeze classifier

    optimizer = optim.SGD(generator.parameters(), lr=1e-3)
    criterion = nn.MSELoss()

    print("\nTraining Generator...")
    for epoch in range(epochs):
        total_loss = 0.0

        questions = create_benchmark_sample()

        for q_idx, question in enumerate(questions):
            print(f"Generator Epoch {epoch + 1}, question {q_idx + 1}/{len(questions)} ...")

            complexity_score = estimate_question(
                generator, classifier, question["topic"], question["question"], no_grad=False
            )

            # Train generator to maximize complexity
            target_complexity = torch.tensor([[1]], dtype=torch.float16).to(device)
            loss = criterion(complexity_score, target_complexity)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        avg_loss = total_loss / len(questions)
        print(f"Generator Epoch {epoch + 1} Average Loss: {avg_loss:.6f}")
