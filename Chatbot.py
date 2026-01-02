import streamlit as st
from openai import OpenAI
from streamlit_chat import message

# ------------------ OpenAI Client ------------------
client = OpenAI(api_key="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")

# ------------------ API Calling Function ------------------
def api_calling(prompt):
    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt,
        max_output_tokens=300
    )
    return response.output_text

# ------------------ Streamlit UI ------------------
st.title("ChatGPT ChatBot With Streamlit and OpenAI")

# Initialize session state
if "user_input" not in st.session_state:
    st.session_state["user_input"] = []

if "openai_response" not in st.session_state:
    st.session_state["openai_response"] = []

# Clear chat button
if st.button("Clear Chat"):
    st.session_state["user_input"] = []
    st.session_state["openai_response"] = []

# ------------------ Input Box ------------------
def get_text():
    return st.text_input("Write here", key="input")

user_input = get_text()

# ------------------ Generate Response ------------------
if user_input:
    output = api_calling(user_input)
    output = output.lstrip("\n")

    st.session_state["user_input"].append(user_input)
    st.session_state["openai_response"].append(output)

# ------------------ Display Chat History ------------------
message_history = st.empty()

if st.session_state["user_input"]:
    for i in range(len(st.session_state["user_input"]) - 1, -1, -1):
        # User message
        message(
            st.session_state["user_input"][i],
            key=str(i),
            avatar_style="icons",
            is_user=True
        )

        # Bot response
        message(
            st.session_state["openai_response"][i],
            key=str(i) + "_bot",
            avatar_style="miniavs"
        )
