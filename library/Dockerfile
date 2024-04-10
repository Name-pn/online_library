FROM python:3.11.9-alpine3.19

WORKDIR /usr/src/backend

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

RUN apk update \
    && pip install --upgrade pip \
    && apk add postgresql-dev gcc python3-dev musl-dev

COPY ./requirenments.txt /usr/src/backend/requirenments.txt
RUN pip install -r requirenments.txt

COPY . .

ENTRYPOINT ["sh", "entrypoint.sh"]
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8001"]
#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8001"]
#"0.0.0.0:8000"