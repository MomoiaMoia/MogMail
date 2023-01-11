# Set-ExecutionPolicy Unrestricted

Write-Output " * Creating Environment."
python -m venv pymail
Write-Output " * Create Environment Success."
.\pymail\Scripts\Activate.ps1
Write-Output " * Activate Environment Success."
pip3 install jinja2
Write-Output " * Load Dependency Success."
.\pymail\Scripts\python.exe .\SendMail.py 