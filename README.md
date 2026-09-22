# extpr-lab

A lab project for working out how external pull requests are accepted. Development happens in the
internal GitLab; this GitHub repository is a mirror and the entry point for external pull requests.

Python 3.11+, standard library only.

## Tests

```sh
# unit: run both in GitHub Actions and in the internal CI
python -m unittest discover -s tests/unit -t . -v

# integration: internal CI only
python -m unittest discover -s tests/integration -t . -v
```

Как прислать изменения — см. [CONTRIBUTING.md](CONTRIBUTING.md).
```
Test PR from an external contributor
```

