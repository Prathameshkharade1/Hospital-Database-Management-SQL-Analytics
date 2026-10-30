from data import load_data

def clean_df():
    df = load_data()

    # Fill missing values
    df["total_icu_los_days"] = df["total_icu_los_days"].fillna(0)

    df["lab_mean_value"] = df["lab_mean_value"].fillna(
        df["lab_mean_value"].mean()
    )
    df["lab_min_value"] = df["lab_min_value"].fillna(
        df["lab_min_value"].mean()
    )
    df["lab_max_value"] = df["lab_max_value"].fillna(
        df["lab_max_value"].mean()
    )

    # Drop columns
    df = df.drop(columns=[
        "total_input_amount",
        "total_output_value",
        "lab_distinct_tests",
        "lab_abnormal_range_count",
        "distinct_drug_count",
        "admission_type",
        "admission_location",
        "insurance",
        "marital_status",
        "race",
        "min_icu_los_days"
    ])

    return df


df_clean = clean_df()

print(df_clean.isnull().sum())
print(df_clean.head())