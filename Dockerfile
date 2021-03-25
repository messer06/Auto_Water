FROM python:3.8

COPY requirements.txt /var/www/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r /var/www/requirements.txt

WORKDIR /var/www

ENTRYPOINT [ "python" ]

