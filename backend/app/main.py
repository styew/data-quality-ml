from fastapi import FastAPI, File, UploadFile
from pathlib import Path
from uuid import uuid4
import shutil, pandas as pd

app = FastAPI()

TEMP_PATH = Path("temp")


@app.get("/")
def root():
    return {"message": "Data Quality API is running"}


@app.post("/datasets/upload")
async def upload_dataset(file: UploadFile = File(...)):

    if not file.filename.endswith(".csv"):
        return {
            "error": "Only CSV files are supported"
        }

    dataset_id = str(uuid4())

    dataset_path = TEMP_PATH / dataset_id
    dataset_path.mkdir(parents=True, exist_ok=True)

    file_path = dataset_path / file.filename

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "dataset_id": dataset_id,
        "filename": file.filename,
        "status": "uploaded"
    }

@app.get("/datasets/{dataset_id}")
def get_dataset(dataset_id: str):

    dataset_path = TEMP_PATH / dataset_id

    if not dataset_path.exists():
        return {"error": "Dataset not found"}

    files = list(dataset_path.glob("*.csv"))

    if not files:
        return {"error": "CSV file not found"}

    file_path = files[0]

    df = pd.read_csv(file_path)

    return {
        "dataset_id": dataset_id,
        "filename": file_path.name,
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": df.columns.tolist(),
        "data_types": df.dtypes.astype(str).to_dict()
    }

@app.get("/datasets/{dataset_id}/issues/missing")
def get_missing_values(dataset_id: str):

    dataset_path = TEMP_PATH / dataset_id

    if not dataset_path.exists():
        return {"error": "Dataset not found"}

    files = list(dataset_path.glob("*.csv"))

    if not files:
        return {"error": "CSV file not found"}

    file_path = files[0]

    df = pd.read_csv(file_path)

    missing_values = df.isna().sum().to_dict()

    return {
        "dataset_id": dataset_id,
        "missing_values": missing_values,
        "total_missing": int(df.isna().sum().sum())
    }