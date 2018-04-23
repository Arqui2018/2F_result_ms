**Microservicio Apuesta por Resultado**
*Docker components*
- result_ms:  ```ports="4005"```
- result_db: ``ports="3013"``
---
Comandos para:
1. Migraciones:
`docker-compose run --rm result_ms python manage.py migrate`
2. Consola Shell:
`docker-compose run --rm result_ms python manage.py shell`

---

Filtro de Rutas:
1. user_id:
`[url]:4005/results/users/[user_id]`

2. match_id:
`[url]:4005/results/matches/[match_id]`

---
# [Django REST framework][docs]

[![build-status-image]][travis]
[![coverage-status-image]][codecov]
[![pypi-version]][pypi]
[![Gitter](https://badges.gitter.im/tomchristie/django-rest-framework.svg)](https://gitter.im/tomchristie/django-rest-framework?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

**Awesome web-browsable Web APIs.**

Full documentation for the project is available at [http://www.django-rest-framework.org][docs].

---
