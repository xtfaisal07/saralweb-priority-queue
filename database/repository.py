from database.db import Database

class PriorityQueueRepository:

    def __init__(self):
        self.db = Database()

    def create(self, value, priority):
        query = """
        INSERT INTO priority_queue(value, priority)
        VALUES (%s, %s)
        RETURNING id;
        """
        result = self.db.execute(query, (value, priority), fetch=True)
        return result[0]["id"]

    def get_all(self):
        query = """
        SELECT id, value, priority
        FROM priority_queue
        ORDER BY id;
        """
        return self.db.execute(query, fetch=True)

    def update(self, node_id, priority):
        query = """
        UPDATE priority_queue
        SET priority=%s,
            updated_at=NOW()
        WHERE id=%s;
        """
        self.db.execute(query, (priority, node_id))

    def delete(self, node_id):
        query = "DELETE FROM priority_queue WHERE id=%s;"
        self.db.execute(query, (node_id,))

    def clear(self):
        self.db.execute("DELETE FROM priority_queue;")

    def close(self):
        self.db.close()