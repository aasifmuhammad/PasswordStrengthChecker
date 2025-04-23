import re # re means regular expression
import streamlit as st

# page styling
st.set_page_config(page_title="Password Strength Checker", page_icon="🔑", layout="centered")

#custom css

st.markdown("""
<style>
            .main {
                text-align:center;
            }
            .stTextInput {
                width: 60% !important;
                margin: auto;
            }
            .stButton button {
                width: 50%;
                background-color: #4CAF50;
                color: white;
                font-size: 18px;
            }
            .stButton button:hover {
            background-color: #45a049;
            }
</style>
""", unsafe_allow_html=True)

#page title and description
st.title("🐺 Password Strength Generator")
st.write("Enter Your Password below to its secured or not! 🛡️")

# Password Strength Checking Function
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1 #increase score by 1
    else:
        feedback.append("⚠️ Password should be **atleast 8 characters long**.")

    if re.search(r"[A-Z]", password) and re.search("[a-z]", password):
        score += 1 #increase score by 1
    else:
        feedback.append("⚠️ Password should be include **both Uppercase [A-Z] & Lowercase [a-z] **.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("⚠️ Password should be include **at least one number (0-9) **.")

    # add special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("⚠️ Include **atleast one special character (!@#$%^&*) **.")

    # Password Strength Display
    if score == 4:
        st.success("🛡️ **Strong Password** your Password is secure.")
    elif score == 3 :
        st.info("🚨 ** Moderate Password ** - Consider improving security by adding more feature.")
    else:
        st.error("😔 **Weak Password** - Follow the suggestion below to strength it. ")
    
    #For Feedback
    if feedback:
        with st.expander("💪 **Keep your password strong**"):
            for item in feedback:
                st.write(item)
    password = st.text_input("Enter Your Password: ", type="password", help="Ensure your password s strong 💪")

    #Button Working
    if st.button("Check Strength"):
        if password:
            check_password_strength(password)
        else:
            st.warning("⚠️ Please enter a password first!") #show warning message if the field is empty.