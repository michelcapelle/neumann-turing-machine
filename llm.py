from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer


def download_and_test_model(name: str, id: str) -> None:
    print(f"Downloading and testing model: {name} ({id})")
    model = AutoModelForCausalLM.from_pretrained(
        id,
        device_map="auto",
        dtype="bfloat16",
    )
    tokenizer = AutoTokenizer.from_pretrained(id)
    streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)
    prompt = f"Who is {name}?"
    input_ids = tokenizer.apply_chat_template(
        [{"role": "user", "content": prompt}],
        add_generation_prompt=True,
        return_tensors="pt",
        tokenize=True,
    ).to(model.device)
    model.generate(
        input_ids,
        do_sample=True,
        temperature=0.1,
        top_k=50,
        top_p=0.1,
        repetition_penalty=1.05,
        max_new_tokens=128,
        streamer=streamer,
    )
    print("\n")

download_and_test_model("Alan Turing", "LiquidAI/LFM2.5-1.2B-Thinking")
download_and_test_model("John von Neumann", "LiquidAI/LFM2.5-1.2B-Instruct")
