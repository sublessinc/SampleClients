FROM python:3.10.0b4

COPY resources.txt resources.txt
RUN pip install -r resources.txt
COPY . .
ENV FLASK_APP=pythonClient
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]
