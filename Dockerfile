FROM python:3
ADD . /code
WORKDIR /code
CMD ["python", "bjack.py"]