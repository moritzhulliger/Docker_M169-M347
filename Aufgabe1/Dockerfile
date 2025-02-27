FROM alpine:latest

LABEL maintainer="test@gmail.com"

# Install Node and NPM
RUN apk add --update nodejs npm curl

# Copy app to /src
COPY . /src

WORKDIR /src

# Install dependencies
RUN  npm install

EXPOSE 8080

# Use a non-root user for security
RUN adduser -D -h /src appuser && chown -R appuser /src
USER appuser

ENTRYPOINT ["node", "./app.js"]
