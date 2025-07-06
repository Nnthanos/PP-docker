FROM ubuntu:latest

# Instala o Python 3 no container e atualizar os pacotes
RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get clean

WORKDIR /app

COPY process.py .

CMD ["python3", "process.py"]