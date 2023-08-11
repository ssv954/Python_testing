import streamlit as st
from joblib import load
from sklearn.preprocessing import StandardScaler

model_load = load('titatic_survival.joblib')

# web title
st.title('Titanic Survival Prediction')

# side bar
st.sidebar.title('Menu')
menu = ['Home', 'Prediction']
st.sidebar.selectbox('', menu)

# input and scaling data
scaler = StandardScaler()

ag = st.slider('Age', 0.42, 80.0, 30.0)
sibsp = st.slider('SibSp', 0, 8, 0)
parch = st.slider('Parch', 0, 9, 0)
fare = st.slider('Fare', 0.0, 512.30, 32.20)

# predict button
btn = st.button('Predict')

st.write(ag, sibsp, parch, fare)

if btn:
    param = [[ag, sibsp, parch, fare]]
    predicted = model_load.predict(param)

    if predicted == 1:
        st.write('Survive')
    else:
        st.write('Pass away')


# command run this file
# 'streamlit run app.py --client.showErrorDetails=false'