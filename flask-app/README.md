# Multi-Container Flask & Redis Application with Nginx Load Balancing

## Overview

This project demonstrates a **multi-container application** built using Docker and Docker Compose. It consists of:

* A **Flask web application** handling HTTP requests
* A **Redis database** acting as a shared in-memory data store
* An **NGINX reverse proxy** used for load balancing across multiple Flask instances

The application exposes two routes:

* `/` → Returns a welcome message
* `/count` → Tracks and increments the number of visits using Redis

---

## Architecture

```
Browser (localhost:5003)
        ↓
     NGINX
        ↓
 ┌───────────────┐
 │ Flask (xN)    │  ← scaled containers
 └───────────────┘
        ↓
      Redis
```

---

## ⚙️ Tech Stack

* Python (Flask)
* Redis
* NGINX
* Docker & Docker Compose

---

## Features Implemented

### ✅ Multi-container setup

* Flask and Redis run in separate containers
* Managed via Docker Compose

### ✅ Redis integration

* Visit count stored using Redis
* Atomic increment using `INCR`

### ✅ Environment configuration

* Redis connection configured via environment variables
* Avoids hardcoding values inside the application

### ✅ Persistent storage

* Redis data persisted using Docker volumes
* Data survives container restarts

### ✅ Horizontal scaling

* Flask service scaled to multiple instances
* Command used:

```bash
docker-compose up --scale web=3
```

### ✅ Load balancing

* NGINX distributes traffic across Flask instances
* Round-robin behavior observed

### ✅ Load balancing verification

* Each Flask container returns its hostname
* Confirmed requests are handled by different containers

---

## Approach

I followed a step-by-step approach:

1. Built a simple Flask app with required routes
2. Integrated Redis for shared state management
3. Containerised the Flask application using Docker
4. Used Docker Compose to orchestrate services
5. Introduced environment variables for configuration
6. Added Redis persistence using volumes
7. Implemented horizontal scaling for Flask
8. Added NGINX as a reverse proxy for load balancing
9. Verified load balancing by tracking container hostnames

---

## Key Learnings

* **Stateless vs Stateful architecture**
  Flask was designed as a stateless service, while Redis handled shared state.

* **Container networking**
  Services communicate using Docker service names instead of `localhost`.

* **Docker Compose orchestration**
  Simplifies running multi-container applications and managing dependencies.

* **Load balancing concepts**
  NGINX distributes traffic across multiple backend instances.

* **Scalability principles**
  Horizontal scaling works effectively when services are stateless.

---

## Challenges & Solutions

### 🔹 1. Redis connection issues

**Problem:** Flask couldn’t connect to Redis using `localhost`
**Solution:** Used service name (`redis`) as hostname in Docker network

---

### 🔹 2. Data resetting unexpectedly

**Problem:** Visit count reset on each request
**Solution:** Removed manual `SET` and used Redis `INCR` command

---

### 🔹 3. Environment variables not working

**Problem:** Variables defined in Docker Compose but not used
**Solution:** Updated Flask app to read values using `os.getenv()`

---

### 🔹 4. Scaling conflicts with ports

**Problem:** Multiple containers couldn’t bind to same port
**Solution:** Removed port exposure from Flask and introduced NGINX

---

### 🔹 5. Verifying load balancing

**Problem:** Couldn’t confirm traffic distribution
**Solution:** Returned container hostname in responses to track routing

---

## ▶️ How to Run

### 1. Build and start services

```bash
docker-compose up --build
```

### 2. Scale Flask service

```bash
docker-compose up --scale web=3
```

### 3. Access application

```
http://localhost:5003
http://localhost:5003/count
```

---

## Summary

This project demonstrates how to build a **scalable, containerised web application** using:

* Stateless services (Flask)
* Shared state (Redis)
* Reverse proxy (NGINX)
* Container orchestration (Docker Compose)

It reflects real-world backend and DevOps patterns used in production systems.
