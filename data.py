# Table to hold users, creation datte
import pandas as pd


users_df = pd.DataFrame(
    columns=[
        "user_id",
        "name",
        "email",
        "is_active"
    ]
)

otc_df = pd.DataFrame(
    columns=[
        "otc_id",
        "user_id",
        "otc_hash",
        "expires_at",
        "used_at"
    ]
)

