FROM nginx:latest

ADD ./server.conf /etc/nginx/conf.d/default.conf

RUN mkdir /root/logs
RUN chmod 755 -R /root

COPY ./public /root/public

CMD ["nginx", "-g", "daemon off;"]
