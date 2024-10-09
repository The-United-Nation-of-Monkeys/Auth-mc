FROM python:3.12

RUN mkdir LKS-Auth-mc

WORKDIR /LKS-Auth-mc

COPY req.txt .

RUN pip install -r req.txt

COPY . .

RUN chmod a+x docker/*.sh
