import sqlite3
import uuid

from django.db import migrations


def fix_invalid_resume_ids(apps, schema_editor):
    db_path = schema_editor.connection.settings_dict["NAME"]
    conn = sqlite3.connect(db_path)
    try:
        rows = conn.execute(
            "SELECT rowid, id FROM api_resume WHERE id IS NULL OR id = '' OR LENGTH(id) != 32 OR id NOT GLOB '[0-9A-Fa-f]*'"
        ).fetchall()
        for rowid, _ in rows:
            new_uuid = uuid.uuid4().hex
            conn.execute("UPDATE api_resume SET id = ? WHERE rowid = ?", (new_uuid, rowid))
        conn.commit()
    finally:
        conn.close()


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(fix_invalid_resume_ids, migrations.RunPython.noop),
    ]
