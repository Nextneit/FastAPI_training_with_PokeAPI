# Variables
DOCKER_COMPOSE	= docker compose
CONTAINER_NAME	= fastapi_pokeapi

.PHONY: all clean fclean re help

# Construir y levantar los contenedores
all:
	$(DOCKER_COMPOSE) build
	$(DOCKER_COMPOSE) up -d

# Detener y eliminar los contenedores
clean:
	$(DOCKER_COMPOSE) down

# Limpiar imágenes huérfanas y volúmenes no usados
fclean:
	$(DOCKER_COMPOSE) down -v
	docker system prune -f

# Reiniciar el proyecto desde cero
re: fclean all

# Mostrar ayuda
help:
	@echo "Comandos disponibles:"
	@echo "  make all    - Construir imágenes y levantar contenedores"
	@echo "  make clean  - Apagar y eliminar contenedores"
	@echo "  make fclean - Limpiar contenedores, volúmenes e imágenes huérfanas"
	@echo "  make re     - Reiniciar el proyecto desde cero"
	@echo "  make help   - Mostrar esta ayuda"