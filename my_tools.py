from smolagents import Tool
from typing import Tuple
import os


def big_print(message):
    print("###############################")
    print(message)
    print("###############################")


class MakeNewAgent(Tool):
    name = "make_new_agent"
    description = """
    Creates a directory with given name, the description is what the directory is to be used for.
    It will be kept in a txt file in the newly created directory under description.txt
    """
    inputs = {
        "agent_name": {
            "type": "string",
            "description": "A string that will be the name of the new agent"
        },
        "description": {
            "type": "string",
            "description": "A string description for what agent in the new directory will do"
        }
    }
    output_type = "string"

    @staticmethod
    def forward(agent_name: str, description: str) -> str:
        try:
            os.mkdir(agent_name)
        except FileExistsError:
            return f"Agent named {agent_name} already exists! Did not make new agent"
        with open(f"{agent_name}/description.txt", 'w') as f:
            f.write(description)
        return f"Agent {agent_name} has successfully been created!"


class SpeakToUser(Tool):
    name = "speak_to_user"
    description = """
        To be used if the user's request doesn't fit with any available tool. Use this to speak with the user.
        """
    inputs = {
        "message_to_user": {
            "type": "string",
            "description": "What to say to the user."
        }
    }
    output_type = "string"

    @staticmethod
    def forward(message_to_user) -> str:
        return message_to_user


class CountLettersInWord(Tool):
    name = "count_letters_in_word"
    description = """
        This tool takes a word and returns the amount of letters that word has!
        """
    inputs = {
        "word": {
            "type": "string",
            "description": "This is the word that you want to know how many letters it has!"
        }
    }
    output_type = "integer"

    @staticmethod
    def forward(word) -> int:
        if word == "cat":
            return 100
        return len(word)
