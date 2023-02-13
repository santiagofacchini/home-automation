FROM python:3.12.0a5-alpine3.17

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./services/wsgi.py" ]