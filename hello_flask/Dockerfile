# FROM python:3.8-slim
# WORKDIR /app
# COPY . .
# RUN apt-get update && apt-get install -y \
#     gcc \
#     python3-dev \
#     libmariadb-dev \
#     pkg-config
# RUN pip install flask mysqlclient
# EXPOSE 5002
# CMD ["python", "app.py"]

# Stage 1 : Build Stage 
FROM python:3.8-slim AS Build

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libmariadb-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*


COPY . .

# RUN pip install flask mysqlclient
RUN pip install --no-cache-dir --prefix=/install flask mysqlclient

# Stage 2 : Production Stage
FROM python:3.8-slim
WORKDIR /app

COPY --from=build /install /usr/local

COPY --from=Build /app /app
EXPOSE 5002

CMD ["python", "app.py"]
