CREATE TABLE IF NOT EXISTS hr_employee (
    employee_id TEXT PRIMARY KEY,
    age INTEGER,
    department TEXT,
    job_role TEXT,
    monthly_income NUMERIC(10,2),
    years_at_company INTEGER,
    overtime TEXT,
    job_satisfaction INTEGER,
    attrition TEXT
);

-- Load with psql, adjusting path:
-- \copy hr_employee FROM '/absolute/path/hr_sample.csv' WITH (FORMAT csv, HEADER true);

-- Overall attrition
SELECT COUNT(*) AS employees,
       SUM(CASE WHEN attrition='Yes' THEN 1 ELSE 0 END) AS employees_left,
       ROUND(100.0 * SUM(CASE WHEN attrition='Yes' THEN 1 ELSE 0 END)
             / NULLIF(COUNT(*),0), 2) AS attrition_rate_pct
FROM hr_employee;

-- Attrition by department
SELECT department, COUNT(*) AS employees,
       SUM(CASE WHEN attrition='Yes' THEN 1 ELSE 0 END) AS employees_left,
       ROUND(100.0 * SUM(CASE WHEN attrition='Yes' THEN 1 ELSE 0 END)
             / NULLIF(COUNT(*),0), 2) AS attrition_rate_pct
FROM hr_employee GROUP BY department ORDER BY attrition_rate_pct DESC;

-- Compare overtime groups
SELECT overtime, COUNT(*) AS employees,
       ROUND(100.0 * SUM(CASE WHEN attrition='Yes' THEN 1 ELSE 0 END)
             / NULLIF(COUNT(*),0), 2) AS attrition_rate_pct
FROM hr_employee GROUP BY overtime;
