import streamlit as st
from streamlit_chat import message
from bardapi import Bard
from bardapi import BardCookies
import json

cookie_dict = {
    "__Secure-1PSID": "your-key",
    "__Secure-1PSIDTS": "your-key",
    # Any cookie values you want to pass session object.
}

bard = BardCookies(cookie_dict=cookie_dict)

#response = bard.get_answer("what is ml")['content']
#print(response)
def generate_response(prompt):
    response = bard.get_answer(prompt)['content']
    return response

def get_text():
    input_text= st.text_input("CN bot: ","hey wassup?",key="input")
    return input_text

#ui
st.title('Personal Tutoring Bot')
#url = 'https://images.unsplash.com/photo-1685814783586-b5abaf7da7df?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1331&q=80'
# data-testid = "stAppViewContainer"
changes= '''
<style>
[data-testid = "stAppViewContainer"]
{
background-image:url(https://images.unsplash.com/photo-1685814783586-b5abaf7da7df?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1331&q=80);
background-size:cover;
}
</style>
'''
st.markdown(changes,unsafe_allow_html=True)

print(st.session_state)
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

#input
user_input = get_text()
if user_input:
   output=generate_response(user_input)
   #response =  generate_response(user_input)
   print(output)
   st.session_state['past'].append(user_input)
   st.session_state['generated'].append(output)


if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1,-1,-1 ):
        message(st.session_state['generated'][i],key=str(i))
        message(st.session_state['past'][i], key="user_" + str(i)), is_user==True

