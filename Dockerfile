FROM python:3.9

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

ENV FLASK_APP webapp
ENV FLASK_ENV production

EXPOSE 5000

CMD ["flask", "run"]
