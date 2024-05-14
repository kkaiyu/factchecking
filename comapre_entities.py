from promptflow import tool
import json

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(Input1entities: list, Input2entities: list):

    # differences = [item for item in Input1entities if item not in Input2entities]

    # print("Strings present in Input1entities but absent in Input2entities:", differences)
    # unique_in_input1 = [item for item in Input1entities if item not in Input2entities]   
    # print("Strings in Input1 but not in Input2:", unique_in_input1)        # print unique elements in list2

    # unique_in_input2 = [item for item in Input2entities if item not in Input1entities]                           # store unique elements in list3
    # print("Strings in Input2 but not in Input1", unique_in_input2)         # print unique elements in list3
   
    # list1 = json.loads(Input1entities) if isinstance(Input1entities, str) else Input1entities
    # list2 = json.loads(Input2entities) if isinstance(Input2entities, str) else Input2entities


# Find items present in list1 and list2
    Input1 = json.loads(Input1entities)
    Input2 = json.loads(Input2entities)

    missing_items = [item for item in Input1 if item in Input2]

    sortedlist = sorted(missing_items)
    return sortedlist