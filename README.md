# Persistent Min-Max Priority Queue

A production-style implementation of a **Persistent Priority Queue** using a custom **Min-Max Heap** with **PostgreSQL** for durable storage. The project exposes a REST API with **FastAPI** and includes a modern **React** dashboard for interactive visualization.

> Software Development Engineer (SDE) Interview Assignment – Saralweb

---

## Live Demo

- **Frontend:** https://saralweb-pq-web.vercel.app/
- **Backend API:** https://saralweb-priority-queue.onrender.com/
- **Swagger Docs:** https://saralweb-priority-queue.onrender.com/docs

---

## Features

- Insert
- Extract Minimum
- Extract Maximum
- Peek (Min & Max)
- Update Priority
- Delete
- Is Empty
- Persistent PostgreSQL Storage
- REST API (FastAPI)
- Interactive React Dashboard

---

## Tech Stack

| Layer | Technology |
|--------|------------|
| Language | Python |
| Backend | FastAPI |
| Frontend | React + Vite + Tailwind CSS |
| Database | PostgreSQL |
| Data Structure | Custom Min-Max Heap |
| Pattern | Repository + Service |

---

## Architecture

```text
              React Dashboard
                     │
                     ▼
              FastAPI REST API
                     │
                     ▼
                module.py
                     │
          PriorityQueue Service
             ├───────────────┐
             │               │
        Min-Max Heap     Repository
             │               │
             └──── PostgreSQL ────┘
```

The application combines an efficient in-memory **Min-Max Heap** with **PostgreSQL** to provide both logarithmic priority queue operations and persistent storage.

---

## Project Structure

```text
saralweb-priority-queue/
│
├── api.py
├── module.py
├── init_db.py
├── requirements.txt
├── README.md
│
├── database/
│   ├── db.py
│   ├── repository.py
│   └── schema.sql
│
├── heap/
│   ├── minmax_heap.py
│   ├── node.py
│   └── exceptions.py
│
└── tests/
    └── test_module.py
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/tasks` | Retrieve all tasks |
| POST | `/insert` | Insert new task |
| GET | `/peek` | View min & max |
| POST | `/extract-min` | Remove minimum |
| POST | `/extract-max` | Remove maximum |
| PUT | `/update/{id}` | Update priority |
| DELETE | `/delete/{id}` | Delete task |

---

## Time Complexity

| Operation | Complexity |
|-----------|------------|
| Insert | O(log n) |
| Extract Min | O(log n) |
| Extract Max | O(log n) |
| Peek | O(1) |
| Update | O(log n) |
| Delete | O(log n) |
| Is Empty | O(1) |

---

## Local Setup

### 1. Clone Repository

```bash
git clone https://github.com/xtfaisal07/saralweb-priority-queue.git
cd saralweb-priority-queue
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Create Database

```sql
CREATE DATABASE saralweb_pq;
```

### 4. Initialize Database

```bash
python init_db.py
```

### 5. Run Backend

```bash
uvicorn api:app --reload
```

API runs at:

```text
http://127.0.0.1:8000
```

Interactive API:

```text
http://127.0.0.1:8000/docs
```

---

## Real-World Applications

- Hospital emergency triage
- CPU & process scheduling
- Customer support ticket prioritization
- Job scheduling systems
- Delivery order management
- Network packet prioritization
- Event-driven simulation systems

---

## Author

**Faisal Naseer**

- B.Tech CSE (Artificial Intelligence & Machine Learning)
- GitHub: https://github.com/xtfaisal07
- Live Demo: https://saralweb-pq-web.vercel.app/
