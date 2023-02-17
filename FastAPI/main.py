from fastapi import FastAPI
import pandas as pd
import duckdb as dk
import os

app = FastAPI()


@app.get("/")
def presentacion():
    return "PROYECTO INDIVIDUAL 01 - Pacheco, Gian Pier"


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}