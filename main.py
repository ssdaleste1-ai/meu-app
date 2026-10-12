import streamlit as st

# 1. Configuração inicial da página e desativação do Dark Mode do Streamlit
st.set_page_config(page_title="Rastreio AMBEV", layout="centered")

# Injeta CSS agressivo para neutralizar o tema escuro e forçar fundo branco com letras pretas
st.markdown(
    """
    <style>
    /* Força o fundo de toda a aplicação a ser branco */
    .stApp, div[data-testid="stAppViewContainer"], div[data-testid="stApp"], html, body {
        background-color: #ffffff !important;
        color: #000000 !important;
    }
    
    /* Garante que absolutamente nenhum texto herde cor clara ou cinza do tema escuro */
    p, span, div, label, h1, h2, h3, h4, h5, h6, input, .stMarkdown p, .stText, blockquote {
        color: #000000 !important;
        font-family: sans-serif !important;
    }
    
    /* Mantém os títulos em destaque e pretos */
    h1, h2, h3 {
        font-weight: bold !important;
    }
    
    /* Corrige o st.caption para não sumir no fundo branco (definido como cinza escuro legível) */
    .stCaption, div[data-testid="stCaptionContainer"] p {
        color: #444444 !important;
    }
    
    /* CAIXA DE DIGITAÇÃO: Fundo totalmente branco, borda preta grossa e texto bem visível */
    .stTextInput input {
        border: 2px solid #000000 !important;
        border-radius: 6px !important;
        background-color: #ffffff !important;
        color: #000000 !important;
        font-size: 16px !important;
        font-weight: bold !important;
    }
    
    /* Caixa Branca de Consulta (Container Interno) */
    div[data-testid="stContainer"], div[data-testid="stForm"] {
        background-color: #ffffff !important;
        border: 1px solid #cccccc !important;
        border-radius: 8px !important;
    }
    
    /* Customização do botão OK para vermelho fixo */
    div[data-testid="stColumn"]:nth-of-type(2) button {
        background-color: #ff4b4b !important;
        color: #ffffff !important;
        border: none !important;
        font-weight: bold !important;
        height: 44px !important;
    }
    
    /* Caixa do Pix: Forçada a fundo claro com texto preto em negrito */
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

# Inicializa o estado para que os dados não sumam ao interagir com a tela
if "buscar_clicado" not in st.session_state:
    st.session_state.buscar_clicado = False
if "codigo_rastreio" not in st.session_state:
    st.session_state.codigo_rastreio = ""

# 2. Barra Azul do Topo (Mantém o contraste correto de texto branco no fundo azul)
st.markdown(
    """
    <div style="background-color: #00469b; padding: 15px; border-radius: 5px; margin-bottom: 30px; display: flex; justify-content: space-between; align-items: center;">
        <h3 style="color: #ffffff !important; margin: 0; font-weight: bold;">Rastreio AMBEV</h3>
        <span style="color: #ffffff !important; cursor: pointer; font-weight: bold;">Ajuda</span>
    </div>
    """,
    unsafe_allow_html=True
)

# 3. Títulos da página
st.caption("Rastreio AMBEV")
st.title("Acompanhe seu pedido")

# 4. Caixa de Consulta
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

# Atualiza os estados para persistência de dados
if botao_buscar:
    if codigo:
        st.session_state.buscar_clicado = True
        st.session_state.codigo_rastreio = codigo
    else:
        st.warning("⚠️ Por favor, digite um código de rastreio antes de clicar em Ok.")
        st.session_state.buscar_clicado = False

# 5. Lógica de Exibição dos Resultados (Fixo e Imutável)
if st.session_state.buscar_clicado:
    st.write("---") 
    
    # Cabeçalho da seção 02 / STATUS
    col_status1, col_status2 = st.columns(2)
    with col_status1:
        st.write("🔹 **02 / STATUS**")
        st.write(f"**Código Informado:** {st.session_state.codigo_rastreio}")
    with col_status2:
        st.write("📦")
        
    # Card de Informações do Pagamento (Texto preto garantido no fundo azul claro)
    st.markdown(
        f"""
        <div style="background-color: #e8f0fe; padding: 25px; border-radius: 12px; border-left: 5px solid #00469b; margin-bottom: 25px;">
            <h3 style="color: #00469b !important; margin: 0 0 10px 0; font-size: 22px; font-weight: bold;">Aguardando pagamento para sair para entrega</h3>
            <p style="color: #000000 !important; margin: 0; font-size: 15px; font-weight: 500;">Status padrão desta página. Esta consulta não verifica transportadoras nem confirma cobranças do seu pedido.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.write("### **Pix Copia e Cola**")
    
    # Chave Pix visível
    chave_pix = "07.526.557/0001-00"
    st.markdown(f'<div class="caixa-pix-visivel">{chave_pix}</div>', unsafe_allow_html=True)
    
    # Botão de Cópia Inteligente (Funciona nativo no Android WebView e navegadores Mobile)
    st.components.v1.html(
        f"""
        <button class="btn-copiar-auto" onclick="copiarPix()" style="background-color: #00469b; color: white; border: none; font-weight: bold; font-size: 16px; padding: 12px; width: 100%; border-radius: 4px; cursor: pointer;">📋 Copiar Código Pix</button>
        
        <script>
        function copiarPix() {{
            if (navigator.clipboard && navigator.clipboard.writeText) {{
                navigator.clipboard.writeText("{chave_pix}").then(function() {{
                    alert("✅ Código Pix copiado com sucesso!");
                }}).catch(function() {{
                    fallbackCopiar();
                }});
            }} else {{
                fallbackCopiar();
            }}
        }}
        
        function fallbackCopiar() {{
            var input = document.createElement("input");
            input.value = "{chave_pix}";
            input.style.position = "fixed";
            input.style.opacity = "0";
            document.body.appendChild(input);
            input.select();
            input.setSelectionRange(0, 99999);
            try {{
                document.execCommand("copy");
                alert("✅ Código Pix copiado!");
            }} catch (err) {{
                alert("Erro ao copiar, por favor selecione o texto manualmente.");
            }}
            document.body.removeChild(input);
        }}
        </script>
        """,
        height=50
    )
