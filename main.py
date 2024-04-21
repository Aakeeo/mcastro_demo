from dotenv import load_dotenv
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from third_party.linkedin import scrape_linkedin_profile
import streamlit as st

load_dotenv()

st.title('Sales Agent Helper')
url_input = st.text_input("Enter the LinkedIn profile URL:")
prompt_input = st.text_area("Enter the prompt for the AI:")
submit_button = st.button('Generate Summary')

if submit_button and url_input:

    st.write('Processing LinkedIn profile...')
    linkedin_data = scrape_linkedin_profile(url_input)

    summary_template = """
     Given the linkedIn information {information} about a person from I want you to create:
     {prompt_input}
"""


    summary_prompt_template = PromptTemplate(
        input_variables=["information", "prompt_input"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    result = chain.run(information=linkedin_data, prompt_input=prompt_input)
    st.write("Generated Text:")
    st.write(result)








