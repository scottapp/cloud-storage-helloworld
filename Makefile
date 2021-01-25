.PHONY: build run

build:
	docker build -t cloud_storage_helloworld .

run:
	docker run -p 8080:8080 --rm -e GOOGLE_APPLICATION_CREDENTIALS='/tmp/keys/credential.json' \
	-e PROJECT_ID='$(PROJECT_ID)' \
	-v $(GOOGLE_APPLICATION_CREDENTIALS):/tmp/keys/credential.json:ro cloud_storage_helloworld

test:
	docker run --rm --entrypoint pytest -e GOOGLE_APPLICATION_CREDENTIALS='/tmp/keys/credential.json' \
	-e PROJECT_ID='$(PROJECT_ID)' \
	-v $(GOOGLE_APPLICATION_CREDENTIALS):/tmp/keys/credential.json:ro cloud_storage_helloworld
