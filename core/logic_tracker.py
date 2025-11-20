from __future__ import annotations

from typing import Dict

from .models import DailyActivity
from .storage import load_profile_json, save_profile_json


_FILENAME = "tracker.json"


def _default() -> DailyActivity:
    return {}


def load_daily_activity() -> DailyActivity:
    data = load_profile_json(_FILENAME, _default())
    if not isinstance(data, dict):
        return _default()
    return data


def save_daily_activity(activity: DailyActivity) -> None:
    save_profile_json(_FILENAME, activity)
