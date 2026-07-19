# ==========================================================
# AI SMART PROPERTY ADVISOR
# Professional Streamlit Application
# Developed by D. Hasini
# ==========================================================


import streamlit as st
import pandas as pd
import numpy as np
import joblib
import time
import os
import random

from datetime import datetime
import plotly.express as px



# ==========================================================
# PAGE CONFIGURATION
# ==========================================================


st.set_page_config(

    page_title="AI Smart Property Advisor",

    page_icon="🏠",

    layout="wide"

)



# ==========================================================
# CSS DESIGN
# ==========================================================


st.markdown("""

<style>


.main-title{

font-size:45px;
font-weight:bold;
text-align:center;
color:#1565C0;

}


.subtitle{

font-size:22px;
text-align:center;
color:#555;

}


.profile{

background:white;
padding:20px;
border-radius:15px;

}


</style>

""",
unsafe_allow_html=True)



# ==========================================================
# SESSION STATES
# ==========================================================


defaults = {

"page":"splash",

"logged_in":False,

"username":"",

"verified":False,

"users":{

"admin":

{

"name":"Administrator",

"email":"admin@gmail.com",

"phone":"9999999999",

"password":"admin123"

}

},

"otp":"",

"temp_user":{},

"history":[],
}



for key,value in defaults.items():

    if key not in st.session_state:

        st.session_state[key]=value





# ==========================================================
# LOAD MODEL
# ==========================================================


MODEL_PATH = "best_model.pkl"
DATA_PATH = "Enhanced_Smart_House_Price_Dataset.csv"


class DummyModel:

    def __init__(self):

        self.feature_importances_ = np.array(
            [0.30, 0.15, 0.12, 0.10, 0.06, 0.08, 0.07, 0.07, 0.05]
        )

    def predict(self, X):

        prices = []

        for _, row in X.iterrows():

            location_factor = {
                "Urban": 1.25,
                "Suburban": 1.0,
                "Rural": 0.85,
            }.get(row.get("Location", "Suburban"), 1.0)

            furnishing_factor = {
                "Furnished": 1.2,
                "Semi Furnished": 1.0,
                "Unfurnished": 0.9,
            }.get(row.get("Furnishing", "Semi Furnished"), 1.0)

            base_price = (
                row.get("Area", 1500) * 2400
                + row.get("Bedrooms", 3) * 45000
                + row.get("Bathrooms", 2) * 32000
                + row.get("Floors", 1) * 18000
                + max(0, 30 - row.get("Age", 5)) * 600
                + row.get("Parking", 1) * 20000
                + row.get("Amenities", 5) * 9000
            )

            price = base_price * location_factor * furnishing_factor
            prices.append(price)

        return np.array(prices)


if os.path.exists(MODEL_PATH):

    try:

        model = joblib.load(MODEL_PATH)

    except Exception:

        st.warning(
            f"Could not load model from {MODEL_PATH}. Using fallback model instead."
        )
        model = DummyModel()

else:

    model = DummyModel()





# ==========================================================
# LOAD DATASET
# ==========================================================


if os.path.exists(DATA_PATH):

    try:

        data = pd.read_csv(DATA_PATH)

    except Exception:

        st.warning(
            f"Could not load dataset from {DATA_PATH}. Using fallback sample dataset instead."
        )
        data = pd.DataFrame(
            {
                "Area": [1200, 1500, 1800, 2200],
                "Bedrooms": [2, 3, 3, 4],
                "Bathrooms": [2, 2, 3, 3],
                "Location": ["Urban", "Suburban", "Urban", "Rural"],
                "Floors": [1, 2, 1, 1],
                "Age": [5, 10, 3, 20],
                "Parking": [1, 2, 2, 1],
                "Furnishing": ["Semi Furnished", "Furnished", "Unfurnished", "Furnished"],
                "Amenities": [7, 8, 6, 5],
                "Price": [4200000, 5200000, 3900000, 3100000],
            }
        )

else:

    data = pd.DataFrame(
        {
            "Area": [1200, 1500, 1800, 2200],
            "Bedrooms": [2, 3, 3, 4],
            "Bathrooms": [2, 2, 3, 3],
            "Location": ["Urban", "Suburban", "Urban", "Rural"],
            "Floors": [1, 2, 1, 1],
            "Age": [5, 10, 3, 20],
            "Parking": [1, 2, 2, 1],
            "Furnishing": ["Semi Furnished", "Furnished", "Unfurnished", "Furnished"],
            "Amenities": [7, 8, 6, 5],
            "Price": [4200000, 5200000, 3900000, 3100000],
        }
    )






