
from promptflow.core import tool

from scipy.spatial import distance
from sentence_transformers import SentenceTransformer, util
import re
# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(input: str) -> str:
   
#     row_pattern = r'\| (Actions|Event Description) \| (.*?) \| (.*?) \|'
#     input1_actions = None
#     input2_actions = None

# # Extract Input1 and Input2 if in the same row as "Actions"
#     discrepancies_less_than_05 = []
#     model = SentenceTransformer('all-MiniLM-L6-v2')
#     matches = re.findall(row_pattern, input)
#     for match in matches:
#         discrepancytype = match[0]
#         input1_actions = match[1].strip()
#         input2_actions = match[2].strip()
#         discrepancyreason = match[3]
        
#         embeddings_inputA = model.encode(input1_actions, convert_to_tensor=True)
#         embeddings_inputB = model.encode(input2_actions, convert_to_tensor=True)

#     # Calculate cosine similarity between corresponding embeddings
#         cosine_similarities = util.pytorch_cos_sim(embeddings_inputA, embeddings_inputB)

#         if cosine_similarities.item() <= 0.65:
#             discrepancies_less_than_05.append(discrepancytype, input1_actions, input2_actions, cosine_similarities.item(), discrepancyreason)

#     # # Print the discrepancies with cosine similarity less than 0.5
#     print("| Type of Discrepancy | Input1 | Input2 | Cosine Similarity | Explanation |")
#     print("|---------------------|--------|--------|-------------------|-------------|")
#     for discrepancytype, input1_actions, input2_actions, cosine_similarities, discrepancyreason in discrepancies_less_than_05:
#         print(f"| {discrepancytype} | {input1_actions} | {input2_actions} | {cosine_similarities:.2f} | {discrepancyreason}")

    lines = input.strip().split('\n')
    model = SentenceTransformer('all-MiniLM-L6-v2')
    cosine_sim = []
    lines[0] += f" Cosine Similarity |"
    lines[1] += f" --- |"
    for line in lines[2:]:
        columns = line.strip('|').split('|')
        input1 = columns[1].strip() 
        input2 = columns[2].strip() 
        explanation = columns[3].strip() 
        if "NA" not in explanation:
            embeddings_inputA = model.encode(input1, convert_to_tensor=True)
            embeddings_inputB = model.encode(input2, convert_to_tensor=True)
            cosine_similarities = util.pytorch_cos_sim(embeddings_inputA, embeddings_inputB)
            # if cosine_similarities.item() <= 0.7:
            cosine_sim.append(round(cosine_similarities.item(), 2))
        else:
            cosine_sim.append("NA")
    for idx, line in enumerate(lines[2:]):
        columns = line.strip('|').split('|')
        columns.append(f" {cosine_sim[idx]} |")  # Append the cosine similarity value
        lines[idx + 2] = '|'.join(columns)  # Update the line
    
    # Construct the updated Markdown table
    updated_table = "\n".join(lines)
    return updated_table