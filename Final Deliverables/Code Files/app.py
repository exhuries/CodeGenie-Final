# app.py
import streamlit as st
from CodeModel import generate_code

st.set_page_config(page_title="CodeGenie")

def main():
    st.header("CodeGenie – AI-Powered Code Generation")
    prompt = st.text_area("Prompt", height=160,
                          placeholder="e.g. write a Python function that checks for prime numbers")
    if st.button("Generate") and prompt.strip():
        with st.spinner("Generating…"):
            code, t0, t1 = generate_code(prompt)
        st.success(f"Completed in {t1 - t0:.2f} s")
        st.code(code, language="python")

if __name__ == "__main__":
    main()
