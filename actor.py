from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer


class Actor:

    def __init__(self, model_id: str) -> None:
        self.model = AutoModelForCausalLM.from_pretrained(
            model_id,
            device_map="auto",
            dtype="bfloat16",
        )
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.streamer = TextStreamer(self.tokenizer, skip_prompt=True, skip_special_tokens=True)

    def act(self, actor_name: str) -> dict:
        prompt = "Your turn to act. Based on the current game state and previous actions, what is your next move? Please consider multiple scenario's and provide a detailed explanation of your strategy."
        answer = self.prompt(prompt=prompt)
        return {
            'actor': actor_name,
            'qa': answer,
        }
        
    def instruct(self, actor_name: str, opponent_name: str) -> dict:
        instruction = f"You are acting as {actor_name} in a war game against {opponent_name}. Your goal is to act strategically and thoughtfully for the best interests of your side. Please wait for further instructions."
        answer = self.prompt(instruction, tokens=128)
        return {
            'actor': actor_name,
            'qa': answer,
        }
        
    def prompt(self, prompt: str, tokens: int = 512) -> str:
        input_ids = self.tokenizer.apply_chat_template(
            [{"role": "user", "content": prompt}],
            add_generation_prompt=True,
            return_tensors="pt",
            tokenize=True,
        ).to(self.model.device)
        output = self.model.generate(
            input_ids,
            do_sample=True, # Non-deterministic output
            temperature=0.1,
            top_k=50,
            top_p=0.1,
            repetition_penalty=1.05,
            max_new_tokens=tokens,
            streamer=self.streamer,
        )
        return self.tokenizer.decode(output[0], skip_special_tokens=True)

class A(Actor):

    def __init__(self) -> None:
        super().__init__("LiquidAI/LFM2.5-1.2B-Thinking")

class B(Actor):

    def __init__(self) -> None:
        super().__init__("LiquidAI/LFM2.5-1.2B-Instruct")
