
from promptflow import tool
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
import re

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(input1: str) -> str:

# Initialize the VADER sentiment analyzer
    sid = SentimentIntensityAnalyzer()
    row_pattern = r'\| (Actions|Event Description) \| (.*?) \| (.*?) \| (.*?) \|'
    input1_actions = None
    input2_actions = None

# Extract Input1 and Input2 if in the same row as "Actions"
    discrepancies = []
    matches = re.findall(row_pattern, input)
    for match in matches:
        discrepancytype = match[0]
        input1_actions = match[1].strip()
        input2_actions = match[2].strip()
        discrepancyreason = match[3].strip()
        sentiment_score1 = sid.polarity_scores(input1_actions)
        # sentiment_score1 = score1[compound]
        sentiment_score2 = sid.polarity_scores(input2_actions)
        # sentiment_score2 = score2[compound]
    if discrepancies:
        for discrepancytype, input1_actions, input2_actions, sentiment_score1, sentiment_score2, discrepancyreason in discrepancies:
            return(f"| Type of Discrepancy | Input1 | Input2 | Sentiment Score 1 | Sentiment Score 2 | Explanation |\n|---------------------|--------|--------|-------------------|-------------------|-------------|\n| {discrepancytype} | {input1_actions} | {input2_actions} | {sentiment_score1:.2f} | {sentiment_score2:.2f} | {discrepancyreason}")