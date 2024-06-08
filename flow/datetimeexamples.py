from promptflow import tool
# import json

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def date_examples():
    return [
        {
            "input1": "Some opposition parties congragulated Mr Lawrence Wong ahead of his swearing-in as prime minister at the Istana on May 15, while thanking outgoing prime minister Lee Hsien Loong for his decades of public service and leadership.", 
            "input2": "Some opposition parties congragulated Mr Lawrence Wong ahead of his swearing-in as prime minister at the Istana on May 15, while thanking outgoing prime minister Lee Hsien Loong for his decades of public service and leadership.",
            "output": "Input1: Some opposition parties congragulated Mr Lawrence Wong ahead of his swearing-in as prime minister at the Istana on May 15, while thanking outgoing prime minister Lee Hsien Loong for his decades of public service and leadership.\n\n" +
            "Input 2: Some opposition parties congragulated Mr Lawrence Wong ahead of his swearing-in as prime minister at the Istana on May 15, while thanking outgoing prime minister Lee Hsien Loong for his decades of public service and leadership."
        },
        {
            "input1": "Singapore “strongly condemns” the attack that took place at a police station in Johor on May 17, said the Ministry of Foreign Affairs (MFA) in a statement.",
            "input2": "Singapore “strongly condemns” the attack that took place at a police station in Johor on April 7, said the Ministry of Foreign Affairs (MFA) in a statement.",
            "output": "Input1: Singapore “strongly condemns” the attack that took place at a police station in Johor on May 17, said the Ministry of Foreign Affairs (MFA) in a statement.\n\n" +
            "Input2: Singapore “strongly condemns” the attack that took place at a police station in Johor on April 7, said the Ministry of Foreign Affairs (MFA) in a statement.\n\n" + 
            # json.dumps(
                {"Date": [
                    {"Sentence1": "Singapore “strongly condemns” the attack that took place at a police station in Johor on May 17, said the Ministry of Foreign Affairs (MFA) in a statement.",
                    "Sentence2": "Singapore “strongly condemns” the attack that took place at a police station in Johor on April 7, said the Ministry of Foreign Affairs (MFA) in a statement.",
                    "Reason": "The date of the attack in Sentence2 was on April 7, whereas the date in Sentence1 was on May 17."
                    }]
                }
            # )
        },
        {
            "input1": "More than 160 automated lanes were installed in 2023, with another 230 lanes to be set up in 2024. ICA intends to install about 800 such lanes across all of Singapore’s checkpoints by 2026.",
            "input2": "More than 160 automated lanes were installed in 2015, with another 230 lanes to be set up in 2018. ICA intends to install about 800 such lanes across all of Singapore’s checkpoints by 2020.",
            "output": "Input1: More than 160 automated lanes were installed in 2023, with another 230 lanes to be set up in 2024. ICA intends to install about 800 such lanes across all of Singapore’s checkpoints by 2026.\n\n" +
            "Input2: More than 160 automated lanes were installed in 2015, with another 230 lanes to be set up in 2018. ICA intends to install about 800 such lanes across all of Singapore’s checkpoints by 2020.\n\n" +
            # json.dumps(
                {"Date": [
                    {"Sentence1": "More than 160 automated lanes were installed in 2023, with another 230 lanes to be set up in 2024.",
                    "Sentence2": "More than 160 automated lanes were installed in 2015, with another 230 lanes to be set up in 2018.",
                    "Reason": "Sentence2 states the automated lanes were installed in 2015 and more to be set up in 2018, whereas Sentence1 states 2023 and 2024 respectively.",
                    },

                    {"Sentence1": "ICA intends to install about 800 such lanes across all of Singapore’s checkpoints by 2026.",
                    "Sentence2": "ICA intends to install about 800 such lanes across all of Singapore’s checkpoints by 2020.",
                    "Reason": "Sentence2 states the installation will be completed by 2026, whereas Sentence2 states it will be completed by 2020."
                    }
                ]
                }
            # )
        }
    ]