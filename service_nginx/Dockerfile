FROM nginx:1.15.3

ARG ENVIRONMENT

RUN mkdir -p /service_nginx
WORKDIR /service_nginx

RUN mkdir -p volumes volumes/nginx volumes/staticfiles volumes/mediafiles volumes/ssl
RUN mkdir -p commands

RUN chown -R nginx:nginx volumes/staticfiles
RUN chown -R nginx:nginx volumes/mediafiles
