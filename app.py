import streamlit as st
import pandas as pd

# Load data
df = pd.read_excel("Checklist_Estudos_12_Semanas.xlsx")

st.set_page_config(page_title="Cronograma de Estudos IA", layout="wide")
st.title("📚 Cronograma de Estudos - IA Generativa")

# Sidebar: filtro por semana
semanas = sorted(df["Semana"].unique())
semana_selecionada = st.sidebar.selectbox("Escolha a semana", semanas)

# Filtrar dados
df_semana = df[df["Semana"] == semana_selecionada]

# Mostrar em formato de checklist
st.subheader(f"📅 {semana_selecionada}")

for i, row in df_semana.iterrows():
    with st.expander(f"{row['Dia']} - {row['Linguagem/Tópico']}"):
        st.markdown(f"**O que estudar:** {row['O que estudar']}")
        st.markdown(f"**Resumo:** {row['Resumo']}")
        st.markdown(f"**Meta do dia:** {row['Meta do dia']}")
        concluido = st.checkbox("Marcar como concluído", key=f"check_{i}")

# Progresso simulado
st.sidebar.markdown("---")
progresso = st.sidebar.slider("Simulação de progresso (%)", 0, 100, 0)
st.sidebar.progress(progresso / 100, text="Progresso geral")
