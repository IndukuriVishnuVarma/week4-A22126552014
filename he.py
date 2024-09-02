import streamlit as st

st.title('Welcome to BMI Calculator')

weight=st.number_input("Enter your weight (in kgs)")

status=st.radio('Select your height format: ',
                  ('cms', 'meters', 'feet'))

if status=='cms':
    height=st.number_input('Centimeters')
elif status=='meters':
    height=st.number_input('Meters')
else:
    height=st.number_input('Feet')

if st.button('Calculate BMI'):
    if weight <= 0 or height <= 0:
        st.error("Please enter valid weight and height")
    else:
        if status=='cms':
            bmi=weight/((height/100)**2)
        elif status=='meters':
            bmi=weight/(height ** 2)
        else:
            bmi=weight/(((height/3.28))**2)

        bmi=round(bmi, 2)
        st.text("Your BMI Index is {}.".format(bmi))

        if bmi < 16:
            st.error("You are Extremely Underweight")
        elif bmi >= 16 and bmi < 18.5:
            st.warning("You are Underweight")
        elif bmi >= 18.5 and bmi < 25:
            st.success("Healthy")
        elif bmi >= 25 and bmi < 30:
            st.warning("Overweight")
        elif bmi >= 30:
            st.error("Extremely Overweight")