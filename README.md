# User Import Script

A script that imports user data from CSV files into a SQLite database.
The script merges account information, associating password with the correct user, applies transformation and finally inserts or updates records. 

---

# Requirements

- Python 3.x
- uv package manager
- SQLite

---

# How to Run

```bash
python src/import_users.py \
  --users data/useraccounts.csv \
  --passwords data/passwords.csv \
  --emailsuffix "@clearcable.ca" \
  --accountprefix "001-"
```

OR

```bash
python src/import_users.py --users data/useraccounts.csv --passwords data/passwords.csv --emailsuffix "@clearcable.ca" --accountprefix "001-"
```

---

# Re-run Behavior

The script is safe to run multiple times. On each run:
- New users are created
- Existing users are updated
- No duplicates are created

---

# Assumptions

- This script is run in a fresh environment where the SQLite DB does not already exist.
Otherwise, schema mismatch issue like VARCHAR length constraint might appear.
- To avoid runtime schema migrations, the provided createUsersTable.sql file was updated to increase column lengths for username and emailaccount.
- Users without passwords are inserted with NULL password.
- Password records that do not match any username are ignored.
