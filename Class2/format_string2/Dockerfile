FROM ubuntu:22.04
LABEL org.opencontainers.image.authors="YJK"
RUN apt-get update
RUN apt-get install xinetd -y
RUN dpkg --add-architecture i386
RUN apt-get update
RUN apt-get install -y apt-utils
RUN apt-get install -y libc6:i386 libncurses5:i386 libstdc++6:i386
RUN useradd -m format_string2
RUN chown -R root:root /home/format_string2
RUN chmod -R 755 /home/format_string2
CMD ["/usr/sbin/xinetd", "-dontfork"]
