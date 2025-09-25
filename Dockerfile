FROM python:3.13.1

WORKDIR /app

COPY modelo_iris.pkl .
COPY api.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "api.py"]