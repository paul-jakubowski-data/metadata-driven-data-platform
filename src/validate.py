import pandas as pd


def run_validations(df: pd.DataFrame, config: dict) -> pd.DataFrame:
    """
    Run validation checks based on configuration rules.
    """
    results = []

    for rule in config["validation_rules"]:
        rule_name = rule["name"]
        column = rule["column"]
        rule_type = rule["rule"]

        try:
            if rule_type == "not_null":
                status = "PASS" if df[column].notna().all() else "FAIL"

            elif rule_type == "greater_than":
                value = rule["value"]
                status = "PASS" if (df[column] > value).all() else "FAIL"

            elif rule_type == "unique":
                status = "PASS" if df[column].is_unique else "FAIL"

            else:
                status = "UNKNOWN_RULE"

        except Exception as e:
            status = f"ERROR: {e}"

        results.append({
            "check_name": rule_name,
            "column": column,
            "rule": rule_type,
            "status": status
        })

    return pd.DataFrame(results)