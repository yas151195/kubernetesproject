FROM centos:latest
MAINTAINER ahmadshaheryar160@gmail.com
RUN yum install -y httpd \
  zip \
 uunzip
ADD https://www.free-css.com/assets/files/free-css-templates/download/page281/koppee.zip /var/www/html
WORKDIR /var/www/html
RUN unzip koppee.zip
RUN cp -rvf koppee/*
RUN rm -rf koppee koppee.zip
CMD ["/usr/sbin/httpd", "-D",  "FOREGROUND"]
EXPOSE 80
