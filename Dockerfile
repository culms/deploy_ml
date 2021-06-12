FROM python:3.8.10-buster

WORKDIR /app

COPY . /app

RUN pip install -r requirement.txt

ENTRYPOINT ["python"]

CMD ["app.py"]