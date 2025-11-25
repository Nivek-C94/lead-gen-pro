import os
import yaml
from dotenv import load_dotenv
from pathlib import Path


def load_config():
    """Load configuration dynamically from .env or config.yaml."""
    base_dir = Path(__file__).resolve().parent
    env_path = base_dir / ".env"
    yaml_path = base_dir / "config.yaml"

    config = {}

    # Load from .env if available
    if env_path.exists():
        load_dotenv(env_path)
        config = {
            "DB_PATH": os.getenv("DB_PATH", str(base_dir / "lead_gen.db")),
            "ADMIN_USERNAME": os.getenv("ADMIN_USERNAME", "admin"),
            "ADMIN_PASSWORD": os.getenv("ADMIN_PASSWORD", "password123"),
            "SECRET_KEY": os.getenv("SECRET_KEY", "supersecretkey"),
            "BOTASAURUS_HEADLESS": os.getenv("BOTASAURUS_HEADLESS", "True").lower()
            == "true",
        }

    # Load from YAML as fallback or override
    elif yaml_path.exists():
        with open(yaml_path, "r") as f:
            yaml_config = yaml.safe_load(f)
            config.update(yaml_config)

    else:
        # Defaults if no external config
        config = {
            "DB_PATH": str(base_dir / "lead_gen.db"),
            "ADMIN_USERNAME": "admin",
            "ADMIN_PASSWORD": "password123",
            "SECRET_KEY": "supersecretkey",
            "BOTASAURUS_HEADLESS": True,
        }

    return config
