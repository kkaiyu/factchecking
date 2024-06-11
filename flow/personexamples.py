from promptflow.core import tool
import json


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def person_examples():
    return [
        {
            "input": "Input1: A woman was charged on Thursday (May 9) with the murder of a 56-year-old man at a condominium along Beach Road. Li Ye, a 37-year-old Chinese national, is accused of causing the death of Lim Lai Guan in a unit at City Gate Residences at about 1.40am on May 8. Li was arrested at the scene and a knife was seized.\n\n" +
            "Input2: A man was charged on Thursday (May 9) with the murder of a 56-year-old man at a condominium along Beach Road. Xiao Ming, a 40-year-old Burmese national, is accused of causing the death of Lim Lai Guan in a unit at City Gate Residences at about 1.40am on May 8. Li was arrested at the scene and a knife was seized.\n\n",
            "output": "Input1: A woman was charged on Thursday (May 9) with the murder of a 56-year-old man at a condominium along Beach Road. Li Ye, a 37-year-old Chinese national, is accused of causing the death of Lim Lai Guan in a unit at City Gate Residences at about 1.40am on May 8. Li was arrested at the scene and a knife was seized.\n\n" +
            "Input2: A man was charged on Thursday (May 9) with the murder of a 56-year-old man at a condominium along Beach Road. Xiao Ming, a 40-year-old Burmese national, is accused of causing the death of Lim Lai Guan in a unit at City Gate Residences at about 1.40am on May 8. Li was arrested at the scene and a knife was seized.\n\n" +
            json.dumps(
                {"Person": [
                    {"Sentence1": "A woman was charged on Thursday (May 9) with the murder of a 56-year-old man at a condominium along Beach Road.",
                    "Sentence2": "A man was charged on Thursday (May 9) with the murder of a 56-year-old man at a condominium along Beach Road.",
                    "Reason": "The accused in Sentence1 is a woman, but in Sentence2, it is a man",
                    },

                    {"Sentence1": " Li Ye, a 37-year-old Chinese national, is accused of causing the death of Lim Lai Guan in a unit at City Gate Residences at about 1.40am on May 8.",
                    "Sentence2": "Xiao Ming, a 40-year-old Burmese national, is accused of causing the death of Lim Lai Guan in a unit at City Gate Residences at about 1.40am on May 8.",
                    "Reason": "The name, age and nationaity of the accused in Sentence2 (Xiao Ming, 40 years old, Burmese) does not match the name, age and nationality of the accused in Sentence1 (Li Ye, 37 years old, Chinese)"
                    }
                ]
                }
            )
        },
        {
            "input": "Input1: A 22-year-old man who was arrested earlier this week after allegedly attempting to flee from the police and having a samurai sword in his car, was charged in a district court on May 17.\n\n" +
            "Input2: A 39-year-old man who was arrested earlier this week after allegedly attempting to flee from the police and having a gun in his van, was charged in a district court on July 2.\n\n" +
            json.dumps(
                {"DateTime": [
                    {"Sentence1": "A 22-year-old man who was arrested earlier this week after allegedly attempting to flee from the police and having a samurai sword in his car, was charged in a district court on May 17.",
                    "Sentence2": "A 39-year-old man who was arrested earlier this week after allegedly attempting to flee from the police and having a gun in his van, was charged in a district court on July 2.",
                    "Reason": "The date of the court charge in Sentence2 (July) 2) does not match with the date in Sentence1 (May 17)."
                    }],
                "Object": [
                    {"Sentence1": "A 22-year-old man who was arrested earlier this week after allegedly attempting to flee from the police and having a samurai sword in his car, was charged in a district court on May 17.",
                    "Sentence2": "A 39-year-old man who was arrested earlier this week after allegedly attempting to flee from the police and having a gun in his van, was charged in a district court on July 2.",
                    "Reason": "The object found in the vehicle is a samurai sword in Sentence1, but in Sentence2, it is a gun. Also, the type of vehicle in Sentence1 is a car, but in Sentence2, it is a van."
                    }]
                }
            ),

            "output": "Input1: A 22-year-old man who was arrested earlier this week after allegedly attempting to flee from the police and having a samurai sword in his car, was charged in a district court on May 17.\n\n" +
            "Input2: A 39-year-old man who was arrested earlier this week after allegedly attempting to flee from the police and having a gun in his van, was charged in a district court on July 2.\n\n" +
            json.dumps(
                {"DateTime": [
                    {"Sentence1": "A 22-year-old man who was arrested earlier this week after allegedly attempting to flee from the police and having a samurai sword in his car, was charged in a district court on May 17.",
                    "Sentence2": "A 39-year-old man who was arrested earlier this week after allegedly attempting to flee from the police and having a gun in his van, was charged in a district court on July 2.",
                    "Reason": "The date of the court charge in Sentence2 (July) 2) does not match with the date in Sentence1 (May 17)."
                    }],
                "Object": [
                    {"Sentence1": "A 22-year-old man who was arrested earlier this week after allegedly attempting to flee from the police and having a samurai sword in his car, was charged in a district court on May 17.",
                    "Sentence2": "A 39-year-old man who was arrested earlier this week after allegedly attempting to flee from the police and having a gun in his van, was charged in a district court on July 2.",
                    "Reason": "The object found in the vehicle is a samurai sword in Sentence1, but in Sentence2, it is a gun. Also, the type of vehicle in Sentence1 is a car, but in Sentence2, it is a van."
                    }],
                "Person": [
                    {"Sentence1": "A 22-year-old man who was arrested earlier this week after allegedly attempting to flee from the police and having a samurai sword in his car, was charged in a district court on May 17.",
                    "Sentence2": "A 39-year-old man who was arrested earlier this week after allegedly attempting to flee from the police and having a gun in his van, was charged in a district court on July 2.",
                    "Reason": "The age of the man in Sentence2 (39 years old) does not match the age in Sentence1 (22 years old)"
                    }], 
                }
            ),
        } 
    ]
