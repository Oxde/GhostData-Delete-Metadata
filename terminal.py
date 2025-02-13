import sys
import os
from ghostdata.cleaner import GhostData


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python remove_metadata.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    if os.path.exists(file_path):
        GhostData.clean(file_path)
    else:
        print(f"File not found: {file_path}")