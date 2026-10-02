import sqlite3
import pytest

@pytest.fixture(scope="function")
def db(tmp_path):
    """Отдельная БД для теста; очистка выполняется и при падении теста."""
    path = tmp_path / "test.sqlite3"
    connection = sqlite3.connect(path)
    connection.execute("CREATE TABLE strings (id INTEGER PRIMARY KEY, value TEXT NOT NULL)")
    connection.commit()
    try:
        yield connection
    finally:
        try:
            connection.execute("DELETE FROM strings")
            connection.commit()
            assert connection.execute("SELECT COUNT(*) FROM strings").fetchone()[0] == 0
        finally:
            connection.close()
            path.unlink()
