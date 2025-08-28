FROM python:3.10

WORKDIR /app

# Instala dependências
RUN apt-get update && apt-get install -y ffmpeg

# Copia o projeto
COPY . .

# Instala pacotes do Python
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "baixar.py"]
