# Team Name: The Conquerors

## Team Members

- Muse Eid
- Josue Rene Nsengiyumva
- Didier
- Joshua Mulongo

# Project Name: MoMo SMS Analyzer

## Project Description

This project is an enterprise-level full-stack application that processes, cleans, categorizes, stores, analyzes, and visualizes MoMo SMS transaction details.

The system will:

- Process MoMo SMS data provided in XML format.
- Clean and categorize the transaction data.
- Store the processed data in a relational database.
- Provide a frontend interface for analyzing and visualizing transaction data.
- Apply collaborative development practices using GitHub and Agile methodologies.

---

# Project Resources & Links

| Resource | Link |
|---|---|
|  Task Sheet / Assignment Instructions | **Add task sheet link here** |
|  ERD Diagram | **[ ERD link here](https://lucid.app/lucidchart/14d29ad4-65ba-4fcf-be05-ce500a5e9075/edit?docId=14d29ad4-65ba-4fcf-be05-ce500a5e9075&shared=true&page=0_0#)** |
|  Database Design Document | **Add PDF link here** |


---

# Project Architecture

The application will follow a full-stack architecture consisting of:

1. **Data Processing Layer** — Reads and processes MoMo SMS data from XML files.
2. **Backend/API Layer** — Handles business logic and communication between the frontend and database.
3. **Database Layer** — Stores cleaned and categorized transaction data in a relational database.
4. **Frontend Layer** — Allows users to analyze and visualize transaction data.

### Architecture Diagram
Architecture Diagram Link: https://miro.com/app/board/uXjVHqP0yrA=/?share_link_id=567406203993

### Scrum Board

[View Scrum Board][(https://trello.com/invite/b/6a9e51d0c8b79abb9265b86b/ATTI6df338577c46f74845a65717183d8ab5D48AE8D8/ewdteam4c1continuousformativeassessmentmomosmsanalyze)](https://trello.com/invite/b/6a9e51d0c8b79abb9265b86b/ATTI6df338577c46f74845a65717183d8ab5D48AE8D8/ewdteam4c1continuousformativeassessmentmomosmsanalyze)

---

# Database Design

The database component of the MoMo SMS Analyzer stores and manages structured transaction information.

## Main Entities

- **Users / Customers** — Stores sender and receiver information.
- **Transactions** — Stores MoMo transaction records.
- **Transaction Categories** — Stores transaction/payment types.
- **System Logs** — Tracks transaction and system processing activity.

## Entity Relationship Diagram

The ERD represents the entities, attributes, primary keys, foreign keys, and relationships within the database.

**ERD file location:**

```text
docs/

```

[View ERD Diagram](ADD_ERD_LINK_HERE)

## SQL Database Implementation

The SQL database implementation is stored in:

```text
database/

```

The SQL script contains:

- Table creation
- Primary keys
- Foreign keys
- CHECK constraints
- Indexes
- Sample data
- CRUD operations
- Database testing queries



## JSON Data Modeling


The JSON file demonstrates:

- JSON representations of the main entities
- Related and nested data
- Transaction data
- User information
- Transaction categories
- System logs
- Complete transaction objects
- SQL-to-JSON mapping

[View JSON Schemas](ADD_JSON_LINK_HERE)

---

# Database Documentation

The Database Design Document contains:

- ERD documentation
- Design rationale and justification
- Data dictionary
- Sample database queries
- Query results
- Database constraints
- Security and accuracy rules
- Screenshots demonstrating database functionality

(ADD_PDF_LINK_HERE)

---

# Project Structure

```text
EWD_Team4_C1_Continuous_Formative_Assessment_MoMo_SMS_Analyzer/
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
├── database/
│   └── database_setup.sql
│
├── docs/
│   ├── ERD DIAGRAM...jpeg
│   ├── erd_diagram_components.txt
│   └── database_design_document.pdf
│
├── examples/
│   └── json_schemas.json
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


