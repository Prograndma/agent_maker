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
        original_message = message_to_matt
        message_to_matt += "\n\n- This message was sent with\n AGENTIC AI\n *ooooooh* (be very impressed)."
        json_data = {"message": message_to_matt,
                     "number": PHONE_NUMBER,
                     "recipients": [ MATTS_NUMBER ]
        }

        _ = requests.post(f'{SIGNAL_SERVICE}/v2/send', json=json_data)

        return f"successfully sent {message_to_matt} to Matt!"
