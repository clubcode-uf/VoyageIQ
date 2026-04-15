<div align="center">
 
<br />
 
```
 ██╗   ██╗ ██████╗ ██╗   ██╗ █████╗  ██████╗ ███████╗██╗ ██████╗
 ██║   ██║██╔═══██╗╚██╗ ██╔╝██╔══██╗██╔════╝ ██╔════╝██║██╔═══██╗
 ██║   ██║██║   ██║ ╚████╔╝ ███████║██║  ███╗█████╗  ██║██║   ██║
 ╚██╗ ██╔╝██║   ██║  ╚██╔╝  ██╔══██║██║   ██║██╔══╝  ██║██║▄▄ ██║
  ╚████╔╝ ╚██████╔╝   ██║   ██║  ██║╚██████╔╝███████╗██║╚██████╔╝
   ╚═══╝   ╚═════╝    ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝ ╚══▀▀═╝
```
 
###  AI-Powered Travel Intelligence Platform
 
**Predict flights · Plan trips · Master your budget**
 
<br />
 
[![Frontend](https://img.shields.io/badge/Frontend-Next.js%2014-black?style=for-the-badge&logo=next.js)](https://nextjs.org)
[![Backend](https://img.shields.io/badge/Backend-Node.js%20%2B%20Express-339933?style=for-the-badge&logo=node.js)](https://nodejs.org)
[![Database](https://img.shields.io/badge/Database-PostgreSQL-4169E1?style=for-the-badge&logo=postgresql)](https://postgresql.org)
[![Language](https://img.shields.io/badge/Language-TypeScript-3178C6?style=for-the-badge&logo=typescript)](https://typescriptlang.org)
[![Styling](https://img.shields.io/badge/Styling-Tailwind%20CSS-06B6D4?style=for-the-badge&logo=tailwindcss)](https://tailwindcss.com)
 
<br />
 
</div>
 
---
 
## 📖 Table of Contents
 
- [About the Project](#-about-the-project)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [Running the Project](#-running-the-project)
- [API Reference](#-api-reference)
- [Deployment](#-deployment)
 
---
 
## 🌍 About the Project
 
VoyageIQ is an AI-powered travel intelligence platform that takes the stress out of trip planning. Instead of jumping between five different apps to book flights, plan hotels, manage a budget, and find restaurants — VoyageIQ does it all in one place.
 
The platform uses machine learning to predict when flight prices are about to rise, generates personalised budget plans based on your destination and group size, and builds complete day-by-day itineraries with flights, accommodation, food, and activities.
 
> **This is a monorepo** — the frontend and backend both live inside this single repository.
 
---
 
##  Features (Current)-----------New Incoming
 
| Feature | Description |
|---|---|
|  **Flight Prediction** | ML model predicts whether a fare will rise or fall — tells you the best time to book |
|  **Smart Budget Planner** | Enter your total budget and get a category-by-category breakdown for any trip |
| **Trip Planner** | Drag-and-drop itinerary builder covering flights, hotels, food, and activities |
| **AI Assistant** | Chat with GPT-4 to plan entire trips in natural language |
| **Price Alerts** | Set a target fare and get notified the moment it drops |
 
---
 
##  Tech Stack
 
### Frontend
| Tool | Purpose |
|---|---|
| Next.js 14 (App Router) | React framework with SSR and file-based routing |
| TypeScript | Static typing across the entire codebase |
| Tailwind CSS | Utility-first CSS styling |
| Zustand | Lightweight global state management |
| Axios | HTTP client for backend API calls |
| Recharts | Data visualisation (price charts, budget breakdowns) |
| Mapbox GL JS | Interactive maps |
 
### Backend
| Tool | Purpose |
|---|---|
| Node.js + Express | REST API server |
| TypeScript | Static typing |
| Prisma | Type-safe database ORM |
| PostgreSQL | Primary relational database |
| JWT + bcrypt | Authentication and password hashing |
| Amadeus SDK | Live flight search and pricing |
| SendGrid | Transactional email |
 
### DevOps
| Tool | Purpose |
|---|---|
| GitHub Actions | CI — lints and builds every PR automatically |
| Vercel | Frontend hosting (auto-deploys on push to main) |
| Render | Backend hosting (auto-deploys on push to main) |
| Supabase | Managed PostgreSQL database |
 
---
 


 
##  Getting Started
 
### Prerequisites
 
Make sure you have these installed before starting:
 
- **Node.js v20+** — [nodejs.org](https://nodejs.org)
- **Git** — [git-scm.com](https://git-scm.com)
- **Git Bash** (Windows only) — installed with Git above
- **VS Code or PyCharm** — your code editor
- **A Supabase account** — free PostgreSQL database at [supabase.com](https://supabase.com)
 
### 1. Clone the Repository
 
```bash
git clone https://github.com/YOUR-USERNAME/voyageiq.git
cd VoyageIQ
```
 
### 2. Switch to the Dev Branch
 
```bash
git checkout dev
```
 
>  Always work on `dev` — never directly on `main`.
 
### 3. Install All Dependencies
 
```bash
npm run install:all
```
 
This installs packages for the root, frontend, and backend in one command.
 
### 4. Set Up Environment Files
 
```bash
# Backend
cd backend && cp .env.example .env
 
# Frontend
cd ../frontend && cp .env.local.example .env.local
```
 
Open each file and fill in the values — ask the lead for real API keys.
 
### 5. Set Up the Database
 
```bash
cd backend
npx prisma migrate dev
```
 
This creates all the database tables. You only need to run this once (and again if the schema changes).
 
### 6. Start the Project
 
```bash
# From the ROOT folder — starts both frontend AND backend together
cd ..
npm run dev
```
 
| App | URL |
|---|---|
|  Frontend | http://localhost:3000 |
|  Backend | http://localhost:4000 |
|  Health check | http://localhost:4000/api/health |
 
---
 
 
## ▶️ Running the Project
 
```bash
# Start BOTH apps at the same time (recommended)
npm run dev
 
# Start only the frontend
npm run dev:fe
 
# Start only the backend
npm run dev:be
 
# Install packages for all apps at once
npm run install:all
```
 
---
 
 
##  API Reference
 
See **[API.md](./API.md)** for the full endpoint contract.
 
Quick overview:
 
| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/auth/register` | Create a new account |
| `POST` | `/api/auth/login` | Log in and receive a JWT token |
| `GET` | `/api/flights/search` | Search flights by route and date |
| `POST` | `/api/budget/calculate` | Generate a budget breakdown |
| `GET` | `/api/trips` | Get all trips for the logged-in user |
| `POST` | `/api/trips` | Create a new trip |
| `PUT` | `/api/trips/:id` | Update a trip |
| `DELETE` | `/api/trips/:id` | Delete a trip |
| `GET` | `/api/health` | Confirm the backend is running |
 
---
 
## Deployment
 
| App | Platform | Trigger |
|---|---|---|
|  Frontend | [Vercel](https://vercel.com) | Auto-deploys when `main` is updated |
| Backend | [Render](https://render.com) | Auto-deploys when `main` is updated |
|  Database | [Supabase](https://supabase.com) | Managed PostgreSQL — always on |
 
### Deploy Settings
 
**Vercel (Frontend)**
- Root Directory: `frontend`
- Framework: Next.js
 
**Render (Backend)**
- Root Directory: `backend`
- Build Command: `npm install && npx prisma generate`
- Start Command: `npm start`
 
>  Never push directly to `main`. Merge `dev` → `main` only when a version is stable and tested.
 
---
 
<div align="center">
 

 
</div>

