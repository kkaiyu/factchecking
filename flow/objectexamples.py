from promptflow.core import tool
import json


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def object_examples():
    return [
        {
            "input": "Input1: Li was arrested at the scene and a knife was seized. \n\n" +
            "Input2: Li was arrested at the scene and a gun was seized. ",
            "output": "Input1: Li was arrested at the scene and a knife was seized.\n\n" +
            "Input2: Li was arrested at the scene and a gun was seized.\n\n" +
            json.dumps(
                {"Object": [          
                    {"Sentence1": "Li was arrested at the scene and a knife was seized.",
                    "Sentence2": "Li was arrested at the scene and a gun was seized.",
                    "Reason": "The object seized at the scene is a knife in Sentence1, but in Sentence2, it is a gun."
                    }]
                }
            )
        }, 
    ]
