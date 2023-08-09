build-deploy:
	docker build --no-cache -t ng-game-service:latest .

build-local:
	docker build --no-cache -t ng-game-service -f ./Dockerfile.dev .

run-local: build-local
	docker run -ti -p 8080:8080 ng-game-service

run-local-with-frontend: build-local
	docker-compose up
