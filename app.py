import streamlit as st
from code_analyzer import run_performance_analysis
from openai_review import ai_code_review

st.title("Kod Performans Analizi ve AI Yorumları 🚀")

code = st.text_area("Kodunuzu buraya yazın:", height=200)

if st.button("Analiz Et"):
    if not code.strip():
        st.warning("⚠️ Lütfen bir kod girin!")
    else:
        performance_results = run_performance_analysis(code)

        review = ai_code_review(code, performance_results)

        st.subheader("📊 Performans Analizi Sonuçları")
        st.json(performance_results)

        st.subheader("🤖 AI Kod İncelemesi")
        st.text_area("AI Yanıtı:", review, height=250)
