import argparse
import sys
from pathlib import Path

from alembic.command import downgrade, upgrade
from alembic.config import Config
from src.config import init_config

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Creates tables from alembic revisions. "
    )

    parser.add_argument("--downgrade", help="Downgrade revision")
    args = parser.parse_args()

    config = init_config()
    alembic_cfg = Config(Path(__file__).parent / "alembic.ini")

    alembic_cfg.set_main_option(
        "sqlalchemy.url",
        f"postgresql://{config['DB_USER']}:{config['DB_PASSWORD']}@{config['DB_HOST']}/{config['DB_DBNAME']}",
    )

    if args.downgrade:
        downgrade(alembic_cfg, "-1")
        sys.exit(0)

    upgrade(alembic_cfg, "head")
