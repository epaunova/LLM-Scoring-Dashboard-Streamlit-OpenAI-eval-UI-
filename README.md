# 🧠 LLM Scoring Dashboard

This is a Streamlit-based dashboard that allows manual evaluation of LLM outputs across key quality dimensions:

- ✅ Factuality  
- ✨ Clarity  
- 🖋 Style

It’s designed as a lightweight interactive tool for PMs, researchers, and developers working with LLM-generated content — enabling fast evaluation loops and structured feedback.

---

## 🔧 Features

- Upload a CSV with prompt + model outputs
- Score each output using dropdowns per category
- View data in real time, then export scored results
- Ready for extension with GPT-based auto-eval or OpenAI API

---

## 📊 Example Input Format

`data/mock_outputs.csv`

```csv
Prompt,Output
"Summarize WW2","World War II began in 1939 and ended in 1945..."
"Explain photosynthesis","Photosynthesis is the process by which green plants..."
"What is blockchain?","Blockchain is a distributed ledger technology..."
🚀 How to Run
bash
Copy
Edit
pip install streamlit pandas
streamlit run app.py
Then upload your mock_outputs.csv or a custom file and begin scoring interactively.

📁 Project Structure
bash
Copy
Edit
llm-scoring-dashboard/
├── app.py                          # Main Streamlit app
├── data/
│   └── mock_outputs.csv           # Example input file
├── prompts/
│   └── example_prompt.txt         # Prompt template placeholder
├── scoring/
│   └── eval_logic_notes.md        # Future scoring extensions
├── utils/
│   └── token_counter_placeholder.py  # Utility stub
└── README.md
🔗 Related Projects
✍️ Prompt Efficiency Sandbox

📊 LLM Eval Playground

🧪 LLM Evaluation Toolkit

Together, these projects cover the full lifecycle:
Prompt Design → Output Evaluation → Model Comparison → Human Feedback Loop

👤 Author
Eva Paunova
🔗 LinkedIn:( https://www.linkedin.com/in/eva-hristova-paunova-a194b3210/)
📂 Portfolio
