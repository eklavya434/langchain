# LangChain & Agentic AI Course Workspace

This repository is a structured development workspace for tracking progress, projects, and code built during the **"Complete Agentic AI Course In 10 Hours"** (covering LangChain, LangGraph, RAG, Vectorless RAG, Guardrails, and Evaluations).

## 🚀 Overview

The workspace is configured to build and test various Agentic AI components step-by-step using Python 3.13 and the fast **`uv`** package manager.

## 🛠️ Tech Stack & Dependencies

- **Package Manager:** `uv`
- **Orchestration:** `langchain`, `langgraph`
- **Model Providers:** `langchain-google-genai` (utilizing Gemini models), `langchain-openai`, `langchain-groq`
- **Other Utilities:** `python-dotenv`, `ipykernel` (for Jupyter Notebook support)

---

## 💻 Getting Started

### 1. Prerequisites
Ensure you have the `uv` tool installed. If not, install it using:
- **Windows (PowerShell):** `irm https://astral.sh/uv/install.ps1 | iex`
- **macOS/Linux:** `curl -LsSf https://astral.sh/uv/install.sh | sh`

### 2. Set Up the Environment
Create a `.env` file in the root directory and add your API keys:
```env
GOOGLE_API_KEY=your_gemini_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```

### 3. Install Dependencies
Run the following command to sync and install the dependencies in a virtual environment:
```bash
uv sync
```

### 4. Run the Application
Run the entry point application script:
```bash
uv run langchain-app
```

---

## 📂 Project Structure

- `src/langchain_app/` — Main application package.
  - `__init__.py` — Entry point script containing active examples and tests.
- `pyproject.toml` — Standard Python package configuration.
- `uv.lock` — Dependency lockfile.
- `.gitignore` — Ignores local environment `.venv/` and API keys `.env`.
