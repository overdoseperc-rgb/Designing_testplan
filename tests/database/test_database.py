import sqlite3
import pytest

@pytest.mark.parametrize("value", ["", "   ", "Первая\nВторая", "O'Reilly", "Привет", "🙂", "a\r\nb"])
@pytest.mark.parametrize("operation", ["insert", "update", "delete"])
def test_database_isolation(db, value, operation):
    assert db.execute("SELECT COUNT(*) FROM strings").fetchone()[0] == 0
    db.execute("INSERT INTO strings(value) VALUES (?)", (value,))
    db.commit()
    assert db.execute("SELECT value FROM strings").fetchall() == [(value,)]
    if operation == "update":
        updated = value + "!"
        db.execute("UPDATE strings SET value = ?", (updated,))
        db.commit()
        assert db.execute("SELECT value FROM strings").fetchall() == [(updated,)]
    elif operation == "delete":
        db.execute("DELETE FROM strings")
        db.commit()
        assert db.execute("SELECT COUNT(*) FROM strings").fetchone()[0] == 0

def test_database_not_null(db):
    with pytest.raises(sqlite3.IntegrityError):
        db.execute("INSERT INTO strings(value) VALUES (?)", (None,))
    db.rollback()
    assert db.execute("SELECT COUNT(*) FROM strings").fetchone()[0] == 0
