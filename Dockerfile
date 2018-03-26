FROM          jfloff/alpine-python:recent

COPY          app.py /app.py
RUN           pip install twilio

ENTRYPOINT   ["python", "/app.py"]
