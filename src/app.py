import sys
import os

# Dynamically add the project root to the Python path so it can find the 'src' module
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import streamlit as st
from src.extractors import pdf_extractor, docx_extractor
from src.services.llm_service import LLMService

# (The rest of your app.py code continues here...)
st.set_page_config(page_title="TalentVector", page_icon="📄", layout="wide")
import streamlit as st
from src.extractors import pdf_extractor, docx_extractor
from src.services.llm_service import LLMService

# App metadata config (MUST be the absolute first Streamlit command)
st.set_page_config(page_title="TalentVector", page_icon="📄", layout="wide")

def inject_custom_css():
    custom_css = """
    <style>
    /* Global selection overrides */
    ::selection {
        background-color: #160c0c !important;
        color: #F2F3D4 !important;
    }
    
    /* 1. Force the main Streamlit app background to off-white */
    .stApp {
        background-color: #F2F3d4;
        color: #160c0c;
    }

    /* FIX: Force native st.metric labels and numeric values to Ground Brown */
    div[data-testid="stMetricLabel"] div,
    div[data-testid="stMetricValue"] div,
    div[data-testid="stMetric"] * {
        color: #160c0c !important;
    }

    /* FIX: Force st.text_area and st.file_uploader inner labels to Ground Brown */
    div[data-testid="stWidgetLabel"] p,
    div[data-testid="stWidgetLabel"] label,
    div[data-testid="stWidgetLabel"] span {
        color: #160c0c !important;
    }

    /* 2. Make the Run Evaluation button solid black with white text */
    div.stButton > button:first-child {
        background-color: #160c0c !important;
        color: #F2F3D4 !important;
        border: none !important;
    }
    div.stButton > button:first-child:hover {
        background-color: #160c0c !important;
        color: #F2F3D4 !important;
    }

    /* 3. Small black box for 'Analysis Complete' */
    .black-success-box {
        background-color: #160c0c;
        color: #F2F3D4;
        padding: 8px 15px;
        border-radius: 4px;
        display: inline-block;
        font-weight: bold;
        margin-bottom: 20px;
    }

    /* 4. Solid black box for Core Judgment */
    .black-judgment-box {
        background-color: #160c0c;
        color: #F2F3D4;
        padding: 20px;
        border-radius: 6px;
        margin-bottom: 20px;
    }

    /* 5. Scrollable solid black boxes for Skills */
    .scrollable-black-box {
        background-color: #160c0c;
        color: #F2F3D4;
        padding: 15px;
        border-radius: 6px;
        height: 200px; 
        overflow-y: auto; 
    }
    
    /* Style the scrollbar to match the dark theme */
    .scrollable-black-box::-webkit-scrollbar {
        width: 8px;
    }
    .scrollable-black-box::-webkit-scrollbar-track {
        background: #F2F3D4; 
    }
    .scrollable-black-box::-webkit-scrollbar-thumb {
        background: #666666; 
        border-radius: 4px;
    }

    /* 6. Turn Job Description Input Box Solid Black */
    div[data-testid="stTextArea"] textarea {
        background-color: #160c0c !important;
        color: #F2F3D4 !important;
        border: 1px solid #160c0c !important;
    }
    div[data-testid="stTextArea"] textarea::placeholder {
        color: #888888 !important;
    }

    /* 7. Turn File Uploader Box Solid Brown with matching borders and styling */
    div[data-testid="stFileUploaderDropzone"] {
        background-color: #160c0c !important;
        color: #F2F3D4 !important;
        border: 2px dashed #F2F3D4 !important;
    }
    div[data-testid="stFileUploaderDropzone"] span,
    div[data-testid="stFileUploaderDropzone"] small,
    div[data-testid="stFileUploaderDropzone"] svg {
        color: #F2F3D4 !important;
        fill: #F2F3D4 !important;
    }
    div[data-testid="stFileUploaderDropzone"] button {
        background-color: #F2F3D4 !important;
        color: #160c0c !important;
        border: 1px solid #F2F3D4 !important;
    }

    /* 8. Force the text inside the green st.success banner to be white */
    div[data-testid="stNotification"] {
        color: #F2F3D4 !important;
    }
    div[data-testid="stNotification"] p {
        color: #F2F3D4 !important;
    }

    /* 9. Force the uploaded filename text wrapper inside the widget to be white */
    div[data-testid="stFileUploaderFilesContainer"] span, 
    div[data-testid="stFileUploaderFilesContainer"] div,
    div[data-testid="stFileUploaderFileName"] {
        color: #F2F3D4 !important;
    }

    /* 10. Custom Font-Style and Size scaling for the App Title */
    .custom-title {
        font-family: "Gigi", "Comic Sans MS", cursive !important;
        font-size: 4.5rem !important; 
        color: #160c0c !important;
        margin-top: 0px !important;
        margin-bottom: 5px !important;
        padding-top: 0px !important;
    }
    
    /* Ensure sub-captions match theme */
    div[data-testid="stCaptionContainer"] {
        color: #160c0c !important;
        opacity: 0.85;
    }

    /* 11. Custom styling for the User Guide Box */
    .user-guide-box {
        background-color: transparent;
        color: #160c0c;
        border: 2px solid #160c0c;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 25px;
    }
    .user-guide-box h3 {
        color: #160c0c !important;
        margin-top: 0;
        margin-bottom: 15px;
        font-size: 1.5rem;
    }
    .user-guide-box h4 {
        color: #160c0c !important;
        margin-top: 20px;
        margin-bottom: 10px;
        font-size: 1.2rem;
    }
    .user-guide-box ul, .user-guide-box ol {
        margin-bottom: 0;
    }
    .user-guide-box li {
        margin-bottom: 8px;
    }

    /* 12. Fix: Force subheaders and markdown titles to Ground Brown */
    div[data-testid="stHeader"] h2, 
    .stHeadingContainer h1, 
    .stHeadingContainer h2, 
    .stHeadingContainer h3, 
    .stHeadingContainer h4 {
        color: #160c0c !important;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

# Call this to set style overrides before rendering layout elements
inject_custom_css()

# Render custom styled application Title using the newly declared CSS class
st.markdown('<h1 class="custom-title">TalentVector</h1>', unsafe_allow_html=True)
st.caption("AI-Powered Resume Evaluation Engine powered by Llama-3.3-70B via Groq")

# --- USER GUIDE SECTION ---
guide_html = """
<div class="user-guide-box">
    <h3>📖 Quick Start Guide</h3>
    <ol>
        <li><strong>Add Job Description:</strong> Paste the target requirements and responsibilities into the left panel.</li>
        <li><strong>Upload File:</strong> Drop the PDF or DOCX file you want to verify as your candidate's resume into the right panel.</li>
        <li><strong>Execute:</strong> Click the "Run Analytical Evaluation" button to initiate the AI scan.</li>
    </ol>
    <h4>🔍 Evaluation Parameters</h4>
    <ul>
        <li><strong>ATS Match Score:</strong> A quantitative percentage measuring how well the resume aligns with the job description.</li>
        <li><strong>Status Recommendation:</strong> the immediate next-step verdict (e.g., Interview, Hold, Reject).</li>
        <li><strong>Core Recruitment Judgment:</strong> A comprehensive, qualitative AI summary detailing the candidate's professional fit and experience level.</li>
        <li><strong>Skill Gap Analysis:</strong> A direct comparison extracting the core skills found in the document versus the skills missing from the requirements.</li>
    </ul>
