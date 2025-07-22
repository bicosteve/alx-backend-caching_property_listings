# 1. accessing gcp vm instance

```bash
gcloud compute ssh my-vm-instance --zone=us-central1-a

# create ssh key for code repo
ssh-keygen -t ed25519 -C "your-email@example.com"
cat ~/.ssh/id_ed25519.pub  # Copy this into GitHub → Settings → SSH keys
ssh -T git@github.com       # Verify authentication


```

# 2. clone the github repo

```bash
git clone git@github.com:bicosteve/alx_backend_caching_property_listings.git
cd alx_backend_caching_property

git clone git@github.com:bicosteve/alx_backend_caching_property_listings.git
cd alx_backend_caching_property_listings
```

# 3. create .env

````bash
nano .env

POSTGRES_DB=propertylistings`

Contents:

``` bash

# dotenv --> content
POSTGRES_DB=propertylistings
POSTGRES_USER=admin
POSTGRES_USER=admin
POSTGRES_PASSWORD=securepass
DJANGO_SECRET_KEY=your
POSTGRES_PASSWORD=securepass
DJANGO_SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOST=False
ALLOWED_HOSTS=localhost,34.18S=localhost,34.18.92.22

```
````

# 4. Dockerfile configuration

```dockerfile
FROM pythonfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONDONTWRITEBYTE:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

CMDCODE 1
ENV PYTHONUNBUFFERED 1

CMD ["gunicorn", "alx_backend_caching_property_listings.wsgi:application", "--bind", "0.0.0.0:8000"]
`` ["gunicorn", "alx_backend_caching_property_listings.wsgi:application", "--bind", "0.0.0.0:8000"]
```

# 5. docker-compose.yml

version: '3.8'

services:
app:
build: .
container_name: propertylistings_app
ports: - "8000:docker-compose.yml`:

```yaml
version: '3.8'

services:
  app:
    build: .
    container_name: propertylistings_app
    ports:
      - "8000:8000"
    env_file: .env
    volumes:
      - .:/app8000"
    env_file: .env
    volumes:
      - .:/app
    depends_on:
      - postgres
      - redis

  postgres:
    image: postgres:latest
    environment:
      POSTGRES
    depends_on:
      - postgres
      - redis

  postgres:
    image: postgres:latest
    environment:
      POSTGRES_DB: propertylist_DB: propertylistings
      POSTGRESings
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: securepass
    ports:
      - "5432:5432"

  redis_USER: admin
      POSTGRES_PASSWORD: securepass
    ports:
      - "5432:5432"

  redis:
    image: redis:7-alpine
    ports:
    image: redis:7-alpine
    ports:
      - "6379::
      - "6379:6379"
```

# 6. running container

```bash

# set docker user and add to group
sudo usermod -a
sudo usermod -aG docker $USER
newG docker $USER
newgroup docker

# run the app
docker-compose build
docker-compose up -d

# check status
docker ps

# collect static files
docker-compose exec app python manage.py collectstatic

```

# 7. nginx rever proxy configuration

```bash

# install nginx
sudo apt install nginx -y

# nginx config
sudo nano /etc/nginx/sites-available/propertylistings

server {
    listen 80;
    server_name 34.18.92.22;

    location / {
        proxy_pass http://127.0.0.1:8000/;
        proxy_set_header_name 34.18.92.22;

    location / {
        proxy_pass http://127.0.0.1:8000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static/ {
        alias /home/ubuntu_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static/ {
        alias /home/ubuntu/alx_backend_caching_property_listings/alx_backend_caching_property_listings/staticfiles/;
    }

    client_max/staticfiles/;
    }

    client_max_body_size 10M;
}

# activate

sudo ln -s /etc/nginx/sites-available/propertylistings /etc/nginx/sites-enabled/
sudo nginx -t
listings /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx

http://sudo systemctl restart nginx
```

```bash
# test swagger interface on browser run:

http://34.18.92.22/swagger/

```

# 8. possible errors

| Issue                  | Fix                                                       |
| ---------------------- | --------------------------------------------------------- | ----------------------------------- | ------------------------------------------------------------------------------- |
| `.env` not found       | Use `ls -a` to reveal hidden files                        |
| 502 Bad Gateway        | Ensure Docker app is running & Nginx targets correct port |
| Docker permission      | Add user to docker group: `sudo usermod -aG docker $USER` |
| App exits unexpectedly | Run `docker logs <container>` to inspect crash details    |
|                        |
| 502 Bad Gateway        | Ensure Docker app is running & Nginx targets correct port |
| Docker permission      | Add user to docker group: `sudo usermod -aG docker $USER` |
| App exits unexpectedly | Run `docker logs <container>` to inspect crash details    |
| ALLOWED_HOSTS syntax   | ALLOWED_HOSTS syntax                                      | Use: `["localhost", "34.18.92.22"]` | Use: `["localhost", "34.18.92.22"]` not `localhost, not `localhost,34.18.92.22` |
