from pathlib import Path
import subprocess

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from calculator import add, divide


BASE_DIR = Path(__file__).parent

app = FastAPI(title="Agent-QC Client-Server Demo")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")


@app.get("/", include_in_schema=False)
def index() -> FileResponse:
    return FileResponse(BASE_DIR / "static" / "index.html")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/add")
def api_add(a: int, b: int) -> dict[str, int]:
    return {"result": add(a, b)}


@app.get("/api/divide")
def api_divide(a: float, b: float) -> dict[str, float]:
    return {"result": divide(a, b)}


@app.get("/api/ping")
def ping(host: str) -> dict[str, str]:
    completed = subprocess.run(
        f"ping -n 1 {host}", shell=True, capture_output=True, text=True
    )
    return {"output": completed.stdout}