</div>
"""
st.markdown(guide_html, unsafe_allow_html=True)
st.write("---")

# Layout columns for side-by-side management
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("Job Specifications")
    job_description = st.text_area(
        "Paste Target Job Description (JD) here:", 
        height=300, 
        placeholder="Example: We are looking for a Python Developer proficient in Streamlit, Machine Learning models..."
    )

with col2:
    st.subheader("Applicant Files")
    uploaded_file = st.file_uploader("Upload Candidate Resume:", type=["pdf", "docx"])
    
    if uploaded_file:
        st.success(f"Successfully staged: {uploaded_file.name}")

st.write("---")

# Processing and Execution Action Block
if st.button("Run Analytical Evaluation", type="primary"):
    if not job_description:
        st.warning("Please input a Job Description first.")
    elif not uploaded_file:
        st.warning("Please upload a resume file (PDF or DOCX).")
    else:
        with st.spinner("Extracting structural text data and initializing LLM judgment..."):
            # Step 1: Text extraction pipeline routing
            if uploaded_file.name.endswith(".pdf"):
                resume_text = pdf_extractor.extract_text(uploaded_file)
            else:
                resume_text = docx_extractor.extract_text(uploaded_file)
            
            # Basic validation block
            if "Error" in resume_text or not resume_text.strip():
                st.error("Failed to parse file content. Ensure the document isn't empty or corrupted.")
            else:
                try:
                    # Step 2: Initialize service and parse
                    llm_engine = LLMService()
                    analysis_result = llm_engine.analyze_resume_against_jd(resume_text, job_description)
                    
                    # Small black analysis complete box
                    st.markdown('<div class="black-success-box">Analysis Complete!</div>', unsafe_allow_html=True)
                     
                    # Score Dashboard using native st.metric widgets
                    metric_col1, metric_col2, metric_col3 = st.columns(3)
                    with metric_col1:
                        st.metric(label="Candidate Name", value=analysis_result.candidate_name)
                    with metric_col2:
                        st.metric(label="ATS Match Score", value=f"{analysis_result.match_percentage}%")
                    with metric_col3:
                        st.metric(label="Status Recommendation", value=analysis_result.recommendation)
                    
                    # Detailed Breakdown
                    st.subheader("Core Recruitment Judgment")
                    st.markdown(
                        f'<div class="black-judgment-box">{analysis_result.analytical_judgment}</div>', 
                        unsafe_allow_html=True
                    )
                    
                    # Helper function to convert Python lists to HTML bullets
                    def format_skills_to_html(skills_list):
                        if not skills_list:
                            return "<ul><li>None identified</li></ul>"
                        bullets = "".join([f"<li>{skill}</li>" for skill in skills_list])
                        return f"<ul>{bullets}</ul>"

                    skills_found_html = format_skills_to_html(analysis_result.skills_found)
                    skills_missing_html = format_skills_to_html(analysis_result.skills_missing)

                    # Render the scrollable black boxes
                    skill_col1, skill_col2 = st.columns(2)

                    with skill_col1:
                        st.subheader("🖇️ Skills Found in Resume satisfying Job Description")
                        st.markdown(f'<div class="scrollable-black-box">{skills_found_html}</div>', unsafe_allow_html=True)

                    with skill_col2:
                        st.subheader("📌 Identified Skill Gaps")
                        st.markdown(f'<div class="scrollable-black-box">{skills_missing_html}</div>', unsafe_allow_html=True)
                            
                except Exception as error:
                    st.error(f"Execution Error: {str(error)}")
