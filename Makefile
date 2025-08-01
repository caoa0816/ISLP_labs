IMAGE_NAME = islp_lab:v0
USER_ID = 1002
PORT = 8888
VOLUME = $(shell pwd)
CONTAINER_NAME = islp 

run:
	docker run -d -p $(PORT):8888 -v $(VOLUME):/home/jovyan --user $(USER_ID):$(USER_ID) --name $(CONTAINER_NAME) $(IMAGE_NAME)

stop:
	docker stop $(CONTAINER_NAME)

restart:
	docker restart $(CONTAINER_NAME)
