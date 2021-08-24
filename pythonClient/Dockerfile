FROM python

COPY resources.txt resources.txt
RUN pip install -r resources.txt
COPY . .
ENV FLASK_APP=examplePythonClient
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]
