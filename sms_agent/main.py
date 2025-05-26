from smolagents import CodeAgent, WikipediaSearchTool, TransformersModel
from sms_agent.sms_tool import TextMatt
from my_tools import CountLettersInWord
from fun_topic import GetFunTopic

def big_print(message):
    print("###############################")
    print(message)
    print("###############################")

model = TransformersModel(model_id="meta-llama/Llama-3.1-3B-Instruct",
                          device_map="auto",
                          max_new_tokens=256)

agent = CodeAgent(tools=[WikipediaSearchTool, TextMatt(), GetFunTopic(), CountLettersInWord(),],
                  model=model,
                  max_steps=5,
                  verbosity_level=2)
while True:
    print("(Your turn to talk.)")
    agent_input = input()
    # print(f"Your inputs type: {type(agent_input)}")
    big_print(f"AgentMaker Sez: {agent.run(agent_input)}\n")
