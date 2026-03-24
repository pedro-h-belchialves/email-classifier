# Email Classifier with AI

Este projeto consiste em uma aplicação web para classificação automática de emails e sugestão de respostas utilizando inteligência artificial. A solução foi desenvolvida como parte do **teste técnico da AutoU**, com foco em organização, escalabilidade e facilidade de execução.

A aplicação permite o envio de texto direto ou arquivos (.txt e .pdf), realiza o processamento do conteúdo e retorna a classificação (Produtivo ou Improdutivo) junto com uma resposta sugerida.

## Arquitetura e Tecnologias

O projeto foi estruturado seguindo princípios de **Clean Architecture** e **SOLID**, visando separação de responsabilidades, facilidade de manutenção e evolução do código.

### Backend

- Python
- FastAPI
- Integração com múltiplos provedores de IA (OpenAI, Gemini, Anthropic)
- Processamento de texto (NLP básico)

A API foi construída com uma abordagem desacoplada baseada em contratos.

#### Integração com IA

Foi definido um **contrato de serviço de IA**, permitindo trocar facilmente o provedor sem alterar a regra de negócio.

Foram implementados três serviços:

- OpenAI
- Gemini AI
- Anthropic

A escolha do provedor é feita dinamicamente através de uma **factory (`Factory.py`)**, que lê as variáveis definidas no `.env`, como:

```
AI_PROVIDER=openai | gemini | anthropic
API_KEY=your_api_key
```

Essa factory instancia o provider correto e injeta no **UseCase**, mantendo o domínio desacoplado da infraestrutura.

#### Classificação e Rotas

A API expõe duas rotas principais:

- `/classify` → recebe texto direto
- `/classify-file` → recebe arquivos

A lógica de classificação é centralizada no UseCase, que utiliza o serviço de IA retornado pela factory para:

- Classificar o email (Produtivo / Improdutivo)
- Gerar uma resposta automática

#### Parser de Arquivos

Foi implementado também um padrão baseado em contrato para parsing de arquivos.

- Um contrato de parser define a interface
- Dois serviços concretos foram implementados:
  - Parser de PDF
  - Parser de TXT

A escolha do parser é feita dinamicamente com base no tipo do arquivo recebido na rota `/classify-file`.

Isso mantém o sistema extensível (ex: adicionar suporte para .docx no futuro sem alterar regras existentes).

---

### Frontend

- HTML + TailwindCSS
- Interface simples, responsiva e focada na experiência do usuário
- Comunicação direta com a API

O frontend foi pensado para ser limpo, intuitivo e direto, priorizando usabilidade e clareza na exibição dos resultados.

---

### Infraestrutura

- Docker
- Docker Compose

Toda a aplicação é orquestrada com Docker Compose, permitindo subir o ambiente completo com um único comando, garantindo consistência entre ambientes.

---

## Estrutura do Projeto

```
/backend     → API em Python
/frontend    → Interface web
/docker-compose.yml
```

---

## Como executar o projeto

### 1. Clonar o repositório

Clone o repositório em sua máquina e acesse a pasta do projeto.

---

### 2. Configurar variáveis de ambiente

Dentro da pasta do backend, crie um arquivo `.env` com as variáveis necessárias.

Exemplo:

```
AI_PROVIDER=openai
OPENAI_API_KEY=your_api_key_here
GEMINI_API_KEY=your_api_key_here
ANTHROPIC_API_KEY=your_api_key_here
```

---

### 3. Subir a aplicação

Execute o comando abaixo na raiz do projeto:

```bash
docker-compose up --build
```

---

### 4. Acessar

A aplicação estará disponível em:

```
http://localhost:3002
```

---

## Deploy na Nuvem

Para o ambiente de produção, optei por separar os serviços para melhor aproveitamento de cada plataforma:

- **Backend (API)** hospedado no Render
- **Frontend** hospedado na Vercel

Essa separação permite melhor otimização, escalabilidade e uso adequado das características de cada serviço.

---

## Decisões técnicas

- Utilização de **Docker Compose** para facilitar execução e padronizar ambiente
- Arquitetura baseada em **Clean Architecture** e **SOLID**
- Uso de **Factory Pattern** para seleção dinâmica do provedor de IA
- Uso de **contratos (interfaces)** para desacoplar serviços de IA e parsing
- Separação clara entre frontend e backend
- Interface pensada para ser simples, funcional e com boa experiência

---

## Experiência prévia

Este projeto foi desenvolvido com base em experiências anteriores na construção de aplicações com integração de IA, APIs e processamento de dados, o que permitiu tomar decisões mais assertivas em arquitetura e organização.

---

## Considerações finais

O foco principal foi entregar uma solução funcional, organizada e fácil de executar, simulando um cenário real de aplicação em produção.

A aplicação foi pensada para ser facilmente extensível, permitindo adicionar novos provedores de IA, novos formatos de arquivo ou novas regras de classificação sem impacto significativo na arquitetura existente.
