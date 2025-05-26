from smolagents import Tool
import requests
from my_secrets import MATTS_NUMBER, PHONE_NUMBER, SIGNAL_SERVICE


class TextMatt(Tool):
    name = "text_matt"
    description = """
        This is the tool to use to send a message to Matt.
        """
    inputs = {
        "message_to_matt": {
            "type": "string",
            "description": "What to say to Matt."
        }
    }
    output_type = "string"

    @staticmethod
    def forward(message_to_matt) -> str:
        json_data = {"message": message_to_matt,
                     "number": PHONE_NUMBER,
                     "recipients": [ MATTS_NUMBER ]
        }

        _ = requests.post(f'{SIGNAL_SERVICE}/v2/send', json=json_data)

        return f"successfully sent {message_to_matt} to Matt!"
