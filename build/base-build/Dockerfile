from alpine:latest
MAINTAINER Husong
#RUN ["/bin/sh", "-c", "http_proxy=http://proxysh.zte.com.cn:80/ apk add --no-cache python python-dev py-pip gcc linux-headers musl-dev ansible"]
RUN ["/bin/sh", "-c", "http_proxy=http://proxysh.zte.com.cn:80/ apk add --no-cache python python-dev py-pip gcc linux-headers musl-dev ansible"]
RUN mkdir -p /root/temp
COPY restframe-*.tar.gz /root/temp/
WORKDIR /root/temp
RUN tar xvfz restframe-*.tar.gz
RUN rm -f restframe-*.tar.gz
RUN mv restframe-* restframe
WORKDIR /root/temp/restframe
RUN ["/bin/sh", "-c", "https_proxy=https://proxysh.zte.com.cn:80/ pip install -U pip"]
RUN ["/bin/sh", "-c", "https_proxy=https://proxysh.zte.com.cn:80/ pip install -U setuptools"]
RUN ["/bin/sh", "-c", "https_proxy=https://proxysh.zte.com.cn:80/ pip install supervisor"]
RUN ["/bin/sh", "-c", "https_proxy=https://proxysh.zte.com.cn:80/ pip install -r requirements.txt"]
RUN rm -rf /usr/lib/gcc
RUN rm -rf /usr/share
RUN rm -rf /usr/libexec
RUN rm -rf /usr/x86_64-alpine-linux-musl
RUN rm -rf /usr/include
RUN rm -rf /usr/lib/libc.a
COPY build_rf_base.sh /etc/
COPY supervisord-base.conf /etc/supervisord.conf
WORKDIR /
ENTRYPOINT ["/usr/bin/supervisord"]
