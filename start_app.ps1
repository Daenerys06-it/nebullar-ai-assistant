Set-Location $PSScriptRoot
$env:PYTHONUTF8 = "1"

.\.venv\Scripts\python.exe -m streamlit run src/app.py `
    --server.address localhost `
    --server.port 8501
