def validate_schema(df, required_cols):
    return all(col in df.columns for col in required_cols)
