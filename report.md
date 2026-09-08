# Assignment -1
## To-Do List Management System

**Student:** ____________________  
**Date:** ____________________  
**GitHub Repository:** [Paste repository URL here]

## 1. Project Overview

Taskline is a browser-based To-Do List Management System. Users can add tasks, mark tasks completed, filter tasks, delete tasks, and see completion progress.

## 2. Jira Scrum Project

### User stories

- **Add Task:** As a user, I want to add a new task to my To-Do List so that I can keep track of my work.
- **Complete Task:** As a user, I want to mark a task as completed so that I can identify the tasks I have finished.

**Sprint:** To-Do Sprint 1  
**Workflow:** To Do -> In Progress -> Done

### Evidence

_Insert the Jira project screenshot here._  
**Explanation:** This screenshot shows the Scrum project created in Jira and its project navigation. It confirms that the assignment is organized using a Scrum project.

_Insert the Product Backlog screenshot here._  
**Explanation:** The Product Backlog contains the two requested user stories: adding a task and completing a task.

_Insert the Sprint Backlog screenshot here._  
**Explanation:** Both user stories have been moved from the Product Backlog into To-Do Sprint 1.

_Insert the started sprint screenshot here._  
**Explanation:** The sprint is active and the stories are ready to be worked on.

_Insert the In Progress screenshot here._  
**Explanation:** The story statuses show the transition from To Do to In Progress during sprint execution.

_Insert the Done screenshot here._  
**Explanation:** Both stories are marked Done, completing the requested Jira workflow.

## 3. Git Operations

| Command | Purpose |
|---|---|
| `git init` | Initializes a new local Git repository. |
| `git status` | Displays the current working-tree state. |
| `git add .` | Stages all project files for commit. |
| `git commit -m "Initial commit"` | Records the staged files in repository history. |
| `git branch feature-task` | Creates a feature branch. |
| `git checkout feature-task` | Switches to the feature branch. |
| `git checkout main` | Switches back to the main branch. |
| `git merge feature-task` | Merges the feature branch into main. |
| `git remote add origin <GitHub-URL>` | Connects the local repository to GitHub. |
| `git push -u origin main` | Publishes the main branch and sets its upstream. |

### Evidence

_Insert terminal screenshot: git init._  
**Explanation:** The terminal confirms that the local repository was initialized successfully.

_Insert terminal screenshot: add and commit._  
**Explanation:** The project files were staged and recorded in the initial commit.

_Insert terminal screenshot: branch creation._  
**Explanation:** The feature-task branch was created and checked out for isolated work.

_Insert terminal screenshot: merge._  
**Explanation:** The feature branch was merged into main, bringing its changes into the main line.

_Insert GitHub repository screenshot._  
**Explanation:** The GitHub website displays the published repository and its project files.

_Insert terminal screenshot: push._  
**Explanation:** The push output confirms that the local main branch was uploaded to GitHub.

## 4. GitHub Actions

The workflow file is `.github/workflows/workflow.yml`:

```yaml
name: Validate To-Do List

on:
  push:
    branches: [ main ]
  workflow_dispatch:

permissions:
  contents: read

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v4
      - name: Validate project files
        run: |
          test -f index.html
          test -f style.css
          test -f script.js
          grep -q "Taskline" index.html
          grep -q "taskForm" script.js
          echo "To-Do List project validation passed"
```

_Insert GitHub Actions YAML screenshot._  
**Explanation:** The workflow runs automatically on every push to main and also supports manual execution.

_Insert successful GitHub Actions run screenshot._  
**Explanation:** The green successful run confirms that GitHub checked out the repository and validated all required project files.

## 5. Conclusion

The To-Do List Management System was planned in Jira, implemented as a Git project, merged through a feature branch, published to GitHub, and verified automatically with GitHub Actions.
