import streamlit as st

def sidebar_layout():
    """
    Renders the sidebar for file uploads and global settings.
    Returns:
        tuple: (uploaded_file, job_description)
    """
    with st.sidebar:
        st.header("Configuration...")
        st.write("Upload the candidate resume and provide the JD to start the analysis.")
        
        # File Uploader
        uploaded_file = st.file_uploader(
            "Upload Resume (PDF/DOCX)", 
            type=["pdf", "docx"],
            help="Supported formats: PDF, DOCX"
        )
        
        # Job Description Input
        job_description = st.text_area(
            "Target Job Description",
            height=300,
            placeholder="Paste the requirements here..."
        )
        
        st.write("---")
        st.caption("v1.0.0 | AI-Powered ATS")
        
    return uploaded_file, job_description