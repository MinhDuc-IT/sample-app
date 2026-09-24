# Agent-QC sample app

Repo Python rất nhỏ dùng để trình diễn Agent-QC pass/fail trên Pull Request.

```powershell
python -m pip install -r requirements.txt
python -m pytest -q
```

Repo local đã có sẵn hai branch: `main` (pass) và `demo/failing-qc` (fail). Sau khi tạo GitHub repository rỗng:

```powershell
git remote add origin https://github.com/<owner>/<repo>.git
git push -u origin main
git push -u origin demo/failing-qc
```

Mở Pull Request vào `main`; GitHub App sẽ publish check `Agent-QC` với conclusion `failure`.
