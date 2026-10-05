from fastapi import FastAPI

from calculator import add


app = FastAPI(title="Agent-QC Sample App")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/add")
def api_add(a: int, b: int) -> dict[str, int]:
    return {"result": add(a, b)}
