FROM fastapi-bp:base

WORKDIR /code

COPY ./app ./app
COPY ./docker-entrypoint.sh .
COPY ./gunicorn.conf.py .

#COPY ./pytest.ini .
ARG MYAPP_API_VERSION
ENV MYAPP_API_VERSION=$MYAPP_API_VERSION
ENV PYTHONPATH=/code

EXPOSE 5000
ENTRYPOINT ["./docker-entrypoint.sh"]
CMD [ "gunicorn" ]
