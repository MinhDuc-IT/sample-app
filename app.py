from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from calculator import add, divide


BASE_DIR = Path(__file__).parent

app = FastAPI(title="Agent-QC Client-Server Demo")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

ORDERS = {
    1001: {"owner": "alice", "item": "keyboard"},
    1002: {"owner": "bob", "item": "monitor"},
}


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


@app.get("/api/orders/{order_id}")
def get_order(order_id: int, current_user: str) -> dict[str, str]:
    # Intentionally vulnerable demo: current_user is not checked against owner.
    return ORDERS[order_id]
