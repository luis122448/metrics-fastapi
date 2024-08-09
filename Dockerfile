FROM python:3.11.4
LABEL luis122448 <luis122448@gmail.com>

WORKDIR /opt

COPY ./requirements.txt /opt/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /opt/requirements.txt

COPY ./app /opt/app/
COPY ./database /opt/database/

EXPOSE 8005

CMD [ "python", "app/server.py" ]