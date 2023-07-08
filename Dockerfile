FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade --default-timeout=1000 -r /code/requirements.txt


COPY ./main.py  /code/main.py

COPY ./saved_model /code/saved_model

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]




