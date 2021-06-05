FROM python:3.10-rc-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt 

COPY . .

CMD [ "pytest", "-v", "merge_sort.py" ]