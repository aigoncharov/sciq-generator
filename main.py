from model import model, tokenizer

prompt = "My favourite condiment is"

messages = [
    {"role": "user", "content": "What is your favourite condiment?"},
    {
        "role": "assistant",
        "content": "Well, I'm quite partial to a good squeeze of fresh lemon juice. It adds just the right amount of zesty flavour to whatever I'm cooking up in the kitchen!",
    },
    {"role": "user", "content": "Do you have mayonnaise recipes?"},
]

formatted_prompt = ""
for message in messages:
    if message["role"] == "user":
        formatted_prompt += f"User: {message['content']}\n"
    else:
        formatted_prompt += f"Assistant: {message['content']}\n"
formatted_prompt += "Assistant: "

inputs = tokenizer(formatted_prompt, return_tensors="pt")
input_ids = inputs["input_ids"].to("mps")
attention_mask = inputs["attention_mask"].to("mps")

generated_ids = model.generate(input_ids, attention_mask=attention_mask, max_new_tokens=100, do_sample=True)
response = tokenizer.batch_decode(generated_ids)[0]

print(response)
