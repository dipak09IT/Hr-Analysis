# Suggested Power BI measures

```DAX
Employees = DISTINCTCOUNT(hr_employee[employee_id])
Employees Left =
CALCULATE([Employees], hr_employee[attrition] = "Yes")
Attrition Rate % = DIVIDE([Employees Left], [Employees], 0)
Average Monthly Income = AVERAGE(hr_employee[monthly_income])
Average Tenure = AVERAGE(hr_employee[years_at_company])
```

Format `Attrition Rate %` as Percentage. Adjust the table name if needed.