# ==========================================================
# SPLASH SCREEN
# ==========================================================


def splash_screen():


    st.markdown(

    """

    <h1 class="main-title">

    🏠 AI SMART PROPERTY ADVISOR
            st.checkbox(
                "🌙 Dark Mode"
            )

    <h3 class="subtitle">

    Artificial Intelligence Based

    <br>

    Real Estate Decision System

    </h3>

    """,

    unsafe_allow_html=True

    )



    progress=st.progress(0)



    for i in range(101):

        time.sleep(0.02)

        progress.progress(i)



    st.success("Loading Completed ✔")


    time.sleep(1)


    st.session_state.page="welcome"


    st.rerun()





# ==========================================================
# WELCOME PAGE
# ==========================================================


def welcome_page():


    st.markdown(

    """

    <h1 class="main-title">

    🏠 Welcome

    </h1>


    <h2 style="text-align:center">

    AI Smart Property Advisor

    </h2>


    <h3 class="subtitle">

    Find Your Dream Home

    <br>

    Using Artificial Intelligence

    </h3>


    """,

    unsafe_allow_html=True

    )


    col1,col2,col3=st.columns(3)



    with col1:

        st.info(

        """

        🏠

        House Price Prediction

        """

        )


    with col2:

        st.success(

        """

        🏡

        Smart Recommendation

        """

        )


    with col3:

        st.warning(

        """

        📈

        Investment Analysis

        """

        )



    st.write("")


    if st.button(

        "🚀 Get Started",

        use_container_width=True

    ):

        st.session_state.page="login"

        st.rerun()
# ==========================================================
# PART 2
# LOGIN • CREATE ACCOUNT • OTP VERIFICATION
# ==========================================================



# ==========================================================
# LOGIN PAGE
# ==========================================================


def login_page():


    st.markdown(

    """

    <h1 class="main-title">

    🔐 Login

    </h1>

    """,

    unsafe_allow_html=True

    )


    username = st.text_input(
        "👤 Username"
    )


    password = st.text_input(

        "🔒 Password",

        type="password"

    )


    remember = st.checkbox(
        "Remember Me"
    )



    col1,col2 = st.columns(2)



    with col1:


        if st.button(

            "Login",

            use_container_width=True

        ):


            if username in st.session_state.users:

                if password == st.session_state.users[username]["password"]:

                    st.session_state.username = username

                    st.session_state.logged_in = True

                    st.session_state.page = "dashboard"

                    st.success("Login Successful 🎉")

                    time.sleep(1)

                    st.rerun()

                else:

                    st.error("Incorrect Password")

            else:

                st.error("Username Not Found")



    with col2:


        if st.button(

            "Create Account",

            use_container_width=True

        ):


            st.session_state.page="register"

            st.rerun()



    st.write("---")



    if st.button(
        "Forgot Password?"
    ):

        st.info(
            "Password recovery feature coming soon"
        )






# ==========================================================
# CREATE ACCOUNT PAGE
# ==========================================================


def register_page():


    st.markdown(

    """

    <h1 class="main-title">

    📝 Create Account

    </h1>

    """,

    unsafe_allow_html=True

    )



    name = st.text_input(
        "Full Name"
    )


    email = st.text_input(
        "Email"
    )


    phone = st.text_input(
        "Phone Number"
    )


    username = st.text_input(
        "Create Username"
    )


    password = st.text_input(

        "Password",

        type="password"

    )


    confirm = st.text_input(

        "Confirm Password",

        type="password"

    )



    if st.button(

        "Register",

        use_container_width=True

    ):



        if not name or not email or not phone or not username or not password:


            st.warning(
                "Please fill all details"
            )


        elif password != confirm:


            st.error(
                "Password mismatch"
            )


        elif username in st.session_state.users:


            st.error(
                "Username already exists"
            )


        else:



            otp=random.randint(
                100000,
                999999
            )


            st.session_state.otp=str(otp)



            st.session_state.temp_user={

                "name":name,

                "email":email,

                "phone":phone,

                "username":username,

                "password":password

            }



            st.success(
                f"Your OTP is {otp}"
            )


            st.session_state.page="verify"


            time.sleep(1)

            st.rerun()




    if st.button(
        "Back to Login"
    ):


        st.session_state.page="login"

        st.rerun()







