FROM python:3.11-slim


WORKDIR /app 

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY books.json main.py ./

CMD ["python", "main.py"]