from typing import Any, Dict
from .utils import timestamp

def populate_props() -> Dict[str, Any]:
  return {
    '$library': 'python',
    '$occurred_at': timestamp(),
  }
