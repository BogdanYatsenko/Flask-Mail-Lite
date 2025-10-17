## Install (local)
```bash
python -m venv .venv && source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -U pip
pip install -r requirements.txt
pip install -e .
```

## Run example
```bash
python examples/app.py
# open http://127.0.0.1:5000/ping
```

## Usage
```python
from flask_mail import Mail, Message
mail = Mail(app)
mail.send(Message("Subject", recipients=["you@example.com"], body="Hi"))
```

## 📝 License
Released under the **MIT License** © 2025 Bogdan Yatsenko.
