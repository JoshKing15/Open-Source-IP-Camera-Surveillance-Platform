# OpenVision - Open Source IP Camera Surveillance Platform

> **A modern, open-source, self-hosted video surveillance platform for RTSP/ONVIF cameras featuring low-latency WebRTC streaming, continuous recording, event-based clips, cloud-native storage, AI-powered analytics, and a modern React dashboard.**

## 🚀 Vision

OpenVision is a vendor-agnostic surveillance platform designed for businesses, retail stores, warehouses, offices, smart homes, and developers. It enables users to securely manage IP cameras, stream live video with ultra-low latency using WebRTC, continuously record footage, generate event-based clips, and perform AI-powered video analytics—all using open-source technologies.

Unlike traditional NVR software, OpenVision is built with a cloud-native, microservice architecture that is scalable, extensible, and easy to deploy using Docker.

---

# ✨ Features

## 📹 Live Streaming

* RTSP & ONVIF camera support
* Ultra-low latency WebRTC streaming
* Powered by Janus Gateway
* Multi-user viewing
* Multi-camera dashboard
* Fullscreen mode
* Adaptive streaming
* Browser-based viewing (no plugins)

---

## 🎥 Recording

### Continuous Recording

* 24/7 background recording
* Configurable recording schedules
* Automatic MP4 segmentation
* Configurable retention policies
* Background upload to cloud storage

### Event-Based Recording

Automatically create short clips when:

* Motion is detected
* AI detects a person
* AI detects a vehicle
* Camera tampering occurs
* User manually records a clip

Each clip includes configurable pre-event and post-event recording windows.

---

## ☁ Storage

* MinIO (default)
* Amazon S3 compatible
* Azure Blob Storage (future)
* Google Cloud Storage (future)

Features:

* Automatic uploads
* Storage lifecycle management
* Automatic cleanup
* Download recordings
* Recording search
* Recording playback

---

## 🧠 AI Analytics

Powered by OpenCV and YOLO.

Supported analytics:

* Motion Detection
* Person Detection
* Vehicle Detection
* Customer Counting
* Queue Monitoring
* Intrusion Detection
* Camera Tampering Detection
* Fire & Smoke Detection (future)
* Object Detection
* Heatmaps (future)

---

## 📊 Monitoring

Built-in monitoring using:

* Grafana
* Prometheus
* Loki

Monitor:

* Camera health
* Recording status
* Storage usage
* CPU & Memory
* Network bandwidth
* WebRTC sessions
* Upload status

---

## 🔐 Authentication

* JWT Authentication
* Role-Based Access Control (RBAC)
* Admin
* Manager
* Operator
* Viewer

---

## 📱 Dashboard

Modern React dashboard featuring:

* Live camera grid
* Camera health
* Recording status
* Event timeline
* Playback
* Search recordings
* AI event notifications
* Storage usage
* User management
* System monitoring

---

# 🏗 Architecture

```text
                  RTSP / ONVIF Camera
                           │
                           ▼
                    Camera Manager
                           │
        ┌──────────────────┼───────────────────┐
        │                  │                   │
        ▼                  ▼                   ▼
  Janus Gateway      Recording Service     AI Analytics
   (WebRTC)            (FFmpeg)         (YOLO/OpenCV)
        │                  │                   │
        ▼                  ▼                   ▼
 React Frontend      Continuous MP4      Motion Events
                           │                   │
                           └─────────┬─────────┘
                                     ▼
                              Event Clip Service
                                     │
                                     ▼
                             Background Upload
                                     │
                                     ▼
                             MinIO Object Storage
                                     │
                                     ▼
                               PostgreSQL
```

---

# 🛠 Technology Stack

## Frontend

* React
* TypeScript
* Vite
* Material UI
* React Router
* TanStack Query
* Zustand

---

## Backend

* Python
* FastAPI
* SQLAlchemy
* Alembic
* WebSockets
* JWT

---

