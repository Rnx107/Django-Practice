# 1. Stop and remove the failing container
podman rm -f n8n

# 2. Force the folder ownership to match the container's internal 'node' user
# Podman unshare allows you to run a command in the same user namespace as the container
podman unshare chown -R 1000:1000 ~/n8n_data

# 3. Start it one more time with the :Z flag
podman run -d \
  --name n8n \
  -p 5678:5678 \
  -v ~/n8n_data:/home/node/.n8n:Z \
  --restart unless-stopped \
  docker.io/n8nio/n8n
