import data


def add_user(users_df, name, email):

    if email in users_df["email"].values:
        return users_df, False

    new_user = {
        "user_id": len(users_df) + 1,
        "name": name,
        "email": email,
        "is_active": True
    }

    users_df.loc[len(users_df)] = new_user

    return users_df, True
