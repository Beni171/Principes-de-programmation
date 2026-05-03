USE school_api;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    prenom VARCHAR(100) NOT NULL,
    age INT NOT NULL CHECK (age >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO students (prenom, age) VALUES
('Arthur', 22),
('Emma', 20),
('Sofia', 19),
('Lyes', 23),
('Jacques', 35)