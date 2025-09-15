FROM python:3.12.0
LABEL version 1.0
LABEL author = "Hamza"

WORKDIR /app 

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY books.json main.py ./

CMD python main.py