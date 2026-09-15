# Team Name: The Conquerors
# Team Members: Leon Njoroge, Muse Eid, Josue Rene Nsengiyumva, Didier, Joshua Mulongo

# Project Name: MoMo SMS Analyzer

## Project Description

This project is an enterprise-level full-stack application that processes, cleans, categorizes, stores, analyzes, and visualizes MoMo SMS transaction details.

The system will:

- Process MoMo SMS data provided in XML format.
- Clean and categorize the transaction data.
- Store the processed data in a relational database.
- Provide a frontend interface for analyzing and visualizing transaction data.
- Apply collaborative development practices using GitHub and Agile methodologies.

## Project Architecture

The application will follow a full-stack architecture consisting of:

1. **Data Processing Layer** — Reads and processes MoMo SMS data from XML files.
2. **Backend/API Layer** — Handles business logic and communication between the frontend and database.
3. **Database Layer** — Stores cleaned and categorized transaction data in a relational database.
4. **Frontend Layer** — Allows users to analyze and visualize the processed data.

### Architecture Diagram Link: https://miro.com/app/board/uXjVHqP0yrA=/?share_link_id=567406203993

### Scrum Board Link: https://trello.com/invite/b/6a9e51d0c8b79abb9265b86b/ATTI6df338577c46f74845a65717183d8ab5D48AE8D8/ewdteam4c1continuousformativeassessmentmomosmsanalyze

## Project Structure

```text

│
├── README.md
├── .env.example
├── requirements.txt
├── index.html
│
├── web/
│   ├── styles.css
│   ├── chart_handler.js
│   └── assets/
│
├── data/
│   ├── raw/
│   │   └── momo.xml
│   ├── processed/
│   │   └── dashboard.json
│   ├── db.sqlite3
│   └── logs/
│       ├── etl.log
│       └── dead_letter/
│
├── etl/
│   ├── __init__.py
│   ├── config.py
│   ├── parse_xml.py
│   ├── clean_normalize.py
│   ├── categorize.py
│   ├── load_db.py
│   └── run.py
│
├── api/
│   ├── __init__.py
│   ├── app.py
│   ├── db.py
│   └── schemas.py
│
├── scripts/
│   ├── run_etl.sh
│   ├── export_json.sh
│   └── serve_frontend.sh
│
└── tests/
    ├── test_parse_xml.py
    ├── test_clean_normalize.py
    └── test_categorize.py
```

