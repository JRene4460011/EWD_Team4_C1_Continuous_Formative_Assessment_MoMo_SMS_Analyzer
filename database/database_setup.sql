-- SQL Codes for the Users Table
CREATE TABLE Users (
    User_id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Phone_number VARCHAR(20) NOT NULL UNIQUE,
    Customer_type VARCHAR(30) NOT NULL,
    Created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT chk_customer_type
        CHECK (Customer_type IN ('Individual', 'Business', 'Agent'))
)

-- SQL Codes for the TransactionCategories Table
CREATE TABLE TransactionCategories (
    Category_ID INT AUTO_INCREMENT PRIMARY KEY,
    Category_Name VARCHAR(50) NOT NULL UNIQUE,
    Description VARCHAR(255)
);

-- SQL Codes for the Transactions Table
CREATE TABLE IF NOT EXISTS Transactions (
    Transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    Sender_user_id INT NOT NULL,
    Recipient_user_id INT NOT NULL,
    Category_id INT NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    fee DECIMAL(10, 2) NOT NULL,
    Transaction_datetime DATETIME NOT NULL,
    Balance_after DECIMAL(10, 2) NOT NULL,
    Status ENUM('Pending', 'Completed', 'Failed') NOT NULL,
    FOREIGN KEY (Sender_user_id) REFERENCES Users(User_id),
    FOREIGN KEY (Recipient_user_id) REFERENCES Users(User_id),
    FOREIGN KEY (Category_id) REFERENCES TransactionCategories(Category_id)
);

-- SQL Codes for the SystemLogs Table
CREATE TABLE IF NOT EXISTS SystemLogs (
    Log_id INT PRIMARY KEY AUTO_INCREMENT,
    Transaction_id INT NOT NULL,
    Log_datetime DATETIME NOT NULL,
    Message_type VARCHAR(50) NOT NULL,
    Source VARCHAR(100),
    Message TEXT,
    Service_center VARCHAR(100),
    Read_status ENUM('Read', 'Unread') NOT NULL DEFAULT 'Unread',
    Status VARCHAR(50),
    Locked BOOLEAN NOT NULL DEFAULT FALSE,
    Date_sent DATETIME,
    FOREIGN KEY (Transaction_id) REFERENCES Transactions(Transaction_id)
);


---SQL codes for inserting a user into the Users table


---SQL codes for inserting a transaction category into the TransactionCategories table


---SQL codes for inserting a transaction into the Transactions table
INSERT INTO Transactions (Sender_user_id, Recipient_user_id, Category_id, Amount, fee, Transaction_datetime, Balance_after, Status)
VALUES (1, 2, 1, 100.00, 2.50, NOW(), 97.50, 'Completed');


---SQL codes for inserting a system log into the SystemLogs table
