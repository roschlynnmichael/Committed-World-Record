import subprocess

REPO_NAME = "world-record-attempt"
TOTAL_COMMITS = 3000001
PUSH_INTERVAL = 50000  # Push every 50k commits to avoid API timeouts

def create_empty_commits():
    # Initialize if needed
    subprocess.run(["git", "init", REPO_NAME])
    
    for i in range(1, TOTAL_COMMITS + 1):
        # The --allow-empty flag is the key here
        subprocess.run(
            ["git", "commit", "--allow-empty", "-m", f"Commit number {i}"],
            cwd=REPO_NAME,
            capture_output=True
        )
        
        # Incremental pushing to prevent the "Pack File" from getting too large
        if i % PUSH_INTERVAL == 0:
            print(f"Pushing batch at {i} commits...")
            subprocess.run(["git", "push", "origin", "main"], cwd=REPO_NAME)

if __name__ == "__main__":
    create_empty_commits()