FROM ubuntu:22.04
LABEL org.opencontainers.image.authors="YJK"
RUN apt-get update
RUN apt-get install xinetd -y
RUN useradd -m bof
RUN chown -R root:root /home/bof
RUN chmod -R 755 /home/bof
CMD ["/usr/sbin/xinetd", "-dontfork"]
