Set-Location $PSScriptRoot
$env:PYTHONUTF8 = "1"

.\.venv\Scripts\python.exe -m streamlit run src/app.py `
    --server.address 127.0.0.1 `
    --server.port 8501 `
    --server.headless true
