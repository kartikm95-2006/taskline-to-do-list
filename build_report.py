from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image as PILImage
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image,
    PageBreak, Preformatted, KeepTogether
)

ROOT = Path(__file__).parent
OUT = ROOT / "Assignment-1-To-Do-List-Report.pdf"

pdfmetrics.registerFont(TTFont("Arial", r"C:\Windows\Fonts\arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", r"C:\Windows\Fonts\arialbd.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Italic", r"C:\Windows\Fonts\ariali.ttf"))
pdfmetrics.registerFont(TTFont("Georgia", r"C:\Windows\Fonts\georgia.ttf"))
pdfmetrics.registerFont(TTFont("Georgia-Bold", r"C:\Windows\Fonts\georgiab.ttf"))
pdfmetrics.registerFont(TTFont("Georgia-Italic", r"C:\Windows\Fonts\georgiai.ttf"))

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="ReportTitle", parent=styles["Title"], fontName="Georgia-Bold",
    fontSize=24, leading=28, textColor=colors.HexColor("#e86950"),
    alignment=TA_CENTER, spaceAfter=6,
))
styles.add(ParagraphStyle(
    name="Subtitle", parent=styles["Normal"], fontName="Georgia-Italic", fontSize=12, leading=16,
    textColor=colors.HexColor("#e86950"), alignment=TA_CENTER, spaceAfter=20,
))
styles.add(ParagraphStyle(
    name="Section", parent=styles["Heading2"], fontName="Georgia",
    fontSize=16, leading=20, textColor=colors.HexColor("#df684c"),
    spaceBefore=18, spaceAfter=8,
))
styles.add(ParagraphStyle(
    name="Subsection", parent=styles["Heading3"], fontName="Georgia",
    fontSize=12, leading=15, textColor=colors.HexColor("#df684c"),
    spaceBefore=10, spaceAfter=4,
))
styles.add(ParagraphStyle(
    name="Body", parent=styles["BodyText"], fontName="Georgia", fontSize=9.5, leading=14,
    textColor=colors.HexColor("#20302d"), spaceAfter=6,
))
styles.add(ParagraphStyle(
    name="Small", parent=styles["BodyText"], fontName="Georgia", fontSize=8, leading=11,
    textColor=colors.HexColor("#52636a"), spaceAfter=3,
))
styles.add(ParagraphStyle(
    name="Caption", parent=styles["BodyText"], fontName="Georgia-Bold",
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
    source_width, source_height = PILImage.open(image_path).size
    max_width, max_height = 6.45 * inch, 4.15 * inch
    scale = min(max_width / source_width, max_height / source_height)
    image = Image(str(image_path), width=source_width * scale, height=source_height * scale)
    image.hAlign = "CENTER"
    card = Table([[P(title, "Caption")], [image], [P(explanation, "Small")]], colWidths=[6.45 * inch])
    card.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f4f0e8")),
        ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor("#d9dfd8")),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    return KeepTogether([card])


def cover(canvas, doc):
    canvas.saveState()
    dark = colors.HexColor("#172724")
    coral = colors.HexColor("#e86950")
    canvas.setFillColor(dark)
    canvas.rect(42, 300, A4[0] - 84, 470, fill=1, stroke=0)
    canvas.setFillColor(coral)
    canvas.rect(42, 760, A4[0] - 84, 8, fill=1, stroke=0)
    canvas.setFillColor(coral)
    canvas.setFont("Arial-Bold", 8)
    canvas.drawString(78, 704, "SCRUM, GIT, GITHUB AND GITHUB ACTIONS")
    canvas.setFillColor(colors.HexColor("#f8f5ed"))
    canvas.setFont("Georgia", 29)
    canvas.drawString(78, 650, "To-Do List Management System")
    canvas.setFillColor(coral)
    canvas.setFont("Georgia-Italic", 28)
    canvas.drawString(78, 610, "Assignment Report")
    canvas.setFont("Arial-Bold", 8)
    canvas.setFillColor(colors.HexColor("#f8f5ed"))
    left_x, right_x = 78, 335
    rows = [("STUDENT", "Kartik R Mahindrakar", "PROJECT", "Daymark To-Do List Management System"),
            ("JIRA PROJECT", "To-Do List Management System (TODO)", "SPRINT", "To-Do Sprint 1"),
            ("GITHUB REPOSITORY", "github.com/kartikm95-2006/taskline-to-do-list", "PREPARED", "September 8, 2026")]
    y = 548
    for left_label, left_value, right_label, right_value in rows:
        canvas.setFont("Arial-Bold", 7)
        canvas.drawString(left_x, y, left_label)
        canvas.drawString(right_x, y, right_label)
        canvas.setFont("Georgia", 9)
        canvas.drawString(left_x, y - 15, left_value)
        canvas.drawString(right_x, y - 15, right_value)
        y -= 56
    canvas.restoreState()


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#d9e3df"))
    canvas.line(42, 32, A4[0] - 42, 32)
    canvas.setFont("Arial", 8)
    canvas.setFillColor(colors.HexColor("#718086"))
    canvas.drawString(42, 20, "Daymark To-Do List | Assignment -1")
    canvas.drawRightString(A4[0] - 42, 20, f"Page {doc.page}")
    canvas.restoreState()


story = [Spacer(1, 1), PageBreak()]

story.extend([
    P("1. Project Overview", "Section"),
    P("Daymark is a browser-based To-Do List Management System built with HTML, CSS, and JavaScript. It runs without package installation or a build step. Users can add tasks, mark tasks completed, filter tasks, delete tasks, view the current date, persist tasks in local storage, and see completion progress.", "Body"),
    P("Technology: HTML, CSS, JavaScript, browser localStorage, Git, GitHub, Jira, and GitHub Actions. The responsive interface is designed for desktop and mobile screens.", "Body"),
    P("2. Jira Scrum Project", "Section"),
    P("The Jira project is To-Do List Management System with project key TODO. The sprint is To-Do Sprint 1.", "Body"),
    P("User Stories", "Subsection"),
    P("1. Add Task: As a user, I want to add a new task to my To-Do List so that I can keep track of my work.", "Body"),
    P("2. Complete Task: As a user, I want to mark a task as completed so that I can identify the tasks I have finished.", "Body"),
    P("Jira execution: TODO-1 and TODO-2 were placed in the sprint and progressed through To Do, In Progress, and Done. The final sprint view shows both stories as Done and the separate backlog empty.", "Body"),
    evidence("jira-sprint-done.png", "Jira evidence: sprint and completed stories", "This screenshot shows the TODO project Backlog view, TODO Sprint 1, both stories, their green Done statuses, and an empty separate backlog. It verifies the Scrum sprint setup and final workflow result."),
    P("3. Sprint Planning and Execution", "Section"),
    P("Both stories were assigned to To-Do Sprint 1 before execution. The sprint was started for the active two-week window, and each story was moved through To Do, In Progress, and Done. Jira's final sprint summary shows 0 items in To Do, 0 items in In Progress, and 2 items in Done.", "Body"),
    P("Status-history evidence: Jira records the stories being assigned to the sprint and progressing from To Do to In Progress and then to Done. The captured final board is the visible completion evidence for this sequence.", "Body"),
    P("4. Git Repository and Operations", "Section"),
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
    [P("git remote -v", "Small"), P("Displays the configured fetch and push URLs.", "Small")],
    [P("git log --oneline --decorate -3", "Small"), P("Shows the latest commits and branch references.", "Small")],
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
    P("5. GitHub Repository", "Section"),
    P("The published repository is https://github.com/kartikm95-2006/taskline-to-do-list. The main branch contains the application, README, report, evidence, and workflow files.", "Body"),
    evidence("github-repository.png", "GitHub website evidence: published repository", "This screenshot shows the repository under the kartikm95-2006 account. It verifies that the project files and assignment report were published to GitHub."),
    P("6. Delivered Application", "Section"),
    evidence("taskline-app.png", "Application evidence: Daymark browser interface", "The application screenshot displays two assignment-related open tasks and reports 2 tasks. This confirms that client-side task creation, persistence, filtering, and open-task counting are functioning."),
    PageBreak(),
        P("7. GitHub Actions", "Section"),
        P("The workflow file is .github/workflows/workflow.yml and runs automatically on pushes to main and pull requests targeting main. It also supports manual execution. The validation job checks index.html, style.css, script.js, the Daymark title, and the task form.", "Body"),
])
yaml = """name: Daymark To-Do List CI

on:
  push:
    branches: [ main ]
    pull_request:
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
          echo \"Daymark To-Do List project files validated successfully\"
"""
story.extend([Preformatted(yaml, styles["CodeSmall"]), Spacer(1, 10), evidence("github-actions-success.png", "GitHub Actions evidence: successful workflow runs", "The green checks show successful Daymark To-Do List CI runs on main. The workflow executes after pushes and is configured to validate pull requests targeting main as well."), P("8. Conclusion", "Section"), P("The Daymark To-Do List Management System was planned with two Jira Scrum stories, delivered through one sprint, versioned with Git, published to GitHub, and validated automatically with GitHub Actions. The repository link and evidence are included for submission.", "Body")])

doc = SimpleDocTemplate(str(OUT), pagesize=A4, rightMargin=42, leftMargin=42, topMargin=42, bottomMargin=44, title="Assignment -1 To-Do List Management System", author="Student")
doc.build(story, onFirstPage=cover, onLaterPages=footer)
print(OUT)
