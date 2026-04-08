import streamlit as st
from datetime import date

# 1. Configuração do título na aba do navegador
st.set_page_config(page_title="Mensagem Diária", page_icon="✨")

# 2. Lógica para escolher a imagem do dia (1 a 14)
dia_do_ano = date.today().timetuple().tm_yday
numero_imagem = (dia_do_ano % 14) + 1
nome_arquivo = f"msg{numero_imagem}.jpg"

# 3. O que aparece na tela
st.title("☀️ Mensagem Diária")
st.write(f"Que seu dia seja abençoado! Hoje é **{date.today().strftime('%d/%m/%Y')}**")

try:
    # Tenta mostrar a foto
    st.image(nome_arquivo, use_container_width=True)
    
    st.markdown(f'<p style="color:gray; font-size:0.9rem;">Arte Visual: Evelyn Ferreira Falcão</p>', unsafe_allow_html=True)
    st.write("---")
    
    # 4. Botão de Compartilhar configurado
    link_wa = "https://api.whatsapp.com/send?text=Olha%20que%20mensagem%20linda%20eu%20recebi%20hoje%20no%20app%20da%20Evelyn!"

    st.link_button("📲 Compartilhar no WhatsApp", link_wa)
    st.caption("💡 Dica: No celular, pressione a imagem para salvá-la.")

except:
    # Se der erro, ele mostra essa frase amigável
    st.warning(f"O sistema está procurando pela imagem {nome_arquivo}...")

# 5. Seu crédito no final
st.write("---")
st.markdown("<p style='text-align: center; font-size: 0.8rem;'>Desenvolvido por Evelyn Ferreira Falcão</p>", unsafe_allow_html=True)