# Agent-QC client-server sample

Ứng dụng demo gồm:

- Web client HTML/CSS/JavaScript tại `/`.
- FastAPI server cung cấp `/api/add`, `/api/divide` và `/health`.
- Unit/API tests bằng pytest.
- Functional browser scenario cho Hercules.
- Keploy fixtures cho integration replay.
- k6 script cho performance smoke test.

## Chạy local

```powershell
python -m pip install -r requirements.txt
python -m uvicorn app:app --host 127.0.0.1 --port 8080
```

Mở `http://127.0.0.1:8080` và dùng calculator trên trình duyệt.

## Chạy test

```powershell
python -m pytest -q
```

Các branch `demo/*` cố tình đưa từng loại regression riêng biệt vào ứng dụng để
kiểm tra khả năng phát hiện của từng Agent-QC worker.
