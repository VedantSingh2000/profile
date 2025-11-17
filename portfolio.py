import streamlit as st
from PIL import Image

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Vedant Portfolio",
    page_icon="✨",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
    body { background-color: #0d1117; color: white; }
    .title { font-size: 45px; font-weight: 700; color: #4F46E5; text-align: center; margin-bottom: 5px; }
    .subtitle { font-size: 22px; text-align: center; color: #6B7280; margin-bottom: 20px; }
    .section-title { font-size: 30px; font-weight: 600; color: #10B981; margin-top: 30px; }
    .card { background-color: #161b22; padding: 15px; border-radius: 12px; border: 1px solid #30363d; margin-bottom: 10px; }
    a { color: #3b82f6; text-decoration: none; }
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.image("pic.jpg", width=180)

st.sidebar.markdown("### 🔗 Connect")
st.sidebar.markdown("[GitHub](https://github.com)")
st.sidebar.markdown("[LinkedIn](https://linkedin.com)")

st.sidebar.write("---")
st.sidebar.markdown("### 📧 Contact")
st.sidebar.write("vedants953@gmail.com")
st.sidebar.write("+91 6261462323")

# ---------------- HEADER ----------------
st.markdown('<div class="title">✨ Vedant Singh Portfolio</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Data Analyst | ML Enthusiast | Python Developer</div>', unsafe_allow_html=True)
st.write("---")

# ---------------- ABOUT ----------------
st.markdown('<div class="section-title">👤 About Me</div>', unsafe_allow_html=True)
st.write("Hey! I'm **Vedant**, a Data Analyst & ML enthusiast passionate about building dashboards, ML pipelines, and extracting insights from data.")

# ---------------- SKILLS ----------------
st.markdown('<div class="section-title">🛠 Skills</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card"><h4>Programming</h4><p>Python, SQL, Pandas, NumPy, Matplotlib</p></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card"><h4>ML Techniques</h4><p>Classification, Feature Engineering, TF-IDF, Clustering</p></div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card"><h4>Tools</h4><p>Power BI, Jupyter Notebook, VS Code, Excel</p></div>', unsafe_allow_html=True)

# ---------------- PROJECTS ----------------
st.markdown('<div class="section-title">📂 Projects</div>', unsafe_allow_html=True)

st.markdown('<div class="card"><h4>Housing Price Prediction</h4><p>Predicting house prices using LightGBM and Power BI dashboard.</p></div>', unsafe_allow_html=True)
st.markdown('<div class="card"><h4>Twitter Sentiment Classification</h4><p>NLP model using TF-IDF and Logistic Regression (~14.6K tweets analyzed).</p></div>', unsafe_allow_html=True)
st.markdown('<div class="card"><h4>Resume Analysis & Classification</h4><p>ML + Gemini API pipeline to automatically classify resumes and extract insights.</p></div>', unsafe_allow_html=True)

# ---------------- EDUCATION & CERTIFICATIONS ----------------
st.markdown('<div class="section-title">🎓 Education & Certifications</div>', unsafe_allow_html=True)

education_html = '''
<div class="card">
<h4>Education</h4>
<p><b>B.Tech – Computer Science & Engineering</b><br>
Shri Vaishnav Vidyapeeth Vishwavidyalaya, Indore (2019–2023)<br>
CGPA: 7.5</p>
<p><b>Class XII – PCM</b><br>
St. Joseph's Convent Sr. Sec. School, Ratlam (2018)<br>
79.6% CBSE</p>
</div>
'''

certifications_html = '''
<div class="card">
<h4>Certifications</h4>
<p>• Google Advanced Data Analytics – 2024</p>
<p>• Google AI Essentials – 2024</p>
<p>• ExcelR Data Scientist/Analyst – 2025</p>
</div>
'''

st.markdown(education_html, unsafe_allow_html=True)
st.markdown(certifications_html, unsafe_allow_html=True)

# ---------------- CONTACT SECTION ----------------
st.markdown('<div class="section-title">📞 Contact Me</div>', unsafe_allow_html=True)
st.markdown('''
<div class="card">
<p><strong>📍 Location:</strong> Ratlam, M.P.</p>
<p><strong>📧 Email:</strong> vedants953@gmail.com</p>
<p><strong>📞 Phone:</strong> +91 6261462323</p>
<p><strong>🔗 Links:</strong><br>
<a href='https://github.com' target='_blank'>GitHub</a><br>
<a href='https://linkedin.com' target='_blank'>LinkedIn</a></p>
</div>
''', unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.write("---")
st.write("© 2025 Vedant Singh | Portfolio Website")
