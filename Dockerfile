FROM python:3.12

RUN mkdir test-task-cats

WORKDIR /test-task-cats

COPY req.txt .

RUN pip install -r req.txt

COPY . .

