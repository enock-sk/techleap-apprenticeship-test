# Git Collaboration

To collaborate on a team project using Git, I follow these steps to ensure smooth teamwork and code management:

1. **Repository Setup**:
   - Initialize a repository or clone the project using `git clone <repo-url>`.
   - Create feature branches for each task (`git branch feature-name` and `git checkout feature-name`).

2. **Workflow**:
   - Pull the latest changes from the main branch (`git pull origin main`) to stay updated.
   - Commit changes frequently with clear messages (`git commit -m "Add user profile page"`).
   - Push feature branches to the remote repository (`git push origin feature-name`).
   - Create pull requests (PRs) on platforms like GitHub for code review.
   - Merge approved PRs into the main branch after resolving feedback.

3. **Collaboration Practices**:
   - Use descriptive branch names (e.g., `feature/login-page`).
   - Write clear commit messages and PR descriptions.
   - Regularly sync with the main branch to avoid conflicts.
   - Communicate with the team to coordinate changes and avoid duplicate work.

**Common Git Command**:
- `git pull`: I use `git pull origin main` frequently to fetch and merge the latest changes from the main branch, ensuring my local branch is up-to-date before starting new work.

**Problem Faced and Solution**:
- **Problem**: Merge conflicts when integrating my feature branch with the main branch, caused by multiple developers editing the same file.
- **Solution**: 
  - Ran `git pull origin main` to get the latest changes.
  - Used a code editor or `git mergetool` to manually resolve conflicts by reviewing both versions and keeping the intended changes.
  - Tested the resolved code to ensure functionality.
  - Committed the resolved changes (`git commit`) and pushed the branch.
  - To prevent future conflicts, I now pull frequently and communicate with teammates about overlapping changes.