
from promptflow.client import load_flow
import streamlit as st
import pandas as pd

# load Prompt Flow from parent folder
flow_path = "flow"
f = load_flow(flow_path)

st.title('Cross Checking between Documents')


input1 = st.text_input("Input 1")
input2 = st.text_input("Input 2")

st.button(label="Run", key=None)

flow_result = f(Input1=input1, Input2=input2)

outputfilter = flow_result["output"]
output = flow_result["extractdiscrepancies"]

st.subheader("Absolute Discrepancies")
st.markdown(output)

st.subheader("Filtered Discrepancies")
st.markdown(outputfilter)

# rows = outputfilter.strip().split('\n')

    # Extract header from the first row
# header = [cell.strip() for cell in rows[0].split('|') if cell.strip()]
    
#     # Extract data rows
# data_rows = [row.split('|') for row in rows[2:]]
   
#     # Create DataFrame
# df = pd.DataFrame(data_rows, columns=header)

# print(df)
# st.subheader("\nEntities present in both Input 1 and Input 2")

# for i in entity_output:
#     st.markdown("- " + i)
# st.subheader("Categorised Entities")
# st.markdown(entity_output)


# if 'entity_output_history' not in st.session_state:
#    st.session_state.entity_output_history = []
# if 'outputfilter_history' not in st.session_state:
#    st.session_state.outputfilter_history = []
# if 'input1_history' not in st.session_state:
#     st.session_state.input1_history = []
# if 'input2_history' not in st.session_state:
#     st.session_state.input2_history = []
# if 'output_history' not in st.session_state:
#    st.session_state.output_history = []

# if st.button("Save Output"):
#     st.session_state.input1_history.append(input1)
#     st.session_state.input2_history.append(input2)
#     st.session_state.entity_output_history.append(entity_output)
#     st.session_state.output_history.append(output)
#     st.session_state.outputfilter_history.append(outputfilter)
    

# selected_output = st.selectbox("Select output to display:", list(range(len(st.session_state.outputfilter_history))))
# if selected_output is not None:
#     st.write("Selected Input:")
#     st.write(st.session_state.input1_history[selected_output])
#     st.write(st.session_state.input2_history[selected_output])

    # st.write("Selected Output:")
   
   
    # st.write(st.session_state.output_history[selected_output])
    # st.write(st.session_state.outputfilter_history[selected_output])
    # st.write(st.session_state.entity_output_history[selected_output])