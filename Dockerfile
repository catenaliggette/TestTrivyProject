FROM python:3.13-slim


WORKDIR /app


COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*


COPY . .


RUN useradd -m flaskuser


USER flaskuser


EXPOSE 5000


HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl --fail http://localhost:5000/ || exit 1


CMD ["python", "app.py"]