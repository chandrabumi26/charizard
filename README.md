# 🔥 Charizard — Pokémon TCG ETL Pipeline

> *"Like Charizard, this project is built to burn through raw data and transform it into something powerful."*

## 🧩 Overview
**Charizard** is a Python-based project designed to perform **ETL (Extract, Transform, Load)** processes for **Pokémon Trading Card Game (TCG)** data.

The repository is named **Charizard** as a tribute to one of the most iconic Pokémon — known for its power, intensity, and ability to dominate the battlefield. Those same traits are reflected in how this project handles data: **aggressively extracting**, **cleanly transforming**, and **reliably loading** Pokémon TCG data into a data warehouse–ready format.

---

## 🐉 Why Charizard?
Charizard represents:
- 🔥 **Raw power** → High-volume data extraction from external APIs
- 🛠️ **Controlled flames** → Careful transformation, validation, and normalization of data
- 🏔️ **Battle readiness** → Data prepared for analytics, reporting, and warehousing

Just as Charizard evolves from Charmander → Charmeleon → Charizard, this ETL pipeline evolves data from:

**Raw API Data → Structured Models → Analytics-Ready Datasets**

---

## 🎯 Service Purpose
This repository is built to:
- Extract Pokémon TCG data using **TCGdex SDK / API**
- Transform raw card and set data into structured Python models
- Handle missing or inconsistent fields safely (e.g. optional rarity)
- Prepare datasets suitable for **data warehouses**, analytics, or downstream pipelines

This project is ideal for:
- Data engineering experiments
- Pokémon TCG analytics
- ETL pipeline prototyping
- Learning async Python data workflows

---

## ⚙️ ETL Flow (High Level)

```text
EXTRACT   → Fetch Pokémon TCG data from TCGdex API
TRANSFORM → Validate, normalize, and model the data
LOAD      → Prepare data for data warehouse ingestion
```

Each step is designed to be:
- Deterministic
- Reproducible
- Easy to extend

---

## 📁 Project Structure

```text
charizard/
├── test.py              # ETL and data extraction experiments
├── README.md            # Project documentation
├── venv/                # Local virtual environment (not tracked)
```

> ⚠️ Note: Only modified SDK components (if any) are tracked intentionally for experimentation.

---

## 🚀 Getting Started

### 1️⃣ Create virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

### 2️⃣ Install dependencies
```bash
pip install tcgdex-sdk aiohttp
```

### 3️⃣ Run example extraction
```bash
python test.py
```

---

## 🧠 Design Philosophy
- **Fail-safe over fail-fast**: missing fields should not break the pipeline
- **Explicit models** over loose dictionaries
- **Readable > clever** code
- Designed with **data warehousing** in mind

---

## 🧱 Future Plans
- [ ] Export to CSV / Parquet
- [ ] Load into PostgreSQL / BigQuery
- [ ] Incremental ETL runs
- [ ] Data quality checks
- [ ] CI pipeline for validation

---

## 📜 Disclaimer
This project is **not affiliated** with Pokémon, Nintendo, or The Pokémon Company.
All Pokémon names and trademarks belong to their respective owners.

This project is non-profit, created solely for educational, experimental, and learning purposes related to data engineering

---

## ⭐ Closing Note
Just like Charizard on the battlefield, this ETL pipeline is designed to be:

> **Aggressive when extracting, disciplined when transforming, and reliable when loading.**

🔥 Happy data engineering!