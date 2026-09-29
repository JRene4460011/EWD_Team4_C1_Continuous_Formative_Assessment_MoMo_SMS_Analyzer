-- SQL Codes for the Users Table
CREATE TABLE Users (
    User_id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Phone_number VARCHAR(20) NOT NULL UNIQUE,
    Customer_type VARCHAR(30) NOT NULL,
    Created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT chk_customer_type
        CHECK (Customer_type IN ('Individual', 'Business', 'Agent'))
);

-- SQL Codes for the TransactionCategories Table
CREATE TABLE TransactionCategories (
    Category_Id INT AUTO_INCREMENT PRIMARY KEY,
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

####### Sample DML statements to insert test data (at least 5 records per main table)

# Inserting sample data into Users table
INSERT INTO Users (Name, Phone_number, Customer_type) VALUES 
('Muse Eid', '252636529997', 'Business'),
('Josue Rene Nsengiyumva', '250795013860', 'Agent'),
('Didier Abizera', '250790156404', 'Individual'),
('Joshua Gunnogere Mulongo', '+256778406494', 'Business'),
('David Nwza', '+271713456789', 'Individual');

# Inserting sample data into TransactionCategories table
INSERT INTO TransactionCategories (Category_Name, Description) VALUES
('Cash Transfer', 'Direct money transfer between individual users'),
('Merchant Payment', 'Payments made directly to business tills or merchant accounts'),
('Cash Withdrawal', 'Agent-assisted cash out transactions'),
('Airtime Purchase', 'Direct top-up for mobile airtime and data bundles'),
('Bill Payment', 'Utility and formal service subscription payments');

# Inserting sample data into Transactions table
INSERT INTO Transactions (Sender_user_id, Recipient_user_id, Category_id, Amount, fee, Transaction_datetime, Balance_after, Status) VALUES
(1, 4, 1, 1500.00, 15.00, '2026-06-01 10:30:00', 8500.00, 'Completed'),
(2, 5, 2, 12500.00, 0.00, '2026-06-01 11:15:00', 45000.00, 'Completed'),
(1, 3, 3, 5000.00, 55.00, '2026-06-02 09:00:00', 3500.00, 'Completed'),
(4, 1, 4, 200.00, 0.00, '2026-06-02 14:20:00', 1800.00, 'Completed'),
(5, 2, 5, 3400.00, 10.00, '2026-06-03 16:45:00', 41600.00, 'Pending');

# Inserting sample data into SystemLogs table
INSERT INTO SystemLogs (Transaction_id, Log_datetime, Message_type, Source, Message, Service_center, Read_status, Status, Locked, Date_sent) VALUES
(1, '2026-06-01 10:30:05', 'SMS_RECEIVED', 'Gateway_A', 'Confirmed. RWF1,500.00 sent to Didier...', 'Nairobi Hub', 'Read', 'Success', FALSE, '2026-06-01 10:30:00'),
(2, '2026-06-01 11:15:02', 'SMS_RECEIVED', 'Gateway_B', 'Confirmed. RWF12,500 paid to Joshua Mulongo...', 'Mombasa Hub', 'Unread', 'Success', FALSE, '2026-06-01 11:15:00'),
(3, '2026-06-01 09:00:10', 'SMS_RECEIVED', 'Gateway_A', 'Withdrawal of RWF5,000 at Agent Josue Rene...', 'Kigali Hub', 'Read', 'Success', FALSE, '2026-06-01 09:00:00'),
(4, '2026-06-02 14:20:03', 'SMS_RECEIVED', 'Gateway_C', 'You have bought RWF200 airtime...', 'Kigali Hub', 'Unread', 'Success', FALSE, '2026-06-02 14:20:00'),
(5, '2026-06-03 16:45:08', 'SMS_RECEIVED', 'Gateway_B', 'Bill payment of RWF3,400 processing...', 'Kampala Hub', 'Unread', 'Processing', TRUE, '2026-06-03 16:45:00');
-- Indexes for performance optimization
CREATE INDEX idx_transactions_sender ON Transactions(Sender_user_id);
CREATE INDEX idx_transactions_recipient ON Transactions(Recipient_user_id);
CREATE INDEX idx_transactions_category ON Transactions(Category_id);
CREATE INDEX idx_transactions_datetime ON Transactions(Transaction_datetime);
CREATE INDEX idx_transactions_status ON Transactions(Status);
CREATE INDEX idx_systemlogs_transaction ON SystemLogs(Transaction_id);
CREATE INDEX idx_systemlogs_datetime ON SystemLogs(Log_datetime);

-- Additional CHECK constraints
ALTER TABLE Transactions ADD CONSTRAINT chk_amount_positive CHECK (Amount > 0);
ALTER TABLE Transactions ADD CONSTRAINT chk_fee_non_negative CHECK (fee >= 0);
ALTER TABLE Transactions ADD CONSTRAINT chk_balance_non_negative CHECK (Balance_after >= 0);