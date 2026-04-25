# Docker Basic Tutorial & FAQ

Welcome to this Docker tutorial! This guide covers the essentials you need to know when starting with Docker, specifically tailored for the 42 environment and general development.

---

## 1. Images vs. Containers: The Golden Rule

Understanding the difference between an **Image** and a **Container** is fundamental.

*   **Image**: Think of it as a **Template** or a **Blueprint**. It is a read-only file that contains the OS, libraries, and tools needed to run your application. (Analogy: A class in programming or a cake recipe).
*   **Container**: This is a **Running Instance** of an image. It is the actual environment where your code executes. You can have multiple containers running from the same image. (Analogy: An object in programming or the actual cake).

**Key Command:**
*   `docker images`: Lists all images on your machine.
*   `docker ps`: Lists all **running** containers.
*   `docker ps -a`: Lists **all** containers (running and stopped).

---

## 2. Basic Management & Monitoring

### Running a Container
To start a new container from an image:
```bash
docker run -it --name my_container image_name
```
*   `-i`: Interactive.
*   `-t`: Terminal (TTY).
*   `--name`: Give it a friendly name.
*   `--rm`: (Highly recommended) Automatically remove the container when you exit.

### Monitoring Containers
Standard commands like `docker ps` can be messy. Use formatting for a cleaner view:

**Pretty-print all containers (Running and Stopped):**
```bash
docker ps -a --format "table {{.ID}}\t{{.Image}}\t{{.Status}}\t{{.Names}}"
```

**See resource usage (CPU/Memory) in real-time:**
```bash
docker stats
```

### Stopping, Restarting, and Removing
*   **Stop**: `docker stop <container_id_or_name>` (Sends a SIGTERM).
*   **Restart**: `docker restart <container_id_or_name>`.
*   **Remove Container**: `docker rm <container_id_or_name>` (Must be stopped first).
*   **Remove Image**: `docker rmi <image_id_or_name>`.

#### ⚠️ Common Pitfall: `rm` vs `rmi`
A common mistake is trying to delete an image while using a **Container ID** or **Container Name**.

If you run:
```bash
docker rmi my_container_name
```
You will get: `Error response from daemon: No such image: my_container_name:latest`.

**The fix:**
1.  Check if you are targeting a container or an image.
2.  If it's a **Container**: Use `docker rm` (and stop it first).
3.  If it's an **Image**: Use `docker rmi`.
4.  Remember: You cannot delete an image if it is currently being used by a container (even if the container is stopped). You must delete the container first.

---

## 3. Why are some containers running automatically?

If you notice containers starting by themselves when Docker starts (or after a crash), it's likely due to a **Restart Policy**.

When a container is created with the `--restart` flag, Docker will manage its lifecycle automatically.
Common policies:
*   `always`: Always restarts the container regardless of the exit status.
*   `unless-stopped`: Restarts unless it was manually stopped by the user.
*   `on-failure`: Restarts only if it exited with an error.

### How to stop this?
If you have a container that keeps restarting, you can update its policy to "no":
```bash
docker update --restart=no <container_id_or_name>
docker stop <container_id_or_name>
```

**To check the current restart policy of a container:**
```bash
docker inspect <container_name> --format '{{.HostConfig.RestartPolicy.Name}}'
```

---

## 4. Freeing Up Space (Cleaning the House)

Docker can consume a lot of disk space over time with unused images, stopped containers, and volumes.

### Assessing Space Usage
Before cleaning, check how much space Docker is actually using:
```bash
docker system df
```
To see which specific containers are occupying space (including their writable layer):
```bash
docker ps -as
```

### The "Magic" Command
```bash
docker system prune
```
This will remove:
*   All stopped containers.
*   All networks not used by at least one container.
*   All dangling images (images without a tag).
*   All dangling build cache.

**To be even more aggressive (removes all unused images, not just dangling ones):**
```bash
docker system prune -a
```

**To remove volumes (careful, this deletes data!):**
```bash
docker system prune --volumes
```

**Manual cleanup of "Created" or "Exited" containers:**
```bash
docker container prune
```

---

## 5. Portainer: The GUI for Docker

Portainer is a popular web-based interface to manage your Docker environment.

### How to locate it?
If Portainer is installed as a container, you can find it using:
```bash
docker ps | grep portainer
```

### How to access it?
Portainer usually runs on one of these ports:
*   **9443**: HTTPS (Standard for newer versions).
*   **9000**: HTTP (Older versions).

Open your browser and go to:
*   `https://localhost:9443`
*   `http://localhost:9000`

---

## 6. Accessing Localhost

### Accessing the Host from a Container
If you are inside a container and want to access a service running on your physical machine (the host), use this special DNS name:
`host.docker.internal`

*Example:* If you have a database on your host at port 5432, you connect to `host.docker.internal:5432`.

### Accessing a Container from the Host
To see a web server running inside a container from your browser, you must **map the ports** when running the container:
```bash
docker run -p 8080:80 my_web_image
```
Now, you can access it at `http://localhost:8080` on your host.

---

## 7. Project-Specific: The `42` Command

In this repository, you have a special tool to make your life easier: the `42` alias.

*   **What it does**: It runs the `./run.sh` script, which builds the image (if needed) and starts a container with your current directory mounted at `/app`.
*   **Why use it**: It handles all the complex `docker run` flags for you (SSH agent forwarding, volume mounting, history persistence, etc.).
*   **Automatic Cleanup**: The `42` command uses the `--rm` flag, meaning the container is **automatically deleted** when you exit. This keeps your system clean.

To set it up (if you haven't):
```bash
./setup_alias.sh
source ~/.bashrc  # or ~/.zshrc
```

---

## 8. Useful Tips for Beginners

1.  **Exec into a running container**: If a container is already running and you want to open a new terminal inside it:
    ```bash
    docker exec -it <container_name> bash
    ```
2.  **View Logs**: If a container is behaving weirdly:
    ```bash
    docker logs -f <container_name>
    ```
3.  **Inspect everything**: To see the technical details (IP, mounts, config):
    ```bash
    docker inspect <container_name>
    ```

---

*This tutorial was created to help you navigate the 42Container environment and master the basics of Docker.*
