FROM python

COPY resources.txt resources.txt
RUN pip install -r resources.txt
COPY . .
ENV FLASK_APP=examplePythonClient
ENTRYPOINT [ "flask", "run", "--host=localhost"]