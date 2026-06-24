FROM python:3.12-slim

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Instala as dependências do sistema necessárias
RUN apt-get update \
    && apt-get install -y build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia os arquivos de dependência primeiro (para aproveitar o cache do Docker)
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código do projeto
COPY . /app/

# Expõe a porta que o Django vai rodar
EXPOSE 8000

# Comando padrão para rodar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
