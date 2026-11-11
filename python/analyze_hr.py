from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "data" / "hr_sample.csv")
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

required = {"employee_id", "department", "job_role", "monthly_income", "years_at_company", "overtime", "job_satisfaction", "attrition"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Missing required columns: {sorted(missing)}")

print("Rows, columns:", df.shape)
print("Duplicate employee IDs:", df["employee_id"].duplicated().sum())
print("Missing values:\n", df.isna().sum())
left = (df["attrition"] == "Yes").sum()
print("Employees:", len(df), "| Left:", left, "| Attrition rate (%):", round(100*left/len(df), 2))

df["left_flag"] = (df["attrition"] == "Yes").astype(int)
for col in ["department", "job_role", "overtime", "job_satisfaction"]:
    summary = df.groupby(col, as_index=False).agg(employees=("employee_id", "count"), employees_left=("left_flag", "sum"))
    summary["attrition_rate_pct"] = (100 * summary["employees_left"] / summary["employees"]).round(2)
    summary.to_csv(OUT / f"attrition_by_{col}.csv", index=False)

df["tenure_group"] = pd.cut(df["years_at_company"], bins=[-1,1,3,5,10,30], labels=["0-1","2-3","4-5","6-10","11+"])
summary = df.groupby("tenure_group", observed=False).agg(employees=("employee_id","count"), employees_left=("left_flag","sum")).reset_index()
summary["attrition_rate_pct"] = (100*summary["employees_left"]/summary["employees"].replace(0, pd.NA)).round(2)
summary.to_csv(OUT / "attrition_by_tenure.csv", index=False)
print(f"Summary files saved to {OUT}")
