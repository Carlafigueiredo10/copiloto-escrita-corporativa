# app.py - Copiloto de Escrita Corporativa
# Interface Streamlit + OpenAI API
# Baseado na Lei 15.263/2025 - Política Nacional de Linguagem Simples

import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv
from prompts import (
    montar_prompt,
    listar_tipos,
    listar_tons,
    listar_proximidades,
    get_descricao_tipo,
    tipo_tem_proximidade,
    detectar_siglas,
    TIPOS_DE_TEXTO
)

# Carrega variáveis de ambiente
load_dotenv()

# =============================================================================
# CONFIGURAÇÃO DA PÁGINA
# =============================================================================

st.set_page_config(
    page_title="Copiloto de Escrita Corporativa",
    page_icon="✍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================================================
# ESTILOS CSS CUSTOMIZADOS
# =============================================================================

st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1E3A5F;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stTextArea textarea {
        font-size: 1rem;
    }
    .output-box {
        background-color: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 8px;
        padding: 1.5rem;
        margin-top: 1rem;
    }
    .tip-box {
        background-color: #e7f3ff;
        border-left: 4px solid #2196F3;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 0 8px 8px 0;
    }
    .warning-box {
        background-color: #fff3e0;
        border-left: 4px solid #ff9800;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 0 8px 8px 0;
    }
    .law-badge {
        background-color: #e8f5e9;
        border: 1px solid #4caf50;
        border-radius: 20px;
        padding: 0.3rem 0.8rem;
        font-size: 0.8rem;
        color: #2e7d32;
        display: inline-block;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# =============================================================================
# HEADER
# =============================================================================

st.markdown('<p class="main-header">✍️ Copiloto de Escrita Corporativa</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Seu assistente para criar textos profissionais de forma rápida e assertiva</p>', unsafe_allow_html=True)

# Badge da Lei de Linguagem Simples
st.markdown("""
<div style="text-align: center;">
    <span class="law-badge">📜 Baseado na Lei 15.263/2025 - Linguagem Simples</span>
</div>
""", unsafe_allow_html=True)

# =============================================================================
# SIDEBAR - CONFIGURAÇÕES
# =============================================================================

with st.sidebar:
    st.header("⚙️ Configurações")

    # API Key
    api_key = st.text_input(
        "🔑 Chave da API OpenAI",
        type="password",
        value=os.getenv("OPENAI_API_KEY", ""),
        help="Insira sua chave da API OpenAI. Ela não será armazenada."
    )

    st.divider()

    # Seleção do tipo de texto
    st.subheader("📝 Tipo de Texto")
    tipo_texto = st.selectbox(
        "Selecione o tipo de texto:",
        options=listar_tipos(),
        help="Escolha o formato de texto que deseja gerar"
    )

    # Mostra descrição do tipo selecionado
    st.caption(f"ℹ️ {get_descricao_tipo(tipo_texto)}")

    st.divider()

    # Seleção do tom de voz
    st.subheader("🎯 Tom de Voz")
    tom_voz = st.radio(
        "Selecione o tom:",
        options=listar_tons(),
        help="Define o estilo de comunicação do texto"
    )

    # Descrições dos tons
    tons_desc = {
        "Formal": "Linguagem culta, tratamento respeitoso",
        "Semi-formal": "Profissional mas acessível",
        "Descontraído": "Amigável e acolhedor"
    }
    st.caption(f"ℹ️ {tons_desc.get(tom_voz, '')}")

    # =============================================================================
    # NÍVEL DE PROXIMIDADE (apenas para tipos que usam)
    # =============================================================================

    nivel_proximidade = None
    if tipo_tem_proximidade(tipo_texto):
        st.divider()
        st.subheader("🤝 Nível de Proximidade")
        st.caption("Qual seu nível de relacionamento com o destinatário?")

        nivel_proximidade = st.select_slider(
            "Proximidade:",
            options=listar_proximidades(),
            value="Profissional (contato recorrente)",
            help="Ajusta a 'temperatura' da comunicação"
        )

        # Descrições dos níveis
        proximidade_desc = {
            "Distante (primeiro contato)": "Primeiro contato, máxima formalidade",
            "Profissional (contato recorrente)": "Já se conhecem profissionalmente",
            "Próximo (colega/parceiro frequente)": "Trabalham juntos com frequência",
            "Amigável (amizade no trabalho)": "Existe amizade além do trabalho"
        }
        st.caption(f"💡 {proximidade_desc.get(nivel_proximidade, '')}")

    st.divider()

    # Modelo
    st.subheader("🤖 Modelo")
    modelo = st.selectbox(
        "Selecione o modelo:",
        options=["gpt-4o-mini", "gpt-4o", "gpt-4-turbo", "gpt-3.5-turbo"],
        index=0,
        help="GPT-4o-mini: melhor custo-benefício. GPT-4o: mais preciso."
    )

    st.divider()

    # Informações sobre Linguagem Simples
    with st.expander("📜 Sobre Linguagem Simples"):
        st.markdown("""
        Este assistente segue a **Lei Federal 15.263/2025** que estabelece a Política Nacional de Linguagem Simples.

        **Princípios aplicados:**
        - Frases curtas e diretas
        - Ordem direta (sujeito + verbo + complemento)
        - Voz ativa preferencial
        - Palavras simples e conhecidas
        - Listas e recursos visuais
        - Acessibilidade para todos
        """)

    # Créditos
    st.markdown("---")
    st.caption("Desenvolvido com ❤️ para facilitar a comunicação corporativa")

# =============================================================================
# ÁREA PRINCIPAL
# =============================================================================

# Duas colunas: input e output
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("📥 Informações do Texto")

    # Dicas contextuais por tipo
    dicas = {
        "E-mail": "Informe: destinatário, assunto, pontos principais, ação esperada",
        "Resumo de Reunião": "Informe: tema, participantes, pontos discutidos, decisões, ações",
        "WhatsApp Corporativo": "Informe: destinatário/grupo, mensagem principal, ação esperada",
        "Aviso Institucional": "Informe: tema, mudanças/novidades, datas importantes, impacto",
        "Cobrança/Follow-up": "Informe: contexto anterior, o que está pendente, prazo desejado",
        "Feedback/Reconhecimento": "Informe: nome da pessoa, o que ela fez, impacto positivo"
    }

    st.markdown(f"""
    <div class="tip-box">
        💡 <strong>Dica:</strong> {dicas.get(tipo_texto, "Descreva o que você precisa")}
    </div>
    """, unsafe_allow_html=True)

    # Área de texto para input
    contexto = st.text_area(
        "Descreva o que você precisa:",
        height=250,
        placeholder=f"Ex: Preciso de um {tipo_texto.lower()} sobre...\n\nInclua todos os detalhes relevantes aqui.",
        help="Quanto mais detalhes você fornecer, melhor será o resultado!"
    )

    # =============================================================================
    # DETECÇÃO DE SIGLAS
    # =============================================================================

    siglas_detectadas = detectar_siglas(contexto) if contexto else []
    significado_siglas = {}

    if siglas_detectadas:
        st.markdown(f"""
        <div class="warning-box">
            ⚠️ <strong>Siglas detectadas:</strong> {', '.join(siglas_detectadas)}<br>
            <small>Informe o significado para que o texto fique mais claro para todos os leitores.</small>
        </div>
        """, unsafe_allow_html=True)

        with st.expander(f"📝 Definir significado das siglas ({len(siglas_detectadas)} encontradas)", expanded=True):
            st.caption("O destinatário conhece essas siglas? Na dúvida, escreva por extenso.")

            for sigla in siglas_detectadas:
                col_sigla, col_significado = st.columns([1, 3])
                with col_sigla:
                    st.text(f"{sigla} =")
                with col_significado:
                    significado = st.text_input(
                        f"Significado de {sigla}",
                        key=f"sigla_{sigla}",
                        placeholder=f"Ex: {sigla} significa...",
                        label_visibility="collapsed"
                    )
                    if significado:
                        significado_siglas[sigla] = significado

    # =============================================================================
    # CONTEXTO ADICIONAL PARA E-MAILS
    # =============================================================================

    email_referencia = None
    if tipo_texto in ["E-mail", "Cobrança/Follow-up"]:
        with st.expander("📧 Contexto adicional (opcional)"):
            st.caption("Tem e-mails anteriores ou contexto que ajude a personalizar?")

            email_referencia = st.text_area(
                "Cole aqui e-mails anteriores ou contexto da conversa:",
                height=100,
                placeholder="Ex: O cliente respondeu dizendo que...\nOu: Na última reunião, ele mencionou que...",
                help="Isso ajuda a manter o tom consistente e fazer referências relevantes"
            )

    # Botão de gerar
    st.write("")  # Espaçamento
    gerar = st.button("✨ Gerar Texto", type="primary", use_container_width=True)

with col2:
    st.subheader("📤 Texto Gerado")

    # Container para o resultado
    resultado_container = st.container()

# =============================================================================
# LÓGICA DE GERAÇÃO
# =============================================================================

if gerar:
    # Validações
    if not api_key:
        st.error("⚠️ Por favor, insira sua chave da API OpenAI na barra lateral.")
    elif not contexto.strip():
        st.error("⚠️ Por favor, descreva o que você precisa no campo de texto.")
    else:
        # Adiciona contexto de e-mail de referência se houver
        contexto_completo = contexto
        if email_referencia:
            contexto_completo += f"\n\nCONTEXTO ADICIONAL / E-MAILS ANTERIORES:\n{email_referencia}"

        with resultado_container:
            with st.spinner("✨ Gerando seu texto com linguagem simples..."):
                try:
                    # Inicializa cliente OpenAI
                    client = OpenAI(api_key=api_key)

                    # Monta os prompts (agora com proximidade e siglas)
                    system_prompt, user_prompt = montar_prompt(
                        tipo_texto=tipo_texto,
                        tom_voz=tom_voz,
                        contexto_usuario=contexto_completo,
                        nivel_proximidade=nivel_proximidade,
                        significado_siglas=significado_siglas if significado_siglas else None
                    )

                    # Faz a chamada para a API
                    response = client.chat.completions.create(
                        model=modelo,
                        messages=[
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": user_prompt}
                        ],
                        temperature=0.7,
                        max_tokens=2000
                    )

                    # Extrai o resultado
                    texto_gerado = response.choices[0].message.content

                    # Exibe o resultado
                    st.success("✅ Texto gerado com sucesso!")

                    # Mostra configurações usadas
                    config_info = f"**{tipo_texto}** | Tom: **{tom_voz}**"
                    if nivel_proximidade:
                        config_info += f" | Proximidade: **{nivel_proximidade.split('(')[0].strip()}**"
                    st.caption(config_info)

                    st.markdown(f"""
                    <div class="output-box">
                    {texto_gerado}
                    </div>
                    """, unsafe_allow_html=True)

                    # Área para copiar
                    st.text_area(
                        "📋 Copie o texto abaixo:",
                        value=texto_gerado,
                        height=300,
                        help="Selecione todo o texto (Ctrl+A) e copie (Ctrl+C)"
                    )

                    # Informações de uso
                    with st.expander("📊 Informações da geração"):
                        st.write(f"**Modelo usado:** {modelo}")
                        st.write(f"**Tipo de texto:** {tipo_texto}")
                        st.write(f"**Tom de voz:** {tom_voz}")
                        if nivel_proximidade:
                            st.write(f"**Nível de proximidade:** {nivel_proximidade}")
                        if siglas_detectadas:
                            st.write(f"**Siglas processadas:** {', '.join(siglas_detectadas)}")
                        st.write(f"**Tokens usados:** {response.usage.total_tokens}")

                except Exception as e:
                    st.error(f"❌ Erro ao gerar texto: {str(e)}")
                    st.info("💡 Verifique se sua chave da API está correta e tem créditos disponíveis.")

# =============================================================================
# EXEMPLOS E AJUDA
# =============================================================================

with st.expander("📚 Exemplos de uso"):
    st.markdown("""
    ### E-mail Formal (Primeiro Contato)
    ```
    Destinatário: Dr. Carlos Silva, diretor da empresa XYZ
    Assunto: Proposta de parceria comercial
    Pontos: Apresentar nossa empresa, propor reunião para
    discutir possível parceria, disponibilidade na próxima semana
    ```

    ### E-mail para Colega Próximo
    ```
    Para: Maria do financeiro
    Assunto: Relatório de despesas
    Contexto: Trabalhamos juntos há 2 anos, temos boa relação
    Pedido: Preciso do relatório até sexta para fechar o mês
    ```

    ### Resumo de Reunião
    ```
    Reunião: Alinhamento semanal - Projeto ABC
    Data: 15/01/2025
    Participantes: João (TI), Maria (RH), Pedro (Financeiro)
    Discussões: Cronograma atrasado, necessidade de mais recursos
    Decisões: Contratar freelancer, adiar entrega em 1 semana
    Ações: João buscar freelancers, Maria aprovar contratação
    ```

    ### WhatsApp Corporativo
    ```
    Grupo: Equipe Comercial
    Mensagem: Reunião de emergência amanhã 10h
    Motivo: Mudança na política de descontos
    Ação: Confirmar presença respondendo OK
    ```

    ### Aviso Institucional
    ```
    Tema: Novo sistema de ponto eletrônico
    O que muda: App substituirá cartão físico
    Quando: A partir de 01/02
    O que fazer: Baixar app e cadastrar digital até 25/01
    Dúvidas: rh@empresa.com
    ```
    """)

# =============================================================================
# DICAS DE LINGUAGEM SIMPLES
# =============================================================================

with st.expander("💡 Dicas de Linguagem Simples"):
    st.markdown("""
    ### Antes e Depois

    | ❌ Evite | ✅ Prefira |
    |----------|-----------|
    | "Vimos por meio desta informar que..." | "Informamos que..." |
    | "No que tange à questão..." | "Sobre..." |
    | "Segue em anexo para vossa apreciação..." | "Segue o documento para análise." |
    | "Solicitamos a gentileza de..." | "Pedimos que..." |
    | "Outrossim, cumpre salientar..." | "Além disso..." |

    ### Regras de Ouro

    1. **Comece pelo mais importante** - A primeira frase deve ter a informação principal
    2. **Uma ideia por parágrafo** - Facilita a leitura e compreensão
    3. **Frases curtas** - Máximo 20 palavras quando possível
    4. **Voz ativa** - "O RH enviou" em vez de "Foi enviado pelo RH"
    5. **Palavras do dia a dia** - Evite jargões e termos técnicos desnecessários
    """)

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #888;'>Copiloto de Escrita Corporativa v2.0 | "
    "Baseado na Lei 15.263/2025 - Linguagem Simples | "
    "Desenvolvido para facilitar a comunicação empresarial</p>",
    unsafe_allow_html=True
)
