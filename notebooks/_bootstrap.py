import os, sys
from pathlib import Path

repo_root = Path(__file__).resolve().parents[1]
os.chdir(repo_root)
sys.path.insert(0, str(repo_root))
