FROM python:3.12-slim 

ENV PYTHONWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 

# WORK DIR 
WORKDIR /app 

# System dependancies for postgres and psycopg

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

# RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD [ "gunicorn", "alx_backend_caching_property_listings.wsgi:application","--bind","0.0.0.0:8000" ]
