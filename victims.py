#!/usr/bin/env python3
"""
Shooting Victims Data Mediator
A script to manage the victims.json file with duplicate checking and validation.
"""

import json
import os
import sys
from datetime import datetime
import argparse


class VictimsManager:
    def __init__(self, json_file_path="src/assets/victims.json"):
        self.json_file_path = json_file_path
        self.victims = []
        self.load_victims()

    def load_victims(self):
        """Load victims from JSON file"""
        try:
            if os.path.exists(self.json_file_path):
                with open(self.json_file_path, 'r', encoding='utf-8') as file:
                    self.victims = json.load(file)
                self.sort_victims_by_date()
            else:
                print(f"Warning: {self.json_file_path} not found. Starting with empty list.")
                self.victims = []
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON in {self.json_file_path}: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Error loading victims file: {e}")
            sys.exit(1)

    def sort_victims_by_date(self):
        """Sort victims by date of death (most recent first - newest to oldest)"""
        def parse_date(victim):
            try:
                return datetime.strptime(victim.get('dateOfDeath', '1900-01-01'), '%Y-%m-%d')
            except ValueError:
                # Put invalid dates at the end
                return datetime.strptime('1900-01-01', '%Y-%m-%d')
        
        self.victims.sort(key=parse_date, reverse=True)

    def save_victims(self):
        """Save victims to JSON file"""
        try:
            # Ensure directory exists
            os.makedirs(os.path.dirname(self.json_file_path), exist_ok=True)
            
            with open(self.json_file_path, 'w', encoding='utf-8') as file:
                json.dump(self.victims, file, indent=2, ensure_ascii=False)
            print(f"✓ Victims data saved to {self.json_file_path}")
        except Exception as e:
            print(f"Error saving victims file: {e}")
            sys.exit(1)

    def validate_date(self, date_string):
        """Validate date format (YYYY-MM-DD)"""
        try:
            datetime.strptime(date_string, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def victim_exists(self, firstname, lastname, date_of_death):
        """Check if a victim with identical data already exists"""
        for victim in self.victims:
            if (victim.get('firstname', '').lower() == firstname.lower() and
                victim.get('lastname', '').lower() == lastname.lower() and
                victim.get('dateOfDeath') == date_of_death):
                return True
        return False

    def add_victim(self, firstname, lastname, date_of_death):
        """Add a new victim with duplicate checking"""
        # Validate inputs
        if not firstname or not lastname or not date_of_death:
            print("Error: All fields (firstname, lastname, dateOfDeath) are required")
            return False

        # Validate date format
        if not self.validate_date(date_of_death):
            print("Error: Date must be in YYYY-MM-DD format")
            return False

        # Check for duplicates
        if self.victim_exists(firstname, lastname, date_of_death):
            print(f"Error: Victim '{firstname} {lastname}' with date '{date_of_death}' already exists")
            return False

        # Add new victim
        new_victim = {
            "firstname": firstname.strip(),
            "lastname": lastname.strip(),
            "dateOfDeath": date_of_death
        }

        self.victims.append(new_victim)
        self.sort_victims_by_date()
        self.save_victims()
        print(f"✓ Added victim: {firstname} {lastname} - {date_of_death}")
        return True

    def list_victims(self):
        """List all victims"""
        if not self.victims:
            print("No victims found.")
            return

        print(f"\nTotal victims: {len(self.victims)}")
        print("-" * 50)
        for i, victim in enumerate(self.victims, 1):
            firstname = victim.get('firstname', 'Unknown')
            lastname = victim.get('lastname', 'Unknown')
            date_of_death = victim.get('dateOfDeath', 'Unknown')
            print(f"{i:3d}. {firstname} {lastname} - {date_of_death}")

    def remove_victim(self, firstname, lastname, date_of_death):
        """Remove a victim by exact match"""
        for i, victim in enumerate(self.victims):
            if (victim.get('firstname', '').lower() == firstname.lower() and
                victim.get('lastname', '').lower() == lastname.lower() and
                victim.get('dateOfDeath') == date_of_death):
                removed = self.victims.pop(i)
                self.save_victims()
                print(f"✓ Removed victim: {removed['firstname']} {removed['lastname']} - {removed['dateOfDeath']}")
                return True
        
        print(f"Error: Victim '{firstname} {lastname}' with date '{date_of_death}' not found")
        return False


def main():
    parser = argparse.ArgumentParser(description='Manage shooting victims data')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new victim')
    add_parser.add_argument('firstname', help='First name of the victim')
    add_parser.add_argument('lastname', help='Last name of the victim')
    add_parser.add_argument('date', help='Date of death (YYYY-MM-DD)')

    # List command
    list_parser = subparsers.add_parser('list', help='List all victims')

    # Remove command
    remove_parser = subparsers.add_parser('remove', help='Remove a victim')
    remove_parser.add_argument('firstname', help='First name of the victim')
    remove_parser.add_argument('lastname', help='Last name of the victim')
    remove_parser.add_argument('date', help='Date of death (YYYY-MM-DD)')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    manager = VictimsManager()

    if args.command == 'add':
        manager.add_victim(args.firstname, args.lastname, args.date)
    elif args.command == 'list':
        manager.list_victims()
    elif args.command == 'remove':
        manager.remove_victim(args.firstname, args.lastname, args.date)


if __name__ == "__main__":
    main()