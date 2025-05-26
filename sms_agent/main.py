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

login(LOGIN_TOKEN)
model = TransformersModel(model_id="meta-llama/Llama-3.2-3B-Instruct",
                          device_map="auto",
                          max_new_tokens=256)
search_tool = WikipediaSearchTool(
    user_agent="MyFunBot (tocm43841@gmail.com)",
    language="en",
    content_type="summary",
    extract_format="WIKI",
)
agent = CodeAgent(tools=[search_tool, TextMatt(), GetFunTopic(), CountLettersInWord(),],
                  model=model,
                  max_steps=5,
                  verbosity_level=2)

agent_input = ("Hey! Could you help me? I want to send matt a fun snippet or factoid about a fun topic! "
               "Even if the topic is a little weird. Please use wikipedia to learn more about a fun topic.")
big_print(f"SMS Agent Sex: {agent.run(agent_input)}")
exit()
while True:
    print("(Your turn to talk.)")
    agent_input = input()
    # print(f"Your inputs type: {type(agent_input)}")
    big_print(f"AgentMaker Sez: {agent.run(agent_input)}\n")
