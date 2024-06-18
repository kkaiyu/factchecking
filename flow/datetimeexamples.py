from promptflow.core import tool
import json

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def datetime_examples():
    return [
        {
            "input1": "City now have the chance of winning the double when they face Manchester United in the FA Cup final on May 25.",
            "input2": "City now have the chance of winning the double when they face Liverpool in the FA Cup final on May 20.",
            "output": "Input1: City now have the chance of winning the double when they face Manchester United in the FA Cup final on May 25." +
            "Input2: City now have the chance of winning the double when they face Liverpool in the FA Cup final on May 20." +
            json.dumps(
                {"DateTime": [
                    {"Sentence1": "City now have the chance of winning the double when they face Manchester United in the FA Cup final on May 25.",
                    "Sentence2": "City now have the chance of winning the double when they face Liverpool in the FA Cup final on May 20.",
                    "Reason": "The date of the FA Cup final in Sentence2 (May 20) does not match with the date in Sentence1 (May 25)."
                    }]
                }
            )
        },
        {
            "input1": "More than 160 automated lanes were installed in 2023, with another 230 lanes to be set up in 2024. ICA intends to install about 800 such lanes across all of Singapore’s checkpoints by 2026.",
            "input2": "More than 160 automated lanes were installed in 2015, with another 230 lanes to be set up in 2018. BDF intends to install about 800 such lanes across all of Malaysia’s checkpoints by 2020.",
            "output": "Input1: More than 160 automated lanes were installed in 2023, with another 230 lanes to be set up in 2024. ICA intends to install about 800 such lanes across all of Singapore’s checkpoints by 2026.\n\n" +
            "Input2: More than 160 automated lanes were installed in 2015, with another 230 lanes to be set up in 2018. BDF intends to install about 800 such lanes across all of Malaysia’s checkpoints by 2020.\n\n" +
            json.dumps(
                {"DateTime": [
                    {"Sentence1": "More than 160 automated lanes were installed in 2023, with another 230 lanes to be set up in 2024.",
                    "Sentence2": "More than 160 automated lanes were installed in 2015, with another 230 lanes to be set up in 2018.",
                    "Reason": "Sentence2 states the automated lanes were installed in 2015 and more to be set up in 2018, whereas Sentence1 states 2023 and 2024 respectively.",
                    },

                    {"Sentence1": "ICA intends to install about 800 such lanes across all of Singapore’s checkpoints by 2026.",
                    "Sentence2": "BDF intends to install about 800 such lanes across all of Malaysia’s checkpoints by 2020.",
                    "Reason": "Sentence2 states the installation will be completed by 2026, whereas Sentence2 states it will be completed by 2020."
                    }
                ]
                }
            )
        },
        {
            "input1": "The community of Willetton in Perth’s south was shaken after reports surfaced on local news platforms. The incident reportedly took place in High Street before 11.30pm on May 4.",
            "input2": "The community of Willetton in Sydney’s south was shaken after reports surfaced on local news platforms. The incident reportedly took place in Low Street before 12.45pm on June 19.",
            "output": "Input1: The community of Willetton in Perth’s south was shaken after reports surfaced on local news platforms. The incident reportedly took place in High Street before 11.30pm on May 4.\n\n" +
            "Input2: The community of Willetton in Sydney’s south was shaken after reports surfaced on local news platforms. The incident reportedly took place in Low Street before 12.45pm on June 19.\n\n" +
            json.dumps(
                {"DateTime": [
                    {"Sentence1": "The incident reportedly took place in High Street before 11.30pm on May 4.",
                    "Sentence2": "The incident reportedly took place in Low Street before 12.45pm on June 19.",
                    "Reason": "The date and time of the incident in Sentence2 (June 19, 12.45pm) does not match with the date and time in Sentence1 (May 4, 11.30pm)."
                    }]
                }
            )
        }
    ]
