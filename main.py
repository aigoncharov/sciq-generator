import torch
from src.train_classifier import train_classifier
from src.train_generator import train_generator
from src.model import generator, tokenizer
from src.classifier import classifier
from src.training_data import complex_questions, complex_topics
from src.generate_question import generate_question


if __name__ == "__main__":
    # First train the classifier
    train_classifier(generator, classifier, tokenizer, complex_questions, epochs=10)

    # Then train the generator
    train_generator(generator, classifier, tokenizer, complex_topics, epochs=3)

    # Save models
    generator.save_pretrained("./fine_tuned_generator")
    tokenizer.save_pretrained("./fine_tuned_generator")
    torch.save(classifier.state_dict(), "./fine_tuned_classifier.pth")
    print("Fine-tuned models saved.\n")

    generator.eval()
    with open("questions.txt", "w") as questions:
        for i, item in enumerate(complex_topics, 1):
            print(f"Generating question {i}/{len(complex_topics)}")
            question = generate_question(generator, tokenizer, item["topic"])
            questions.write(question)
            questions.write("\n\n--------------------------------\n\n")
    print("Done!")
