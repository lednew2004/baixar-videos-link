# Usa imagem oficial do Python
FROM python:3.10

# Define diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto
COPY . .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta padrão do Flask
EXPOSE 8080

# Comando para iniciar o app
CMD ["python", "baixar.py"]
