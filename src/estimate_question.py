from .generate_question import get_prompt_to_generate_question
from .utils import get_hidden_states
from .model import tokenizer


def estimate_question(generator, classifier, topic, question, no_grad=True):
    prompt = get_prompt_to_generate_question(topic)
    prompt_with_question = f"{prompt} {question}"
    hidden_states = get_hidden_states(generator, tokenizer, prompt_with_question, no_grad)
    complexity_score = classifier(hidden_states)
    return complexity_score
