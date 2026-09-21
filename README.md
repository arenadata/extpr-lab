# extpr-lab

Лабораторный проект для отработки приёма внешних PR. Разработка ведётся во внутреннем
GitLab; этот репозиторий в GitHub — зеркало и точка входа для внешних PR.

Python 3.11+, только стандартная библиотека.

## Тесты

```sh
# unit — запускаются и в GitHub Actions, и во внутреннем CI
python -m unittest discover -s tests/unit -t . -v

# integration — только во внутреннем CI
python -m unittest discover -s tests/integration -t . -v
```

Как прислать изменения — см. [CONTRIBUTING.md](CONTRIBUTING.md).
Test PR from an external contributor
