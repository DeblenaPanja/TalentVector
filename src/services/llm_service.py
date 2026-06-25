import json
from groq import Groq
from src.utils.config import Config
from src.models.schemas import ResumeAnalysis

class LLMService:
    def __init__(self):
        Config.validate()
        self.client = Groq(api_key=Config.GROQ_API_KEY)

    def analyze_resume_against_jd(self, resume_text: str, job_description: str) -> ResumeAnalysis:
        # Define the strict behavior criteria inside the prompt
        schema_instructions = json.dumps(ResumeAnalysis.model_json_schema(), indent=2)
        
            # 2. Build a highly strict system prompt
        system_prompt = f"""
        You are an expert technical recruiter and ATS system. 
        Analyze the provided resume against the job description.
        
        CRITICAL INSTRUCTIONS:
        1. You MUST return your response as a valid JSON object.
        2. Your JSON MUST contain EVERY SINGLE KEY defined in the schema below.
        3. Do NOT omit any keys.
        
        FALLBACK RULES (If data is missing from the resume):
        - For integer fields (like scores or percentages), output 0.
        - For list fields (like strengths or skills), output an empty list [].
        - For string fields, output "Not Provided" or "N/A".
        
        SCHEMA:
        {schema_instructions}
        """
        
        
        user_prompt = f"""
        JOB DESCRIPTION:
        \"\"\"{job_description}\"\"\"
        
        CANDIDATE RESUME:
        \"\"\"{resume_text}\"\"\"
        
        Provide your evaluation based on the schema requirements. Ensure the match percentage is realistic and unbiased.
        """

        try:
            response = self.client.chat.completions.create(
                model=Config.DEFAULT_MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.2,  # Low temperature ensures highly consistent, analytical results
                response_format={"type": "json_object"}
            )
            
            # Parse the raw string response into our structured Pydantic object
            raw_json = json.loads(response.choices[0].message.content)
            return ResumeAnalysis(**raw_json)
            
        except Exception as e:
            raise RuntimeError(f"Failed to process request via Groq: {str(e)}")