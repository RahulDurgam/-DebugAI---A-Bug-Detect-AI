from openai import OpenAI 
import streamlit as st

st.title("'DebugAI'- A Bug Detect AI")

# Read the API key and Setup an OpenAI Client
f = open("keys/.open_api_key.txt")
key = f.read()
client = OpenAI(api_key=key)

# Take User's input 
prompt = st.text_area("Write your Python Code")

# If the button is clicked , generate responses
if st.button("Generate") == True:
    response = client.chat.completions.create(
                model="gpt-3.5-turbo-16k",
                messages=[
            {"role": "system", "content": """You are a helpful AI Assistant.
                
                                            Given a Python code you need to check the code and find the errors in the code,explain them more clearly with examples and fix them."""},

            {"role": "user", "content": prompt}
            ]
    )
    
    # Print the respnse on web app
    st.write(response.choices[0].message.content)