import sqlite3

class TodoDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS todo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            category TEXT,
            status TEXT DEFAULT 'pending'
        );
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_task(self, task, category):
        query = "INSERT INTO todo (task, category) VALUES (?, ?)"
        self.conn.execute(query, (task, category))
        self.conn.commit()

    def view_tasks(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM todo")
        return cursor.fetchall()

    def fetch_tasks(self, status=None, category=None):
        cursor = self.conn.cursor()
        query = "SELECT * FROM todo WHERE 1=1"  # Base query

        parameters = []
        if status:
            query += " AND status = ?"
            parameters.append(status)
        if category:
            query += " AND category = ?"
            parameters.append(category)

        cursor.execute(query, parameters)
        return cursor.fetchall()

    def complete_task(self, task_id):
        query = "UPDATE todo SET status = 'completed' WHERE id = ?"
        self.conn.execute(query, (task_id,))
        self.conn.commit()

    def delete_task(self, task_id):
        query = "DELETE FROM todo WHERE id = ?"
        self.conn.execute(query, (task_id,))
        self.conn.commit()

    def update_task(self, task_id, new_task, new_category=None):
        query = "UPDATE todo SET task = ?, category = ? WHERE id = ?"
        self.conn.execute(query, (new_task, new_category, task_id))
        self.conn.commit()