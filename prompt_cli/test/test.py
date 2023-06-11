from typing import List

from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/me")
async def hello_world():
    return {"Hello": "World"}


@app.post("/median")
async def calculate_median(values: List[int]):
    if len(values) == 0:
        raise HTTPException(status_code=400, detail="No values provided")
    values.sort()
    mid = len(values) // 2
    if len(values) % 2 == 0:
        median = (values[mid - 1] + values[mid]) / 2
    else:
        median = values[mid]
    return {"median": median}