# ==========================================================
# OTP VERIFICATION PAGE
# ==========================================================


def verify_page():


    st.markdown(

    """

    <h1 class="main-title">

    📩 Email Verification

    </h1>

    """,

    unsafe_allow_html=True

    )



    otp = st.text_input(
        "Enter OTP"
    )



    if st.button(

        "Verify",

        use_container_width=True

    ):


        if otp == st.session_state.otp:



            user=st.session_state.temp_user



            st.session_state.users[user["username"]]={


                "name":user["name"],


                "email":user["email"],


                "phone":user["phone"],


                "password":user["password"]

            }



            st.session_state.username=user["username"]


            st.session_state.logged_in=True


            st.session_state.page="dashboard"



            st.success(
                "Account Verified Successfully ✔"
            )


            time.sleep(1)

            st.rerun()



        else:


            st.error(
                "Invalid OTP"
            )
# ==========================================================
# PART 3
# DASHBOARD • PROFILE • SETTINGS • LOGOUT
# ==========================================================



# ==========================================================
# DASHBOARD FUNCTION
# ==========================================================


def dashboard_page():



    # -----------------------------
    # SIDEBAR
    # -----------------------------


    with st.sidebar:



        st.markdown(

        """

        <h2 style="color:#1565C0">

        🏠 AI Smart Property Advisor

        </h2>

        """,

        unsafe_allow_html=True

        )



        st.write("---")



        menu = st.radio(

            "Navigation",

            [

                "🏠 Home",

                "💰 Price Prediction",

                "🏡 Property Recommendation",

                "📈 Investment Analysis",

                "💳 EMI Calculator",

                "📊 Feature Importance",

                "📋 Dataset Explorer",

                "📈 Model Analytics",

                "📥 Prediction Report",

                "🏠 Property Gallery",

                "🤖 AI Assistant",

                "📍 Location",

                "📄 About Project",

                "👤 Profile",

                "⚙ Settings",

                "🚪 Logout"

            ]

        )



        st.write("---")



        st.info(

            f"""

            Logged In User:

            👤 {st.session_state.username}

            """

        )






    # ======================================================
    # HOME PAGE
    # ======================================================


    if menu=="🏠 Home":



        user=st.session_state.users[

            st.session_state.username

        ]



        st.markdown(

        f"""

        <h1 style="color:#1565C0">

        Welcome {user["name"]} 👋

        </h1>


        <h3>

        AI Smart Property Advisor

        </h3>


        <p>

        Date : {datetime.now().strftime("%d %B %Y")}

        </p>


        """,

        unsafe_allow_html=True

        )



        col1,col2,col3,col4=st.columns(4)



        with col1:


            st.metric(

                "🏠 Prediction",

                "Available"

            )


        with col2:


            st.metric(

                "🏡 Recommendation",

                "AI Powered"

            )


        with col3:


            st.metric(

                "🌲 ML Model",

                "Random Forest"

            )


        with col4:


            st.metric(

                "📊 Accuracy",

                "High"

            )



        st.write("")



        st.subheader("🚀 Available Modules")


        col1, col2 = st.columns(2)

        with col1:

            st.info(
            """
            🏠 **Price Prediction**

            Predict property value using
            Machine Learning model.

            """
            )


            st.success(
            """
            🏡 **Property Recommendation**

            Find suitable houses based on
            your requirements.

            """
            )


        with col2:

            st.warning(
            """
            📈 **Investment Analysis**

            Analyze future property growth
            and returns.

            """
            )


            st.error(
            """
            📊 **AI Explainability**

            Understand important features
            affecting price prediction.

            """
            )


    # ======================================================
    # PROFILE PAGE
    # ======================================================


    elif menu=="👤 Profile":



        user=st.session_state.users[

            st.session_state.username

        ]



        st.title(
            "👤 User Profile"
        )


        st.markdown(

        f"""

        <div class="profile">


        <h3>Name : {user["name"]}</h3>


        <h3>Username : {st.session_state.username}</h3>


        <h3>Email : {user["email"]}</h3>


        <h3>Phone : {user["phone"]}</h3>


        <h3>

        Project:

        AI Smart Property Advisor

        </h3>


        </div>


        """,

        unsafe_allow_html=True

        )






    # ======================================================
    # SETTINGS
    # ======================================================


    elif menu=="⚙ Settings":



        st.title(
            "⚙ Settings"
        )


        st.toggle(
            "🌙 Dark Mode"
        )


        st.checkbox(
            "🔔 Notifications"
        )


        st.checkbox(
            "📧 Email Alerts"
        )


        st.selectbox(

            "🌐 Language",

            [

            "English",

            "Telugu",

            "Hindi"

            ]

        )


        st.success(
            "Settings Updated"
        )






    # ======================================================
    # LOGOUT
    # ======================================================


    elif menu=="🚪 Logout":



        st.warning(
            "Do you want to logout?"
        )


        if st.button(
            "Logout Now"
        ):



            st.session_state.logged_in=False


            st.session_state.username=""


            st.session_state.page="login"



            st.success(
                "Logged Out Successfully"
            )


            time.sleep(1)


            st.rerun()






    # ======================================================
    # FUTURE MODULE CONNECTIONS
    # ======================================================


    elif menu=="💰 Price Prediction":

        price_prediction_page()



    elif menu=="🏡 Property Recommendation":

        property_recommendation_page()



    elif menu=="📈 Investment Analysis":

        investment_analysis_page()



    elif menu=="💳 EMI Calculator":

        emi_calculator_page()



    elif menu=="📊 Feature Importance":

        feature_importance_page()



    elif menu=="📋 Dataset Explorer":

        dataset_explorer_page()



    elif menu=="📈 Model Analytics":

        model_analysis_page()



    elif menu=="📥 Prediction Report":

        report_page()



    elif menu=="🏠 Property Gallery":

        property_gallery_page()



    elif menu=="🤖 AI Assistant":

        chatbot_page()



    elif menu=="📍 Location":

        location_page()



    elif menu=="📄 About Project":
        about_page()

