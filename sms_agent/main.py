from smolagents import CodeAgent, WikipediaSearchTool, TransformersModel
from sms_agent.sms_tool import TextMatt
from my_tools import CountLettersInWord
from fun_topic import GetFunTopic
from my_secrets import LOGIN_TOKEN
from huggingface_hub import login


def big_print(message):
    print("###############################")
    print(message)
    print("###############################")
print("LOGGING IN")
login(LOGIN_TOKEN)
print("Getting model")
model = TransformersModel(model_id="meta-llama/Llama-3.2-3B-Instruct",
                          device_map="cpu",
                          max_new_tokens=256)
#
# model = TransformersModel(model_id="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
#                           device_map="auto",
#                           max_new_tokens=256)

# model = TransformersModel(model_id="deepseek-ai/deepseek-coder-1.3b-instruct",
#                           device_map="auto",
#                           max_new_tokens=256)

print("FINISHED!")
search_tool = WikipediaSearchTool(
    user_agent="MyFunBot (tocm43841@gmail.com)",
    language="en",
    content_type="summary",
    extract_format="WIKI",
)
print("Making agent")
agent = CodeAgent(tools=[search_tool, TextMatt(), GetFunTopic(), CountLettersInWord(),],
                  model=model,
                  max_steps=6,
                  verbosity_level=2)

agent_input = ("Find a fun topic, learn about it and then send a message about it to Matt.")
big_print(f"SMS Agent Sez: {agent.run(agent_input)}")
while True:
    print("(Your turn to talk.)")
    agent_input = input()
    # print(f"Your inputs type: {type(agent_input)}")
    big_print(f"AgentMaker Sez: {agent.run(agent_input)}\n")
