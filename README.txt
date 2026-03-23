##Documetação do front

#Incialização local:
rode o comando: "docker compose up -d --build" e o front estará disponívl em http://localhost:3002

#Sobre
Esse projeto é o frontend da aplicação de classificação de emails. Eu desenvolvi usando
HTML, CSS e JavaScript, utilizando Tailwind CSS para acelerar a parte visual e manter
consistência no layout, e em alguns pontos usei CSS puro principalmente para animações.

Também optei por usar SVG direto no código porque facilita na customização e evita depender
de arquivos externos. A interface foi pensada para ser simples e responsiva, funcionando bem
em diferentes tamanhos de tela, seguindo boas práticas de UI/UX como hierarquia visual,
espaçamento e feedback para o usuário, além de aplicar a regra 60-30-10 nas cores, com
predominância de tons neutros e azul como cor principal para transmitir clareza e confiança.

Na parte lógica, o JavaScript faz a integração com a API de classificação, e eu deixei
preparado para funcionar tanto local quanto em produção: quando roda localmente, as
requisições passam por um Nginx usando /api como proxy, e quando está em produção ele chama
direto a API que está no ar (https://email-classifier-api-wvjm.onrender.com/), sem precisar
mudar código. Para rodar local, utilizei Docker com Nginx, que facilita esse proxy e evita
problemas de CORS, e para deploy o frontend pode ser subido direto na Vercel, já que ele é
estático e a lógica já trata a URL correta da API dependendo do ambiente.

O foco foi manter o projeto simples, funcional e organizado, mas já pensando em uma
estrutura que seja fácil de manter e evoluir.