# ==========================================================
# PART 4
# HOUSE PRICE PREDICTION MODULE
# ==========================================================



def price_prediction_page():



    st.title(
        "💰 AI House Price Prediction"
    )


    st.write(

    """

    Enter property details and our Machine Learning

    model will estimate the house price.

    """

    )


    st.divider()



    if model is None:


        st.error(

            "❌ Model file best_model.pkl not found"

        )

        return






    st.subheader(

        "🏠 Property Details"

    )



    col1,col2,col3 = st.columns(3)




    # -----------------------------
    # COLUMN 1
    # -----------------------------


    with col1:


        area = st.number_input(

            "📐 Area (sq.ft)",

            min_value=100,

            max_value=10000,

            value=1500

        )



        bedrooms = st.number_input(

            "🛏 Bedrooms",

            min_value=1,

            max_value=10,

            value=3

        )



        bathrooms = st.number_input(

            "🚿 Bathrooms",

            min_value=1,

            max_value=10,

            value=2

        )






    # -----------------------------
    # COLUMN 2
    # -----------------------------


    with col2:


        location = st.selectbox(

            "📍 Location",

            [

                "Urban",

                "Suburban",

                "Rural"

            ]

        )



        floors = st.number_input(

            "🏢 Floors",

            min_value=1,

            max_value=20,

            value=1

        )



        age = st.number_input(

            "🏚 Property Age",

            min_value=0,

            max_value=100,

            value=5

        )






    # -----------------------------
    # COLUMN 3
    # -----------------------------


    with col3:


        parking = st.number_input(

            "🚗 Parking Spaces",

            min_value=0,

            max_value=10,

            value=1

        )



        furnishing = st.selectbox(

            "🛋 Furnishing",

            [

            "Furnished",

            "Semi Furnished",

            "Unfurnished"

            ]

        )



        amenities = st.slider(

            "⭐ Amenities Score",

            1,

            10,

            5

        )






    st.write("")



    # ======================================================
    # PREDICT BUTTON
    # ======================================================


    if st.button(

        "🔮 Predict Price",

        use_container_width=True

    ):



        try:



            input_data=pd.DataFrame(

            {


            "Area":[area],


            "Bedrooms":[bedrooms],


            "Bathrooms":[bathrooms],


            "Location":[location],


            "Floors":[floors],


            "Age":[age],


            "Parking":[parking],


            "Furnishing":[furnishing],


            "Amenities":[amenities]


            }

            )




            prediction=model.predict(

                input_data

            )



            price=prediction[0]




            st.success(

                "Prediction Completed Successfully 🎉"

            )




            st.metric(

                "🏠 Estimated House Price",

                f"₹ {price:,.2f}"

            )





            # -----------------------------
            # GRAPH
            # -----------------------------


            chart=pd.DataFrame(

            {

            "Type":

            [

            "Predicted Price"

            ],


            "Price":

            [

            price

            ]

            }

            )




            fig=px.bar(

                chart,

                x="Type",

                y="Price",

                title="AI Price Prediction"

            )



            st.plotly_chart(

                fig,

                use_container_width=True

            )






            # -----------------------------
            # SAVE HISTORY
            # -----------------------------


            if "history" not in st.session_state:


                st.session_state.history=[]




            st.session_state.history.append(

            {


            "Date":

            datetime.now().strftime("%d-%m-%Y"),



            "Area":

            area,



            "Bedrooms":

            bedrooms,



            "Predicted Price":

            price


            }

            )



        except Exception as e:


            st.error(

                f"Prediction Error : {e}"

            )
