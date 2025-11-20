from __future__ import annotations

from pathlib import Path
from typing import Any, Optional

from aqt import mw


def get_addon_dir() -> Path:
    return Path(mw.addonManager.addonsFolder()) / "languageforge"


def get_data_dir() -> Path:
    data_dir = get_addon_dir() / "user_data"
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir


def load_json(filename: str, default: Any) -> Any:
    path = get_data_dir() / filename
    if not path.exists():
        return default
    try:
        import json

        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default


def save_json(filename: str, data: Any) -> None:
    path = get_data_dir() / filename
    try:
        import json

        with path.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception:
        pass


# Profile-aware storage functions
def load_profile_json(filename: str, default: Any, profile_id: Optional[str] = None) -> Any:
    """Load JSON from a specific profile's directory.
    
    If profile_id is None, uses the currently active profile.
    """
    from .logic_profiles import get_active_profile_id, get_profile_data_dir
    
    if profile_id is None:
        profile_id = get_active_profile_id()
    
    profile_dir = get_profile_data_dir(profile_id)
    path = profile_dir / filename
    
    if not path.exists():
        return default
    try:
        import json

        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default


def save_profile_json(filename: str, data: Any, profile_id: Optional[str] = None) -> None:
    """Save JSON to a specific profile's directory.
    
    If profile_id is None, uses the currently active profile.
    """
    from .logic_profiles import get_active_profile_id, get_profile_data_dir
    
    if profile_id is None:
        profile_id = get_active_profile_id()
    
    profile_dir = get_profile_data_dir(profile_id)
    path = profile_dir / filename
    
    try:
        import json

        with path.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception:
        pass
