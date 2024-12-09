import torch
from src.train_classifier import train_classifier
from src.train_generator import train_generator
from src.model import generator, tokenizer
from src.classifier import classifier
from src.training_data import complex_questions


if __name__ == "__main__":
    # First train the classifier
    train_classifier(generator, classifier, tokenizer, complex_questions, epochs=10)

    # Then train the generator
    train_generator(generator, classifier, tokenizer, complex_questions, epochs=3)

    # Save models
    generator.save_pretrained("./fine_tuned_generator")
    tokenizer.save_pretrained("./fine_tuned_generator")
    torch.save(classifier.state_dict(), "./fine_tuned_classifier.pth")
    print("Fine-tuned models saved.")
