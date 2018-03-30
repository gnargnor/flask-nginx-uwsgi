FROM tiangolo/uwsgi-nginx-flask:python3.6

ENV STATIC_INDEX 0
ENV FLASK_DEBUG=1

COPY ./app /app