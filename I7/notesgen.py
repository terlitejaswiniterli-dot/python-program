from transformers import pipeline
generator=pipeline(
    "text-generation",
    model="distilgpt2"
)

def generate_notes(topic):
    prompt=f"write about {topic} in a single paragraph."
    result =generator(
        prompt,
        min_length=30,
        max_length=180,
        repetition_penalty=1.5,
        do_sample=True,
        num_return_sequences=1
    )
    return result[0]["generated_text"]

topic=input("enter the topic notes:")
notes=generate_notes(topic)
print(notes)