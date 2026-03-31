import logging
import sqlite3
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATABASE_PATH = os.path.join(os.path.dirname(__file__), "..", "database", "metrics.db")


def init_db():
    """Initialize SQLite database with required tables and seed data."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    logger.info("Creating tables...")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS TBL_PROJECT (
            id         INTEGER  NOT NULL,
            name       VARCHAR,
            created_at DATETIME,
            updated_at DATETIME,
            PRIMARY KEY (id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS TBL_METRICS (
            id            INTEGER      NOT NULL,
            project_id    INTEGER      NOT NULL,
            metrics_type  VARCHAR(50)  NOT NULL,
            name          VARCHAR(50),
            value_integer INTEGER,
            value_float   FLOAT,
            value_string  VARCHAR(50),
            value_date    DATETIME,
            created_at    DATETIME,
            updated_at    DATETIME,
            CONSTRAINT PK_METRICS PRIMARY KEY (id, project_id)
        )
    """)

    conn.commit()
    conn.close()
    logger.info("Database initialization complete.")


if __name__ == "__main__":
    init_db()
