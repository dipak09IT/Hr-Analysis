# 02 — HR Analytics: Employee Attrition

**Level:** Beginner | **Tools:** Python, PostgreSQL, Power BI / Excel

## Business question
How does the attrition rate differ by department, role, overtime, and tenure?

## Included files
- `data/hr_sample.csv`: generated synthetic demonstration data.
- `python/analyze_hr.py`: quality checks and group summaries.
- `sql/hr_analysis.sql`: PostgreSQL queries.
- `powerbi/DAX_MEASURES.md`: measures and dashboard ideas.

## Run
```bash
python -m pip install -r ../requirements.txt
python python/analyze_hr.py
```

## Dashboard ideas
Cards: employees, employees who left, attrition rate.
Charts: attrition rate by department, job role, overtime, and tenure group.
Slicers: department, role, overtime.

## Important limitations
This sample is generated for demonstration and is not real employee data. Even with real data, these comparisons show association, not proof that a factor caused attrition. Avoid drawing conclusions about individuals.
