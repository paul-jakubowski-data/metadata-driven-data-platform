import pandas as pd


def run_validations(df: pd.DataFrame) -> pd.DataFrame:
    results = []

    results.append({
        "check_name": "order_id_not_null",
        "status": "PASS" if df["order_id"].notna().all() else "FAIL"
    })

    results.append({
        "check_name": "customer_id_not_null",
        "status": "PASS" if df["customer_id"].notna().all() else "FAIL"
    })

    results.append({
        "check_name": "sales_amount_positive",
        "status": "PASS" if (df["sales_amount"] > 0).all() else "FAIL"
    })

    results.append({
        "check_name": "order_id_unique",
        "status": "PASS" if df["order_id"].is_unique else "FAIL"
    })

    return pd.DataFrame(results)