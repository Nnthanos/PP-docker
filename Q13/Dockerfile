FROM node:18-alpine
# precisa instalar o git
RUN apk add --no-cache git

WORKDIR /app

RUN git clone https://github.com/eMahtab/node-express-hello-world.git .
# instala as dependências do projeto
RUN npm install

EXPOSE 3000

RUN ["npm", "start" ]