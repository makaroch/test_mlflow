FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install fastapi uvicorn httpx

CMD python3 main.py
