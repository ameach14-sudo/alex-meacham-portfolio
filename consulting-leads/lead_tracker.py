"""
IT Consulting Lead Tracker
Tracks contacts, follow-ups, and outreach status
"""

import json
import os
from datetime import datetime, timedelta

LEADS_FILE = "leads.json"

def load_leads():
    if os.path.exists(LEADS_FILE):
        with open(LEADS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_leads(leads):
    with open(LEADS_FILE, 'w') as f:
        json.dump(leads, f, indent=2)

def add_lead():
    print("\n--- Add New Lead ---")
    lead = {
        "id": len(load_leads()) + 1,
        "company": input("Company name: "),
        "contact_name": input("Contact name (if known): ") or "Unknown",
        "contact_title": input("Contact title: ") or "IT Director",
        "email": input("Email (if known): ") or "",
        "linkedin": input("LinkedIn URL: ") or "",
        "source": input("Source (Upwork/LinkedIn/Apollo/etc): "),
        "status": "new",
        "notes": input("Notes: ") or "",
        "date_added": datetime.now().strftime("%Y-%m-%d"),
        "last_contact": None,
        "follow_up_date": None
    }

    leads = load_leads()
    leads.append(lead)
    save_leads(leads)
    print(f"\n✓ Added: {lead['company']}")

def list_leads(filter_status=None):
    leads = load_leads()
    if not leads:
        print("\nNo leads yet. Add some!")
        return

    if filter_status:
        leads = [l for l in leads if l['status'] == filter_status]

    print(f"\n{'ID':<4} {'Company':<25} {'Contact':<20} {'Status':<12} {'Follow-up':<12}")
    print("-" * 75)

    for lead in leads:
        follow_up = lead.get('follow_up_date', '-') or '-'
        print(f"{lead['id']:<4} {lead['company'][:24]:<25} {lead['contact_name'][:19]:<20} {lead['status']:<12} {follow_up:<12}")

def update_lead():
    list_leads()
    lead_id = int(input("\nEnter lead ID to update: "))

    leads = load_leads()
    lead = next((l for l in leads if l['id'] == lead_id), None)

    if not lead:
        print("Lead not found.")
        return

    print(f"\nUpdating: {lead['company']}")
    print("Status options: new, contacted, responded, meeting, proposal, won, lost, not_interested")

    new_status = input(f"New status [{lead['status']}]: ") or lead['status']
    lead['status'] = new_status

    if new_status == "contacted":
        lead['last_contact'] = datetime.now().strftime("%Y-%m-%d")
        days = input("Follow up in how many days? [7]: ") or "7"
        follow_up = datetime.now() + timedelta(days=int(days))
        lead['follow_up_date'] = follow_up.strftime("%Y-%m-%d")

    new_notes = input(f"Add notes: ")
    if new_notes:
        lead['notes'] = f"{lead['notes']}\n[{datetime.now().strftime('%Y-%m-%d')}] {new_notes}"

    save_leads(leads)
    print(f"\n✓ Updated: {lead['company']}")

def check_follow_ups():
    leads = load_leads()
    today = datetime.now().strftime("%Y-%m-%d")

    due = [l for l in leads if l.get('follow_up_date') and l['follow_up_date'] <= today and l['status'] not in ['won', 'lost', 'not_interested']]

    if not due:
        print("\n✓ No follow-ups due today!")
        return

    print(f"\n⚠ {len(due)} FOLLOW-UPS DUE:")
    print("-" * 50)
    for lead in due:
        print(f"  • {lead['company']} - {lead['contact_name']}")
        print(f"    Email: {lead.get('email', 'N/A')}")
        print(f"    Last contact: {lead.get('last_contact', 'Never')}")
        print()

def show_stats():
    leads = load_leads()
    if not leads:
        print("\nNo leads yet.")
        return

    statuses = {}
    for lead in leads:
        status = lead['status']
        statuses[status] = statuses.get(status, 0) + 1

    print("\n--- Pipeline Stats ---")
    for status, count in sorted(statuses.items()):
        print(f"  {status}: {count}")
    print(f"\n  Total: {len(leads)}")

def main():
    while True:
        print("\n" + "="*40)
        print("  IT CONSULTING LEAD TRACKER")
        print("="*40)
        print("1. Add new lead")
        print("2. List all leads")
        print("3. Update lead status")
        print("4. Check follow-ups due")
        print("5. Pipeline stats")
        print("6. List by status")
        print("0. Exit")

        choice = input("\nChoice: ")

        if choice == "1":
            add_lead()
        elif choice == "2":
            list_leads()
        elif choice == "3":
            update_lead()
        elif choice == "4":
            check_follow_ups()
        elif choice == "5":
            show_stats()
        elif choice == "6":
            status = input("Filter by status (new/contacted/responded/meeting/proposal/won/lost): ")
            list_leads(status)
        elif choice == "0":
            print("\nGood luck with your outreach!")
            break

if __name__ == "__main__":
    main()
