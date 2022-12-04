FROM python:3.10.4

ADD . /app

WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["python", "/app/http_server/main.py"]