from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime
import json

from .storage import get_data_dir


# Profile constraints
MAX_PROFILES = 50
MAX_PROFILE_NAME_LENGTH = 30
MIN_PROFILE_NAME_LENGTH = 1
INVALID_CHARS = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
RESERVED_NAMES = ['settings', 'profiles', 'temp', 'backup', 'default']

_PROFILES_FILENAME = "profiles.json"
_current_profile_id: Optional[str] = None


def get_profiles_dir() -> Path:
    """Get the profiles directory, creating it if needed."""
    profiles_dir = get_data_dir() / "profiles"
    profiles_dir.mkdir(parents=True, exist_ok=True)
    return profiles_dir


def get_profile_data_dir(profile_id: str) -> Path:
    """Get the data directory for a specific profile."""
    profile_dir = get_profiles_dir() / profile_id
    profile_dir.mkdir(parents=True, exist_ok=True)
    return profile_dir


def sanitize_profile_name(name: str) -> str:
    """Clean profile name for safe filesystem usage.
    
    Returns the sanitized folder name (lowercase, no special chars).
    """
    if not name:
        return ""
    
    # Trim whitespace
    name = name.strip()
    
    # Remove invalid filesystem characters
    for char in INVALID_CHARS:
        name = name.replace(char, '')
    
    # Prevent directory traversal
    name = name.replace('..', '')
    
    # Limit length
    name = name[:MAX_PROFILE_NAME_LENGTH]
    
    # Convert to safe folder name (lowercase, replace spaces with underscores)
    folder_name = name.lower().replace(' ', '_')
    
    # Remove multiple consecutive underscores
    while '__' in folder_name:
        folder_name = folder_name.replace('__', '_')
    
    # Remove leading/trailing underscores
    folder_name = folder_name.strip('_')
    
    return folder_name


def _default_profiles_data() -> Dict[str, Any]:
    """Default profiles registry structure."""
    return {
        "active_profile": "default",
        "profiles": [
            {
                "id": "default",
                "display_name": "Default",
                "created_at": datetime.now().isoformat(timespec="seconds"),
                "last_used": datetime.now().isoformat(timespec="seconds"),
            }
        ],
        "version": "1.0"
    }


def _load_profiles_registry() -> Dict[str, Any]:
    """Load the profiles registry from disk."""
    path = get_data_dir() / _PROFILES_FILENAME
    if not path.exists():
        return _default_profiles_data()
    
    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, dict):
                return _default_profiles_data()
            # Ensure required keys exist
            if "profiles" not in data or "active_profile" not in data:
                return _default_profiles_data()
            return data
    except Exception:
        return _default_profiles_data()


def _save_profiles_registry(data: Dict[str, Any]) -> None:
    """Save the profiles registry to disk."""
    path = get_data_dir() / _PROFILES_FILENAME
    try:
        with path.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception:
        pass


def list_profiles() -> List[Dict[str, Any]]:
    """Get list of all profiles."""
    registry = _load_profiles_registry()
    return registry.get("profiles", [])


def get_active_profile_id() -> str:
    """Get the currently active profile ID."""
    global _current_profile_id
    if _current_profile_id is not None:
        return _current_profile_id
    
    registry = _load_profiles_registry()
    active_id = registry.get("active_profile", "default")
    
    # Validate that the active profile exists
    profiles = registry.get("profiles", [])
    profile_ids = {p["id"] for p in profiles}
    
    if active_id not in profile_ids:
        # Fallback to first profile or default
        if profiles:
            active_id = profiles[0]["id"]
        else:
            active_id = "default"
            # Ensure default exists
            _ensure_default_profile()
    
    _current_profile_id = active_id
    return active_id


def set_active_profile(profile_id: str) -> bool:
    """Set the active profile and update last_used timestamp.
    
    Returns True if successful, False if profile doesn't exist.
    """
    global _current_profile_id
    
    registry = _load_profiles_registry()
    profiles = registry.get("profiles", [])
    
    # Check if profile exists
    profile_exists = any(p["id"] == profile_id for p in profiles)
    if not profile_exists:
        return False
    
    # Update active profile
    registry["active_profile"] = profile_id
    _current_profile_id = profile_id
    
    # Update last_used timestamp
    now = datetime.now().isoformat(timespec="seconds")
    for profile in profiles:
        if profile["id"] == profile_id:
            profile["last_used"] = now
            break
    
    _save_profiles_registry(registry)
    return True


def profile_exists(profile_id: str) -> bool:
    """Check if a profile exists."""
    profiles = list_profiles()
    return any(p["id"] == profile_id for p in profiles)


def get_profile_display_name(profile_id: str) -> Optional[str]:
    """Get the display name for a profile ID."""
    profiles = list_profiles()
    for profile in profiles:
        if profile["id"] == profile_id:
            return profile["display_name"]
    return None


