import streamlit as st
import numpy as np
import pickle
model=pickle.load(open('model.pkl','rb'))
st.title("The prediction For a Concrete compressive Strength ")
cement=st.number_input("Enter the cement Quantity:(In density)")
blast_furnace_slag=st.number_input("Enter Furnace Slag Quantity:(In density)")
fly_ash=st.number_input("Enter the Fly_Ash Quantity:(In density)")
water=st.number_input("Enter the Water Quantity:(In density)")
superplasticizer=st.number_input("Enter the SuperPlasticizer Quantity:(In density)")
coarse_aggregate=st.number_input("Enter the Coarse Aggregate Quantity:(In density)")
fine_aggregate=st.number_input("Enter the Fine Aggregate Quantity:(In density)")
age=st.number_input("How many days ?From created",min_value=0,)
value=model.predict(np.array([[cement,blast_furnace_slag,fly_ash,water,superplasticizer,coarse_aggregate,fine_aggregate,age]]))
but=st.button("Predict")
if but:
    st.text(f"Your value is(in Mpa): {value}")




