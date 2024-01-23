FROM ubuntu:jammy


# Fix locale
RUN apt-get update && \
    echo 'Etc/UTC' > /etc/timezone && \
    ln -s /usr/share/zoneinfo/Etc/UTC /etc/localtime && \
    apt-get install -y \
        sudo \
        locales \
        tzdata
RUN locale-gen en_US.UTF-8; dpkg-reconfigure -f noninteractive locales
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LC_ALL en_US.UTF-8

RUN apt-get update && \
    apt-get install -y \
        software-properties-common \
        curl \
        gnupg2\
        bash-completion \
        build-essential \
        cmake \
        git \
        iproute2 \
        build-essential \
        python3-pip &&\
    pip3 install matplotlib &&\
    rm -rf /var/lib/apt/lists/*

RUN useradd -ms /bin/bash user \
    && echo "user:user" | chpasswd \
    && usermod -aG sudo user \
    && echo 'user ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers.d/user \
    && usermod --uid 1000 user \
    && usermod --gid 1000 user   

USER user
WORKDIR /app

