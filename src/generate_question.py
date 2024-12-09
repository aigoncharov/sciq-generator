from .device import device


def generate_question(generator, tokenizer, topic, max_length=400):
    prompt = f"Generate a complex, thought-provoking question on the topic: {topic}\nQuestion:"
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512).to(device)
    outputs = generator.generate(
        **inputs,
        max_length=max_length,
        temperature=0.7,
        top_p=0.9,
        do_sample=True,
        num_return_sequences=1,
        pad_token_id=tokenizer.eos_token_id,
    )
    question = tokenizer.decode(outputs[0], skip_special_tokens=True).split("Question:")[-1].strip()
    return question
