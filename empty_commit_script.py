import pygit2
import os
import time
import sys

def run_integrated_sprint():
    # 1. User Inputs
    try:
        goal = int(input("How many times do you want to commit? \n"))
        auto_push = input("Auto git push when committed? (y/n) \n").lower()
    except ValueError:
        print("Please enter a valid number.")
        return

    # 2. Setup High-Performance Engine
    repo_path = os.getcwd()
    try:
        repo = pygit2.Repository(repo_path)
    except:
        print("Error: Could not find a Git repository in this folder.")
        return

    # Identity
    author = pygit2.Signature("Roschlynn Michael Dsouza", "hidden@record-attempt.local")
    committer = author

    if repo.is_empty:
        print("Error: Repo is empty. Run 'git commit --allow-empty -m \"init\"' once first.")
        return

    # Branch and Tree Setup
    head = repo.head
    target_branch = head.name 
    parent_id = [head.target]
    tree_id = repo[head.target].tree.id

    print(f"\n[STARTING] Sprinting to {goal} commits on {repo_path}...")
    start_time = time.time()
    
    # 3. High-Speed Loop
    batch_size = 50000 if goal > 100000 else 1000
    
    for i in range(1, goal + 1):
        commit_id = repo.create_commit(
            target_branch,
            author,
            committer,
            f"Commit {i} of {goal}", 
            tree_id,
            parent_id
        )
        parent_id = [commit_id]

        if i % batch_size == 0:
            elapsed = time.time() - start_time
            speed = int(i / elapsed)
            sys.stdout.write(f"\rProgress: {i}/{goal} | Speed: {speed} commits/sec")
            sys.stdout.flush()

    end_time = time.time()
    print(f"\n\n[DONE] Committed {goal} times in {end_time - start_time:.2f}s")

    # 4. Auto-Push Logic (Optimized)
    if auto_push == "y":
        print("Running 'git gc' to optimize objects for network transfer...")
        os.system("git gc --auto") # Quick cleanup
        print("Pushing to GitHub...")
        os.system("git push origin main") 
        print("Push complete!")

if __name__ == "__main__":
    run_integrated_sprint()