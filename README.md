# flask-test-genius-api

Passos para rodar o projeto:

    1 - Após clonar o projeto, entrar na pasta "flask-test-genius-api" e realizar a instalação das dependências
    que estão no arquivo requirements.txt através do comando "pip install -r requiriments.txt".

    2 - Adicionar as credenciais da AWS através do comando "aws configure".

    3 - Rodar o script "create_table.py" através do comando "python create_table.py",
    passando os parâmetros:
            "AWS ACCESS KEY id",
            "AWS SECRET ACCESS KEY",
            "Default Region Name"

    4 - Rodar o script "python app.py"


Realizando Testes :

Para realizar os testes, utilizar a seguinte url: "http://127.0.0.1:5000/genius/<nome_do_artista>/"

Exemplos de teste:

    http://127.0.0.1:5000/genius/metallica/

    http://127.0.0.1:5000/genius/nirvana/

    http://127.0.0.1:5000/genius/nirvana/?cache=False

    http://127.0.0.1:5000/genius/aerosmith/

    http://127.0.0.1:5000/genius/eminem/

    http://127.0.0.1:5000/genius/eminem/?cache=False



Para visualizar os dados no redis, utilizar o redis-cli e os seguintes comandos:

    KEYS *                      (Visualizar todos artistas que estão salvos no redis)
    GET "nome_do_artista"       (Verificar as informações do artista que foram salvas) 
    TTL "nome_do_artista"       (Verificar o tempo de expiração (em segundos) do registro) 



