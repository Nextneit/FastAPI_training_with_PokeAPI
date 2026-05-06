# Variables para facilitar cambios
DOCKER_COMPOSE = docker compose
CONTAINER_NAME = fastapi_pokeapi

.PHONY: build up down restart logs test shell help

# Construir las imágenes
build:
	$(DOCKER_COMPOSE) build

# Levantar los contenedores en segundo plano
up:
	$(DOCKER_COMPOSE) up -d

# Detener y eliminar los contenedores
down:
	$(DOCKER_COMPOSE) down

# Reiniciar el proyecto (limpia y levanta)
restart:
	$(DOCKER_COMPOSE) down
	$(DOCKER_COMPOSE) up -d

# Ver logs en tiempo real
logs:
	$(DOCKER_COMPOSE) logs -f

# Ejecutar los tests unitarios dentro del contenedor
test:
	docker exec -it $(CONTAINER_NAME) python -m pytest

# Entrar a la terminal del contenedor (shell)
shell:
	docker exec -it $(CONTAINER_NAME) /bin/bash

# Limpiar imágenes huérfanas y volúmenes no usados (Cuidado: uso general)
clean:
	$(DOCKER_COMPOSE) down -v
	docker system prune -f

# Comando por defecto al escribir solo 'make'
help:
	@echo "Comandos disponibles:"
	@echo "  make build   - Construir imágenes de Docker"
	@echo "  make up      - Levantar contenedores"
	@echo "  make down    - Apagar contenedores"
	@echo "  make restart - Reiniciar el proyecto"
	@echo "  make logs    - Ver logs de la API"
	@echo "  make test    - Ejecutar tests unitarios"
	@echo "  make shell   - Abrir terminal en el contenedor"