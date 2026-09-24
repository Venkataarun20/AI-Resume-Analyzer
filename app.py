import streamlit as st
from PyPDF2 import PdfReader

# Page Settings
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and get an ATS score based on detected skills.")

# Upload Resume
uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    # Read PDF
    pdf = PdfReader(uploaded_file)

    text = ""

    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    # Display Resume Content
    st.subheader("Resume Content")
    st.text_area("Extracted Text", text, height=250)

    # Skills Database
    skills = [
        "Python",
        "Java",
        "C++",
        "SQL",
        "Machine Learning",
        "Deep Learning",
        "Data Science",
        "TensorFlow",
        "PyTorch",
        "Pandas",
        "NumPy",
        "Git",
        "GitHub",
        "Docker",
        "AWS",
        "Azure",
        "Power BI",
        "Tableau",
        "Hadoop",
        "Spark"
    ]

    # Find Skills
    found_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    # Missing Skills
    missing_skills = []

    for skill in skills:
        if skill not in found_skills:
            missing_skills.append(skill)

    # Display Skills
    st.subheader("✅ Skills Found")
    if found_skills:
        st.write(found_skills)
    else:
        st.warning("No matching skills found.")

    st.subheader("❌ Missing Skills")
    st.write(missing_skills)

    # ATS Score
    score = int((len(found_skills) / len(skills)) * 100)

    st.subheader("📊 ATS Score")
    st.progress(score)
    st.success(f"ATS Score: {score}%")

    # Suggestions
    st.subheader("💡 Suggestions")

    if score >= 80:
        st.success("Excellent Resume! Strong skill coverage.")
    elif score >= 50:
        st.info("Good Resume. Add more relevant technical skills.")
    else:
        st.error("Resume needs improvement. Add more technical skills and projects.")