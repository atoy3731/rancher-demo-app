FROM python:3

COPY requirements.txt /tmp/requirements.txt

RUN pip3 install -r /tmp/requirements.txt && \
    rm -f /tmp/requirements.txt

COPY app/app.py /app.py

CMD [ "python3", "/app.py" ]