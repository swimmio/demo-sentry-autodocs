---
title: Makefile Usage in Project Management
---
This document provides a detailed explanation of how the Makefile is utilized within the Sentry project to manage various development and deployment tasks.

<SwmSnippet path="/Makefile" line="1">

---

# General Makefile Usage

The Makefile defines a default target `all`, which depends on the `develop` target. This setup indicates that running `make` without arguments will trigger the `develop` target. Various environment variables like `PIP`, `WEBPACK`, and `POSTGRES_CONTAINER` are set for use in other commands.

```
.PHONY: all
all: develop

PIP := python -m pip --disable-pip-version-check
WEBPACK := yarn build-acceptance
POSTGRES_CONTAINER := sentry_postgres
```

---

</SwmSnippet>

<SwmSnippet path="/Makefile" line="8">

---

# Dependency Management

The `freeze-requirements` target is used for freezing Python dependencies. It executes a Python script using a specific Python interpreter to generate a frozen requirements file, which helps in maintaining consistent environments across different setups.

```
freeze-requirements:
	@python3 -S -m tools.freeze_requirements
```

---

</SwmSnippet>

<SwmSnippet path="/Makefile" line="11">

---

# Development Setup

Targets like `bootstrap`, `develop`, and `clean` are grouped together and use a script `do.sh` for execution. This approach allows for batch processing of common development setup tasks, making it easier to manage and execute them collectively.

```
bootstrap \
develop \
clean \
init-config \
run-dependent-services \
drop-db \
create-db \
apply-migrations \
reset-db \
setup-git \
node-version-check \
install-js-dev \
install-py-dev :
```

---

</SwmSnippet>

<SwmSnippet path="/Makefile" line="32">

---

# Building Assets

The `build-js-po` target handles the preparation of JavaScript translation files. It involves cleaning up cache directories and setting environment variables to influence the build process, specifically using Webpack configured through the `WEBPACK` variable.

```
build-js-po: node-version-check
	mkdir -p build
	rm -rf node_modules/.cache/babel-loader
	SENTRY_EXTRACT_TRANSLATIONS=1 $(WEBPACK)
```

---

</SwmSnippet>

<SwmSnippet path="/Makefile" line="37">

---

# Documentation and API Specs

Targets `build-spectacular-docs` and `build-deprecated-docs` are used for generating API documentation. The process includes building JSON files from Django and then dereferencing them to make the API schema more manageable.

```
build-spectacular-docs:
	@echo "--> Building drf-spectacular openapi spec (combines with deprecated docs)"
	@OPENAPIGENERATE=1 sentry django spectacular --file tests/apidocs/openapi-spectacular.json --format openapi-json --validate --fail-on-warn

build-deprecated-docs:
	@echo "--> Building deprecated openapi spec from json files"
	yarn build-deprecated-docs

build-api-docs: build-deprecated-docs build-spectacular-docs
	@echo "--> Dereference the json schema for ease of use"
	yarn deref-api-docs
```

---

</SwmSnippet>

<SwmSnippet path="/Makefile" line="92">

---

# Testing and Validation

The `run-acceptance` and `test-cli` targets are examples of how the Makefile is used to manage different types of tests, including acceptance tests and command-line interface tests, to ensure the application functions as expected.

```
run-acceptance:
	@echo "--> Running acceptance tests"
	pytest tests/acceptance --cov . --cov-report="xml:.artifacts/acceptance.coverage.xml" --json-report --json-report-file=".artifacts/pytest.acceptance.json" --json-report-omit=log
	@echo ""

test-cli: create-db
	@echo "--> Testing CLI"
	rm -rf test_cli
	mkdir test_cli
	cd test_cli && sentry init test_conf
	cd test_cli && sentry --config=test_conf help
	cd test_cli && sentry --config=test_conf upgrade --traceback --noinput
	cd test_cli && sentry --config=test_conf export
	rm -r test_cli
	@echo ""
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>
