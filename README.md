# GraphQL File Upload

Short description about the package.

- 📀 [Development server](http://127.0.0.1:8000/graphql/)

## 🚀 Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### 💼 Prerequisites

You need:

- `Python 3` installed on your local machine.
  - use `pyenv` to manage multiple versions (**recommended**): [link](https://github.com/pyenv/pyenv#simple-python-version-management-pyenv),
  - or you will find installation steps for your platform on the
    python [official website](https://www.python.org/downloads/),
- `pipenv` for virtual environment management: [link](https://formulae.brew.sh/formula/pipenv).

### 🖥 Installing

Clone the project:

```shell script
git clone https://github.com/rjNemo/graphql-file_upload.git
```

Create a virtual environment and install dependencies with:

```shell script
make local-setup
```

Then launch the development server using:

```shell script
make run
```

A GraphiQL API explorer is available on the development server address: http://127.0.0.1:8000/graphql/.

🎉 Enjoy!

### ⚡️ Scripts

See [Makefile](Makefile) for available scripts:

- dev server
- run tests

## 🧪 Running the tests

Tests are run using `pytest` and the test coverage is checked using `pytest-cov`.

```shell script
make test
```

### Unit tests

```shell script
pipenv run test
```

### Functional tests

```shell script
pipenv run python -m pytest tests/functional_api
```

### 💅 And coding style tests

Coding style is enforced using `black` for formatting, `flake8` for linting and `mypy` for static type checking. Additional
security check are performed using `bandit` and `safety`.

```shell script
make lint
```

❗️ It is encouraged to run linters and tests using `make lint` before committing to the repository.

## 👩‍🏫 GraphQL: GraphCool-Grammar

We use a GraphQL grammar to structure the endpoints systematically.

![GraphCool Grammar](./docs/graphcool_grammer.png)

## 🛠 Built with

- [FastAPI](https://fastapi.tiangolo.com/) - FastAPI framework, high performance, easy to learn, fast to code, ready for production
- [Ariadne](https://ariadnegraphql.org/) - Python GraphQL schema-first

## 💻 Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting
merge requests.
