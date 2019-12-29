FROM python:3.9-rc-alpine3.10

RUN apk update && \
    apk add bash && \
    mkdir -p /app
COPY . ./app
WORKDIR /app
CMD tail -f /dev/null