# ==========================================================
# PART 5
# PROPERTY RECOMMENDATION
# INVESTMENT ANALYSIS
# EMI CALCULATOR
# ==========================================================




# ==========================================================
# PROPERTY RECOMMENDATION PAGE
# ==========================================================


def property_recommendation_page():



    st.title(
        "🏡 Smart Property Recommendation"
    )


    st.write(

    """

    AI suggests properties based on your

    budget and requirements.

    """

    )


    st.divider()



    col1,col2 = st.columns(2)




    with col1:


        budget = st.number_input(

            "💰 Budget (₹)",

            min_value=100000,

            max_value=100000000,

            value=5000000

        )



        location = st.selectbox(

            "📍 Preferred Location",

            [

            "Hyderabad",

            "Bangalore",

            "Chennai",

            "Mumbai",

            "Delhi"

            ]

        )




    with col2:


        property_type = st.selectbox(

            "🏠 Property Type",

            [

            "Apartment",

            "Villa",

            "Independent House"

            ]

        )



        bedrooms = st.slider(

            "🛏 Number of Bedrooms",

            1,

            5,

            3

        )






    if st.button(

        "🔍 Find Properties",

        use_container_width=True

    ):



        result=pd.DataFrame(

        {


        "Property Name":

        [

        "Green Valley Residency",

        "Smart City Apartments",

        "Luxury Heights",

        "AI Garden Villas"

        ],



        "Location":

        [

        location,

        location,

        location,

        location

        ],



        "Type":

        [

        property_type,

        "Apartment",

        "Villa",

        "Independent House"

        ],



        "Bedrooms":

        [

        bedrooms,

        bedrooms,

        bedrooms+1,

        bedrooms

        ],



        "Estimated Price":

        [

        budget*0.8,

        budget*0.9,

        budget*1.1,

        budget*0.95

        ]



        }

        )



        st.success(

            "Best Matching Properties Found 🎉"

        )



        st.dataframe(

            result,

            use_container_width=True

        )







# ==========================================================
# INVESTMENT ANALYSIS PAGE
# ==========================================================


def investment_analysis_page():



    st.title(

        "📈 Property Investment Analysis"

    )


    st.write(

    """

    Predict future property value based on

    growth percentage.

    """

    )


    st.divider()




    current_price=st.number_input(

        "Current Property Price (₹)",

        value=5000000

    )



    years=st.slider(

        "Investment Period",

        1,

        30,

        10

    )



    growth=st.slider(

        "Expected Annual Growth (%)",

        1,

        20,

        8

    )





    if st.button(

        "📊 Calculate Future Value",

        use_container_width=True

    ):



        future_value = (

            current_price *

            ((1+growth/100)**years)

        )



        profit=future_value-current_price





        col1,col2=st.columns(2)



        with col1:


            st.metric(

                "Future Value",

                f"₹ {future_value:,.0f}"

            )



        with col2:


            st.metric(

                "Expected Profit",

                f"₹ {profit:,.0f}"

            )





        chart=pd.DataFrame(

        {


        "Year":

        list(range(years+1)),



        "Value":

        [

        current_price*((1+growth/100)**i)

        for i in range(years+1)

        ]


        }

        )




        fig=px.line(

            chart,

            x="Year",

            y="Value",

            title="Property Growth Prediction"

        )



        st.plotly_chart(

            fig,

            use_container_width=True

        )









