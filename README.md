# [`ds_api_on_docker`]
API que prevê a temperatura do dia seguinte baseado na temperatura de hoje, e na condicão de chuva ou não no dia de hoje.

Para rodar:
Abra o terminal na pasta do projeto. Insira o comando abaixo no terminal:
docker build -t  nomequalquer .

Espere a imagem ser gerada. Após isso, rodar no terminal:
docker run -p 7009:5050 nomequalquer

Agora a API estara recebendo requisições no localhost, porta 7009.

Argumentos

choveu: bool, aceita 0 ou 1.

temp: float.

Exemplo de requisição no navegador:

http://0.0.0.0:7009/?choveu=1&temp=12

