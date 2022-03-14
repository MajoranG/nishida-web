FROM httpd:latest
RUN apt-get update &&\
    apt-get install -y python3 python3-pip locales&&\
    pip3 install pytz
RUN usermod -u 1000 www-data &&\
    groupmod -g 1000 www-data