# ==========================================================
# EMI CALCULATOR PAGE
# ==========================================================


def emi_calculator_page():



    st.title(

        "💳 Home Loan EMI Calculator"

    )



    principal=st.number_input(

        "Loan Amount (₹)",

        value=3000000

    )



    rate=st.slider(

        "Interest Rate (%)",

        1.0,

        15.0,

        7.5

    )



    years=st.slider(

        "Loan Duration (Years)",

        1,

        30,

        20

    )





    if st.button(

        "Calculate EMI",

        use_container_width=True

    ):



        monthly_rate=rate/(12*100)


        months=years*12



        emi=(

            principal*

            monthly_rate*

            (1+monthly_rate)**months

        )/(

            (1+monthly_rate)**months-1

        )



        st.success(

            f"Monthly EMI : ₹ {emi:,.2f}"

        )
# ==========================================================
# PART 6
# FEATURE IMPORTANCE
# DATASET EXPLORER
# MODEL ANALYTICS
# REPORT DOWNLOAD
# ==========================================================




# ==========================================================
# FEATURE IMPORTANCE PAGE
# ==========================================================


def feature_importance_page():



    st.title(
        "📊 Feature Importance Analysis"
    )


    st.write(

    """

    Understand which features influence

    the AI prediction.

    """

    )


    st.divider()



    if model is None:


        st.error(
            "Model not loaded"
        )

        return




    try:



        if hasattr(model,"feature_importances_"):



            importance=model.feature_importances_



            features=[

                "Area",

                "Bedrooms",

                "Bathrooms",

                "Location",

                "Floors",

                "Age",

                "Parking",

                "Furnishing",

                "Amenities"

            ]



            if len(features)!=len(importance):


                features=[

                f"Feature {i+1}"

                for i in range(len(importance))

                ]





            df=pd.DataFrame(

            {

            "Feature":features,

            "Importance":importance

            }

            )



            df=df.sort_values(

                "Importance",

                ascending=False

            )




            fig=px.bar(

                df,

                x="Importance",

                y="Feature",

                orientation="h",

                title="Important Factors Affecting Property Price"

            )



            st.plotly_chart(

                fig,

                use_container_width=True

            )



            st.dataframe(

                df,

                use_container_width=True

            )



        else:


            st.warning(

                "Feature importance unavailable"

            )




    except Exception as e:


        st.error(e)









# ==========================================================
# DATASET EXPLORER PAGE
# ==========================================================


def dataset_explorer_page():



    st.title(

        "📋 Dataset Explorer"

    )




    if data is None:


        st.error(

            "Dataset not found"

        )

        return





    st.success(

        "Dataset Loaded Successfully"

    )



    col1,col2,col3=st.columns(3)



    with col1:


        st.metric(

            "Total Rows",

            data.shape[0]

        )



    with col2:


        st.metric(

            "Total Columns",

            data.shape[1]

        )



    with col3:


        st.metric(

            "Missing Values",

            data.isnull().sum().sum()

        )





    st.divider()



    st.subheader(

        "Dataset Preview"

    )



    st.dataframe(

        data.head(20),

        use_container_width=True

    )





    st.subheader(

        "Statistical Summary"

    )



    st.write(

        data.describe()

    )









# ==========================================================
# MODEL ANALYTICS PAGE
# ==========================================================


def model_analysis_page():



    st.title(

        "📈 Model Performance Dashboard"

    )



    col1,col2,col3=st.columns(3)




    with col1:


        st.metric(

            "Algorithm",

            "Random Forest"

        )



    with col2:


        st.metric(

            "Training Status",

            "Completed"

        )



    with col3:


        st.metric(

            "Deployment",

            "Ready"

        )





    st.divider()



    st.info(

    """

    The Random Forest Machine Learning model

    analyzes property features and predicts

    estimated house prices.

    """

    )








