FROM python:3.8-alpine

WORKDIR /src

COPY ./requirements.txt /src/requirements.txt

RUN pip install --no-cache-dir --default-timeout=1000 --upgrade -r /src/requirements.txt

COPY ./app /src/app

# RUN Server with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "9000"]
