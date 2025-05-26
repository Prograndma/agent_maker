import random
from smolagents import Tool


class GetFunTopic(Tool):
    name = "get_fun_topic"
    description = """
        This tool provides a fun topic from a list of good choices!
        """
    inputs = {

    }
    output_type = "string"

    @staticmethod
    def forward():
        topics = ["Pizza farm"
                  "Spite house"
                  "list of tautological place names",
                  "Valeriepieris circle",
                  "Cheese",
                  "modern Toilet Restaurant",
                  "Neutrality Monument",
                  "616 (number)",
                  "65537-gon",
                  "All horses are the same color",
                  "Almost everywhere",
                  "Hairy ball theorem",
                  "Cinnamon Roll Day",
                  "Thanksgivukkah",
                  "Undecimber",
                  "Bouba/kiki effect",
                  "Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo",
                  "Covfefe",
                  "Duck test",
                  "Ghost characters",
                  "Inherently funny word",
                  "James while John had had had had had had had had had had had a better effect on the teacher",
                  "Lion-Eating Poet in the Stone Den",
                  "List of English words without rhymes",
                  "List of English words containing Q not followed by U",
                  "Archaeoacoustics",
                  "Buttered cat paradox",
                  "Kardashian Index",
                  "John G. Trump",
                  "Furry's theorem",
                  "Mpemba effect",
                  "Shower-curtain effect",
                  "Continental drip",
                  "Mothers against decapentaplegic",
                  "Death from laughter",
                  "Execution by elephant",
                  "What Is It Like to Be a Bat?",
                  ]

        return random.choice(topics)