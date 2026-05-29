import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

from app.main import app
from app.db.database import connect_db
import asyncio

# Vercel doesn't fire startup events — connect DB manually
try:
    asyncio.get_event_loop().run_until_complete(connect_db())
except Exception as e:
    print(f"DB init warning: {e}")

handler = app
