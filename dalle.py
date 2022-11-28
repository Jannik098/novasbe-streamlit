#!/usr/bin/env python
# coding: utf-8

# # ** DALL E PROMPT GENERATOR**
# 
# 

# # **Import API**


# # Streamlit Web App

# In[2]:


import streamlit as st


# In[ ]:


st.set_page_config(page_title="Nova SBE - DALL E Team", page_icon=":tada:", layout="wide")

if "page" not in st.session_state:
    st.session_state["page"] = 1

empty = st.empty()

if st.button("Next"):
    st.session_state["page"] += 1

if st.button("Previous"):
    st.session_state["page"] -= 1

if st.session_state["page"] == 1:
    empty.write("Page 1")
elif st.session_state["page"] == 2:
    empty.write("Page 2")
elif st.session_state["page"] == 3:
    empty.write("Page 3")
else:
    empty.write(">3 page")

# Add a title and intro text
st.title('DALL-E 2 WEB APP')
st.text('This is a web app to allow Nova students to easily play around with AI image generation!')
st.text('Simply answer our questions and we will help you to create your first AI image')


# In[ ]:

if st.session_state["page"] == 1:
    theme_list = ['Select Theme', "Oil painting", "Unreal Engine", "Photorealistic"]
    theme_result = st.selectbox("Select your image theme:", theme_list)
    st.write(f'You have picked {theme_result}')


# In[ ]:

if st.session_state["page"] == 2:
    subject_list = ['Select Subject', "Panda", "Astronaut", "Racing Car"]
    subject_result = st.selectbox("Select your image subject:", subject_list)
    st.write(f'You have picked {subject_result}')

# In[ ]:


#action_list = ['Select Action', "Eat", "Sleep", "Compete", "Fight"]

#action_result = st.selectbox("Select your image action:", action_list)

#st.write(f'You have picked {action_result}')


