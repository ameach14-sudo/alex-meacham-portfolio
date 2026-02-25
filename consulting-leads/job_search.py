"""
IT Consulting Job Search Tool
Opens job boards for ServiceNow, Citrix, Documentation, and Help Desk consulting
"""

import webbrowser

# Search URLs organized by category
SERVICENOW_JOBS = {
    "Indeed - ServiceNow Remote": "https://www.indeed.com/q-servicenow-consultant-remote-jobs.html",
    "Upwork - ServiceNow": "https://www.upwork.com/freelance-jobs/servicenow/",
    "Arc.dev - ServiceNow": "https://arc.dev/remote-jobs/servicenow",
    "Jobgether - ServiceNow Remote": "https://jobgether.com/remote-jobs/servicenow",
}

CITRIX_VDI_JOBS = {
    "ZipRecruiter - Citrix": "https://www.ziprecruiter.com/Jobs/Citrix",
    "Upwork - Citrix": "https://www.upwork.com/freelance-jobs/citrix/",
    "Dice - Citrix": "https://www.dice.com/jobs/q-citrix-jobs",
    "Guru - Citrix Engineers": "https://www.guru.com/m/hire/freelancers/citrix/",
}

DOCUMENTATION_JOBS = {
    "Upwork - Technical Documentation": "https://www.upwork.com/freelance-jobs/technical-documentation/",
    "Upwork - Tech Doc Writers": "https://www.upwork.com/hire/technical-documentation-writers/",
    "ZipRecruiter - SOP Writer": "https://www.ziprecruiter.com/Jobs/Freelance-Sop-Technical-Writer",
    "Fiverr - SOP Writing": "https://www.fiverr.com/gigs/sop-writing",
    "Indeed - Knowledge Base": "https://www.indeed.com/q-knowledge-base-specialists-l-remote-jobs.html",
}

HELPDESK_JOBS = {
    "Upwork - Helpdesk": "https://www.upwork.com/freelance-jobs/helpdesk-support/",
    "Upwork - IT Consultants": "https://www.upwork.com/hire/it-consultants/",
    "Fiverr - IT Help Desk": "https://www.fiverr.com/hire/it-help-desk",
    "ZipRecruiter - IT Consultant": "https://www.ziprecruiter.com/n/Freelance-It-Consultant-Jobs-Near-Me",
}

FEDERAL_CONTRACTS = {
    "SAM.gov - IT Contracts": "https://sam.gov/search/?keywords=IT%20support&sort=-relevance&index=opp&is_active=true",
    "SAM.gov - Documentation": "https://sam.gov/search/?keywords=technical%20documentation&sort=-relevance&index=opp&is_active=true",
}

LINKEDIN_SEARCHES = {
    "LinkedIn - ServiceNow Remote": "https://www.linkedin.com/jobs/search/?keywords=servicenow%20consultant&f_WT=2",
    "LinkedIn - Citrix Remote": "https://www.linkedin.com/jobs/search/?keywords=citrix%20consultant&f_WT=2",
    "LinkedIn - IT Documentation": "https://www.linkedin.com/jobs/search/?keywords=IT%20documentation%20consultant&f_WT=2",
    "LinkedIn - IT Consultant Texas": "https://www.linkedin.com/jobs/search/?keywords=IT%20consultant&location=Texas",
}

EMAIL_TOOLS = {
    "Apollo.io - Email Finder": "https://www.apollo.io/email",
    "Hunter.io": "https://hunter.io",
}

ALL_CATEGORIES = {
    "ServiceNow": SERVICENOW_JOBS,
    "Citrix/VDI": CITRIX_VDI_JOBS,
    "Documentation/SOP": DOCUMENTATION_JOBS,
    "Help Desk/IT Consulting": HELPDESK_JOBS,
    "Federal Contracts": FEDERAL_CONTRACTS,
    "LinkedIn": LINKEDIN_SEARCHES,
    "Email Tools": EMAIL_TOOLS,
}

def show_menu():
    print("\n" + "="*55)
    print("  IT CONSULTING JOB SEARCH")
    print("="*55)

    idx = 1
    index_map = {}

    for category, jobs in ALL_CATEGORIES.items():
        print(f"\n[{category}]")
        for name, url in jobs.items():
            print(f"  {idx}. {name}")
            index_map[idx] = (name, url)
            idx += 1

    print(f"\n  S. Open all ServiceNow jobs")
    print(f"  C. Open all Citrix jobs")
    print(f"  D. Open all Documentation jobs")
    print(f"  H. Open all Help Desk jobs")
    print(f"  A. Open ALL job boards")
    print(f"  0. Exit")

    return index_map

def open_url(url, name):
    print(f"  Opening: {name}")
    webbrowser.open(url)

def open_category(category_dict):
    for name, url in category_dict.items():
        open_url(url, name)

def main():
    print("""
    ╔════════════════════════════════════════════════════════════╗
    ║  IT Consulting Job Search Tool                              ║
    ║                                                             ║
    ║  Categories: ServiceNow, Citrix/VDI, Documentation,         ║
    ║  Help Desk Optimization, Federal Contracts                  ║
    ╚════════════════════════════════════════════════════════════╝
    """)

    while True:
        index_map = show_menu()
        choice = input("\nChoice: ").strip().upper()

        if choice == "0":
            print("\nGood luck with your search!")
            break
        elif choice == "S":
            print("\nOpening ServiceNow jobs...")
            open_category(SERVICENOW_JOBS)
        elif choice == "C":
            print("\nOpening Citrix jobs...")
            open_category(CITRIX_VDI_JOBS)
        elif choice == "D":
            print("\nOpening Documentation jobs...")
            open_category(DOCUMENTATION_JOBS)
        elif choice == "H":
            print("\nOpening Help Desk jobs...")
            open_category(HELPDESK_JOBS)
        elif choice == "A":
            print("\nOpening all job boards...")
            for category_dict in [SERVICENOW_JOBS, CITRIX_VDI_JOBS, DOCUMENTATION_JOBS, HELPDESK_JOBS]:
                open_category(category_dict)
        else:
            try:
                idx = int(choice)
                if idx in index_map:
                    name, url = index_map[idx]
                    open_url(url, name)
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Invalid choice.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
