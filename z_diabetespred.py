import numpy as np
import pickle 
import streamlit as st
loaded_model=pickle.load(open('trained_model.sav','rb'))
def pred(input_data):
  x=np.array(input_data).reshape(1,-1)
  prediction=loaded_model.predict(x)
  if prediction[0]==0:
    return 'The person is not diabetic'
  else:
    return 'The person is diabetic'
st.title('Diabetes prediction')
Pregnancies=st.text_input('Number of Pregnancies')
Glucose=st.text_input('Glucose level')
BloodPressure=st.text_input('BloodPressure level')
SkinThickness=st.text_input('SkinThickness value')
Insulin=st.text_input('Insuline level')
BMI=st.text_input('BMI value')
DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function value')
Age=st.text_input('Age')
diagnosis=''  
if st.button('Diabets test result'):
     diagnosis=pred([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
st.success(diagnosis)