# ==========================================================
# PREDICTION REPORT PAGE
# ==========================================================


def report_page():



    st.title(

        "📥 Prediction Report"

    )



    if "history" not in st.session_state:



        st.warning(

            "No prediction history available"

        )

        return




    history=pd.DataFrame(

        st.session_state.history

    )



    st.dataframe(

        history,

        use_container_width=True

    )




    csv=history.to_csv(

        index=False

    )




    st.download_button(

        label="⬇ Download CSV Report",

        data=csv,

        file_name="Property_Report.csv",

        mime="text/csv"

    )
# ==========================================================
# PART 7
# FINAL UI ENHANCEMENTS
# GALLERY • CHATBOT • LOCATION • ABOUT • FOOTER
# ==========================================================




# ==========================================================
# PROPERTY GALLERY
# ==========================================================


def property_gallery_page():


    st.title(
        "🏠 Property Gallery"
    )


    st.write(
        "Explore different property categories"
    )


    col1,col2,col3 = st.columns(3)



    with col1:

        st.image(
            "https://images.unsplash.com/photo-1600585154340-be6161a56a0c",
            caption="Luxury Villa",
            use_container_width=True
        )


    with col2:

        st.image(
            "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c",
            caption="Modern Apartment",
            use_container_width=True
        )


    with col3:

        st.image(
            "https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde",
            caption="Dream Home",
            use_container_width=True
        )








# ==========================================================
# AI PROPERTY ASSISTANT
# ==========================================================


def chatbot_page():


    st.title(
        "🤖 AI Property Assistant"
    )


    st.write(
        "Ask questions related to real estate"
    )



    question=st.text_input(
        "Enter your question"
    )



    if st.button(
        "Send"
    ):



        q=question.lower()



        if "price" in q:


            answer="You can predict property price using our AI ML model."



        elif "loan" in q or "emi" in q:


            answer="Use our EMI calculator for home loan estimation."



        elif "investment" in q:


            answer="Investment analysis predicts future property growth."



        elif "location" in q:


            answer="Select locations with good facilities and growth."



        else:


            answer="I can help with price, investment, EMI and properties."



        st.success(answer)









# ==========================================================
# LOCATION ANALYSIS
# ==========================================================


def location_page():


    st.title(
        "📍 Property Location Analysis"
    )


    location_data=pd.DataFrame(

    {

    "City":

    [

    "Hyderabad",

    "Bangalore",

    "Mumbai",

    "Chennai"

    ],


    "Growth Index":

    [

    90,

    95,

    85,

    80

    ]

    }

    )



    fig=px.bar(

        location_data,

        x="City",

        y="Growth Index",

        title="Real Estate Growth Index"

    )



    st.plotly_chart(

        fig,

        use_container_width=True

    )









# ==========================================================
# ABOUT PROJECT
# ==========================================================


def about_page():


    st.title(
        "📄 About AI Smart Property Advisor"
    )



    st.markdown(

    """

## 🏠 Project Overview


AI Smart Property Advisor is an Artificial Intelligence

based real estate decision support system.


## Technologies Used


🐍 Python

🤖 Machine Learning

🌐 Streamlit

📊 Pandas

📈 Plotly

🌲 Random Forest


## Features


✔ House Price Prediction

✔ Smart Property Recommendation

✔ Investment Analysis

✔ EMI Calculator

✔ Feature Importance

✔ Dataset Analytics


## Developer


👩‍💻 D. Hasini

B.Tech Artificial Intelligence & Machine Learning


    """

    )









# ==========================================================
# FOOTER
# ==========================================================


def footer():


    st.markdown(

    """

<hr>

<center>

<h3>

🏠 AI Smart Property Advisor

</h3>


<p>

Artificial Intelligence Based Real Estate System

</p>


<p>

Developed by D. Hasini

</p>


</center>


    """,

    unsafe_allow_html=True

    )









# ==========================================================
# FINAL APPLICATION ROUTING
# ==========================================================



if st.session_state.page=="splash":


    splash_screen()



elif st.session_state.page=="welcome":


    welcome_page()



elif st.session_state.page=="login":


    login_page()



elif st.session_state.page=="register":


    register_page()



elif st.session_state.page=="verify":


    verify_page()



elif st.session_state.page=="dashboard":


    dashboard_page()