# Persistent Min-Max Priority Queue

A production-style implementation of a persistent priority queue using a custom Min-Max Heap and PostgreSQL.

## Features

- Insert
- Extract Minimum
- Extract Maximum
- Peek (Min & Max)
- Update Priority
- Delete
- Is Empty

## Architecture

- Language: Python
- Database: PostgreSQL
- Data Structure: Min-Max Heap
- Pattern: Repository + Service


             module.py
                 │
        PriorityQueue Service
         ├───────────────┐
         │               │
   Min-Max Heap      Repository
         │               │
         └──── PostgreSQL ────┘

## Complexity

| Operation | Time |
|-----------|------|
| Insert | O(log n) |
| Extract Min | O(log n) |
| Extract Max | O(log n) |
| Peek | O(1) |
| Update | O(log n) |
| Delete | O(log n) |

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create database:

```sql
CREATE DATABASE saralweb_pq;
```

Initialize:

```bash
python init_db.py
```

Run demo:

```bash
python demo.py
```

## Real-world Applications

- Hospital emergency triage
- CPU scheduling
- Customer support ticket prioritization
- Job scheduling systems
- Delivery order management