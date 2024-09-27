import streamlit as st

st.title('BMI Calculator')
st.subheader('This application is designed to calculate BMI')
name = st.text_input('Name',placeholder ='Enter your name')
gender = st.radio('Gender',('Male','Female'))
if(gender=='Male'):
    initial = 'Mr'
else:
    initial = 'Mrs'
if(name!=''):
    st.text(f'Hello{initial}{name},Please enter appropriate fields')


weight = st.slider('Range of weight',min_value =0,max_value=250)
height = st.slider('Range of height',min_value=0,max_value=300)
click = st.button('Calculate BMI')
if(click==True):
    bmi=weight/height**2*10000
    st.subheader(f'BMI : {round(bmi)}')
    if(bmi>=30):
        st.title('obese')
    elif(bmi>=25):
        st.title('Over weight')
    elif(bmi>=20):
        st.title('Normal weight')
        st.balloons()
    else:
        st.title('Underweight')













# from function import *
# bmi(78,175)
# bmi(64,166)

