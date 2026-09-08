from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image,
    PageBreak, Preformatted, KeepTogether
)

ROOT = Path(__file__).parent
OUT = ROOT / "Assignment-1-To-Do-List-Report.pdf"

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="ReportTitle", parent=styles["Title"], fontName="Helvetica-Bold",
    fontSize=24, leading=28, textColor=colors.HexColor("#176b65"),
    alignment=TA_CENTER, spaceAfter=6,
))
styles.add(ParagraphStyle(
    name="Subtitle", parent=styles["Normal"], fontSize=12, leading=16,
    textColor=colors.HexColor("#5c6b70"), alignment=TA_CENTER, spaceAfter=20,
))
styles.add(ParagraphStyle(
    name="Section", parent=styles["Heading2"], fontName="Helvetica-Bold",
    fontSize=16, leading=20, textColor=colors.HexColor("#176b65"),
    spaceBefore=18, spaceAfter=8,
))
styles.add(ParagraphStyle(
    name="Subsection", parent=styles["Heading3"], fontName="Helvetica-Bold",
    fontSize=12, leading=15, textColor=colors.HexColor("#df684c"),
    spaceBefore=10, spaceAfter=4,
))
styles.add(ParagraphStyle(
    name="Body", parent=styles["BodyText"], fontSize=9.5, leading=14,
    textColor=colors.HexColor("#26363d"), spaceAfter=6,
))
styles.add(ParagraphStyle(
    name="Small", parent=styles["BodyText"], fontSize=8, leading=11,
    textColor=colors.HexColor("#52636a"), spaceAfter=3,
))
styles.add(ParagraphStyle(
    name="Caption", parent=styles["BodyText"], fontName="Helvetica-Bold",
    fontSize=9, leading=12, textColor=colors.HexColor("#df684c"), spaceBefore=4,
))
styles.add(ParagraphStyle(
    name="CodeSmall", parent=styles["Code"], fontName="Courier",
    fontSize=7.2, leading=9.2, textColor=colors.HexColor("#e7f1ed"),
))


def P(text, style="Body"):
    return Paragraph(text, styles[style])


def evidence(image_name, title, explanation):
    image_path = ROOT / image_name
    image = Image(str(image_path), width=6.45 * inch, height=3.55 * inch)
    image.hAlign = "CENTER"
    card = [
        P(title, "Caption"),
        image,
        P(explanation, "Small"),
    ]
    return KeepTogether(card)


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#d9e3df"))
    canvas.line(42, 32, A4[0] - 42, 32)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#718086"))
    canvas.drawString(42, 20, "Daymark To-Do List | Assignment -1")
    canvas.drawRightString(A4[0] - 42, 20, f"Page {doc.page}")
    canvas.restoreState()


story = []
story.extend([
    Spacer(1, 34),
    P("Assignment -1", "ReportTitle"),
    P("To-Do List Management System", "Subtitle"),
])
meta = Table([
    [P("Student", "Small"), P("Kartik R Mahindrakar", "Small")],
    [P("Date", "Small"), P("8 September 2026", "Small")],
    [P("GitHub Repository", "Small"), P("https://github.com/kartikm95-2006/taskline-to-do-list", "Small")],
], colWidths=[1.45 * inch, 5.0 * inch])
meta.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#eef6f3")),
    ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor("#d0e1dc")),
    ("INNERGRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#d0e1dc")),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("LEFTPADDING", (0, 0), (-1, -1), 10),
    ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ("TOPPADDING", (0, 0), (-1, -1), 7),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
]))
story.extend([meta, Spacer(1, 14)])

story.extend([
    P("1. Project Overview", "Section"),
    P("Daymark is a browser-based To-Do List Management System. Users can add tasks, mark tasks completed, filter tasks, delete tasks, persist tasks in local storage, and see completion progress.", "Body"),
    P("Technology: HTML, CSS, JavaScript, browser localStorage, Git, GitHub, Jira, and GitHub Actions.", "Body"),
    P("2. Jira Scrum Project", "Section"),
    P("The Jira project is To-Do List Management System with project key TODO. The sprint is To-Do Sprint 1.", "Body"),
    P("User Stories", "Subsection"),
    P("1. Add Task: As a user, I want to add a new task to my To-Do List so that I can keep track of my work.", "Body"),
    P("2. Complete Task: As a user, I want to mark a task as completed so that I can identify the tasks I have finished.", "Body"),
    P("Jira execution: TODO-1 and TODO-2 were placed in the sprint and progressed through To Do, In Progress, and Done. The final sprint view shows both stories as Done and the separate backlog empty.", "Body"),
    evidence("jira-sprint-done.png", "Jira evidence: sprint and completed stories", "This screenshot shows the TODO project Backlog view, TODO Sprint 1, both stories, their green Done statuses, and an empty separate backlog. It verifies the Scrum sprint setup and final workflow result."),
    PageBreak(),
    P("3. Git Operations", "Section"),
    P("The local repository was initialized, the project files were committed, a feature branch was created and merged into main, and the result was pushed to GitHub.", "Body"),
])

