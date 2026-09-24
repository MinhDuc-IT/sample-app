# Agent-QC sample app

Repo Python rất nhỏ dùng để trình diễn Agent-QC pass/fail trên Pull Request.

```powershell
python -m pip install -r requirements.txt
python -m pytest -q
```

Nhánh `main` nên giữ implementation đúng. Để tạo PR lỗi, tạo branch và đổi `add` thành phép trừ:

```powershell
git switch -c demo/failing-qc
# sửa calculator.py: return left - right
git add calculator.py
git commit -m "demo: introduce failing test"
git push -u origin demo/failing-qc
```

Mở Pull Request vào `main`; GitHub App sẽ publish check `Agent-QC` với conclusion `failure`.

