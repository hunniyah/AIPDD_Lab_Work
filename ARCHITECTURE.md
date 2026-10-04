# System Requirements & Software Architecture Specification

## 1. Functional Requirements (Smart Automated Attendance System)

| ID | Requirement Name | Description | Target Metric / Constraint |
|---|---|---|---|
| FR-01 | Face Detection & Alignment | Automatically detect human faces in video feed and align them for feature extraction. | Latency < 150 ms per frame |
| FR-02 | Feature Vector Extraction | Generate unique facial embeddings using deep learning feature extractors. | 128/512-dimensional vector |
| FR-03 | Attendance Logging | Match embeddings against database and mark attendance status automatically. | Real-time database insert |
| FR-04 | Database Synchronization | Sync local attendance logs with centralized Cloud/Enterprise database. | Periodic auto-sync every 60s |
| FR-05 | Admin Alert Dispatch | Trigger dynamic alerts when unauthorized personnel or spoof attempts are detected. | Immediate push/email notification |

---

## 2. Non-Functional Requirements

| ID | Requirement Category | Constraint Specification | Standard Target |
|---|---|---|---|
| NFR-01 | System Performance | Processing Frame Rate | Minimum 25 FPS live video processing |
| NFR-02 | Accuracy Threshold | Precision/Recall on facial identification | Precision >= 98.5% |
| NFR-03 | Resource Efficiency | Edge Device Memory Footprint | Peak RAM usage <= 2.0 GB |
| NFR-04 | Power Optimization | Operational Power Consumption | Designed for <= 15W TDP edge hardware |
| NFR-05 | Data Security & Privacy | Encrypted feature store and compliant logs | AES-256 encryption at rest |

---

## 3. System Boundary, Actors, & I/O Mapping

### System Actors
* **Security Operator:** Monitors live streams, ROI alerts, and detection logs.
* **System Administrator:** Configures thresholds, camera streams, and manages database entries.
* **Automated Trigger System:** Ingests events and generates notifications automatically.

### System Input/Output Specification

| Data Component | Type | Source / Destination | Format / Specification |
|---|---|---|---|
| RTSP Video Stream | Input | Surveillance Camera | 1080p @ 30 FPS |
| Camera Calibration Parameters | Input | Config File | JSON / YAML (`configs/`) |
| Bounding Box Coordinates | Output | Display Overlay | Dynamic Pixel Coordinates $[x_{min}, y_{min}, x_{max}, y_{max}]$ |
| Intrusion Alert Payload | Output | Security Dashboard / API | JSON Payload |
| Attendance Event Log | Output | Local & Remote Database | Relational SQL Entry |

---

## 4. Data-Flow Diagram (Mermaid.js)

```mermaid
graph TD
    A[Camera Feed / RTSP] -->|Raw Frames| B(Process 1.0: Data Ingestion)
    B -->|Bayer/BGR Image| C(Process 2.0: Image Preprocessing)
    C -->|Normalized 640x640 Tensor| D(Process 3.0: Model Inference Engine)
    D -->|Bounding Boxes & Confidences| E(Process 4.0: Post-Processing & Analytics)
    E -->|Filtered Detections| F[(Data Store: Events & Logs)]
    E -->|Intrusion Alert Signal| G[Security Dashboard / Alert System]
