# Documentação da API

Essa API classifica emails  em "produtivo" e "improdutivo" e gera respostas automaticamente usando ia

Eu construí o projeto seguindo os princípios Clean Architecture e SOLID porque isso deixa tudo mais organizado,
fácil de manter e principalmente fácil de evoluir sem quebrar o que já existe

A lógica principal fica nos use cases (no caso deste projeto um exemplo é o arquivo "classify_email.py"). A API recebe
o email, passa pelo use case e ali eu resolvo tudo: classificação e geração da resposta usando LLM eos servios de ia

Para melhorar o resultado da ia, eu não só mando o texto direto, eu defini exemplos separados (em training_data.py), percorro esses
exemplos em um loop e monto o contexto e passo ele de exemplo antes de chamar o modelo. Isso ajuda a deixar a resposta mais consistente
e previsível

Eu usei ia tanto para classificar quanto para responder, a ideia foi centralizar tudo na LLM ao invés de ficar
criando regras fixas no código

O projeto suporta três provedores: OpenAI, Anthropic e Gemini. Todos seguem o mesmo padrão de entrada e saída.
Isso foi possível por causa da separação bem feita das camadas. Na prática, eu consigo trocar o provider só mudando
uma variável no .env

O modelo de ia é montado em factory.py. Ele pega a variável de ambiente "AI_PROVIDER", que pode ser tanto "openai", "gemini" ou "anthropic",
e retorna o modelo correto

A estrutura está separada basicamente em controllers, use cases, providers de IA e config. Cada parte tem sua
responsabilidade, sem misturar lógica

Eu me baseei bastante em dois projetos que já fiz em Python. Um era um sistema que pegava conversas de grupos
e gerava um resumo no final do dia. O outro era um agente financeiro que recebia mensagens via WhatsApp, salvava
no banco e depois gerava análises como diário, semanal e mensal. Usei a mesma linha de raciocínio e princípios nesses
projetos aqui

O objetivo foi criar uma base bem organizada para trabalhar com IA, que dê pra crescer sem virar bagunça
