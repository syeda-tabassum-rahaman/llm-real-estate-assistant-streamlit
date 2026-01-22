import streamlit as st

from src.rag import process_urls, generate_answer


st.set_page_config(
    page_title="Real Estate Assistant",
    layout="centered"
)

st.title("Real Estate Assistant")
st.write(
    "Provide one or more URLs. The assistant will read them and answer your questions with sources."
)


# -------- URL INPUT --------
st.subheader("Step 1: Add URLs")

urls_input = st.text_area(
    "Enter one URL per line",
    placeholder="https://example.com/article-1\nhttps://example.com/article-2"
)

process_button = st.button("Process URLs")


if process_button:
    if not urls_input.strip():
        st.error("Please provide at least one URL.")
    else:
        urls = [u.strip() for u in urls_input.splitlines() if u.strip()]

        with st.spinner("Processing documents..."):
            statuses = process_urls(urls) or []
            for status in statuses:
                st.write(status)

        st.success("Documents processed successfully.")


# -------- QUESTION INPUT --------
st.subheader("Step 2: Ask a Question")

question = st.text_input(
    "Enter your question",
    placeholder="What was the 30 year fixed mortgage rate and on which date?"
)

ask_button = st.button("Ask")


if ask_button:
    if not question.strip():
        st.error("Please enter a question.")
    else:
        with st.spinner("Generating answer..."):
            answer, sources = generate_answer(question)

        st.markdown("### Answer")
        st.write(answer)

        if sources:
            st.markdown("### Sources")
            if isinstance(sources, str):
                for src in sources.split(","):
                    st.write(src.strip())
            else:
                for src in sources:
                    st.write(src)
