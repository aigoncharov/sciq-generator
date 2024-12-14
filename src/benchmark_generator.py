import numpy as np
from .training_data import complex_topics
from .model import tokenizer, generator
from .classifier import classifier
from .generate_question import generate_question
from .estimate_question import estimate_question

Q_NUM_PER_TOPIC = 10


def create_benchmark_sample():
    questions = []

    for i, item in enumerate(complex_topics):
        for j in range(Q_NUM_PER_TOPIC):
            question = generate_question(generator, tokenizer, item["topic"])
            questions.append({"topic": item["topic"], "question": question})

    return questions


def benchmark_generator(out_filename):
    print("Running generator benchmark...")

    length = len(complex_topics) * Q_NUM_PER_TOPIC
    complexities = np.zeros((length))

    generator.eval()

    questions = create_benchmark_sample()

    with open(out_filename, "w") as questions_out:
        for idx, question in enumerate(questions):
            complexity = estimate_question(generator, classifier, question["topic"], question["question"])
            complexities[idx] = complexity.cpu().detach().numpy()

            questions_out.write(
                f"Topic: {question["topic"]}\nQuestion: {question["question"]}\n\n--------------------------------\n\n"
            )

    return complexities
