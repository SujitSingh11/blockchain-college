FROM python:3.8-slim

WORKDIR /usr/src/app

RUN pip install Flask

COPY . .

CMD [ "python", "./lab4.py" ]