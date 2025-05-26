from smolagents import CodeAgent, ToolCallingAgent, tool, InferenceClientModel, TransformersModel
from mistral_model import MODEL_ID, BNB_CONFIG
import os
from typing import Tuple
import torch
from my_tools import MakeNewAgent, SpeakToUser, CountLettersInWord
from my_secrets import LOGIN_TOKEN
from my_prompt_templates import DEFAULT_CODE_PROMPT_TEMPLATE

def big_print(message):
    print("###############################")
    print(message)
    print("###############################")


@tool
def create_agent(agent_name: str, description: str) -> Tuple[bool, str]:
    """
    Creates a directory with given name, the description is what the directory is to be used for.
    It will be kept in a txt file in the newly created directory under description.txt

    Args:
        agent_name: A string that will be the name of the new agent
        description: A string description for what agent in the new directory will do
    Returns:
         Tuple[bool, str]: A tuple the first element is a boolean indicating whether the directory was
         successfully created, and the second element is a message or error description.
    """
    big_print("Called make an agent or whatever!")
    try:
        os.mkdir(agent_name)
    except FileExistsError:
        return False, f"Agent named {agent_name} already exists!"
    with open(f"{agent_name}/description.txt", 'w') as f:
        f.write(description)
    big_print(f"MADE A FUKN DIRECTORY! ({agent_name})")
    return True, f"Agent {agent_name} has successfully been created!"


@tool
def do_nothing() -> str:
    """
    To be used if the user's request doesn't fit with any available tool. Use this to speak with the user.

    Returns:
         str: An empty string
    """
    big_print("Called do_nothing!!")
    return ""


# model = TransformersModel(model_id=MODEL_ID, device_map="auto", quantization_config=BNB_CONFIG)
# model = TransformersModel(model_id="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
#                           device_map="cuda",
#                           max_new_tokens=500)


# model = TransformersModel(model_id="meta-llama/Llama-3.2-1B-Instruct",
#                           device_map="auto",
#                           # torch_dtype=torch.bfloat8,
#                           max_new_tokens=256)
model = TransformersModel(model_id="meta-llama/Llama-3.2-3B-Instruct",
                          device_map="auto",
                          # torch_dtype=torch.bfloat8,
                          max_new_tokens=256)
# model = InferenceClientModel(model_id="meta-llama/Llama-3.1-8B-Instruct",
#                              token=LOGIN_TOKEN)
#                              # device="cuda")
#                              # torch_dtype=torch.bfloat8,
#                              # max_new_tokens=256)


# model_inputs = tokenizer(["Certainly! Here is a poem about Intel's new budget GPU:"], return_tensors="pt").to("cuda")
# print(f"The model's Type! {type(model)}")
# generated_ids = model.generate(**model_inputs, max_length=200)
# result = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
#
# print(result)


# main_pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)


# agent = ToolCallingAgent(tools=[MakeNewAgent(), SpeakToUser()], model=model, max_steps=3)
agent = CodeAgent(tools=[MakeNewAgent(), SpeakToUser(), CountLettersInWord()], model=model, max_steps=1,
                  verbosity_level=2)
# agent = CodeAgent(tools=[create_agent, do_nothing], model=model, max_steps=3) #, verbosity_level=2)


while True:
    print("(Your turn to talk.)")
    agent_input = input()
    # print(f"Your inputs type: {type(agent_input)}")
    big_print(f"AgentMaker Sez: {agent.run(agent_input)}\n")
