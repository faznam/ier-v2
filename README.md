# ier-v2

## setup
- create new env (whatever its name) : 

```console 
conda create -n zoro python=3.10
```
- activate the env : 

```console 
conda activate zoro
```
- run : 

```console 
pip install -r requirements.txt
```
- to run the app : 

```console 
uvicorn zoro.main:app --reload
```

## format code
- run: black .
