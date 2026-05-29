import sys
import os

# Add backend directory to path so `app` package is importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

from app.main import app

# Vercel needs a handler named `app`
handler = app
