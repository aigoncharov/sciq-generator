import numpy as np
from .training_data import complex_topics
from .model import tokenizer, generator
from .classifier import classifier
from .generate_question import generate_question
from .estimate_question import estimate_question

Q_NUM_PER_TOPIC = 5


def benchmark_generator(out_filename):
    print("Running generator benchmark...")

    complexities = []

    generator.eval()
    with open(out_filename, "w") as questions:
        for i, item in enumerate(complex_topics, 1):
            for j in range(1, Q_NUM_PER_TOPIC, 1):
                print(f"Generating a pre-train question {i * j}/{len(complex_topics * Q_NUM_PER_TOPIC)}")
                question = generate_question(generator, tokenizer, item["topic"])
                questions.write(question)
                questions.write("\n\n--------------------------------\n\n")

                complexity = estimate_question(generator, classifier, item["topic"], question)
                complexities.append(complexity)

    return np.array(complexities)
