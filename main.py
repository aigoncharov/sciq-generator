import torch
import numpy as np
from src.train_classifier import train_classifier
from src.train_generator import train_generator
from src.model import generator, tokenizer
from src.classifier import classifier
from src.training_data import complex_questions
from src.benchmark_generator import benchmark_generator


if __name__ == "__main__":
    # First train the classifier
    train_classifier(generator, classifier, complex_questions, epochs=30)

    complexities_pretrain = benchmark_generator("questions_pretrain.txt")

    # Then train the generator
    train_generator(generator, classifier, epochs=10)
    generator.save_pretrained("./fine_tuned_generator")
    tokenizer.save_pretrained("./fine_tuned_generator")
    torch.save(classifier.state_dict(), "./fine_tuned_classifier.pth")
    print("Fine-tuned models saved.\n")

    complexities_posttrain = benchmark_generator("questions_posttrain.txt")

    print(
        f"Question complexity before training: mean {np.mean(complexities_pretrain)}, stddev {np.std(complexities_pretrain)}. Question complexity after training: mean {np.mean(complexities_posttrain)}, stddev {np.std(complexities_posttrain)}."
    )

    print("Done!")
