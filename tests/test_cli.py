import os
import re
import subprocess
import tempfile
import pytest

SCRIPT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ytp"))

def strip_ansi(text: str) -> str:
    return re.sub(r'\x1b\[[0-9;]*m', '', text)

def test_version():
    res = subprocess.run([SCRIPT_PATH, "--version"], capture_output=True, text=True)
    assert res.returncode == 0
    clean = strip_ansi(res.stdout)
    assert "ytp version" in clean

def test_help():
    res = subprocess.run([SCRIPT_PATH, "--help"], capture_output=True, text=True)
    assert res.returncode == 0
    clean = strip_ansi(res.stdout)
    assert "USAGE:" in clean
    assert "ytp <url_or_alias>" in clean

def test_save_and_list_and_remove():
    with tempfile.TemporaryDirectory() as tmpdir:
        env = os.environ.copy()
        env["XDG_CONFIG_HOME"] = tmpdir
        
        # Initially empty list
        res = subprocess.run([SCRIPT_PATH, "--list-saved"], env=env, capture_output=True, text=True)
        assert res.returncode == 0
        clean = strip_ansi(res.stdout)
        assert "No playlists saved yet" in clean

        # Save an alias
        res = subprocess.run([SCRIPT_PATH, "--save", "https://youtube.com/playlist?list=123", "testalias"], env=env, capture_output=True, text=True)
        assert res.returncode == 0
        clean = strip_ansi(res.stdout)
        assert "Saved playlist alias: testalias" in clean

        # List should show testalias
        res = subprocess.run([SCRIPT_PATH, "--list-saved"], env=env, capture_output=True, text=True)
        assert res.returncode == 0
        clean = strip_ansi(res.stdout)
        assert "testalias" in clean

        # Remove alias
        res = subprocess.run([SCRIPT_PATH, "--remove", "testalias"], env=env, capture_output=True, text=True)
        assert res.returncode == 0
        clean = strip_ansi(res.stdout)
        assert "Removed playlist alias: testalias" in clean
