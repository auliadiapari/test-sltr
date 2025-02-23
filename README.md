# Preliminary Test STLR Group

This is a repository that contains Python-Flask Application, could use by start locally & docker

## To run locally

Run the following command to install virtual environments:

```sh
python3 -m venv .venv
```
Run the following command to install the depedencies & run app.py:

```sh
source .venv/bin/activate
pip install -r requirements.txt

To run the application
python src/app.py

access using 127.0.0.1:5000 locally on your browser
```


## Run & Build using Docker Compose:

```sh
doccker compose up -d
or
docker compose up -d --force-recreate --build 

acess ussing 127.0.0.1:8000 locally on your browser
```
