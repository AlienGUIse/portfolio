FROM nginx:latest
COPY ./src/* /usr/share/nginx/html
EXPOSE 8080