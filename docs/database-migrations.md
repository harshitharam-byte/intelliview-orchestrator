# Database Migrations

This project uses **Alembic** for database schema migrations.
Migrations live in `alembic/versions/` and are generated from SQLAlchemy models.

## Why migrations?

- Keep schema changes versioned and reviewable.
- Avoid using `Base.metadata.create_all()` in production.
- Apply schema updates safely across environments.

## Existing migration layout

- `alembic.ini` — Alembic config file.
- `alembic/env.py` — migration environment using `config.DATABASE_URL`.
- `alembic/versions/` — revision history.

## Local workflow

### Apply all pending migrations

```bash
python scripts/migrate.py upgrade head
```

or with Makefile support:

```bash
make migrate
```

### Create a new migration revision

1. Update SQLAlchemy models in `database/models.py`.
2. Generate the revision:

```bash
python scripts/migrate.py revision -m "Add foo column to candidates" --autogenerate
```

or with Makefile support:

```bash
make migrate-revision MSG="Add foo column to candidates"
```

3. Review the generated file in `alembic/versions/`.
4. Apply it locally:

```bash
make migrate
```

### Inspect migration state

```bash
python scripts/migrate.py current
python scripts/migrate.py history
```

### Roll back the last migration

```bash
python scripts/migrate.py downgrade -1
```

or with Makefile support:

```bash
make migrate-downgrade
```

## Environment configuration

Alembic uses the same database URL as the application.
Set `DATABASE_URL` or the database settings in `.env` before running migrations.

If you do not have a `make` command available, use `python scripts/migrate.py` directly.

## Best practices

- Always generate a revision when changing `database/models.py`.
- Keep the migration file and model changes together in one PR.
- Review generated SQL carefully before applying.
- Do not use `Base.metadata.create_all()` for production schema updates.

## Notes

The migration helper script is `scripts/migrate.py`.
It wraps Alembic commands and ensures the project root is on `PYTHONPATH`.
