# Prova 2 - Módulo 10 - Luana Dinamarca Parra 

A questão prática contempla a entrega de: 
1. Realizar a adequação do projeto desenvolvido em Flask para FastAPI (até 1.0 ponto).

2. Adicionar o log em todas as rotas do sistema. O log deve ficar armazenado em um arquivo. Logar apenas informações de nível WARNING em diante (até 3.0 pontos).

3. Implementar o sistema em um container docker (até 1.0 ponto).

4. Adicionar um container com um Gateway utilizando NGINX para o sistema (até 2.0 pontos).

5. Criar um arquivo docker-compose que permita executar toda a aplicação (até 2.0 pontos).

6. Implementar os testes da API com Insomnia (até 1.0 ponto).

## Como executar?

Em primeiro lugar é necessário clonar o repositório com o seguinte comando:

```
git clone https://github.com/luanaparra/prova2_modulo10
```

Dessa maneira, é possível entrar na pasta `/src` e instalar as dependências:

```
python -m pip install -r requirements.txt
```

Por conseguinte, para rodar a implementação na pasta `/src`, execute o comando:
```
docker compose up
```
