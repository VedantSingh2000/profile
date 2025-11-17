import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Vedant Singh | Data Analyst Portfolio",
    page_icon="😀",
    layout="wide"
)

# ---- DARK BACKGROUND CSS ----
st.markdown("""
    <style>
        body {
            background-color: #0E1117;
            color: white;
        }
        .stApp {
            background-color: #0E1117;
        }
        .sidebar .sidebar-content {
            background-color: #111827 !important;
        }
    </style>
""", unsafe_allow_html=True)


# --- SIDEBAR ---
st.sidebar.header("Contact Info")

st.sidebar.markdown("[LinkedIn](https://your-link-here)")
st.sidebar.markdown("[GitHub](https://your-link-here)")

st.sidebar.markdown("---")
st.sidebar.header("Key Skills")
st.sidebar.write("Python, SQL, Power BI, Machine Learning, Streamlit")


# --- HEADER ---
st.title("VEDANT SINGH")
st.subheader("Data Analyst | Data Science Aspirant")

st.header("About Me")
st.info("Passionate about turning data into actionable insights.")

st.markdown("---")  


# ---- Project Card Function ----
def project_card(title, description, tech, achievement, link):
    st.markdown(
        f"""
        <div style="background-color:#1A1C24; padding:15px; border-radius:10px; margin-bottom:12px;">
            <h4 style="color:#4FC3F7;">{title}</h4>
            <p><strong>Description:</strong> {description}</p>
            <p><strong>Technologies:</strong> {tech}</p>
            <p><strong>Achievement:</strong> {achievement}</p>
            <a href="{link}" style="color:#4FC3F7; font-weight:bold;">💻 View GitHub Repository</a>
        </div>
        """,
        unsafe_allow_html=True
    )


# --- PROJECTS ---
st.header("Featured Projects")


with st.expander("Customer Segmentation Dashboard"):
    project_card(
        "Customer Segmentation Dashboard",
        "Built a customer segmentation and prediction dashboard.",
        "Python, Streamlit, Random Forest, KMeans",
        "Interactive dashboard with 80%+ accuracy",
        "Your_Project_Repo_Link"
    )


with st.expander("Twitter Sentiment Classification"):
    project_card(
        "Twitter Sentiment Classification",
        "Sentiment analysis on ~14.6K tweets.",
        "NLTK, TF-IDF, Logistic Regression",
        "Achieved ~80% accuracy",
        "Your_Project_Repo_Link"
    )


with st.expander("Resume Classification"):
    project_card(
        "Resume Classification",
        "Classified different types of resumes.",
        "Python, Pandas, TF-IDF, Scikit-learn",
        "Built a complete ML pipeline",
        "Your_Project_Repo_Link"
    )


# --- TECHNICAL SKILLS ---
st.header("Technical Skills")

col1, col2, col3 = st.columns(3)

col1.subheader("Programming")
col1.write("- Python\n- SQL")

col2.subheader("Tools")
col2.write("- Pandas\n- NumPy\n- Power BI\n- MySQL")

col3.subheader("Machine Learning")
col3.write("- Scikit-learn\n- LightGBM\n- Data Preprocessing")

st.markdown("---")

st.write("© 2025 Vedant Singh | Data Analyst Portfolio")

