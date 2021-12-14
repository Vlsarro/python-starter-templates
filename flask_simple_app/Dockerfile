FROM python:3.7
RUN apt-get update && apt-get -y install openssl ca-certificates
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
RUN cp localhost.crt /usr/local/share/ca-certificates/ && update-ca-certificates
ENTRYPOINT [ "uwsgi", "--ini", "uwsgi.ini" ]
