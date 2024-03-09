#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install --upgrade openai
from openai import OpenAI
client = OpenAI(api_key="")


# In[2]:


resume = "Resume: "


file_path = 'resume.txt'

# Open the text file and append its contents to the string
with open(file_path, 'r', encoding='utf-8') as file:
    document_content = file.read()
    resume += document_content


# In[3]:


jd = "job description: "


file_path = 'jd.txt'

# Open the text file and append its contents to the string
with open(file_path, 'r', encoding='utf-8') as file:
    document_content = file.read()
    jd += document_content


# In[5]:


system_prompt = "role: You are a job expert you've worked as a hiring manager for decades and have personally applied to millions of jobs and have got respones from a lot of them. You are a collection of all the understanding of the job market  and how to get a good job. You were also a teach lead at multiple companies and a star in the world of programming and have recruited thousands of highly talented employess adn just budidng interns into your oragnization your self using your experience as a hiring manager in your parallel job. "
temperature = 2
user_prompt= "Problem: I need the following resume tailored for the job decription" + resume + 'Job Description:' + jd


# In[6]:


def get_response( user_prompt, system_prompt = 'Answer the following', temperature = 0.5 ):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content":system_prompt },
            {"role": "user", "content": user_prompt }])
    return completion.choices[0].message


# In[7]:


Chat_response = get_response(user_prompt, system_prompt, temperature )


# In[8]:


print (Chat_response.content)

