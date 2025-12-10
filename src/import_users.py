#!/usr/bin/env python3

import argparse
import os
import sys

def validate_file(path, label):
    """Ensure file exists"""
    if not os.path.exists(path):
        print(f"Error: {label} file not found at '{path}'")
        sys.exit(1)


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


if __name__ == "__main__":
    main()
