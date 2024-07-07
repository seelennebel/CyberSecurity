FROM node:latest

WORKDIR /app

COPY package.json ./

RUN npm install

COPY server /app

EXPOSE 8080

CMD [ "node", "server.js" ]