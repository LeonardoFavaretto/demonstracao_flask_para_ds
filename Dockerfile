FROM python:3.6-slim-buster
RUN apt-get update
WORKDIR /ds_api_on_docker
COPY . .
RUN pip install -r requirements.txt

EXPOSE 5050

CMD ["gunicorn", "-w", "1", "--bind", "0.0.0.0:5050", "main:app"]

