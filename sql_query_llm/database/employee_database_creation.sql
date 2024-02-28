create database employe_database;
use employe_database;
CREATE TABLE Employee (
    id INT AUTO_INCREMENT PRIMARY KEY,
    emp_name VARCHAR(255) NOT NULL,
    department VARCHAR(255) NOT NULL
);

CREATE TABLE Leave_Request (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    reason TEXT NOT NULL,
    leave_status VARCHAR(50) NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES Employee(id)
);

CREATE TABLE Manager (
    id INT AUTO_INCREMENT PRIMARY KEY,
    manager_name VARCHAR(255) NOT NULL
);

CREATE TABLE Approval (
    id INT AUTO_INCREMENT PRIMARY KEY,
    leave_request_id INT NOT NULL,
    manager_id INT NOT NULL,
    approval_status VARCHAR(50) NOT NULL,
    comment TEXT,
    FOREIGN KEY (leave_request_id) REFERENCES Leave_Request(id),
    FOREIGN KEY (manager_id) REFERENCES Manager(id)
);

INSERT INTO Employee (emp_name, department)
VALUES ('John Doe', 'HR'),
       ('Jane Smith', 'IT'),
       ('Mike Johnson', 'Finance'),
       ('Mary Brown', 'Marketing'),
       ('Chris Davis', 'HR'),
       ('Amanda Wilson', 'IT'),
       ('Tom Roberts', 'Finance'),
       ('Laura Lee', 'Marketing'),
       ('Mark Thompson', 'HR'),
       ('Jennifer White', 'IT'),
       ('David Smith', 'Finance'),
       ('Emily Johnson', 'Marketing'),
       ('Steven Wilson', 'HR'),
       ('Sarah Davis', 'IT'),
       ('Brian Roberts', 'Finance');
select * from employee;

INSERT INTO Leave_Request (employee_id, start_date, end_date, reason, leave_status)
VALUES (1, '2024-02-01', '2024-02-05', 'Vacation', 'pending'),
       (2, '2024-02-10', '2024-02-12', 'Sick leave', 'approved'),
       (3, '2024-02-15', '2024-02-20', 'Personal leave', 'pending'),
       (4, '2024-02-01', '2024-02-05', 'Vacation', 'pending'),
       (5, '2024-02-10', '2024-02-12', 'Sick leave', 'approved'),
       (6, '2024-02-15', '2024-02-20', 'Personal leave', 'pending'),
       (7, '2024-02-01', '2024-02-05', 'Vacation', 'pending'),
       (8, '2024-02-10', '2024-02-12', 'Sick leave', 'approved'),
       (9, '2024-02-15', '2024-02-20', 'Personal leave', 'pending'),
       (10, '2024-02-01', '2024-02-05', 'Vacation', 'pending'),
       (11, '2024-02-10', '2024-02-12', 'Sick leave', 'approved'),
       (12, '2024-02-15', '2024-02-20', 'Personal leave', 'pending'),
       (13, '2024-02-01', '2024-02-05', 'Vacation', 'pending'),
       (14, '2024-02-10', '2024-02-12', 'Sick leave', 'approved'),
       (15, '2024-02-15', '2024-02-20', 'Personal leave', 'pending');
select * from Leave_Request;
INSERT INTO Manager (manager_name)
VALUES ('Alice Brown'),
       ('Bob White'),
       ('Cathy Green'),
       ('David Black'),
       ('Eva Gray'),
       ('Frank Yellow'),
       ('Grace Orange'),
       ('Henry Purple'),
       ('Ivy Red'),
       ('Jack Blue'),
       ('Karen Pink'),
       ('Larry Brown'),
       ('Mandy Green'),
       ('Nick Yellow'),
       ('Olivia Red');

-- Insert random approval data
INSERT INTO Approval (leave_request_id, manager_id, approval_status, comment)
VALUES (1, 1, 'approved', 'Enjoy your vacation!'),
       (2, 2, 'approved', 'Get well soon.'),
       (3, 3, 'rejected', 'Please resubmit with more details.'),
       (4, 4, 'approved', 'Have a great time off.'),
       (5, 5, 'rejected', 'Please provide a doctor\'s note.'),
       (6, 6, 'approved', 'Approved for personal reasons.'),
       (7, 7, 'approved', 'Enjoy your vacation!'),
       (8, 8, 'rejected', 'Please provide a doctor\'s note.'),
       (9, 9, 'approved', 'Approved for personal reasons.'),
       (10, 10, 'approved', 'Have a great time off.'),
       (11, 11, 'rejected', 'Please resubmit with more details.'),
       (12, 12, 'approved', 'Enjoy your vacation!'),
       (13, 13, 'rejected', 'Please provide a doctor\'s note.'),
       (14, 14, 'approved', 'Approved for personal reasons.'),
       (15, 15, 'approved', 'Have a great time off.');
select * from leave_request;
select * from approval where approval_status ="Rejected" ;


