import sys
import json
from pathlib import Path

try:
    data = json.load(sys.stdin)
    transcript_path = data.get("transcriptPath")
    
    if transcript_path and Path(transcript_path).exists():
        with open(transcript_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        for line in reversed(lines):
            entry = json.loads(line)
            if entry.get("type") == "USER_INPUT":
                user_text = entry.get("content", "")
                with open("chat.log", "a", encoding="utf-8") as log_file:
                    log_file.write(user_text.strip() + "\n---\n")
                break
except Exception:
    pass

# Always output valid JSON to stdout
print("{}")
