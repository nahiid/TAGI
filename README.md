# TAGI
TAGI package implementation in Python
## Installing dependencies
You can use this command on debian distributions. (For windows refer to related documentation for installing `make` command)
```
make install
```
Or you can install `poetry` and run the follwing commands.

```
poetry lock -n && poetry export --without-hashes > requirements.txt
poetry install -n
```
## Test
For running tests run the following command.
```
make test
```
## Code Style
For running linter and checking code styles, run the following command.
```
make check-codestyle
```
