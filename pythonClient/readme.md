# Subless Python Client

This client demonstrates the login and creator registration workflows for subless partner
websites. It expectes that you have a partner account set up with subless, and as such
have a client ID and client secret. If you don't have these or don't know what they are,
connect with Subless to ask.

Requirements:

- Your subless client ID and secret
- Python 3
- Pip

# Running the example

First, edit `testProfile.py`. Inside, change the two variable declarations:

```python
    clientId = 'Your client ID';
    clientSecret = 'Your client secret';
```

to reflect your clientID and secret, e.g.

```python
    # garbage example IDS
    clientId = 'abvrao8q542mkjm16ogt01kd33';
    clientSecret = 'lhfdjlfhul4hr4tu4t4bh4vgtcsueon2984nusxv4324bvfk2345';
```

Then, to run on your local machine directly, run the commands:

```shell
    pip install -r resources.txt
    export FLASK_APP=examplePythonClient
    flask run
```
Alternatively, to run using Docker:
```shell
    docker build -t subless_example .

    # Note: we use --net=host here so that the running address is "localhost", which
    # is important because "localhost:5000" is the approved redirect URL. If you run
    # without --net=host, you will succesfully run the client, but all redirects will
    # fail.
    docker run -p 5000:5000 subless_example
```

From here, navigating to http://localhost:5000/ should bring you to the demo.
