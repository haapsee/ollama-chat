FROM python:3.12

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install

EXPOSE 8000

CMD ["pipenv", "run", "start"]
