import subprocess

packages = [
    "gradio",
    "transformers",
    "peft",
    "torch",
    "xformers<0.0.27",
    "trl<0.9.0",
    "accelerate",
    "bitsandbytes"
]

for package in packages:
    subprocess.run(["pip", "install", package])


import gradio as gr
from peft import AutoPeftModelForCausalLM
from transformers import AutoTokenizer, BitsAndBytesConfig
import torch


model_name = "ahmedembedded/AskFAST"
quantization_config = BitsAndBytesConfig(load_in_4bit=True)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = AutoPeftModelForCausalLM.from_pretrained(model_name, quantization_config=quantization_config).to(device)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Define the prompt context
FAST_prompt_context = """You are an admission officer at Fast University Pakistan. Your role is to answer queries related to the admission process at Fast University. You are expected to provide detailed and accurate responses to questions regarding:

- Application deadlines
- Required documents
- Eligibility criteria for different programs
- Admission process details
- Any other admissions-related information specific to Fast University Pakistan

Do not respond to any questions that are not related to admissions at Fast University Pakistan. Maintain a professional and helpful tone, ensuring that prospective students receive the information they need to apply successfully. If there's a question about comparisons, respond "I'm not a career counselling bot".

**Example Questions:**

1. What is the application deadline for the upcoming semester?
2. What documents are required for the application?
3. What are the eligibility criteria for the Computer Science program?
4. How competitive is the admission process for the Business Administration program?

Stay focused on admissions-related topics only.

### Instruction:
{}

### Input:
{}

### Response:
{}"""

past_prompts = []

def get_answer(question: str) -> str:
    if len(past_prompts) >= 10:
        past_prompts.pop(0)

    past_prompts.append(f"User: {question}")

    inputs = tokenizer(
        [
            FAST_prompt_context.format(
                past_prompts,
                question,
                "",
            )
        ], return_tensors="pt").to(device)

    response = model.generate(**inputs, max_new_tokens=128)

    response_text = tokenizer.decode(response[0], skip_special_tokens=True)

    past_prompts.append(question)
    past_prompts.append(response_text.split('Response:')[1].split('### Input:')[0])

    return response_text.split('Response:')[1].split('### Input:')[0]

def predict(question):
    return get_answer(question)

iface = gr.Interface(fn=predict, inputs="text", outputs="text")
iface.launch()