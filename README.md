<div align="center">

<!-- Top Banner Badge -->
![TalentVector Banner](https://img.shields.io/badge/TALENT_VECTOR-AI_RESUME_ENGINE-00C853?style=for-the-badge&logo=rocket&logoColor=white&labelColor=111827)

<!-- Main Title -->
# 🚀 TalentVector

<!-- Tagline Description -->
### **AI-Powered Resume Evaluation & Recruitment Intelligence Engine**

<br />

<!-- Shields Badges Row 1 -->
[![Live Demo](https://img.shields.io/badge/LIVE_DEMO-VISIT_NOW-00C853?style=for-the-badge)](https://github.com/deblena2007/TalentVector)
![AI Model](https://img.shields.io/badge/MODEL-LLAMA_3.3_70B-76B900?style=for-the-badge&logo=meta&logoColor=white)
![LLM Provider](https://img.shields.io/badge/POWERED_BY-GROQ_API-F50057?style=for-the-badge)

<!-- Shields Badges Row 2 -->
![Python](https://img.shields.io/badge/PYTHON-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Frontend](https://img.shields.io/badge/FRONTEND-STREAMLIT-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Container](https://img.shields.io/badge/DOCKER-READY-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Deployment](https://img.shields.io/badge/DEPLOYED_ON-RENDER-46E3B7?style=for-the-badge&logo=render&logoColor=white)

<br />

*Leverage Llama 3.3 70B to instantly parse resumes, calculate ATS match scores, perform skill gap analysis, and generate actionable recruitment insights 🎯*

---

</div>

## ✨ Features

* **📄 Intelligent Resume Parsing:** Seamlessly extracts text from both **PDF** and **DOCX** files regardless of formatting.
* **🎯 Contextual Evaluation:** Evaluates candidate experience, qualifications, and core competencies against provided Job Descriptions.
* **📊 ATS Match Scoring:** Calculates quantitative **ATS Match Scores (%)** for quick candidate ranking.
* **🧠 Core Recruitment Insights:** Provides in-depth suitability analysis and professional role alignment.
* **🔍 Skill Gap Analysis:** Highlights both ✅ **Skills Present** and ❌ **Skills Missing** to reveal critical qualification gaps.
* **🚦 Actionable Hiring Recommendation:** Classifies candidates into clear next steps: **Interview**, **Review Further**, or **Reject**.

---

## 🛠️ Technology Stack

| Category | Technology |
| :--- | :--- |
| **Frontend UI** | Streamlit |
| **AI Core Model** | Llama 3.3 70B |
| **LLM Inference** | Groq API |
| **Language** | Python 3.x |
| **Containerization** | Docker |
| **CI/CD Pipeline** | GitHub Actions |
| **Cloud Hosting** | Render |

---

## 📈 Workflow Overview



```text
  📄 Resume Upload (PDF / DOCX)
                │
                ▼
  🔍 Text Extraction & Parsing
                │
                ▼
  🎯 Job Description Matching
                │
                ▼
  ⚡ Llama-3.3-70B Analysis (via Groq)
                │
                ▼
  📊 ATS Match Score & Skill Gap Matrix
                │
                ▼
  🚦 Final Hiring Recommendation

```

## 📁 Project Structure

```text
TalentVector/
│
├── .github/
│   └── workflows/              # CI/CD automation pipelines
│
├── prompts/                     # Prompt engineering and evaluation assets
│
├── src/
│   ├── components/              # Modular Streamlit UI components
│   ├── extractors/              # PDF and DOCX text extraction
│   ├── models/                  # Data schemas and validation modules
│   ├── services/                # Core business logic and Groq integration
│   ├── utils/                   # Configuration and logging utilities
│   └── app.py                   # Main Streamlit application
│
├── tests/                       # Unit and integration tests
│
├── .env.example                 # Environment variable template
├── .gitignore                   # Files excluded from version control
├── config.yaml                  # Application configuration
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```
1. set up Clone the Repository
   ```text
   git clone [https://github.com/deblena2007/TalentVector.git](https://github.com/deblena2007/TalentVector.git)
   cd TalentVector
    ```
2. Set Up Virtual Environment
    ```text
    python -m venv .venv
    ```
Windows:
   ```text
    .venv\Scripts\activate
   ```
macOS / Linux:
   ```text
   source .venv/bin/activate
   ```
3. Install Dependencies
   ```text
   pip install -r requirements.txt
   ```
4. Configure Environment Secrets
Create a .env file in the project root folder:
 ```text
   GROQ_API_KEY=your_groq_api_key_here
   ```
5. Launch Application
```text
   streamlit run src/app.py
   ```
Open http://localhost:8501 in your browser.

🌐 Deployment
TalentVector is production-ready for deployment on platforms such as Render:

Push your latest code changes to GitHub .

Connect your repository to your Render dashboard .

Add the required environment variable (GROQ_API_KEY) under secret settings .

Trigger the deployment .

🔮 Roadmap & Future Enhancements
📦 Multi-resume batch processing & dynamic queue

📊 Comprehensive recruiter dashboard

🏆 Candidate ranking & comparison analytics

📑 Export evaluation summaries to PDF / docs

💬 Automated interview question generation

👨‍💻 Author
Deblena Panja

GitHub: @deblena2007
app live at:  https://lnkd.in/gY3F6Dpw

⭐ Give a Star!
If you find this repository useful, please consider giving it a Star on GitHub!

Built with ❤️ using Python, Streamlit, Groq, and Llama 3.3 70B

