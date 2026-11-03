CREATE DATABASE IF NOT EXISTS rpms_db;
USE rpms_db;

CREATE TABLE IF NOT EXISTS candidates (
    candidate_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    mobile VARCHAR(20) NOT NULL UNIQUE,
    technology VARCHAR(100),
    percentage DECIMAL(5,2) NOT NULL,
    passing_year INT NOT NULL,
    backlogs INT NOT NULL DEFAULT 0,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    CHECK (percentage BETWEEN 0 AND 100),
    CHECK (backlogs >= 0)
);

CREATE TABLE IF NOT EXISTS companies (
    company_id INT AUTO_INCREMENT PRIMARY KEY,
    company_name VARCHAR(150) NOT NULL,
    location VARCHAR(150),
    email VARCHAR(150),
    mobile VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS jobs (
    job_id INT AUTO_INCREMENT PRIMARY KEY,
    company_id INT NOT NULL,
    job_title VARCHAR(150) NOT NULL,
    technology VARCHAR(100),
    openings INT NOT NULL,
    location VARCHAR(150),
    package_lpa DECIMAL(10,2),
    min_percentage DECIMAL(5,2),
    passing_year INT,
    max_backlogs INT,
    deadline DATE,
    status VARCHAR(20) DEFAULT 'OPEN',
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);

CREATE TABLE IF NOT EXISTS applications (
    application_id INT AUTO_INCREMENT PRIMARY KEY,
    candidate_id INT NOT NULL,
    job_id INT NOT NULL,
    application_date DATE NOT NULL,
    status VARCHAR(30) DEFAULT 'APPLIED',
    UNIQUE(candidate_id, job_id),
    FOREIGN KEY (candidate_id) REFERENCES candidates(candidate_id),
    FOREIGN KEY (job_id) REFERENCES jobs(job_id)
);

CREATE TABLE IF NOT EXISTS interviews (
    interview_id INT AUTO_INCREMENT PRIMARY KEY,
    application_id INT NOT NULL,
    round_name VARCHAR(100),
    interview_date DATETIME,
    mode VARCHAR(30),
    interviewer VARCHAR(100),
    technical_rating INT,
    communication_rating INT,
    remarks TEXT,
    result VARCHAR(30),
    status VARCHAR(30),
    FOREIGN KEY (application_id) REFERENCES applications(application_id)
);

CREATE TABLE IF NOT EXISTS offers (
    offer_id INT AUTO_INCREMENT PRIMARY KEY,
    application_id INT NOT NULL UNIQUE,
    designation VARCHAR(100),
    package_lpa DECIMAL(10,2),
    offer_date DATE,
    joining_date DATE,
    offer_status VARCHAR(30),
    FOREIGN KEY (application_id) REFERENCES applications(application_id)
);

CREATE TABLE IF NOT EXISTS placements (
    placement_id INT AUTO_INCREMENT PRIMARY KEY,
    candidate_id INT NOT NULL,
    company_id INT NOT NULL,
    designation VARCHAR(100),
    final_package DECIMAL(10,2),
    actual_joining_date DATE,
    joining_status VARCHAR(30),
    FOREIGN KEY (candidate_id) REFERENCES candidates(candidate_id),
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);
