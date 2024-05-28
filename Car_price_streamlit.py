import streamlit as st
import numpy as np
import pandas as pd
import datetime
import joblib

# Load the RandomForest model
model = joblib.load('car_price11.pkl')

date_time = datetime.datetime.now()

def main(): 
    html_temp = """
     <div style="background-color:lightblue;padding:16px">
     <h2 style="color:black;text-align:center;">Car Price Prediction Using ML</h2>
     </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
   
    st.markdown("##### Are you planning to sell your car !?\n##### So let's try evaluating the price..")
    
    st.write('')
    st.write('')
    p1 = st.number_input('What is the current ex-showroom price of the car? (In Lakhs)', 2.5, 25.0, step=1.0) 
    p2 = st.number_input('What is the distance completed by the car in Kilometers?', 100, 500000, step=100)

    s1 = st.selectbox('What is the fuel type of the car?', ('Petrol', 'Diesel', 'CNG'))
    p3 = {'Petrol': 0, 'Diesel': 1, 'CNG': 2}[s1]
        
    s2 = st.selectbox('Are you a dealer or an individual?', ('Dealer', 'Individual'))
    p4 = {'Dealer': 0, 'Individual': 1}[s2]
        
    s3 = st.selectbox('What is the transmission type?', ('Manual', 'Automatic'))
    p5 = {'Manual': 0, 'Automatic': 1}[s3]
        
    p6 = st.slider("Number of owners the car previously had", 0, 3)
    
    years = st.number_input('In which year was the car purchased?', 1990, date_time.year, step=1)
    p7 = date_time.year - years
    
    data_new = pd.DataFrame({
        'Present_Price': [p1],
        'Kms_Driven': [p2],
        'Fuel_Type': [p3],
        'Seller_Type': [p4],
        'Transmission': [p5],
        'Owner': [p6],
        'Age': [p7]
    })

    if st.button('Predict'):
        try:
            prediction = model.predict(data_new)
            if prediction > 0:
                st.balloons()
                st.success(f'You can sell the car for {prediction[0]:.2f} lakhs')
            else:
                st.warning("You will not be able to sell this car!")
        except Exception as e:
            st.error(f"Prediction error: {e}")

if __name__ == '__main__':
    main()
