-- SQL Codes for the Users Table


-- SQL Codes for the TransactionCategories Table


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
    External_transaction_id VARCHAR(255),
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