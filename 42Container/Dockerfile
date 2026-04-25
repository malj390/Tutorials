# ============================================
# 42-Like Environment for C Projects & Testing
# Ubuntu 22.04 LTS - Matching 42 Málaga versions
# ============================================

FROM ubuntu:22.04

LABEL maintainer="42-compatible environment" \
      description="Docker image replicating the 42 toolchain setup for consistent testing (Valgrind, Norminette, compilers, shells, etc.)"

ENV DEBIAN_FRONTEND=noninteractive

# ---------------------------
# System and basic toolchain
# ---------------------------
RUN apt update && apt install -y \
    build-essential \
    clang-12 \
    gcc-10 g++-10 \
    cmake \
    make \
    valgrind \
    gdb \
    lldb-12 \
    zsh \
    fish \
    expect \
    git \
    curl \
    wget \
    bash \
    python3 python3-pip \
    ruby-full \
    perl \
    openjdk-17-jdk \
    nodejs npm \
    sudo \
    fzf \
    asciinema \
    locales \
    libreadline-dev \
    libbsd-dev \
    libx11-dev \
    libxext-dev \
    libglfw3-dev \
    libgl1-mesa-dev \
    xorg-dev \
    zlib1g-dev \
    && apt clean && rm -rf /var/lib/apt/lists/*

# ---------------------------
# Configure Locales
# ---------------------------
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# ---------------------------
# Set default compilers
# ---------------------------
RUN update-alternatives --install /usr/bin/cc cc /usr/bin/clang-12 100 \
 && update-alternatives --install /usr/bin/c++ c++ /usr/bin/clang++-12 100 \
 && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-10 90 \
 && update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-10 90

# ---------------------------
# Install Norminette
# ---------------------------
RUN pip3 install --upgrade pip==22.0.2 \
 && pip3 install norminette==3.3.58

# ---------------------------
# Fix Norminette crash
# ---------------------------
COPY norminette_wrapper.sh /tmp/norminette_wrapper.sh
RUN mv /usr/local/bin/norminette /usr/local/bin/norminette.bin && \
    mv /tmp/norminette_wrapper.sh /usr/local/bin/norminette && \
    chmod +x /usr/local/bin/norminette


# ---------------------------
# Create a non-root user
# ---------------------------
ARG USER_ID
ARG GROUP_ID

RUN if [ -n "$USER_ID" ] && [ -n "$GROUP_ID" ]; then \
    groupadd -g $GROUP_ID 42user && \
    useradd -l -u $USER_ID -g $GROUP_ID -m 42user && \
    adduser 42user sudo && \
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers; \
    fi

# ---------------------------
# Setup shell history and custom commands
# ---------------------------
RUN mkdir -p /home/42user/.config/fish && \
    mkdir -p /home/42user/.local/share/fish && \
    touch /home/42user/.bash_history && \
    touch /home/42user/.zsh_history && \
    chown -R $USER_ID:$GROUP_ID /home/42user

USER 42user
ENV HOME /home/42user
ENV SHELL /usr/bin/fish
WORKDIR /home/42user/project

# ---------------------------
# Configure git account from config file
# ---------------------------
RUN git config --global user.name "42user" && \
	git config --global user.email "42user@example.com"




# ---------------------------
# Verify core tool versions
# ---------------------------
RUN echo "==== Installed tool versions ====" && \
    export PATH="/usr/bin:$PATH" && \
    echo "cc: $(cc --version | head -n 1)" && \
    echo "gcc: $(gcc --version | head -n 1)" && \
    echo "clang: $(clang-12 --version | head -n 1)" && \
    echo "python3: $(python3 --version)" && \
    echo "pip3: $(pip3 --version)" && \
    echo "make: $(make --version | head -n 1)" && \
    echo "valgrind: $(valgrind --version)" && \
    echo "norminette: $(norminette --version)" && \
    echo "git: $(git --version)" && \
    echo "curl: $(curl --version | head -n 1)" && \
    echo "wget: $(wget --version | head -n 1)" && \
    echo "bash: $(bash --version | head -n 1)" && \
    echo "zsh: $(zsh --version)" && \
    echo "fish: $(fish --version)" && \
    echo "asciinema: $(asciinema --version)" && \
    echo "gdb: $(gdb --version | head -n 1)" && \
    echo "lldb: $(lldb-12 --version | head -n 1)" && \
    echo "ruby: $(ruby --version)" && \
    echo "node: $(node --version)" && \
    echo "java: $(java -version 2>&1 | head -n 1)" && \
    echo "================================="

# ---------------------------
# Default working directory
# ---------------------------
WORKDIR /app

# ---------------------------
# Default command
# ---------------------------
CMD ["fish"]
