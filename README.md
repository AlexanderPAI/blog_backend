# blog_backend
Backend for Blog Application (including api)

Аутентификация сделана через BasicAuthentification, так как в ТЗ нет вводных по необходимому способу аутентификации.
При этом лучше было бы сделать через JWT.

```bash
docker-compose run --rm blog_backend sh -c "python ./src/manage.py generate_test_data"
```