import datetime
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]
progress_file = project_root / "PROJECT_PROGRESS.md"


def update_progress():
    if not progress_file.exists():
        print("PROJECT_PROGRESS.md not found.")
        return

    text = progress_file.read_text()
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    # Replace last updated timestamp
    if "_Last updated:" in text:
        new_text = text.split("_Last updated:")[0] + f"_Last updated: {now}_"
    else:
        new_text = text + f"\n\n_Last updated: {now}_"

    progress_file.write_text(new_text)
    print(f"Updated PROJECT_PROGRESS.md timestamp → {now}")


if __name__ == "__main__":
    update_progress()
