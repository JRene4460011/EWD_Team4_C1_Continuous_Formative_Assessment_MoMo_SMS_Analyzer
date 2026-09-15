-- SQL Codes for the Users Table
CREATE TABLE Users (
    User_id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Phone_number VARCHAR(20) NOT NULL UNIQUE,
    Customer_type VARCHAR(30) NOT NULL,
    Created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT chk_customer_type
        CHECK (Customer_type IN ('Individual', 'Business', 'Agent'))

-- SQL Codes for the TransactionCategories Table
CREATE TABLE TransactionCategories (
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
    External_transaction_id VARCHAR(255),
    FOREIGN KEY (Sender_user_id) REFERENCES Users(User_id),
    FOREIGN KEY (Recipient_user_id) REFERENCES Users(User_id),
    FOREIGN KEY (Category_id) REFERENCES TransactionCategories(Category_id)
);


-- SQL Codes for the SystemLogs Table