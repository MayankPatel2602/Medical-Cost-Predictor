import streamlit as st
import pickle
import numpy as np

rf_random =  pickle.load(open('model.pkl','rb'))

st.header('Medical Cost Predictor')

age = st.number_input('Age:',step=1)

sex = st.selectbox('Gender:',['Male','Female'])

if sex=='Male':
    sex=1
else:
    sex=0

bmi = st.number_input('BMI(Avg value is 30):')

no_children= st.selectbox('No of Children',[0,1,2,3,4,5])

smoker = st.selectbox('Is Smoker',['Yes',"No"])

if smoker=='Yes':
    smoker=1
else:
    smoker=0

region = st.selectbox('Region',['North East','North West','South East','South West'])

region_northeast=0
region_northwest=0
region_southeast=0
region_southwest=0

if region=='North East':
    region_northeast=1
elif region == 'North West':
    region_northwest=1
elif region == 'South East':
    region_southeast=1
else:
    region_southwest=1

query = np.array([age,sex,bmi,no_children,smoker,region_northeast,region_northwest,region_southeast,region_southwest])
query = query.reshape(1,9)
prediction = rf_random.predict(query)[0]

if st.button('Predict Cost'):
    st.header('Predicted Cost is {}'.format(round(prediction)))


