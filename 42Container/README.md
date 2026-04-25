## File Purposes

* **`Dockerfile`**: Defines the Docker image for a 42-like development environment. It starts from an Ubuntu 22.04 base and installs all the necessary tools like `clang`, `gcc`, `make`, `valgrind`, `norminette`, etc. It also creates a non-root user to avoid permission issues.
* **`norminette_wrapper.sh`**: A wrapper script to fix a crash with `norminette`. It calls the original `norminette.bin` with the provided arguments.
* **`run.sh`**: This script builds the Docker image (if it doesn't exist) and runs the container. It mounts the current working directory, shell history files, and git configuration into the container.
* **`setup_alias.sh`**: This script creates a shell function (alias) named `42` in the user's shell configuration file (`.bashrc`, `.zshrc`, or `config.fish`). This allows the user to run the Docker container from any directory.
* 

# 42 Environment Docker Container

This repository provides a Docker-based development environment that replicates the setup used at 42 schools. It allows you to work on your projects in a consistent and predictable environment, regardless of your host operating system.

> **Important Note for Graphical Projects:** This container is designed for terminal-based projects and does not have a graphical environment. Projects that require a graphical interface (like those using MiniLibX, such as `so_long` or `cub3d`) will not run out-of-the-box. Tools like `valgrind` may also behave differently with graphical applications due to the lack of an X11 connection to the host.

## Features

- **OS:** Ubuntu 22.04, matching the 42 network environment.
- **C/C++ Development:** `clang-12` (default `cc`), `gcc-10`, `make`, `gdb`, `lldb-12`, `valgrind`.
- **42 Tools:** `norminette` (v3.3.58).
- **Libraries:** Includes `libreadline-dev`, `libbsd-dev`, `libx11-dev`, and `libxext-dev` for Minishell and MiniLibX support.
- **Shells:** `fish` (default), `zsh`, and `bash`.
- **Project Directory Access:** Your current working directory is mounted inside the container.
- **User Permissions:** Runs with your user and group ID to avoid file ownership issues.
- **Persistent Shell History:** Your `bash`, `zsh`, and `fish` shell histories are shared between your host and the container.
- **Git Integration:**
  - **Authentication:** Forwards your host's SSH agent to the container for secure `git` operations.
  - **Identity:** Uses your host's `.gitconfig` file, or a custom `git_config.env` file.
  - **SSH Keys:** Automatically mounts your `~/.ssh` directory (Read-Write), allowing you to generate and save keys from within the container.
- **Other Development Tools:** Includes `python3`, `ruby`, `perl`, `nodejs`, `java`, and more.

## Configuration

### Git Identity
You can configure your Git user and email by editing the `git_config.env` file in the root of this repository. Uncomment the lines and add your details:
```bash
GIT_USER="Your Name"
GIT_EMAIL="your.email@example.com"
```
These settings will be passed to the container and used for your Git commits.

### SSH Keys
Your `~/.ssh` directory is automatically mounted into the container with Read-Write access.
- **Existing Keys:** Keys on your host are available inside the container.
- **New Keys:** You can generate new SSH keys inside the container (e.g., `ssh-keygen`), and they will be saved to your host machine's `~/.ssh` directory, persisting across sessions.

## Prerequisites

- **Docker:** You must have Docker installed and running on your system.
- **Git:** Your name and email should be configured in your global `.gitconfig` file (`~/.gitconfig`).

## For Windows Users: Using WSL 2

This project is designed for a Linux environment and its scripts (`.sh` files) are not compatible with Windows PowerShell. The recommended way to use this environment on Windows is through the **Windows Subsystem for Linux (WSL 2)**.

WSL 2 provides a full Linux kernel running directly on Windows, offering the best performance and compatibility for Docker.

### WSL 2 Setup Guide

* **Ensure [Docker Desktop](https://www.docker.com/products/docker-desktop/) is Running:** Before proceeding with any steps, make sure Docker Desktop is installed and actively running on your Windows machine. The Docker engine must be operational for any Docker commands (including building images or running containers) to succeed.
1. **Install WSL 2:** If you don't have WSL installed, open a PowerShell terminal as an administrator and run:
   
   ```powershell
   wsl --install
   ```
   
   This command will install the latest Ubuntu distribution by default. A reboot may be required.

2. **Install Docker Desktop:** Download and install [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop). During setup, ensure you select the option to **"Use the WSL 2 based engine"**. If you already have it installed, you can enable WSL 2 integration in Docker Desktop's settings under `Settings > Resources > WSL Integration`.

3. **Open the WSL Terminal:** Once installed, open your WSL distribution (e.g., "Ubuntu") from the Start Menu.

4. **Clone the project:** Inside the WSL terminal, clone this repository.
   
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

5. **Follow the standard instructions:** From this point on, you are in a Linux environment. You can now follow the main `Getting Started` guide as written, by running `./run.sh` and `./setup_alias.sh` from within your WSL terminal. Your files will be accessible from both Windows and WSL.

### A Note on Performance

You might be concerned about performance, thinking this setup is like a "virtual machine inside a virtual machine." However, the integration between WSL 2 and Docker Desktop is highly optimized to be very efficient.

- **CPU and Memory are Near-Native:** WSL 2 runs on a lightweight, highly integrated hypervisor, not a traditional, slow VM. For CPU-intensive tasks like compiling or running `valgrind`, the performance is near-native. You should not experience any significant slowdown.

- **File System I/O is Key:** The most important factor for a smooth experience is where you store your project files. For the best performance, **always store your project files inside the WSL filesystem** (e.g., in your WSL home directory, `~/projects/`). Accessing files from the Windows filesystem (e.g., `/mnt/c/Users/...`) is much slower and not recommended for active development.

By following this advice, you will have a fast and responsive development environment on Windows.

> **Note:** With this setup, Docker commands are run from within WSL, and Docker Desktop for Windows handles the container management.

## How it Works: The `42` Command

The main goal of this project is to provide a seamless workflow. The intended use is to `cd` into one of your 42 project directories and simply run the `42` command.

When you do this, you will be placed inside a container that has all the necessary tools for your project (`cc`, `make`, `valgrind`, etc.). The directory you were in is now mounted at `/app` inside the container, so you can compile your code, run your tests, and use `git` as if you were on a 42 school machine.

## Getting Started: A Step-by-Step Guide

### Step 1: Initial Container Setup

Before you can use the `42` command, you need to build the Docker image and set up the shell shortcut.

1. **Run the script:** Navigate to this project directory (the one containing the `Dockerfile`) and run the following command:
   
   ```bash
   ./run.sh
   ```
   
   You must run this command from this specific directory because it needs to find the `Dockerfile` to build the image. The first time you run this, it will take a few minutes to build the Docker image. The script will then drop you into a shell inside the container. You can simply `exit` for now.

2. **Set up the shortcut:** To create the convenient `42` command, run the setup script from the same directory:
   
   ```bash
   ./setup_alias.sh
   ```
   
   This script adds a function named `42` to your shell's configuration file (`.zshrc`, `.bashrc`, or `config.fish`). This function is a shortcut that calls the `./run.sh` script from this project's directory, allowing you to launch the container from anywhere on your system.

   > **Warning:** Do not move this repository directory after running the setup script! The alias stores the *absolute path* to this folder. If you move the folder, the `42` command will stop working.

3. **Restart your terminal:** For the `42` command to become active, you need to either restart your terminal or "source" your shell's configuration file (e.g., `source ~/.zshrc`).

### Step 2: Your Daily Workflow

Once the setup is complete, your workflow will be simple:

1. Open a terminal and navigate to the 42 project you want to work on.
   
   ```bash
   cd ~/path/to/your/42_project
   ```

2. Run the `42` command.
   
   ```bash
   42
   ```

3. You are now inside the container! Your project files are right there, in the `/app` directory. You can compile your code, run `norminette`, use `valgrind`, and `git push` your changes, all using the familiar 42 environment.
   
   ```bash
   # Inside the container
   42user@42container /app> ls
   Makefile  includes/  libft/  sources/
   42user@42container /app> make
   ...
   ```

### Step 3: Exiting the Container

To exit the container's interactive session, you can either run the `exit` command or press `Ctrl+D`. The container will automatically stop and remove itself.

## Container Management

### Checking if the Container is Running

If you are running the

 `42` command in one terminal, you can verify that the container is active from another terminal using `docker ps`. Since the container is configured with `--rm` (remove on exit), it will only appear in this list while it's actively running an interactive session.

```bash
docker ps
```

### Forcing a Rebuild

If you modify the `Dockerfile` or suspect the Docker image is corrupted, you may need to force a rebuild.

1. **Remove the existing image:**
   
   ```bash
   docker rmi 42-env
   ```

2. **Run the container again:**
   The next time you run `./run.sh` or the `42` command, the script will detect that the image is missing and build a new one.
   
   ```bash
   42
   ```

### Installing New Programs or Upgrading

To add new tools to your environment or upgrade existing ones, you should modify the `Dockerfile` and rebuild the image. For detailed instructions on how to do this (both temporarily and permanently), see the **[Docker Tutorial](Docker_tutorial.md#9-upgrading--installing-new-programs)**.
