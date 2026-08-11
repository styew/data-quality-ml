from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Data Quality API is running"}