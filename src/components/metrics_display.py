import streamlit as st

def render_analysis_metrics(analysis):
    """
    Renders the evaluation results into a clean, professional dashboard.
    Args:
        analysis: A Pydantic ResumeAnalysis object.
    """
    
    # 1. High-level KPIs
    st.subheader("Evaluation Dashboard")
    m1, m2, m3, m4 = st.columns(4)
    
    with m1:
        st.metric("Match Score", f"{analysis.match_percentage}%")
    with m2:
        st.metric("Technical", f"{analysis.technical_score}/10")
    with m3:
        st.metric("Experience", f"{analysis.experience_score}/10")
    with m4:
        st.metric("Recommendation", analysis.recommendation)

    st.write("---")

    # 2. Detailed Qualitative Analysis
    st.subheader("Recruitment Insights")
    st.info(analysis.analytical_judgment)

    # 3. Two-Column Layout for Strengths and Weaknesses
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("### Strengths")
        for strength in analysis.strengths:
            st.success(f"• {strength}")
            
    with col_b:
        st.markdown("### ⚠️ Areas for Improvement")
        for weakness in analysis.weaknesses:
            st.warning(f"• {weakness}")

    st.write("---")

    # 4. Skill Gap Analysis
    col_x, col_y = st.columns(2)
    with col_x:
        st.markdown("### Skills Found")
        st.write(", ".join(analysis.skills_found))
    with col_y:
        st.markdown("### Skills Missing")
        if analysis.skills_missing:
            st.write(", ".join(analysis.skills_missing))
        else:
            st.write("None identified - Strong candidate!")