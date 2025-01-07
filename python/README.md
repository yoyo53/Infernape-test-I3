# Running tests

```
# Install Python dependencies

$ python -m venv .venv 
# or
$ python3 -m venv .venv
$ source .venv/bin/activate
# or
$ .venv\Scripts\activate.bat
$ pip install -r requirements.txt

# Install browser
$ playwright install chromium

# Run the tests
$ pytest -vs --browser=chromium --slowmo=1000 --headed --base-url=https://<letter>.<group>.hr.dmerej.info/
```
