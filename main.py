import streamlit as st

# 1. Configuração inicial da página
st.set_page_config(page_title="Rastreio AMBEV", layout="centered")

# Injeta CSS para sumir com transparências e deixar tudo muito nítido
st.markdown(
    """
    <style>
    /* Força todos os textos do site a ficarem pretos e bem visíveis */
    html, body, p, div, span, label {
        color: #000000 !important;
        font-family: sans-serif !important;
    }
    
    /* DESTACANDO A CAIXINHA DE DIGITAÇÃO: Borda preta grossa e fundo visível */
    .stTextInput input {
        border: 2px solid #000000 !important;
        border-radius: 6px !important;
        background-color: #ffffff !important;
        color: #000000 !important;
        font-size: 16px !important;
        font-weight: bold !important;
    }
    
    /* Customização do botão OK para vermelho */
    div[data-testid="stColumn"]:nth-of-type(2) button {
        background-color: #ff4b4b !important;
        color: white !important;
        border: none !important;
        font-weight: bold !important;
        height: 44px !important;
    }
    
    /* Caixa do Pix: Fundo claro, borda azul forte e texto totalmente preto */
    .caixa-pix-visivel {
        background-color: #f1f3f4 !important;
        border: 2px dashed #00469b !important;
        padding: 15px !important;
        border-radius: 8px !important;
        font-size: 20px !important;
        color: #000000 !important;
        font-weight: bold !important;
        text-align: center !important;
        margin-top: 10px !important;
        margin-bottom: 15px !important;
        font-family: monospace !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 2. Barra Azul do Topo
st.markdown(
    """
    <div style="background-color: #00469b; padding: 15px; border-radius: 5px; margin-bottom: 30px; display: flex; justify-content: space-between; align-items: center;">
        <h3 style="color: white !important; margin: 0; font-weight: bold;">Rastreio AMBEV</h3>
        <span style="color: white !important; cursor: pointer; font-weight: bold;">Ajuda</span>
    </div>
    """,
    unsafe_allow_html=True
)

# 3. Títulos da página
st.caption("Rastreio AMBEV")
st.title("Acompanhe seu pedido")

# 4. Caixa Branca de Consulta
with st.container(border=True):
    st.write("🔍 **01 / CONSULTA**")
    st.write("**Código de rastreio**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        codigo = st.text_input(
            "Digite seu código de rastreio", 
            label_visibility="collapsed", 
            placeholder="Clique aqui e digite o código..."
        )
        
    with col2:
        botao_buscar = st.button("➔ Ok", use_container_width=True)
        
    st.write("Você encontra o código no e-mail de confirmação do seu pedido.")

# 5. Lógica do Botão - Exibe o status e o Pix nítidos e copiáveis
if botao_buscar:
    if codigo:
        st.write("---") 
        
        # Cabeçalho da seção 02 / STATUS
        col_status1, col_status2 = st.columns(2)
        with col_status1:
            st.write("🔹 **02 / STATUS**")
            st.write(f"**Código Informado:** {codigo}")
        with col_status2:
            st.write("📦")
            
        # Card Azul de Aguardando Pagamento
        st.markdown(
            f"""
            <div style="background-color: #e8f0fe; padding: 25px; border-radius: 12px; border-left: 5px solid #00469b; margin-bottom: 25px;">
                <h3 style="color: #00469b !important; margin: 0 0 10px 0; font-size: 22px; font-weight: bold;">Aguardando pagamento para sair para entrega</h3>
                <p style="color: #000000 !important; margin: 0; font-size: 15px; font-weight: 500;">Status padrão desta página. Esta consulta não verifica transportadoras nem confirma cobranças do seu pedido.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Seção do Pix Copia e Cola (Aviso removido daqui)
        st.write("### **Pix Copia e Cola**")
        
        # CNPJ/Chave em destaque
        chave_pix = "07.526.557/0001-00"
        st.markdown(f'<div class="caixa-pix-visivel">{chave_pix}</div>', unsafe_allow_html=True)
        
        # BOTÃO COM LÓGICA DE COPIA AUTOMÁTICA INJETADA DIRETAMENTE
        st.components.v1.html(
            f"""
            <input type="text" value="{chave_pix}" id="pixInput" style="position:absolute; left:-9999px;">
            <button class="btn-copiar-auto" onclick="copiarPix()" style="background-color: #00469b; color: white; border: none; font-weight: bold; font-size: 16px; padding: 12px; width: 100%; border-radius: 4px; cursor: pointer;">📋 Copiar Código Pix</button>
            
            <script>
            function copiarPix() {{
                var copyText = document.getElementById("pixInput");
                copyText.select();
                copyText.setSelectionRange(0, 99999);
                document.execCommand("copy");
                alert("✅ Código Pix copiado com sucesso!");
            }}
            </script>
            """,
            height=50
        )
            
    else:
        st.warning("⚠️ Por favor, digite um código de rastreio antes de clicar em Ok.")
