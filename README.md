Testing email authentication in Streamlit
Using hashed one time code (OTC) method

Hold list of authenticated users in dataframe , validate against table
send otc to email, validate against hash of otc value in otc table (dataframe)
pass / fail to dummy homepage

flow: 

User enters email
       ↓
Look up user in users_df
       ↓
Generate 6-digit OTC
       ↓
Hash OTC
       ↓
Store hash in otc_df
       ↓
Email actual OTC to user
       ↓
User enters OTC
       ↓
Hash/verify against otc_df
       ↓
Check expiry + used status
       ↓
Login successful
