FROM python:3.8-slim-buster

RUN pip install uv

WORKDIR /codeapp

COPY requirements.txt requirements.txt

RUN uv pip install -r requirements.txt

COPY . .
# First . shows the folder in which this file is (source) and 2nd . means the working dir (destination)

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000

