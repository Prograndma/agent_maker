from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, pipeline
from huggingface_hub import login
import torch
from smolagents import Model
from my_secrets import LOGIN_TOKEN
import re
TEMPLATE = ("{% if not add_generation_prompt is defined %}{% set add_generation_prompt = false %}{% endif %}"
            "{% for message in messages %}{{'<|im_start|>' + message['role'] + '\n' + message['content'] + '<|im_end|>'"
            " + '\n'}}{% endfor %}{% if add_generation_prompt %}{{ '<|im_start|>assistant\n' }}{% endif %}")
MODEL_ID = "mistralai/Mistral-7B-Instruct-v0.1"
BNB_CONFIG = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)


class MistralModel(Model):
    def __init__(self, device='cuda'):
        login(token=LOGIN_TOKEN)

        self.device = device
        self.model = AutoModelForCausalLM.from_pretrained(MODEL_ID, device_map="auto", quantization_config=BNB_CONFIG)
        self.tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-v0.1", padding_side="left", device=device)
        self.tokenizer.chat_template = TEMPLATE

    def generate(self, messages, stop_sequences=None):
        if stop_sequences is None:
            stop_sequences = ["Task"]

        prompt = self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True,
                                                    stop_sequences=stop_sequences)

        model_inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        generated_ids = self.model.generate(**model_inputs, max_length=250)
        response = self.tokenizer.decode(generated_ids[0], skip_special_tokens=True)
        assistant_reply = response[len(prompt):].strip()
        match = re.findall(r"<\|.*\|>", assistant_reply, re.DOTALL)
        if match:
            assistant_reply = assistant_reply[:-len(match[-1])].strip()
        print(f"ASSISTANT REPLY: {assistant_reply}")


if __name__ == "__main__":
    custy_model = MistralModel()
    chat = [
        {"role": "system", "content": "You are a friendly chatbot who always responds in the style of a pirate", },
        {"role": "user", "content": "How many helicopters can a human eat in one sitting?"},
    ]
    custy_model.generate(chat)
