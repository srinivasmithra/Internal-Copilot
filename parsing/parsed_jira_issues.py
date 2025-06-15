import os
import json



ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SOURCE_FILE = os.path.join(ROOT_DIR, 'mock_data/jira_issues/jira_issues.json')
OUTPUT_DIR = os.path.join(ROOT_DIR, 'processed_data/parsed_jira_issues')
os.makedirs(OUTPUT_DIR, exist_ok=True)


try:
    with open(SOURCE_FILE, 'r') as f:
        issues = json.load(f)

    for issue in issues:
        content = f"Ticket: {issue['ticket_id']}\nTitle: {issue['title']}\nDescription: {issue['description']}\nSubsystem: {issue['subsystem']}\nSeverity: {issue['severity']}"
        filename = os.path.join(OUTPUT_DIR, f"{issue['ticket_id']}.txt")
        with open(filename, 'w') as out_f:
            out_f.write(content)
except Exception as e:
    print(f"Error while processing jira issues: {str(e)}")
