import streamlit as st
import pandas as pd
from annotated_text import annotated_text

# Set page configuration
st.set_page_config(
    page_title="Final Mark Calculator",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Apply dark mode theme
st.markdown(
    """
    <style>
    body {
        background-color: #0E1117;
        color: white;
    }
    input, select, textarea {
        background-color: #161B22 !important;
        color: white !important;
    }
    .stButton>button {
        background-color: #1F6FEB;
        color: white;
    }
    .stTable {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

##### google form link

# Function to toggle the visibility of the sidebar
def toggle_sidebar():
    if 'sidebar_visible' not in st.session_state:
        st.session_state.sidebar_visible = True


# Sidebar for feedback form
if st.session_state.get('sidebar_visible', False):
    with st.sidebar:
        st.header("Feedback Form")
        feedback_form_url = "https://docs.google.com/forms/d/e/1FAIpQLSe0yf7dPDmsvSlL27nQTtbxjXdcCRe6QN-3BUGSVO3LgO5TFA/viewform?usp=sf_link"  # Replace with your Google Form URL
        if st.button("Provide Feedback"):
            js = f"window.open('{feedback_form_url}', '_blank')"
            html = f"<script>{js}</script>"
            st.markdown(html, unsafe_allow_html=True)



# App Title
st.title("Final Mark Calculator")
st.markdown("---")


st.text("This program uses the following equation to calculate the required A2 mark:")
st.latex(r'''
    FM = (SM \cdot w_{SM}) + (A1 \cdot w_{A1}) + (A2 \cdot w_{A2}) 
    ''')

st.latex(r'''
    A2 = \frac{FM - (SM \cdot w_{SM}) - (A1 \cdot w_{A1})}{w_{A2}}
    ''')

st.text("Where:")
annotated_text("Final Mark = 75% for ",
               ("Distinction", ""),
               ", 50% for ",
               ("Pass", ""))

st.text("SM = Semester Mark")
st.text("A1 = Assessment 1 Mark")

st.text("w_sm = Weight of semester mark in %")
st.text("w_a1 = Weight of A1 in %")
st.text("w_a2 = Weight of A2 in %")


st.header("Enter Marks")
sm = st.number_input("Semester Mark (SM):", min_value=0.0, max_value=100.0, step=0.1)
a1 = st.number_input("Assessment 1 Mark (A1):", min_value=0.0, max_value=100.0, step=0.1)

st.header("Enter the Weights (%)")
w_sm = st.number_input(
    "Weight of Semester Mark (w_SM):", min_value=0.0, max_value=100.0, value=20.0, step=0.1
)
w_a1 = st.number_input(
    "Weight of Assessment 1 (w_A1):", min_value=0.0, max_value=100.0, value=30.0, step=0.1
)
w_a2 = st.number_input(
    "Weight of Assessment 2 (w_A2):", min_value=0.0, max_value=100.0, value=50.0, step=0.1
)

# Validate Weights
total_weight = w_sm + w_a1 + w_a2
if total_weight != 100.0:
    st.error("The sum of the weights must equal 100%. Please adjust the weights.")
else:
    if st.button("📊 Calculate Required A2 Marks"):
        # Convert weights to decimals
        w_sm_dec = w_sm / 100
        w_a1_dec = w_a1 / 100
        w_a2_dec = w_a2 / 100

        # Calculate required A2 marks
        required_a2_pass = (50 - (sm * w_sm_dec) - (a1 * w_a1_dec)) / w_a2_dec
        required_a2_distinction = (75 - (sm * w_sm_dec) - (a1 * w_a1_dec)) / w_a2_dec

        # Round results
        required_a2_pass = round(required_a2_pass, 2)
        required_a2_distinction = round(required_a2_distinction, 2)

        # Prepare Results
        if required_a2_pass < 0:
            result_pass = "Already achieved"
        elif required_a2_pass > 100:
            result_pass = "Not achievable"
        else:
            result_pass = f"{required_a2_pass}%"
            if required_a2_pass < 40:
                result_pass += " \n\n(Note: Minimum 40% required in A2 to pass.)"

        if required_a2_distinction < 0:
            result_distinction = "Already achieved"
        elif required_a2_distinction > 100:
            result_distinction = "Not achievable"
        else:
            result_distinction = f"{required_a2_distinction}%"

        # Display Results in a Table
        st.markdown("---")
        st.header("Results")

        results_df = pd.DataFrame({
            ' ': ['A2 Mark Required'],
            'Pass': [result_pass],
            'Distinction': [result_distinction]
        }).set_index(' ')

        st.table(results_df.style.set_properties(**{'color': 'white'}))