def create_profile(display_name: str) -> tuple[bool, str]:
    """Create a new profile.
    
    Returns (success: bool, message: str).
    """
    # Validate name length
    if len(display_name) < MIN_PROFILE_NAME_LENGTH:
        return False, "Profile name is too short."
    
    if len(display_name) > MAX_PROFILE_NAME_LENGTH:
        return False, f"Profile name must be {MAX_PROFILE_NAME_LENGTH} characters or less."
    
    # Check profile count limit
    profiles = list_profiles()
    if len(profiles) >= MAX_PROFILES:
        return False, f"Maximum profiles ({MAX_PROFILES}) reached. Delete unused profiles first."
    
    # Sanitize name
    profile_id = sanitize_profile_name(display_name)
    
    if not profile_id:
        return False, "Profile name contains only invalid characters."
    
    # Check reserved names
    if profile_id.lower() in RESERVED_NAMES:
        return False, f"'{display_name}' is a reserved name."
    
    # Check if exists
    if profile_exists(profile_id):
        return False, f"Profile '{display_name}' already exists."
    
    # Create profile directory
    try:
        profile_dir = get_profile_data_dir(profile_id)
    except Exception as e:
        return False, f"Failed to create profile directory: {e}"
    
    # Add to registry
    registry = _load_profiles_registry()
    now = datetime.now().isoformat(timespec="seconds")
    
    new_profile = {
        "id": profile_id,
        "display_name": display_name,
        "created_at": now,
        "last_used": now,
    }
    
    registry["profiles"].append(new_profile)
    _save_profiles_registry(registry)
    
    return True, f"Profile '{display_name}' created successfully."


def delete_profile(profile_id: str) -> tuple[bool, str]:
    """Delete a profile.
    
    Returns (success: bool, message: str).
    """
    # Cannot delete default profile
    if profile_id == "default":
        return False, "Cannot delete the default profile."
    
    # Cannot delete active profile
    if profile_id == get_active_profile_id():
        return False, "Cannot delete the currently active profile. Switch to another profile first."
    
    # Check if exists
    if not profile_exists(profile_id):
        return False, f"Profile '{profile_id}' does not exist."
    
    # Remove from registry
    registry = _load_profiles_registry()
    registry["profiles"] = [p for p in registry["profiles"] if p["id"] != profile_id]
    _save_profiles_registry(registry)
    
    # Delete directory (with safety check)
    try:
        profile_dir = get_profiles_dir() / profile_id
        if profile_dir.exists() and profile_dir.is_dir():
            # Extra safety: only delete if it's inside profiles directory
            if profile_dir.parent == get_profiles_dir():
                import shutil
                shutil.rmtree(profile_dir)
    except Exception as e:
        # Non-fatal: registry is updated, just couldn't delete folder
        pass
    
    return True, f"Profile deleted successfully."


def rename_profile(profile_id: str, new_display_name: str) -> tuple[bool, str]:
    """Rename a profile (display name only, ID stays the same).
    
    Returns (success: bool, message: str).
    """
    # Validate new name length
    if len(new_display_name) < MIN_PROFILE_NAME_LENGTH:
        return False, "Profile name is too short."
    
    if len(new_display_name) > MAX_PROFILE_NAME_LENGTH:
        return False, f"Profile name must be {MAX_PROFILE_NAME_LENGTH} characters or less."
    
    # Check if profile exists
    if not profile_exists(profile_id):
        return False, f"Profile '{profile_id}' does not exist."
    
    # Update display name in registry
    registry = _load_profiles_registry()
    for profile in registry["profiles"]:
        if profile["id"] == profile_id:
            profile["display_name"] = new_display_name
            break
    
    _save_profiles_registry(registry)
    return True, f"Profile renamed to '{new_display_name}'."


def cleanup_orphaned_folders() -> int:
    """Remove profile folders not in registry.
    
    Returns the number of orphaned folders removed.
    """
    registry = _load_profiles_registry()
    registered_ids = {p["id"] for p in registry.get("profiles", [])}
    profiles_dir = get_profiles_dir()
    
    removed_count = 0
    
    try:
        for folder in profiles_dir.iterdir():
            if folder.is_dir() and folder.name not in registered_ids:
                # Orphaned folder - delete it
                try:
                    import shutil
                    shutil.rmtree(folder)
                    removed_count += 1
                except Exception:
                    pass
    except Exception:
        pass
    
    return removed_count


def _ensure_default_profile() -> None:
    """Ensure the default profile exists."""
    if not profile_exists("default"):
        registry = _load_profiles_registry()
        now = datetime.now().isoformat(timespec="seconds")
        
        default_profile = {
            "id": "default",
            "display_name": "Default",
            "created_at": now,
            "last_used": now,
        }
        
        if "profiles" not in registry:
            registry["profiles"] = []
        
        registry["profiles"].append(default_profile)
        registry["active_profile"] = "default"
        _save_profiles_registry(registry)
        
        # Ensure directory exists
        get_profile_data_dir("default")


def initialize_profiles_system() -> None:
    """Initialize the profiles system on startup.
    
    - Ensures default profile exists
    - Validates active profile
    - Cleans up orphaned folders
    """
    _ensure_default_profile()
    
    # Validate active profile
    active_id = get_active_profile_id()
    if not profile_exists(active_id):
        set_active_profile("default")
    
    # Cleanup orphaned folders
    cleanup_orphaned_folders()
