# Bloxio - A Modular Real-Time Collaboration Web App

Bloxio is a modern web application that lets users create and organise ideas using modular content blocks - like digital sticky notes, but smarter. Each block can represent notes, tasks, links, or ideas, and can be arranged freely on a workspace.

The goal:  
> **A flexible space for thinking, planning, and collaborating - in real time.**

---

## Features (planned)

- Create, edit, and arrange blocks on a workspace  
- Real-time collaboration (multiple users editing together)  
- Persistent storage (autosave)  
- Authentication and user workspaces  
- Works across devices (browser-based)

---

## Tech Stack (planned)

| Layer          | Technology |
|----------------|------------|
| **Frontend**   | Next.js (App Router), Tailwind CSS |
| **Backend**    | FastAPI (Python) |
| **Realtime**   | Yjs + Hocuspocus (CRDT + WebSockets) |
| **Database**   | PostgreSQL |
| **Auth**       | Cookie-based session auth |
| **Infra**      | Docker & Docker Compose |

---

## Roadmap (MVP)

1. Landing page + app layout 
2. Authentication (login / register / sessions)
3. Workspaces + blocks (CRUD)
4. Real-time collaboration (Yjs / Hocuspocus)  
5. Polish / UX improvements
6. User testing + iteration 

---

## Vision

Bloxio combines the freedom of a whiteboard with the structure of a notes app.
Think: Notion + Miro + sticky notes - built for planning, thinking and collaboration.

---

> _This project is currently in early development. I aim to have a working version by February 2026._
