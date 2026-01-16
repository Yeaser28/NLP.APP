import os
import streamlit as st
import google.genai as genai
from dotenv import load_dotenv

# ---------------- ENV ----------------
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def get_client():
    return genai.Client(api_key=GEMINI_API_KEY)

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="NLP Application",
    page_icon="🧠",
    layout="wide"
)

# ---------------- SESSION STATE ----------------
if "users" not in st.session_state:
    st.session_state.users = {}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "current_user" not in st.session_state:
    st.session_state.current_user = None

# ---------------- TITLE ----------------
st.title("🧠 NLP Application")

# ---------------- SIDEBAR AUTH ----------------
with st.sidebar:
    st.header("User Authentication")

    if not st.session_state.logged_in:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Log In"):
            if username in st.session_state.users and \
               st.session_state.users[username]["password"] == password:
                st.session_state.logged_in = True
                st.session_state.current_user = username
                st.success("Login successful")
                st.rerun()
            else:
                st.error("Invalid credentials")

        st.markdown("---")
        st.subheader("Sign Up")

        new_user = st.text_input("New Username", key="su_user")
        new_pass = st.text_input("New Password", type="password", key="su_pass")
        email = st.text_input("Email", key="su_email")

        if st.button("Sign Up"):
            if new_user in st.session_state.users:
                st.error("User already exists")
            else:
                st.session_state.users[new_user] = {
                    "password": new_pass,
                    "email": email
                }
                st.success("Signup successful! Please login.")

    else:
        st.success(f"Welcome, {st.session_state.current_user}")
        if st.button("Log Out"):
            st.session_state.logged_in = False
            st.session_state.current_user = None
            st.rerun()

# ---------------- MAIN APP ----------------
if not st.session_state.logged_in:
    st.info("Please login from sidebar")
    st.stop()

client = get_client()

st.subheader("🔧 Choose NLP Feature")

feature = st.selectbox(
    "Select Feature",
    [
        "Sentiment Analysis",
        "Language Translation",
        "Text Summarization",
        "Text Generation",
        "Text Classification",
        "Text Extraction",
        "Topic Modeling",
        "Named Entity Recognition",
        "Language Detection"
    ]
)

text = st.text_area("Enter your text")

target_language = ""
if feature == "Language Translation":
    target_language = st.text_input("Target Language (e.g. English, French)")

if st.button("Run"):
    if not text.strip():
        st.warning("Text required")
        st.stop()

    if feature == "Sentiment Analysis":
        prompt = f"Analyze sentiment: Positive, Negative or Neutral.\nText: {text}"

    elif feature == "Language Translation":
        prompt = f"Translate this text to {target_language}:\n{text}"

    elif feature == "Text Summarization":
        prompt = f"Summarize the following text:\n{text}"

    elif feature == "Text Generation":
        prompt = f"Generate text based on:\n{text}"

    elif feature == "Text Classification":
        prompt = f"Classify the following text into a category:\n{text}"

    elif feature == "Text Extraction":
        prompt = f"Extract key information from this text:\n{text}"

    elif feature == "Topic Modeling":
        prompt = f"Identify main topics in this text:\n{text}"

    elif feature == "Named Entity Recognition":
        prompt = f"Find named entities and their types:\n{text}"

    elif feature == "Language Detection":
        prompt = f"Detect the language of this text:\n{text}"

    with st.spinner("Processing..."):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

    st.markdown("### 🧠 Result")
    st.write(response.text.strip())

