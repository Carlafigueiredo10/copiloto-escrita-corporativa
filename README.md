# ✍️ Copiloto de Escrita Corporativa

Assistente inteligente para criar textos corporativos de forma rápida e assertiva, utilizando IA Generativa (OpenAI GPT).

## 🎯 Objetivo

Ajudar colaboradores (especialmente RH e comunicação interna) a escrever textos profissionais no dia a dia, economizando tempo e mantendo a qualidade.

## 📝 Tipos de Texto Suportados

| Tipo | Descrição |
|------|-----------|
| **E-mail** | E-mails formais, informais, follow-ups |
| **Resumo de Reunião** | Atas, decisões, action items |
| **WhatsApp Corporativo** | Mensagens curtas e diretas |
| **Aviso Institucional** | Comunicados e memorandos |
| **Cobrança/Follow-up** | Lembretes gentis de pendências |
| **Feedback/Reconhecimento** | Elogios e reconhecimentos |

## 🎨 Tons de Voz

- **Formal**: Linguagem culta, tratamento respeitoso
- **Semi-formal**: Profissional mas acessível
- **Descontraído**: Amigável e acolhedor

---

## 🚀 Como Usar

### Pré-requisitos

- Python 3.8 ou superior
- Chave da API OpenAI ([obter aqui](https://platform.openai.com/api-keys))

### Instalação

1. **Clone o repositório ou baixe os arquivos**

2. **Crie um ambiente virtual (recomendado)**
   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # Linux/Mac
   source venv/bin/activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure sua chave da API**
   ```bash
   # Copie o arquivo de exemplo
   copy .env.example .env

   # Edite o arquivo .env e coloque sua chave
   OPENAI_API_KEY=sk-sua-chave-aqui
   ```

### Executando

```bash
streamlit run app.py
```

A aplicação abrirá automaticamente no navegador em `http://localhost:8501`

---

## 💡 Exemplos de Uso

### E-mail Formal
```
Destinatário: Gerente de Projetos
Assunto: Solicitação de aprovação do orçamento Q1
Pontos: Orçamento de R$ 50.000 para marketing digital,
inclui campanhas no Google Ads e redes sociais,
prazo para aprovação: até sexta-feira
```

### Resumo de Reunião
```
Reunião: Alinhamento semanal da equipe de vendas
Participantes: João, Maria, Pedro
Discussões: Metas do mês, novos leads
Decisões: Aumentar meta em 10%
Ações: João vai preparar relatório até sexta
```

### WhatsApp Corporativo
```
Grupo: Equipe Marketing
Aviso: Reunião de emergência amanhã às 10h
Motivo: Mudança na campanha
Ação: Confirmar presença
```

---

## 🛠️ Tecnologias

- **Streamlit**: Interface web simples e interativa
- **OpenAI API**: GPT-3.5/GPT-4 para geração de texto
- **Python**: Linguagem de programação
- **Prompt Engineering**: Técnicas para otimizar resultados

---

## 📁 Estrutura do Projeto

```
copiloto-escrita-corporativa/
├── app.py              # Interface Streamlit
├── prompts.py          # Templates de prompts
├── requirements.txt    # Dependências Python
├── .env.example        # Template de configuração
├── .gitignore          # Arquivos ignorados pelo Git
└── README.md           # Esta documentação
```

---

## 🔧 Personalização

### Adicionar novo tipo de texto

Edite o arquivo `prompts.py` e adicione uma nova entrada no dicionário `TIPOS_DE_TEXTO`:

```python
"Novo Tipo": {
    "nome": "Nome Completo do Tipo",
    "descricao": "Descrição breve",
    "prompt": """Instruções para a IA..."""
}
```

### Ajustar tom de voz

Edite o dicionário `TONS_DE_VOZ` em `prompts.py` para personalizar os estilos.

---

## 📊 Custos Estimados (OpenAI API)

| Modelo | Custo aproximado por texto |
|--------|---------------------------|
| GPT-3.5-turbo | ~$0.001 - $0.003 |
| GPT-4 | ~$0.01 - $0.03 |
| GPT-4-turbo | ~$0.005 - $0.015 |

*Valores aproximados, podem variar conforme tamanho do texto.*

---

## 🤝 Contribuindo

Sugestões e melhorias são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

---

## 📄 Licença

Este projeto é de uso livre para fins educacionais e corporativos.

---

Desenvolvido com ❤️ para facilitar a comunicação corporativa.
