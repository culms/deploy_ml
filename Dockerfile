FROM python:3.8.10-buster

WORKDIR /app

COPY . /app

RUN pip install -r requirement.txt

EXPOSE 8000
ENTRYPOINT ["sh","to_run.sh"]
