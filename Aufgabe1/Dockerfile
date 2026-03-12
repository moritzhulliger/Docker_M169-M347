FROM node:20-bullseye-slim

LABEL maintainer="test@gmail.com"

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

RUN adduser --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

EXPOSE 8084

CMD ["node", "dist/app.mjs"]