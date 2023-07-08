FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN RUN pip install --no-cache-dir --upgrade --default-timeout=1000 -r /code/requirements.txt


COPY ./app/api  /code/api

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80"]