commands = [
    [P("Command", "Small"), P("Purpose", "Small")],
    [P("git init", "Small"), P("Initializes a new local Git repository.", "Small")],
    [P("git status", "Small"), P("Displays the current working-tree state.", "Small")],
    [P("git add .", "Small"), P("Stages all project files for commit.", "Small")],
    [P('git commit -m "Initial commit"', "Small"), P("Records the staged files in repository history.", "Small")],
    [P("git branch feature-task", "Small"), P("Creates a feature branch.", "Small")],
    [P("git checkout feature-task", "Small"), P("Switches to the feature branch.", "Small")],
    [P("git checkout main", "Small"), P("Switches back to the main branch.", "Small")],
    [P("git merge feature-task", "Small"), P("Merges the feature branch into main.", "Small")],
    [P("git remote add origin <GitHub-URL>", "Small"), P("Connects the local repository to GitHub.", "Small")],
    [P("git push -u origin main", "Small"), P("Publishes main and sets its upstream branch.", "Small")],
]
command_table = Table(commands, colWidths=[2.55 * inch, 3.9 * inch], repeatRows=1)
command_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#176b65")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#c6d5d1")),
    ("INNERGRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#d8e1de")),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f3f8f6")]),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 7),
    ("RIGHTPADDING", (0, 0), (-1, -1), 7),
    ("TOPPADDING", (0, 0), (-1, -1), 5),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
]))
story.extend([command_table, Spacer(1, 12), evidence("terminal-evidence.png", "Terminal evidence: complete Git sequence", "This screenshot records git init, staging, the initial commit, feature branch creation, checkout, merge, remote configuration, and push. The final verification confirms main tracks origin/main and the working tree is clean."), PageBreak()])

story.extend([
    P("4. GitHub Repository", "Section"),
    P("The published repository is https://github.com/kartikm95-2006/taskline-to-do-list. The main branch contains the application, README, report, evidence, and workflow files.", "Body"),
    evidence("github-repository.png", "GitHub website evidence: published repository", "This screenshot shows the repository under the kartikm95-2006 account. It verifies that the project files and assignment report were published to GitHub."),
    P("5. Delivered Application", "Section"),
    evidence("taskline-app.png", "Application evidence: Daymark browser interface", "The application screenshot shows the delivered To-Do List interface with task entry, filtering controls, task count, and completion progress. It represents the working software built for the Jira stories."),
    PageBreak(),
    P("6. GitHub Actions", "Section"),
    P("The workflow file is .github/workflows/workflow.yml and runs automatically on every push to main. It checks out the repository and validates index.html, style.css, script.js, the Daymark title, and the task form.", "Body"),
])
yaml = """name: Validate To-Do List

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
          grep -q \"Daymark\" index.html
          grep -q \"taskForm\" script.js
          echo \"Daymark To-Do List project validation passed\"
"""
story.extend([Preformatted(yaml, styles["CodeSmall"]), Spacer(1, 10), evidence("github-actions-success.png", "GitHub Actions evidence: successful workflow runs", "The green checks show successful Validate To-Do List runs on main. The workflow executed after pushes and confirmed that the required project files and content are valid."), P("7. Conclusion", "Section"), P("The Daymark To-Do List Management System was planned in Jira, implemented as a functional web application, tracked through a Scrum sprint, managed with Git branches and commits, published to GitHub, and verified automatically with GitHub Actions. The repository link and evidence are included for submission.", "Body")])

doc = SimpleDocTemplate(str(OUT), pagesize=A4, rightMargin=42, leftMargin=42, topMargin=42, bottomMargin=44, title="Assignment -1 To-Do List Management System", author="Student")
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUT)
