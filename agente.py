# MVP do Agente Bíblico IA usando Streamlit (sem necessidade de API ou chave de acesso externa)

import streamlit as st
import pandas as pd
import random

# Base fictícia de versículos (você pode substituir por um CSV depois)
versiculos = [
    {"livro": "João", "capitulo": 3, "versiculo": 16, "texto": "Porque Deus amou o mundo de tal maneira...", "tags": "amor, salvação"},
    {"livro": "Salmos", "capitulo": 23, "versiculo": 1, "texto": "O Senhor é o meu pastor, nada me faltará.", "tags": "confiança, provisão"},
    {"livro": "Romanos", "capitulo": 8, "versiculo": 28, "texto": "Todas as coisas cooperam para o bem...", "tags": "propósito, esperança"},
    {"livro": "Provérbios", "capitulo": 3, "versiculo": 5, "texto": "Confia no Senhor de todo o teu coração...", "tags": "juventude, fé"},
    {"livro": "Efésios", "capitulo": 5, "versiculo": 25, "texto": "Maridos, amai vossas mulheres, como também Cristo amou a igreja...", "tags": "casamento, amor"},
]

# Função para buscar versículo por tema
def buscar_versiculo_por_tema(tema):
    encontrados = [v for v in versiculos if tema.lower() in v["tags"]]
    return random.choice(encontrados) if encontrados else None

# Função para devocional personalizado
def devocional_personalizado(perfil):
    if perfil == "Jovem":
        return buscar_versiculo_por_tema("juventude")
    elif perfil == "Líder":
        return buscar_versiculo_por_tema("fé")
    elif perfil == "Casal":
        return buscar_versiculo_por_tema("casamento")
    else:
        return random.choice(versiculos)

# Função para exegese e análise profunda (simulada)
def exegese_analise(v):
    texto_original = "Texto original em grego/hebraico (simulado)"
    contexto_historico = f"O livro de {v['livro']} foi escrito em um contexto de desafios espirituais específicos... (simulado)"
    interpretacao = "Esse versículo nos encoraja a confiar plenamente em Deus, mesmo sem entender tudo. (simulado)"
    return texto_original, contexto_historico, interpretacao

# Streamlit UI
st.set_page_config(page_title="Agente Bíblico IA", page_icon="📖")
st.title("📖 Agente Bíblico MVP")
st.subheader("Explorador de versículos e devocionais simples")

menu = st.sidebar.selectbox("Escolha uma funcionalidade", [
    "Devocional do Dia",
    "Devocional Diário Personalizado",
    "Buscar por Tema",
    "Versículo Aleatório",
    "Exegese e Análise Profunda"
])

if menu == "Devocional do Dia":
    st.markdown("### 🙏 Devocional do Dia")
    v = random.choice(versiculos)
    st.write(f"**{v['livro']} {v['capitulo']}:{v['versiculo']}**")
    st.write(v['texto'])
    st.info("Reflexão: Deus cuida de você em todo tempo. Confie nele!")

elif menu == "Devocional Diário Personalizado":
    st.markdown("### 🙏 Devocional Diário Personalizado")
    perfil = st.selectbox("Selecione seu perfil:", ["Jovem", "Líder", "Casal"])
    if perfil:
        v = devocional_personalizado(perfil)
        if v:
            st.write(f"**{v['livro']} {v['capitulo']}:{v['versiculo']}**")
            st.write(v['texto'])
            st.success(f"Devocional para {perfil}: Que Deus abençoe sua caminhada!")
        else:
            st.warning("Nenhum devocional encontrado para esse perfil.")

elif menu == "Buscar por Tema":
    st.markdown("### 🔍 Buscar versículo por tema")
    tema = st.text_input("Digite um tema (ex: amor, esperança, provisão):")
    if tema:
        resultado = buscar_versiculo_por_tema(tema)
        if resultado:
            st.write(f"**{resultado['livro']} {resultado['capitulo']}:{resultado['versiculo']}**")
            st.write(resultado['texto'])
        else:
            st.warning("Tema não encontrado. Tente outro termo.")

elif menu == "Versículo Aleatório":
    st.markdown("### 📜 Versículo Aleatório")
    v = random.choice(versiculos)
    st.write(f"**{v['livro']} {v['capitulo']}:{v['versiculo']}**")
    st.write(v['texto'])

elif menu == "Exegese e Análise Profunda":
    st.markdown("### 🔍 Exegese e Análise Profunda")
    v = random.choice(versiculos)
    st.write(f"**{v['livro']} {v['capitulo']}:{v['versiculo']}**")
    st.write(v['texto'])
    st.divider()
    texto_original, contexto, interpretacao = exegese_analise(v)
    st.subheader("📜 Texto Original (simulado)")
    st.write(texto_original)
    st.subheader("🏛 Contexto Histórico (simulado)")
    st.write(contexto)
    st.subheader("🧠 Interpretação (simulado)")
    st.write(interpretacao)