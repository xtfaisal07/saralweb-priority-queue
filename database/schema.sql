DROP TABLE IF EXISTS priority_queue;

CREATE TABLE priority_queue (
    id SERIAL PRIMARY KEY,
    value TEXT NOT NULL,
    priority INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_priority
ON priority_queue(priority);

CREATE INDEX idx_created
ON priority_queue(created_at);