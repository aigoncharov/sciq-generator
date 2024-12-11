import torch
import numpy as np
from src.train_classifier import train_classifier
from src.train_generator import train_generator
from src.model import generator, tokenizer
from src.classifier import classifier
from src.training_data import complex_questions, complex_topics
from src.generate_question import generate_question
from src.estimate_question import estimate_question

Q_NUM_PER_TOPIC = 5


if __name__ == "__main__":
    # First train the classifier
    train_classifier(generator, classifier, tokenizer, complex_questions, epochs=10)

    complexities_pretrain = []

    generator.eval()
    with open("questions_pretrain.txt", "w") as questions:
        for i, item in enumerate(complex_topics, 1):
            for j in range(Q_NUM_PER_TOPIC, 1):
                print(f"Generating a pre-train question {i * j}/{len(complex_topics * Q_NUM_PER_TOPIC)}")
                question = generate_question(generator, tokenizer, item["topic"])
                questions.write(question)
                questions.write("\n\n--------------------------------\n\n")

                complexity = estimate_question(generator, classifier, item["topic"], question)
                complexities_pretrain.append(complexity)

    # Then train the generator
    train_generator(generator, classifier, tokenizer, complex_topics, epochs=3)
    generator.save_pretrained("./fine_tuned_generator")
    tokenizer.save_pretrained("./fine_tuned_generator")
    torch.save(classifier.state_dict(), "./fine_tuned_classifier.pth")
    print("Fine-tuned models saved.\n")

    complexities_posttrain = []

    generator.eval()
    with open("questions_posttrain.txt", "w") as questions:
        for i, item in enumerate(complex_topics, 1):
            print(f"Generating question {i}/{len(complex_topics)}")
            question = generate_question(generator, tokenizer, item["topic"])
            questions.write(question)
            questions.write("\n\n--------------------------------\n\n")

            complexity = estimate_question(generator, classifier, item["topic"], question)
            complexities_posttrain.append(complexity)

    complexities_pretrain = np.array(complexities_pretrain)
    complexities_posttrain = np.array(complexities_posttrain)

    print(
        f"Question complexity before training: mean {np.mean(complexities_pretrain)}, stddev {np.std(complexities_pretrain)}. Question complexity after training: mean {np.mean(complexities_posttrain)}, stddev {np.std(complexities_posttrain)}."
    )

    print("Done!")
