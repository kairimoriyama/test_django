# Use the official Nginx image as the base image
FROM nginx:latest


RUN cp -f /etc/nginx/nginx.conf /etc/nginx/nginx_bk._conf
RUN mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default_bk._conf


# RUN rm -f /etc/nginx/nginx.conf
# COPY ./config/nginx.conf /etc/nginx/nginx.conf

# COPY ./config/nginx.conf /etc/nginx/sites-available/django_config
# RUN ln -s /etc/nginx/sites-available/django_config /etc/nginx/sites-enaled/

