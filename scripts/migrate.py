"""Database migration helper for IntelliView Orchestrator.

This script wraps Alembic so developers can run migrations from the project
root without manually configuring `PYTHONPATH` or the Alembic package.
"""

from __future__ import annotations

import argparse
import os
import sys

from alembic.config import Config

from alembic import command

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ALEMBIC_INI = os.path.join(ROOT, "alembic.ini")


def make_config() -> Config:
    config = Config(ALEMBIC_INI)
    config.set_main_option("script_location", os.path.join(ROOT, "alembic"))
    return config


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Alembic migration helper for IntelliView Orchestrator",
    )
    parser.add_argument(
        "command",
        choices=["upgrade", "downgrade", "revision", "current", "history"],
        help="Alembic command to run",
    )
    parser.add_argument(
        "revision", nargs="?", default="head", help="Revision identifier or path"
    )
    parser.add_argument("-m", "--message", help="Message for revision generation")
    parser.add_argument(
        "--autogenerate", action="store_true", help="Autogenerate revision from models"
    )

    args = parser.parse_args()
    sys.path.insert(0, ROOT)

    config = make_config()

    if args.command == "upgrade":
        command.upgrade(config, args.revision)
    elif args.command == "downgrade":
        command.downgrade(config, args.revision)
    elif args.command == "revision":
        if args.autogenerate and not args.message:
            parser.error("--message is required when using --autogenerate")
        command.revision(
            config, message=args.message or "", autogenerate=args.autogenerate
        )
    elif args.command == "current":
        command.current(config)
    elif args.command == "history":
        command.history(config)
    else:
        parser.error(f"Unsupported command: {args.command}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
