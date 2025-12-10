#!/usr/bin/env python3

import argparse
import os
import sys
import csv

def validate_file(path, label):
    """Ensure file exists"""
    if not os.path.exists(path):
        print(f"Error: {label} file not found at '{path}'")
        sys.exit(1)


def load_user_accounts(path):
    """Load user accounts csv into a dict"""

    accounts = {}

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        # Normalize headers
        reader.fieldnames = [name.strip() for name in reader.fieldnames]

        for row in reader:
            # Normalize row
            row = {k.strip(): v.strip() for k, v in row.items()}

            username = row["Username"].strip()

            accounts[username] = {
                "accountnumber": row["accountNumber"].strip(),
                "username": username,
                "phonenumber": row["phonenumber"].strip(),
                "address": row["address"].strip()
            }
    
    return accounts


def load_passwords(path):
    """Load passwords csv into a dict"""

    passwords = {}

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        # Normalize headers
        reader.fieldnames = [name.strip() for name in reader.fieldnames]

        for row in reader:
            # Normalize row
            row = {k.strip(): v.strip() for k, v in row.items()}

            username = row["Username"].strip()
            passwords[username] = row["Password"].strip()
    
    return passwords


def merge_user_data(accounts, passwords, email_suffix, account_prefix):
    """Merge account and password data into a final list"""

    final_users = []

    for username,data in accounts.items():
        password = passwords.get(username)

        # When account exists but password is missing
        if password is None:
            print(f"Warning: No password found for username '{username}'")

        record = {
            "accountnumber": f"{account_prefix}{data["accountnumber"]}",
            "username": username,
            "emailaccount": f"{data["username"]}{email_suffix}",
            "phonenumber": data["phonenumber"],
            "address": data["address"],
            "password": password
        }
    
        final_users.append(record)

    # When password exists but doesn't correspond to an account 
    for username in passwords:
        if username not in accounts:
            print(f"Warning: Password found for an unknown user '{username}'")

    return final_users


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--users",
        required=True
    )

    parser.add_argument(
        "--passwords",
        required=True
    )

    parser.add_argument(
        "--emailsuffix",
        required=True
    )

    parser.add_argument(
        "--accountprefix",
        required=True
    )

    args = parser.parse_args()

    validate_file(args.users, "User Accounts")
    validate_file(args.passwords, "Passwords")

    return args


def main():
    args = parse_arguments()

    print("Arguments parsed successfully:")
    print(f"  Users CSV      : {args.users}")
    print(f"  Passwords CSV  : {args.passwords}")
    print(f"  Email Suffix   : {args.emailsuffix}")
    print(f"  Account Prefix : {args.accountprefix}")

    accounts = load_user_accounts(args.users)
    passwords = load_passwords(args.passwords)

    print(f"Loaded {len(accounts)} user accounts")
    print(f"Loaded {len(passwords)} passwords")

    final_users = merge_user_data(accounts, passwords, args.emailsuffix, args.accountprefix)

    print(f"Final merged records: {len(final_users)} users")

if __name__ == "__main__":
    main()
