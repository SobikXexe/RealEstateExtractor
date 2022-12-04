FROM python:3.10.4

ADD . /app

WORKDIR /app
RUN pip install -r requirements.txt
RUN playwright install
RUN playwright install-deps

ENTRYPOINT ["python", "/app/web_scraper/main.py"]