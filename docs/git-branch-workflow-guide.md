# Git Branch Workflow Guide

This guide explains the full process of working with Git branches, from
start to finish.

------------------------------------------------------------------------

## 🚀 Full Git Branch Workflow

### 1. Get the latest `main`

``` bash
git switch main
git pull origin main
```

------------------------------------------------------------------------

### 2. Create a new branch

``` bash
git switch -c feature/awesome-thing
```

✅ `feature/awesome-thing` is just an example. Use a descriptive name.

------------------------------------------------------------------------

### 3. Do your work

``` bash
# edit files...
git add .
git commit -m "Implement awesome thing"
```

------------------------------------------------------------------------

### 4. Push branch to remote

``` bash
git push -u origin feature/awesome-thing
```

-   Now your branch exists on GitHub/GitLab/etc.
-   You can create a draft PR or let CI start running.

------------------------------------------------------------------------

### 5. Keep your branch up to date with `main`

#### Merge method

``` bash
git switch main
git pull origin main
git switch feature/awesome-thing
git merge main        # resolve conflicts if any
git push              # update remote branch
```

#### Rebase method (cleaner history)

``` bash
git fetch origin
git rebase origin/main   # resolve conflicts, continue with: git rebase --continue
git push -f              # -f required after rebase
```

------------------------------------------------------------------------

### 6. Open a Pull Request (PR)

-   Go to your Git hosting service.
-   Open a PR from `feature/awesome-thing` → `main`.
-   CI/tests/reviews happen here.

------------------------------------------------------------------------

### 7. Update PR as needed

If `main` moves again while PR is open, repeat **step 5** and push again
so your PR stays current.

------------------------------------------------------------------------

### 8. Merge the PR

-   Once approved, merge via GitHub/GitLab UI.
-   Usually "Squash and merge" or "Rebase and merge" is used in modern
    repos.
-   After merge, many teams auto-delete the remote branch.

------------------------------------------------------------------------

### 9. Cleanup local branch

After merge:

``` bash
git switch main
git pull origin main             # get latest with your merged code
git branch -d feature/awesome-thing   # safe delete (works if merged)
git fetch --prune                 # remove deleted remote refs
```

If PR was closed without merging and you want to drop it:

``` bash
git branch -D feature/awesome-thing   # force delete
```

------------------------------------------------------------------------

## ✅ Summary Flow

1.  `git switch main && git pull`\
2.  `git switch -c feature/...`\
3.  work → commit\
4.  `git push -u origin feature/...`\
5.  **(repeat while branch is active)** sync with `main` → push again\
6.  Open PR\
7.  Merge PR\
8.  Cleanup local + prune remote
