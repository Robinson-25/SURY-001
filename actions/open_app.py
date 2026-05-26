"""open_app.py — Clean application launcher."""
import os
import subprocess

def open_app(parameters: dict, response=None, player=None) -> str:
    """Launch local desktop applications based on user request."""
    app_name = parameters.get("app_name", "").lower().strip()
    if not app_name:
        return "App name is required, sir."
    
    # Common mappings
    mappings = {
        "notepad": "notepad.exe",
        "bloc de notas": "notepad.exe",
        "calculator": "calc.exe",
        "calculadora": "calc.exe",
        "chrome": "chrome.exe",
        "google chrome": "chrome.exe",
        "explorer": "explorer.exe",
        "explorador de archivos": "explorer.exe",
        "cmd": "cmd.exe",
        "terminal": "powershell.exe",
        "paint": "mspaint.exe"
    }
    
    executable = mappings.get(app_name, app_name)
    
    try:
        # Try to launch standard subprocess
        subprocess.Popen(executable, shell=True)
        msg = f"Opening {app_name}..."
        if player:
            player.write_log(f"🚀 {msg}")
        return f"Successfully launched {app_name}."
    except Exception as e:
        return f"Failed to open '{app_name}': {e}"
