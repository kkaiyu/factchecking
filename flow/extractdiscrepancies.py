
from promptflow.core import tool


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(input: str) -> str:
    lines = input.strip().split('\n')

# Filter out rows with "Actions" and "Event Description"
    filtered_lines = [line for line in lines if "Actions" not in line and "Event Description" not in line]

# Join the filtered lines to create the output string
    output_str = '\n'.join(filtered_lines)

    return(output_str)