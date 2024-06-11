from promptflow.core import tool
import json


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def location_examples():
    return [
        {
            "input": "Input1: The incident took place on May 7 just three hours after Eva Air’s BR08 flight left Taipei for San Francisco, according to TVBS News.\n\n" +
            "Input2: The incident took place on May 7 just three hours after Eva Air’s BR08 flight left Singapore for New York, according to TVBS News.",
            "output": "Input1: The incident took place on May 7 just three hours after Eva Air’s BR08 flight left Taipei for San Francisco, according to TVBS News.\n\n" +
            "Input2: The incident took place on May 7 just three hours after Eva Air’s BR08 flight left Singapore for New York, according to TVBS News.\n\n" +
            json.dumps(
                {"Location": [
                    {"Sentence1": "The incident took place on May 7 just three hours after Eva Air’s BR08 flight left Taipei for San Francisco, according to TVBS News.",
                    "Sentence2": "The incident took place on May 7 just three hours after Eva Air’s BR08 flight left Singapore for New York, according to TVBS News.",
                    "Reason": "BR08 flight left from Taipei for San Francisco in Sentence1, but is stated to have left from Singapore for New York in Sentence2."
                    }]
                }
            )
        }, 
        {
            "input": "Input1: “At the invitation of Chinese President Xi Jinping, Vladimir Putin will pay a state visit to China on May 16 to 17 as his first foreign trip after taking office,” the Kremlin said.\n\n" +
            "Input2: “At the invitation of Chinese President Xi Jinping, Vladimir Putin will pay a state visit to England on May 1 to 2 as his first foreign trip after taking office,” the Kremlin said.\n\n" +
            json.dumps (
                {"DateTime": [
                    {"Sentence1": "“At the invitation of Chinese President Xi Jinping, Vladimir Putin will pay a state visit to China on May 16 to 17 as his first foreign trip after taking office,” the Kremlin said.",
                    "Sentence2": "“At the invitation of Chinese President Xi Jinping, Vladimir Putin will pay a state visit to England on May 1 to 2 as his first foreign trip after taking office,” the Kremlin said.",
                    "Reason": "The date of the state visit in Sentence2 (May 1 to 2) does not match with the date in Sentence1 (May 16 to 17)."
                    }]
                }
            ),

            "output": "Input1: “At the invitation of Chinese President Xi Jinping, Vladimir Putin will pay a state visit to China on May 16 to 17 as his first foreign trip after taking office,” the Kremlin said.\n\n" +
            "Input2: “At the invitation of Chinese President Xi Jinping, Vladimir Putin will pay a state visit to England on May 1 to 2 as his first foreign trip after taking office,” the Kremlin said.\n\n" +
            json.dumps (
                {"DateTime": [
                    {"Sentence1": "“At the invitation of Chinese President Xi Jinping, Vladimir Putin will pay a state visit to China on May 16 to 17 as his first foreign trip after taking office,” the Kremlin said.",
                    "Sentence2": "“At the invitation of Chinese President Xi Jinping, Vladimir Putin will pay a state visit to England on May 1 to 2 as his first foreign trip after taking office,” the Kremlin said.",
                    "Reason": "The date of the state visit in Sentence2 (May 1 to 2) does not match with the date in Sentence1 (May 16 to 17)."
                    }],
                "Location": [
                    {"Sentence1": "“At the invitation of Chinese President Xi Jinping, Vladimir Putin will pay a state visit to China on May 16 to 17 as his first foreign trip after taking office,” the Kremlin said.",
                    "Sentence2": "“At the invitation of Chinese President Xi Jinping, Vladimir Putin will pay a state visit to England on May 1 to 2 as his first foreign trip after taking office,” the Kremlin said.",
                    "Reason": "Vladimir Putin is stated to visit China in Sentence1, but is stated to visit England in Sentence2."
                    }]
                }
            ),            
        }
    ]