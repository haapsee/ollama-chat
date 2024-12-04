FROM nvidia/cuda:12.3.2-cudnn9-runtime-ubuntu22.04

WORKDIR /app
COPY . /app
RUN chmod +x entrypoint.sh

RUN apt-get update && \
    apt-get install -y curl git nvidia-cuda-toolkit python3-pip python3-dev python-is-python3 && \
    pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install

RUN curl -fsSL https://ollama.com/install.sh | sh

EXPOSE 5000

CMD ["./entrypoint.sh"]
