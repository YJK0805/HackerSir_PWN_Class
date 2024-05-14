FROM ubuntu:22.04
LABEL org.opencontainers.image.authors="YJK"
RUN apt-get update
RUN apt-get install xinetd -y
RUN useradd -m FormatString2
RUN chown -R root:root /home/FormatString2
RUN chmod -R 755 /home/FormatString2
CMD ["/usr/sbin/xinetd", "-dontfork"]
