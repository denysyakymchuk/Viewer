FROM python:3.9

WORKDIR /fastapi

COPY ./requirements.txt /fastapi/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /fastapi/requirements.txt

COPY ./main.py /fastapi/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]