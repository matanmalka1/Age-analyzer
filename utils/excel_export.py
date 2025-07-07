import pandas as pd
import os

def export_to_excel(data: list, filename: str = "analysis.xlsx"):
    filename = os.path.join("data", filename)
    if not data:
        print("No data to export.")
        return

    all_data_df = pd.DataFrame(data)

    ages = [record["age"] for record in data if isinstance(record.get("age"), (int, float))]
    average = round(sum(ages) / len(ages), 2) if ages else 0
    summary_df = pd.DataFrame(
        {"Average Age": [average]},
        index=["Summary"]
    )
    print(summary_df)

    valid_records = [record for record in data if isinstance(record.get("age"), (int, float))]
    sorted_records = sorted(valid_records, key=lambda x: x["age"], reverse=True)
    sorted_df = pd.DataFrame(sorted_records)

    recent_records = data[-5:] if len(data) >= 5 else data
    recent_df = pd.DataFrame(recent_records)

    with pd.ExcelWriter(filename) as writer:
        all_data_df.to_excel(writer, sheet_name="All Data", index=False)
        summary_df.to_excel(writer, sheet_name="Summary", index=False)
        sorted_df.to_excel(writer, sheet_name="Sorted by Age", index=False)
        recent_df.to_excel(writer, sheet_name="Last 5 Entries", index=False)

    print(f" Analysis exported to {filename}")

