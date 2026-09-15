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
|  Task Sheet / Assignment Instructions | **(https://docs.google.com/spreadsheets/d/1FEtbr-OIVN7AzKFJV_M4lCoeNIGhVSA_8NuFQvvO9X0/edit?gid=0#gid=0)** |
|  ERD Diagram | **[ ERD link here](https://lucid.app/lucidchart/14d29ad4-65ba-4fcf-be05-ce500a5e9075/edit?docId=14d29ad4-65ba-4fcf-be05-ce500a5e9075&shared=true&page=0_0#)** |
|  Database Design Document | **(https://docs.google.com/document/d/1nYUTSs9r7u8KCLCKc5Qsr_BQXlR3AOKZnnTKD6Qn39c/edit?tab=t.0)** |


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



The SQL script contains:

- Table creation
- Primary keys
- Foreign keys
- CHECK constraints
- Indexes
- Sample data
- CRUD operations
- Database testing queries



## Database to JSON Mapping

### Users Table

| SQL Column | JSON Field | JSON Type | Description |
|---|---|---|---|
| `User_id` | `user_id` | Number | Unique user ID |
| `Name` | `name` | String | User's name |
| `Phone_number` | `phone_number` | String | User's phone number, including country code |
| `Customer_type` | `customer_type` | String | Customer type: Individual, Business, or Agent |
| `Created_at` | `created_at` | String | User creation date and time in ISO format |

### TransactionCategories Table

| SQL Column | JSON Field | JSON Type | Description |
|---|---|---|---|
| `Category_ID` | `category_id` | Number | Unique category ID |
| `Category_Name` | `category_name` | String | Name of the transaction category |
| `Description` | `description` | String | Description of the transaction category |

### Transactions Table

| SQL Column | JSON Field | JSON Type | Description |
|---|---|---|---|
| `Transaction_id` | `transaction_id` | Number | Unique transaction ID |
| `Sender_user_id` | `sender` | Object | Sender's user information |
| `Recipient_user_id` | `recipient` | Object | Recipient's user information |
| `Category_id` | `category` | Object | Transaction category information |
| `Amount` | `amount` | Number | Transaction amount |
| `fee` | `fee` | Number | Transaction processing fee |
| `Balance_after` | `balance_after` | Number | Wallet balance after the transaction |
| `Status` | `status` | String | Transaction status: Pending, Completed, or Failed |

### SystemLogs Table

| SQL Column | JSON Field | JSON Type | Description |
|---|---|---|---|
| `Log_id` | `log_id` | Number | Unique log ID |
| `Transaction_id` | `system_logs` | Array | SMS logs linked to the transaction |
| `Log_datetime` | `log_datetime` | String | Date and time when the SMS was captured |
| `Message_type` | `message_type` | String | Type of SMS event, e.g. `SMS_RECEIVED` |
| `Source` | `source` | String | Gateway that handled the SMS |
| `Message` | `message` | String | Raw SMS message |
| `Locked` | `locked` | Boolean | Whether the log is locked |

---
**(https://docs.google.com/document/d/1nYUTSs9r7u8KCLCKc5Qsr_BQXlR3AOKZnnTKD6Qn39c/edit?tab=t.wud1xv73ze3x
)** 

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


