# 📄 Kong Gateway Assignment Solution: Rate & Request Size Limiting

This project demonstrates the implementation of **Rate Limiting** and **Request Size Limiting** on a Streamlit Python application using the **Kong API Gateway** in Declarative (DB-less) Mode.

---

## 🚀 Overview and Architecture

The goal was to protect an upstream application (the Plagiarism Checker) by enforcing two traffic control policies using Kong Gateway.

We used a **DB-less architecture**, which simplifies the setup by eliminating the need for a separate PostgreSQL database. Kong loads all configurations (Services, Routes, and Plugins) directly from the mounted `kong.yml` file at startup.

| Component | Image | Role | Ports |
| :--- | :--- | :--- | :--- |
| **my-api** | `plagiarism-checker-api` | Upstream Streamlit Application | `8501` (Internal) |
| **kong** | `kong:latest` | API Gateway enforcing policies | `8000` (External Proxy) |

---

## ⚙️ Configuration Details

The limiting policies are defined in the `kong.yml` file and applied to the **`assignment-service`** which routes traffic via the path `/api`.

### 1. Rate Limiting Plugin

* **Plugin:** `rate-limiting`
* **Rule:** **5 requests per minute** (`config.minute: 5`)
* **Target:** Client IP address (`config.limit_by: ip`)
* **Purpose:** Prevents abuse and overload from a single client.

### 2. Request Size Limiting Plugin

* **Plugin:** `request-size-limiting`
* **Rule:** Max payload size of **100 kilobytes (KB)** (`config.allowed_payload_size: 100`, `config.size_unit: kilobytes`)
* **Purpose:** Protects the upstream service from memory exhaustion and denial-of-service attacks by blocking oversized file uploads/payloads.

---

## 📁 Required Files

To run the solution, ensure these files are present in the project's root directory:

### 1. `docker-compose.yml`

```yaml
version: "3.8"
services:
  # 1. Your API Service
  my-api:
    image: plagiarism-checker-api # Replace with your actual image name if different
    ports:
      - "8501:8501" 
    restart: always

  # 2. Kong Gateway (DB-less Mode)
  kong:
    image: kong:latest
    environment:
      KONG_DATABASE: "off" 
      KONG_DECLARATIVE_CONFIG: "/etc/kong/kong.yml"
      KONG_PROXY_ACCESS_LOG: /dev/stdout
      KONG_PROXY_ERROR_LOG: /dev/stderr
      KONG_ADMIN_LISTEN: 0.0.0.0:8001
    ports:
      - "8000:8000" # Client Proxy Port
      - "8001:8001" # Admin Port
    volumes:
      - ./kong.yml:/etc/kong/kong.yml # Mounts the config file
    depends_on:
      my-api:
        condition: service_started
    command: "kong start"
    restart: always
