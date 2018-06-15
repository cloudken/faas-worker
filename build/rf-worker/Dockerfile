#add msframe
FROM alpine:latest
MAINTAINER Husong
RUN mkdir -p /root/temp
COPY restframe-*.tar.gz /root/temp/
WORKDIR /root/temp
RUN tar xvfz restframe-*.tar.gz
RUN rm -f restframe-*.tar.gz
RUN mv restframe-* restframe
WORKDIR /root/temp/restframe
RUN mkdir -p /var/log/restframe
RUN mkdir -p /root/data
COPY supervisord-worker.conf /etc/supervisord.conf
WORKDIR /
ENTRYPOINT ["/usr/bin/supervisord"]
