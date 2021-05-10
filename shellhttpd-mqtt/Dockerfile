# shellhttpd-mqtt/Dockerfile
FROM alpine

RUN apk add --no-cache mosquitto-clients
RUN apk add --no-cache vim

COPY httpd.sh /usr/local/bin/

CMD ["/usr/local/bin/httpd.sh"]
