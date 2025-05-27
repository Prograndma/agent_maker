from smolagents import CodeAgent, WikipediaSearchTool, TransformersModel, GradioUI
from sms_agent.sms_tool import TextMatt
from my_tools import CountLettersInWord
from fun_topic import GetFunTopic
from my_secrets import LOGIN_TOKEN
from huggingface_hub import login
from sql_tool import SQLEngine, get_random_topic_id


def big_print(message):
    print("###############################")
    print(message)
    print("###############################")
print("LOGGING IN")
login(LOGIN_TOKEN)
print("Getting model")
model = TransformersModel(model_id="meta-llama/Llama-3.1-8B-Instruct",
                          device_map="cpu",
                          max_new_tokens=256)
# model = TransformersModel(model_id="meta-llama/Llama-3.2-3B-Instruct",
#                           device_map="cpu",
#                           max_new_tokens=256)
# model = TransformersModel(model_id="meta-llama/Llama-Guard-3-8B-INT8",
#                           device_map="cpu",
#                           max_new_tokens=256)
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
agent = CodeAgent(tools=[search_tool, TextMatt(), SQLEngine(), get_random_topic_id,],
                  model=model,
                  max_steps=1,
                  verbosity_level=2)

GradioUI(agent, file_upload_folder="./data").launch()
# agent_input = ("Find a fun topic from the database, "
#                "learn about it on wikipedia "
#                "and then send a message about something cool you learned to Matt."
#                "Do not just send the wikipedia article to matt. Read it yourself and then send your thoughts to matt.")
# big_print(f"SMS Agent Sez: {agent.run(agent_input)}")
# while True:
#     print("(Your turn to talk.)")
#     agent_input = input()
#     # print(f"Your inputs type: {type(agent_input)}")
#     big_print(f"AgentMaker Sez: {agent.run(agent_input)}\n")
