import pygit2
import os
import time

# Ensure this script is inside your 'Committed-World-Record' folder
REPO_PATH = os.getcwd() 
GOAL = 3000005  # Surpassing the 3M mark
BATCH_SIZE = 100000 

def break_the_record():
    try:
        repo = pygit2.Repository(REPO_PATH)
        print(f"Targeting Repository: {REPO_PATH}")
        
        # Identity
        author = pygit2.Signature("Roschlynn Michael D'souza", "roschlynn@example.com")
        committer = author

        # Get the current branch and its latest commit
        head = repo.head
        target_branch = head.name # e.g., 'refs/heads/main'
        parent_id = [head.target]
        
        # We use the existing tree (no files changed = empty commits)
        tree = repo[head.target].tree.id

        print(f"Currently at {repo.revparse_single('HEAD').hex[:7]}. Starting sprint...")
        start_time = time.time()

        for i in range(1, GOAL + 1):
            # The Magic: Create commit and move the branch pointer in one go
            commit_id = repo.create_commit(
                target_branch, 
                author, 
                committer, 
                f"Commit {i}: World Record Progress", 
                tree, 
                parent_id
            )
            
            parent_id = [commit_id]

            if i % BATCH_SIZE == 0:
                elapsed = time.time() - start_time
                print(f"Progress: {i}/{GOAL} | Speed: {int(i/elapsed)} commits/sec")

        print(f"Sprint Complete! Total Time: {time.time() - start_time:.2f}s")

    except Exception as e:
        print(f"Critical Error: {e}")
        print("Check: Did you make at least one manual commit in this repo first?")

if __name__ == "__main__":
    break_the_record()