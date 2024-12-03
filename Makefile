build:
	sudo docker compose up -d --build 

run:
	sudo docker compose up

stop:
	sudo docker compose stop

up:
	uvicorn src.main:app --reload