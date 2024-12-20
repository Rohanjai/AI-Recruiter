# AI Recruiter

The AI Recruiter is an advanced resume processing and data extraction system that leverages AI models, such as Ollama (Llama 3.2), to extract key information like name, skills, experience, and education from resumes. This repository is designed to streamline the recruitment process by automating the extraction of structured data from unstructured documents.


## Features

- **Resume Data Extraction**: Extracts critical information such as name, skills, experience, and education from resumes.
- **Customizable Agents**: Use Swarm-based agents to manage tasks like data extraction and processing.
- **Integration with Ollama**: Uses a self-hosted Llama model (Llama 3.2) via Ollama for natural language understanding.
- **JSON Output**: Processes resumes and returns structured data in JSON format for easy integration with other systems.


## Installation

### Prerequisites
- Python 3.8 or higher
- Ollama (Self-hosted Llama model)
- Dependencies listed in `requirements.txt`

### Steps
1. Clone the repository:
```bash
git clone https://github.com/Rohanjai/AI-Recruiter.git
cd ai-recruiter-agency
```
2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
  
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run the Ollama
5. Run the application
```bash
streamlit run app.py
```
