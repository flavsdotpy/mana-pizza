PROJECT_NAME=mana-pizza

build-web:
	docker build \
		-t $(PROJECT_NAME)-webapp \
		-f ./app/Dockerfile \
		--progress=plain \
		.

run-web:
	docker run \
		-p 5000:5000 \
		-v /tmp:/tmp:ro \
		--env-file ./.env \
		--name $(PROJECT_NAME)-webapp \
		$(PROJECT_NAME)-webapp
