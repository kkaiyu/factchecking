from promptflow.core import tool
import json


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def event_examples():
    return [
        {
            "input": "Input1: Manchester City won an unprecedented fourth straight English top flight title with a 3-1 win over West Ham United on May 19 to pip rivals Arsenal on the final day of a thrilling Premier League season, sending fans onto the pitch in a sea of blue." +
            "Input2: Imperious Manchester City beat West Ham 3-1 at Old Trafford to become the first team to win the English league title three seasons in a row.",
            "output": "Input1: Manchester City won an unprecedented fourth straight English top flight title with a 3-1 win over West Ham United on May 19 to pip rivals Arsenal on the final day of a thrilling Premier League season, sending fans onto the pitch in a sea of blue." +
            "Input2: Imperious Manchester City beat West Ham 3-1 at Old Trafford to become the first team  to win the English league title three seasons in a row." + 
            json.dumps(
                {"Event Description": [
                    {"Sentence1": "Manchester City won an unprecedented fourth straight English top flight title with a 3-1 win over West Ham United on May 19 to pip rivals Arsenal on the final day of a thrilling Premier League season, sending fans onto the pitch in a sea of blue.",
                    "Sentence2": "Imperious Manchester City beat West Ham 3-1 at Old Trafford to become the first team  to win the English league title three seasons in a row.",
                    "Reason": "Sentence2 states that Manchester City won the English league title three seasons in a row, whereas Sentence1 states that they won it four times in a row."
                    }]
                }
            )
        }
    ]
