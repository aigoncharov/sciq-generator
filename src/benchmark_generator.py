import numpy as np
from .training_data import complex_topics
from .model import tokenizer, generator
from .classifier import classifier
from .generate_question import generate_question
from .estimate_question import estimate_question

Q_NUM_PER_TOPIC = 10


def benchmark_generator(out_filename):
    print("Running generator benchmark...")

    length = len(complex_topics) * Q_NUM_PER_TOPIC
    complexities = np.zeros((length))

    generator.eval()
    with open(out_filename, "w") as questions:
        for i, item in enumerate(complex_topics):
            for j in range(Q_NUM_PER_TOPIC):
                idx = i * Q_NUM_PER_TOPIC + j
                print(f"Generating question {idx + 1}/{length}")
                question = generate_question(generator, tokenizer, item["topic"])
                questions.write(question)
                questions.write("\n\n--------------------------------\n\n")

                complexity = estimate_question(generator, classifier, item["topic"], question)
                complexities[idx] = complexity.cpu().detach().numpy()
                print(complexities[idx])

    return complexities
