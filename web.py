import os
import pickle
import streamlit as st  # type: ignore
from streamlit_option_menu import option_menu  # type: ignore

st.set_page_config(page_title='Prediction Of Disease Outbreaks',
                   layout='wide',
                   page_icon='🩺')

# Load trained models
diabetes_model = pickle.load(open(r"E:\AI Internship\Predictions\training_models\diabetes_model.sav", "rb"))
heart_model = pickle.load(open(r"E:\AI Internship\Predictions\training_models\heart_model.sav", "rb"))
parkinsons_model = pickle.load(open(r"E:\AI Internship\Predictions\training_models\parkinsons_model.sav", "rb"))

# Sidebar Menu
with st.sidebar:
    selected = option_menu(
        'Prediction Of Disease Outbreak System',
        ['Diabetes Prediction', 'Heart Disease Prediction', '🧠 Parkinsons Disease Prediction'],
        menu_icon='hospital-fill',
        icons=['activity', 'heart', 'brain']
    )

# Diabetes Prediction
if selected == 'Diabetes Prediction':
    st.title('🩺 Diabetes Prediction using ML')

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0)
        Skinthickness = st.number_input('Skin Thickness Value', min_value=0.0)
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function', min_value=0.0)

    with col2:
        Glucose = st.number_input('Glucose Level', min_value=0.0)
        Insulin = st.number_input('Insulin Level', min_value=0.0)
        Age = st.number_input('Age of Person', min_value=0)

    with col3:
        Bloodpressure = st.number_input('Blood Pressure Value', min_value=0)
        BMI = st.number_input('BMI Value', min_value=0.0)

    if st.button('🔍 Predict Diabetes'):
        user_input = [Pregnancies, Glucose, Bloodpressure, Skinthickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            st.success('🛑 The Person is **Diabetic**')
        else:
            st.success('✅ The Person is **Not Diabetic**')

# Heart Disease Prediction
elif selected == 'Heart Disease Prediction':
    st.title('💖 Heart Disease Prediction using ML')

    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

    with col1:
        age = st.number_input('Age', min_value=0)
        chol = st.number_input('Cholesterol Level', min_value=0)
        exang = st.number_input('Exercise Induced Angina (0/1)', min_value=0, max_value=1)

    with col2:
        sex = st.number_input('Sex (0 = Female, 1 = Male)', min_value=0, max_value=1)
        fbs = st.number_input('Fasting Blood Sugar (>120 mg/dl) (0/1)', min_value=0, max_value=1)
        oldpeak = st.number_input('ST Depression Induced by Exercise', min_value=0.0)

    with col3:
        cp = st.number_input('Chest Pain Type (0-3)', min_value=0, max_value=3)
        restecg = st.number_input('Resting Electrocardiographic Results (0-2)', min_value=0, max_value=2)
        slope = st.number_input('Slope of the Peak Exercise ST Segment (0-2)', min_value=0, max_value=2)

    with col4:
        trestbps = st.number_input('Resting Blood Pressure', min_value=0)
        thalach = st.number_input('Maximum Heart Rate Achieved', min_value=0)
        ca = st.number_input('Number of Major Vessels (0-3)', min_value=0, max_value=3)
        thal = st.number_input('Thalassemia (1-3)', min_value=1, max_value=3)

    if st.button('🔍 Predict Heart Disease'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        heart_prediction = heart_model.predict([user_input])

        if heart_prediction[0] == 1:
            st.success('🛑 The Person **has Heart Disease**')
        else:
            st.success('✅ The Person **does NOT have Heart Disease**')

# Parkinson's Disease Prediction
elif selected == '🧠 Parkinsons Disease Prediction':
    st.title('🧠 Parkinsons Disease Prediction using ML')

    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

    with col1:
        
        MDVP_Fo_Hz = st.number_input('MDVP:Fo(Hz)', min_value=0.0)
        MDVP_Fhi_Hz = st.number_input('MDVP:Fhi(Hz)', min_value=0.0)
        MDVP_Flo_Hz = st.number_input('MDVP:Flo(Hz)', min_value=0.0)
        MDVP_Jitter_ = st.number_input('MDVP:Jitter(%)', min_value=0.0)
        spread2 = st.number_input('Spread2', min_value=0.0)

    with col2:
        MDVP_Jitter_Abs = st.number_input('MDVP:Jitter(Abs)', min_value=0.0)
        MDVP_RAP = st.number_input('MDVP:RAP', min_value=0.0)
        MDVP_PPQ = st.number_input('MDVP:PPQ', min_value=0.0)
        Jitter_DDP = st.number_input('Jitter:DDP', min_value=0.0)
        MDVP_Shimmer = st.number_input('MDVP:Shimmer', min_value=0.0)

    with col3:
        MDVP_Shimmer_dB = st.number_input('MDVP:Shimmer(dB)', min_value=0.0)
        Shimmer_APQ3 = st.number_input('Shimmer:APQ3', min_value=0.0)
        Shimmer_APQ5 = st.number_input('Shimmer:APQ5', min_value=0.0)
        MDVP_APQ = st.number_input('MDVP:APQ', min_value=0.0)
        Shimmer_DDA = st.number_input('Shimmer:DDA', min_value=0.0)
        D2=st.number_input('D2',min_value=0.0)

    with col4:
        PPE = st.number_input('PPE', min_value=0.0)
        NHR = st.number_input('NHR', min_value=0.0)
        HNR = st.number_input('HNR', min_value=0.0)
        RPDE = st.number_input('RPDE', min_value=0.0)
        DFA = st.number_input('DFA', min_value=0.0)
        spread1 = st.number_input('Spread1', min_value=0.0)

    if st.button('🔍 Predict Parkinsons Disease'):
        user_input = [ MDVP_Fo_Hz, MDVP_Fhi_Hz, MDVP_Flo_Hz, MDVP_Jitter_, spread2,
                    MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ, Jitter_DDP, MDVP_Shimmer, 
                    D2, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, 
                    Shimmer_DDA, PPE, NHR, HNR, RPDE, DFA, spread1]  # D2 was missing

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            st.success('🛑 The Person **has Parkinsons Disease**')
        else:
            st.success('✅ The Person **does NOT have Parkinsons Disease**')
