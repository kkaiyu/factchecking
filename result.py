from promptflow.client import load_flow
import streamlit as sl

flow_path = load_flow("flow")
sl.title("Consistency Checker")
input1 = sl.text_input("Input 1")
input2 = sl.text_input("Input 2")
sl.button(label="Run", key=None)

flow_result = flow_path(Input1=input1, Input2=input2)

output = flow_result["discrepancies"]

sl.subheader("Discrepancies")
sl.markdown(output)

