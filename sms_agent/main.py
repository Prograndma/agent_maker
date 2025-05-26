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
                          device_map="auto",
                          max_new_tokens=256)
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
                  max_steps=3,
                  verbosity_level=2)

agent_input = ("you're a tool following agent, so why don't you get a fun topic "
               "and then get the wikipedia summary about it in step one. In step two summarize"
               "what you learned in a message to matt! ")
big_print(f"SMS Agent Sex: {agent.run(agent_input)}")
exit()
while True:
    print("(Your turn to talk.)")
    agent_input = input()
    # print(f"Your inputs type: {type(agent_input)}")
    big_print(f"AgentMaker Sez: {agent.run(agent_input)}\n")
