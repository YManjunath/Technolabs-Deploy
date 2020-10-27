import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st
import joblib

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

data = open('credit.pkl','rb')
classifier = joblib.load(data)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(EDUCATION,MARRIAGE,AGE,LIMIT_BAL,PAY_1,BILL_AMT1,BILL_AMT2,BILL_AMT3,BILL_AMT4,BILL_AMT5,BILL_AMT6,PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6):

    """Let's Authenticate the Banks Note
    This is using docstrings for specifications.
    ---
    parameters:
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values

    """

    prediction=classifier.predict([[EDUCATION,MARRIAGE,AGE,LIMIT_BAL,PAY_1,BILL_AMT1,BILL_AMT2,BILL_AMT3,BILL_AMT4,BILL_AMT5,BILL_AMT6,PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6]])
    print(prediction)
    return prediction



def main():
    st.title("Credit Card Default")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Credit Card Default ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    EDUCATION = st.text_input("EDUCATION","Enter 1-Graduate School; 2-University; 3-High School; 4-Others")
    MARRIAGE = st.text_input("MARRIAGE","Enter 1-Married; 2-Single; 3-Others")
    AGE = st.text_input("AGE","Enter the Age")
    LIMIT_BAL = st.text_input("LIMIT_BAL","Enter the Limit Balance($NT)")
    PAY_1 = st.text_input("PAY_1","Enter the Last Month Paid Amount")
    BILL_AMT1 = st.text_input("BILL_AMT1","Enter the Bill Statement Amount for Respective Month")
    BILL_AMT2 = st.text_input("BILL_AMT2","Enter the Bill Statement Amount for Respective Month")
    BILL_AMT3 = st.text_input("BILL_AMT3","Enter the Bill Statement Amount for Respective Month")
    BILL_AMT4 = st.text_input("BILL_AMT4","Enter the Bill Statement Amount for Respective Month")
    BILL_AMT5 = st.text_input("BILL_AMT5","Enter the Bill Statement Amount for Respective Month")
    BILL_AMT6 = st.text_input("BILL_AMT6","Enter the Bill Statement Amount for Respective Month")
    PAY_AMT1 = st.text_input("PAY_AMT1","Enter the Bill Statement Amount for Respective Month")
    PAY_AMT2 = st.text_input("PAY_AMT2","Enter the Bill Statement Amount for Respective Month")
    PAY_AMT3 = st.text_input("PAY_AMT3","Enter the Bill Statement Amount for Respective Month")
    PAY_AMT4 = st.text_input("PAY_AMT4","Enter the Bill Statement Amount for Respective Month")
    PAY_AMT5 = st.text_input("PAY_AMT5","Enter the Bill Statement Amount for Respective Month")
    PAY_AMT6 = st.text_input("PAY_AMT6","Enter the Bill Statement Amount for Respective Month")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(EDUCATION,MARRIAGE,AGE,LIMIT_BAL,PAY_1,BILL_AMT1,BILL_AMT2,BILL_AMT3,BILL_AMT4,BILL_AMT5,BILL_AMT6,PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6)
        if result == 0:
            st.success('Credit Card Holder Will Not Default {}'.format(result))
        if result == 1:
            st.success('Credit Card Holder Will Default {}'.format(result))
    if st.button("About"):
        st.text("A app that predicts if Credit Card Holder will Default on his upcoming month credit or Not")
    html_temp = """<h4 style="text-align:center;">Built with Streamlit © Y Manjunatha🧡</h2>"""
    st.markdown(html_temp,unsafe_allow_html=True)

if __name__=='__main__':
    main()
