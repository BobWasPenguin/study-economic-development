# Economic Development App - Study Center with Visuals

A Flask-based learning platform for Economic Development students, structured around Todaro's framework. This scaffold includes user authentication, course/chapter management, resource library, and placeholders for quizzes & simulation modules.

## Quick Start (Dev)

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=app.py
flask db init && flask db migrate -m "Initial" && flask db upgrade
python app.py  # runs on http://127.0.0.1:5000
```

## Current Task
1. Add content to templates/ (Jinja2 HTML files) 
2. Implement quiz grading logic & simulation engine (NumPy/Pandas)
3. Write integration tests (pytest + Flask-Testing)
4. Deploy on Heroku/Fly.io or containerize via Docker

## Contributing
Feel free to create issues or pull requests on GitHub with feedback or feature suggestions.
