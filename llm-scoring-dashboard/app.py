import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="LLM Output Scoring Dashboard", layout="wide")

st.title("📊 LLM Output Scoring Dashboard")

uploaded_file = st.file_uploader("Upload your CSV file with model outputs", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Uploaded Data", df.head())

    if "Factuality" not in df.columns:
        df["Factuality"] = ""
        df["Clarity"] = ""
        df["Style"] = ""

    for idx, row in df.iterrows():
        st.markdown(f"#### 🔹 Prompt: {row['Prompt']}")
        st.markdown(f"**Output:** {row['Output']}")

        factuality = st.selectbox(f"Factuality (row {idx})", options=["", "Poor", "Average", "Good", "Excellent"], key=f"factuality_{idx}")
        clarity = st.selectbox(f"Clarity (row {idx})", options=["", "Poor", "Average", "Good", "Excellent"], key=f"clarity_{idx}")
        style = st.selectbox(f"Style (row {idx})", options=["", "Poor", "Average", "Good", "Excellent"], key=f"style_{idx}")

        df.at[idx, "Factuality"] = factuality
        df.at[idx, "Clarity"] = clarity
        df.at[idx, "Style"] = style
        st.markdown("---")

    if st.button("Save Scores"):
        df.to_csv("data/scored_outputs.csv", index=False)
        st.success("Scores saved to data/scored_outputs.csv")
