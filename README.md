```
python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

```
export FLASK_APP=app:app
flask run
```

```
pip install --require-virtualenv appmap
appmap-python flask run
```