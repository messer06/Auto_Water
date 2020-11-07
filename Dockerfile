FROM python:3.8

COPY requirements.txt /var/www/requirements.txt
COPY app /var/www/app
RUN pip install --upgrade pip
RUN pip install -r /var/www/requirements.txt

# Add demo app
COPY ./app /app
WORKDIR /app

ENTRYPOINT [ "python" ]

CMD [ "wsgi.py" ]
