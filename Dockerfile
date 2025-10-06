# syntax=docker/dockerfile:1

# 1) Imagem base (Python 3.12 leve)
FROM python:3.12-slim

# 2) Configs para logs imediatos e evitar .pyc
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 3) Pasta de trabalho dentro do container
WORKDIR /app

# 4) Instalar dependências primeiro (cache eficiente)
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 5) Copiar o restante do projeto
COPY . /app

# 6) Garantir que a pasta do SQLite exista
RUN mkdir -p /app/instance

# 7) Expor a porta que o Flask usa
EXPOSE 5000

# 8) Comando padrão: iniciar a API
CMD ["python", "run.py"]
