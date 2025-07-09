import openai
import yaml

with open("config/llm_config.yaml") as f:
    config = yaml.safe_load(f)

openai.api_key = config["openai"]["api_key"]

def summarize_text_block(text: str, purpose: str = "generic") -> str:
    prompt = config["prompts"].get(purpose, config["prompts"]["generic"])
    messages = [{"role": "user", "content": f"{prompt}\n\n{text}"}]
    response = openai.ChatCompletion.create(
        model=config["openai"]["model"],
        temperature=config["openai"]["temperature"],
        max_tokens=config["openai"]["max_tokens"],
        messages=messages
    )
    return response.choices[0].message["content"].strip()
