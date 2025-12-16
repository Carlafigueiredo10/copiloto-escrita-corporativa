# Copiloto de Escrita Corporativa

Assistente inteligente para criar textos corporativos de forma rápida e assertiva, utilizando IA Generativa (OpenAI GPT) e princípios de Linguagem Simples conforme a Lei Federal 15.263/2025.

## Objetivo

Ajudar colaboradores (especialmente RH e comunicação interna) a escrever textos profissionais no dia a dia, economizando tempo, mantendo a qualidade e seguindo boas práticas de comunicação clara.

## Funcionalidades Principais

### Tipos de Texto Suportados

| Tipo | Descrição |
|------|-----------|
| **E-mail** | E-mails formais, informais, follow-ups |
| **Resumo de Reunião** | Atas, decisões, action items |
| **WhatsApp Corporativo** | Mensagens curtas e diretas |
| **Aviso Institucional** | Comunicados e memorandos |
| **Cobrança/Follow-up** | Lembretes gentis de pendências |
| **Feedback/Reconhecimento** | Elogios e reconhecimentos |

### Tons de Voz

- **Formal**: Linguagem culta, tratamento respeitoso
- **Semi-formal**: Profissional mas acessível
- **Descontraído**: Amigável e acolhedor

### Níveis de Proximidade (para e-mails)

| Nível | Quando usar |
|-------|-------------|
| **Distante** | Primeiro contato, cliente novo |
| **Profissional** | Contato recorrente de trabalho |
| **Próximo** | Colega frequente, parceiro |
| **Amigável** | Amizade no trabalho |

### Detecção Automática de Siglas

O assistente detecta automaticamente siglas no texto e solicita ao usuário que informe o significado, garantindo que o texto final seja compreensível para todos os leitores. São detectados padrões como:

- Siglas clássicas: RH, TI, PNGI, CEO
- Com números: ISO9001, G20, COVID19
- Com barras: DECIPEX/SGP, MEC/INEP
- Com hífens: COVID-19, SARS-CoV-2
- Com minúsculas intercaladas: CNPq, UnB, eSocial
- Plurais: ONGs, CPFs, PDFs

### Princípios de Linguagem Simples

A solução segue as diretrizes da **Lei Federal 15.263/2025** (Política Nacional de Linguagem Simples):

- Frases curtas e diretas (máximo 20 palavras)
- Ordem direta: sujeito + verbo + complemento
- Voz ativa preferencial
- Palavras simples e conhecidas
- Uso de listas e recursos visuais
- Acessibilidade para todos os leitores

---

## Como Usar

### Pré-requisitos

- Python 3.8 ou superior
- Chave da API OpenAI ([obter aqui](https://platform.openai.com/api-keys))

### Instalação Local

1. **Clone o repositório**
   ```bash
   git clone https://github.com/Carlafigueiredo10/copiloto-escrita-corporativa.git
   cd copiloto-escrita-corporativa
   ```

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

4. **Execute a aplicação**
   ```bash
   streamlit run app.py
   ```

A aplicação abrirá automaticamente no navegador em `http://localhost:8501`

### Acesso Online

A aplicação também está disponível online:

**https://copiloto-escrita-corporativa.streamlit.app/**

---

## Fluxo de Uso

1. O usuário acessa a aplicação web
2. Insere sua própria chave da API OpenAI
3. Seleciona o tipo de texto desejado
4. Define o tom de voz e o nível de proximidade (quando aplicável)
5. Informa os tópicos e o contexto do texto
6. A aplicação monta dinamicamente um prompt estruturado
7. O prompt é enviado ao modelo de linguagem via API
8. O texto gerado é exibido para uso e eventual revisão

---

## Exemplos de Uso

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

### Aviso Institucional
```
Tema: Novo sistema de ponto eletrônico
O que muda: App substituirá cartão físico
Quando: A partir de 01/02
O que fazer: Baixar app e cadastrar digital até 25/01
Dúvidas: rh@empresa.com
```

---

## Tecnologias Utilizadas

- **Streamlit**: Interface web simples e interativa
- **OpenAI API**: Modelos GPT-3.5-turbo, GPT-4, GPT-4o e GPT-4o-mini
- **Python**: Linguagem de programação
- **Prompt Engineering**: Técnicas para otimizar resultados da IA

---

## Estrutura do Projeto

```
copiloto-escrita-corporativa/
├── app.py              # Interface Streamlit (aplicação principal)
├── prompts.py          # Templates de prompts e lógica de geração
├── requirements.txt    # Dependências Python
├── .env.example        # Template de configuração da API key
├── .gitignore          # Arquivos ignorados pelo Git
└── README.md           # Esta documentação
```

---

## Modelos de LLM Disponíveis

| Modelo | Características | Custo Aproximado |
|--------|-----------------|------------------|
| gpt-4o-mini | Melhor custo-benefício | ~$0.001 - $0.003 |
| gpt-4o | Alta qualidade | ~$0.005 - $0.015 |
| gpt-4-turbo | Precisão avançada | ~$0.01 - $0.03 |
| gpt-3.5-turbo | Econômico | ~$0.0005 - $0.002 |

*Valores aproximados por texto gerado, podem variar conforme tamanho.*

---

## Personalização

### Adicionar novo tipo de texto

Edite o arquivo `prompts.py` e adicione uma nova entrada no dicionário `TIPOS_DE_TEXTO`:

```python
"Novo Tipo": {
    "nome": "Nome Completo do Tipo",
    "descricao": "Descrição breve",
    "tem_proximidade": True,  # ou False
    "prompt": """Instruções para a IA..."""
}
```

### Ajustar tom de voz

Edite o dicionário `TONS_DE_VOZ` em `prompts.py` para personalizar os estilos de comunicação.

---

## Considerações de Segurança e Privacidade

- Os dados enviados são processados pela API da OpenAI e não são utilizados para treinamento do modelo
- Cada usuário utiliza sua própria chave de API, garantindo controle individual sobre o consumo
- Não há armazenamento persistente de dados na aplicação
- Recomenda-se evitar o envio de informações sensíveis ou dados pessoais
- A solução deve ser utilizada em conformidade com a LGPD e políticas de governança da informação

---

## Licença

Este projeto é de uso livre para fins educacionais e corporativos.

---

Desenvolvido para facilitar a comunicação corporativa, seguindo princípios de Linguagem Simples e boas práticas de escrita profissional.