## Streaming

* Janus Gateway
* WebRTC
* RTSP
* ONVIF
* FFmpeg
* GStreamer

---

## Storage

* PostgreSQL
* MinIO

---

## AI

* OpenCV
* YOLOv8
* ONNX Runtime

---

## Monitoring

* Prometheus
* Grafana
* Loki

---

## Deployment

* Docker
* Docker Compose

Future:

* Kubernetes
* Helm

---

# 📂 Project Structure

```text
openvision/
│
├── backend/
│   ├── api/
│   ├── auth/
│   ├── cameras/
│   ├── recordings/
│   ├── websocket/
│   ├── analytics/
│   ├── uploads/
│   ├── events/
│   ├── workers/
│   └── Dockerfile
│
├── frontend/
│   ├── src/
│   ├── components/
│   ├── pages/
│   ├── hooks/
│   ├── services/
│   ├── layouts/
│   ├── contexts/
│   └── Dockerfile
│
├── janus/
│   ├── config/
│   └── Dockerfile
│
├── recorder/
│   ├── ffmpeg/
│   ├── workers/
│   ├── clips/
│   └── Dockerfile
│
├── storage/
│   ├── minio/
│   └── lifecycle/
│
├── ai/
│   ├── yolov8/
│   ├── opencv/
│   ├── motion/
│   ├── detection/
│   └── inference/
│
├── database/
│   ├── postgres/
│   ├── migrations/
│   └── seed/
│
├── monitoring/
│   ├── grafana/
│   ├── prometheus/
│   ├── loki/
│   └── alertmanager/
│
├── nginx/
│
├── docs/
│
├── scripts/
│
├── docker-compose.yml
│
├── README.md
│
└── LICENSE
```

---

# 🗺 Roadmap

## Phase 1 — Camera Management

* Camera discovery (ONVIF & RTSP)
* Add camera
* Edit camera
* Remove camera
* Camera status monitoring
* Snapshot preview
* Live RTSP preview
* Camera grouping
* Camera health checks

---

## Phase 2 — Live Streaming

* Janus Gateway integration
* WebRTC streaming
* Multi-camera dashboard
* Fullscreen mode
* Multi-user support
* Adaptive streaming
* Browser playback
* Stream statistics

---

## Phase 3 — Recording & Playback

* Continuous background recording
* Event-based recording
* Manual recording
* MP4 segmentation
* Timeline playback
* Download recordings
* Recording search
* MinIO integration
* Background upload workers
* Retention policies

---

## Phase 4 — Authentication & Security

* JWT authentication
* User management
* Role-Based Access Control (RBAC)
* Admin dashboard
* API security
* Audit logs

---

## Phase 5 — AI Analytics

* Motion detection
* Person detection
* Vehicle detection
* Customer counting
* Queue monitoring
* Camera tampering detection
* Object detection
* AI event clips
* Smart alerts

---

## Phase 6 — Monitoring & Notifications

* Grafana dashboards
* Prometheus metrics
* Loki logging
* Alertmanager integration
* Email notifications
* Telegram notifications
* Discord notifications
* System health monitoring
* Camera uptime monitoring

---

## Phase 7 — Mobile & Cloud

* Progressive Web App (PWA)
* React Native mobile application
* Remote access
* Multi-site management
* Cloud synchronization
* Automatic backups
* Kubernetes deployment
* Helm charts

---

# 🎯 Long-Term Goals

* Support hundreds of cameras
* Support multiple business locations
* Enterprise-ready architecture
* Plugin system
* Public REST API
* SDK for integrations
* AI model marketplace
* Edge AI support
* High Availability (HA)
* Distributed recording services

---

# 📜 License

This project is released under the MIT License.

---

**OpenVision** aims to become a fully open-source alternative to commercial video management systems (VMS), combining modern web technologies, real-time WebRTC streaming, scalable recording, intelligent analytics, and cloud-native deployment into a single, extensible platform.
