from pydantic import BaseModel, Field
from typing import List

class ResumeAnalysis(BaseModel):
    """
    Schema for structured resume analysis.
    This structure forces the LLM to return consistent, high-quality data.
    """
    candidate_name: str = Field(description="The full name of the candidate extracted from the resume.")
    
    # Grading Metrics
    match_percentage: int = Field(description="An objective score from 0-100 indicating fit for the job.")
    technical_score: int = Field(description="Score 0-10 for technical skills alignment.")
    experience_score: int = Field(description="Score 0-10 for experience relevance.")
    
    # Categorized Insights
    skills_found: List[str] = Field(description="List of relevant skills found in the resume.")
    skills_missing: List[str] = Field(description="List of key requirements from the JD that are absent.")
    strengths: List[str] = Field(description="List of 3 top candidate strengths.")
    weaknesses: List[str] = Field(description="List of 3 improvement areas or concerns.")
    
    # Final Judgment
    analytical_judgment: str = Field(description="A 2-3 sentence professional recruitment summary.")
    recommendation: str = Field(description="The hiring decision: 'Interview', 'Review', or 'Reject'.")