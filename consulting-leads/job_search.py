"""
Job Search Aggregator
Fetches healthcare IT consulting opportunities from multiple sources
"""

import urllib.request
import urllib.parse
import json
import webbrowser
from datetime import datetime

# Search URLs for healthcare IT consulting jobs
SEARCH_URLS = {
    "Upwork - Healthcare IT": "https://www.upwork.com/freelance-jobs/healthcare-information-technology/",
    "Upwork - EMR": "https://www.upwork.com/freelance-jobs/emr/",
    "ZipRecruiter - Cerner": "https://www.ziprecruiter.com/Jobs/Cerner-Consultant",
    "ZipRecruiter - EHR": "https://www.ziprecruiter.com/Jobs/Ehr-Consultant",
    "Dice - Cerner PowerChart": "https://www.dice.com/jobs/q-cerner+powerchart+analyst-jobs",
    "Dice - EHR": "https://www.dice.com/jobs/q-ehr-jobs",
    "Indeed - Remote EHR": "https://www.indeed.com/q-ehr-consultant-remote-jobs.html",
    "Glassdoor - Remote EHR": "https://www.glassdoor.com/Job/remote-ehr-consultant-jobs-SRCH_IL.0,6_IS11047_KO7,21.htm",
    "FlexJobs - Healthcare": "https://www.flexjobs.com/remote-jobs/healthcare-consultant",
    "SAM.gov - Federal Contracts": "https://sam.gov/search/?keywords=healthcare%20IT&sort=-relevance&index=opp&is_active=true",
    "Texas HHS - Procurement": "https://www.hhs.texas.gov/business/contracting-hhs/procurement-opportunities",
}

# LinkedIn search queries (opens in browser)
LINKEDIN_SEARCHES = {
    "Healthcare IT Consultant Texas": "https://www.linkedin.com/jobs/search/?keywords=healthcare%20IT%20consultant&location=Texas",
    "EHR Implementation Remote": "https://www.linkedin.com/jobs/search/?keywords=EHR%20implementation&f_WT=2",
    "Cerner Consultant Remote": "https://www.linkedin.com/jobs/search/?keywords=cerner%20consultant&f_WT=2",
}

# Email finder tools
EMAIL_TOOLS = {
    "Apollo.io": "https://www.apollo.io/email",
    "Hunter.io": "https://hunter.io",
    "Clearbit Connect": "https://connect.clearbit.com/",
}

def show_menu():
    print("\n" + "="*50)
    print("  HEALTHCARE IT CONSULTING JOB SEARCH")
    print("="*50)
    print("\n[Job Boards]")
    for i, (name, url) in enumerate(SEARCH_URLS.items(), 1):
        print(f"  {i}. {name}")

    print("\n[LinkedIn Searches]")
    offset = len(SEARCH_URLS)
    for i, (name, url) in enumerate(LINKEDIN_SEARCHES.items(), offset + 1):
        print(f"  {i}. {name}")

    print("\n[Email Finder Tools]")
    offset2 = offset + len(LINKEDIN_SEARCHES)
    for i, (name, url) in enumerate(EMAIL_TOOLS.items(), offset2 + 1):
        print(f"  {i}. {name}")

    print(f"\n  A. Open ALL job boards")
    print(f"  0. Exit")

def open_url(url, name):
    print(f"Opening: {name}")
    webbrowser.open(url)

def main():
    all_urls = {**SEARCH_URLS, **LINKEDIN_SEARCHES, **EMAIL_TOOLS}
    url_list = list(all_urls.items())

    while True:
        show_menu()
        choice = input("\nChoice: ").strip().upper()

        if choice == "0":
            print("\nGood luck with your search!")
            break
        elif choice == "A":
            print("\nOpening all job boards...")
            for name, url in SEARCH_URLS.items():
                open_url(url, name)
        else:
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(url_list):
                    name, url = url_list[idx]
                    open_url(url, name)
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Invalid choice.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║  Healthcare IT Consulting Job Search Tool                  ║
    ║                                                            ║
    ║  This tool opens job boards and lead-finding tools in      ║
    ║  your browser for healthcare IT consulting opportunities.  ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    main()
