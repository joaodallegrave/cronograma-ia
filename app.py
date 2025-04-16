import streamlit as st
import pandas as pd

# ======= CONFIGURAÇÃO =======
SENHA_CORRETA = "joao2025"
ARQUIVO_EXCEL = "Checklist_Estudos_12_Semanas.xlsx"

# ======= INTERFACE DE LOGIN =======
st.set_page_config(page_title="Cronograma de Estudos IA", layout="wide")
st.title("🔐 Acesso ao Cronograma de Estudos")

senha_digitada = st.sidebar.text_input("Digite a senha para acessar o cronograma:", type="password")

if senha_digitada != SENHA_CORRETA:
    st.warning("Acesso restrito. Digite a senha correta para visualizar o conteúdo.")
    st.stop()

# ======= APP PRINCIPAL =======
st.success("✅ Acesso autorizado!")
df = pd.read_excel(ARQUIVO_EXCEL)

st.title("📚 Cronograma de Estudos - IA Generativa")

# Ordenar as semanas numericamente
semanas = sorted(df["Semana"].unique(), key=lambda x: int(x.split()[-1]))
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
