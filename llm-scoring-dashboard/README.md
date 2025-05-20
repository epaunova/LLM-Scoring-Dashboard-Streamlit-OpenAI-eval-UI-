# 🧠 LLM Scoring Dashboard

Streamlit-based interactive dashboard to evaluate LLM outputs on key qualitative metrics:

- Factuality
- Clarity
- Style

## 💡 Features

- Upload CSV with Prompt + Output
- Manual scoring using dropdowns
- Auto-evaluation extension ready (mock scoring or OpenAI integration)
- Saves scores to CSV for later analysis

## 🛠 How to Run

```bash
pip install streamlit pandas
streamlit run app.py
```

## 📂 Structure

- `app.py` – main Streamlit app
- `data/mock_outputs.csv` – example inputs
- `prompts/`, `scoring/`, `utils/` – placeholders for extensions
