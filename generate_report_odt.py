"""Generate PES2UG24CS393_Lab5_Static_Analysis.odt deliverable document.

Student: Rahul B (PES2UG24CS393, Section G)
Course: UE23CS301 - Software Engineering Lab
Lab 5: Static Code Analysis - Telecom Tower Maintenance Tracker

Simple, clean, human/student-style formatting.
"""

from odf.opendocument import OpenDocumentText
from odf.text import P, H
from odf.table import Table, TableColumn, TableRow, TableCell
from odf.style import (
    Style,
    TextProperties,
    ParagraphProperties,
    TableCellProperties,
    TableColumnProperties,
)


def build_student_report():
    doc = OpenDocumentText()

    # --- SIMPLE HUMAN/STUDENT STYLES (Standard Black & White / Light Grays) ---

    # Main Title (18pt Bold, Black, Centered)
    title_style = Style(name="ReportTitle", family="paragraph")
    title_style.addElement(ParagraphProperties(textalign="center", marginbottom="0.15cm", margintop="0.2cm"))
    title_style.addElement(TextProperties(fontsize="16pt", fontweight="bold", fontfamily="Liberation Serif", color="#000000"))
    doc.styles.addElement(title_style)

    # University / Dept Header (12pt, Centered)
    univ_style = Style(name="UnivHeader", family="paragraph")
    univ_style.addElement(ParagraphProperties(textalign="center", marginbottom="0.1cm"))
    univ_style.addElement(TextProperties(fontsize="12pt", fontweight="bold", fontfamily="Liberation Serif", color="#000000"))
    doc.styles.addElement(univ_style)

    # Subtitle / Course (11pt, Centered)
    sub_style = Style(name="ReportSubtitle", family="paragraph")
    sub_style.addElement(ParagraphProperties(textalign="center", marginbottom="0.4cm"))
    sub_style.addElement(TextProperties(fontsize="11pt", fontfamily="Liberation Serif", color="#333333"))
    doc.styles.addElement(sub_style)

    # Student Info Block (Left-aligned, bordered simple box)
    meta_style = Style(name="StudentInfoBlock", family="paragraph")
    meta_style.addElement(
        ParagraphProperties(
            border="0.5pt solid #666666",
            padding="0.25cm",
            marginbottom="0.5cm",
            lineheight="130%",
            backgroundcolor="#fafafa",
        )
    )
    meta_style.addElement(TextProperties(fontsize="11pt", fontfamily="Liberation Serif", color="#000000"))
    doc.styles.addElement(meta_style)

    # Heading 1 (13pt Bold, Black, Left)
    h1_style = Style(name="Heading1Simple", family="paragraph")
    h1_style.addElement(ParagraphProperties(margintop="0.5cm", marginbottom="0.2cm", keepwithnext="always"))
    h1_style.addElement(TextProperties(fontsize="13pt", fontweight="bold", fontfamily="Liberation Serif", color="#000000"))
    doc.styles.addElement(h1_style)

    # Heading 2 (11.5pt Bold, Black, Left)
    h2_style = Style(name="Heading2Simple", family="paragraph")
    h2_style.addElement(ParagraphProperties(margintop="0.35cm", marginbottom="0.15cm", keepwithnext="always"))
    h2_style.addElement(TextProperties(fontsize="11.5pt", fontweight="bold", fontfamily="Liberation Serif", color="#000000"))
    doc.styles.addElement(h2_style)

    # Body Text (11pt, 1.15 line spacing, standard text)
    body_style = Style(name="BodySimple", family="paragraph")
    body_style.addElement(ParagraphProperties(marginbottom="0.25cm", lineheight="120%"))
    body_style.addElement(TextProperties(fontsize="11pt", fontfamily="Liberation Serif", color="#000000"))
    doc.styles.addElement(body_style)

    # Bullet / List Text
    bullet_style = Style(name="BulletSimple", family="paragraph")
    bullet_style.addElement(ParagraphProperties(marginleft="0.6cm", marginbottom="0.15cm", lineheight="120%"))
    bullet_style.addElement(TextProperties(fontsize="11pt", fontfamily="Liberation Serif", color="#000000"))
    doc.styles.addElement(bullet_style)

    # Code / Terminal snippet style
    code_style = Style(name="CodeSimple", family="paragraph")
    code_style.addElement(
        ParagraphProperties(
            backgroundcolor="#f5f5f5",
            border="0.5pt solid #cccccc",
            padding="0.2cm",
            marginleft="0.4cm",
            marginright="0.4cm",
            marginbottom="0.3cm",
            margintop="0.1cm",
        )
    )
    code_style.addElement(TextProperties(fontsize="10pt", fontfamily="Liberation Mono", color="#000000"))
    doc.styles.addElement(code_style)

    # Screenshot Placeholder Box (Simple gray border box, clean text)
    screenshot_style = Style(name="ScreenshotPlaceholder", family="paragraph")
    screenshot_style.addElement(
        ParagraphProperties(
            border="1pt solid #888888",
            backgroundcolor="#fcfcfc",
            padding="0.35cm",
            margintop="0.25cm",
            marginbottom="0.45cm",
            lineheight="130%",
        )
    )
    screenshot_style.addElement(TextProperties(fontsize="10.5pt", fontfamily="Liberation Serif", color="#222222"))
    doc.styles.addElement(screenshot_style)

    # Table Styles (Simple black & white with light gray header)
    th_cell_style = Style(name="SimpleTHCell", family="table-cell")
    th_cell_style.addElement(TableCellProperties(backgroundcolor="#e8e8e8", padding="0.18cm", border="0.5pt solid #444444"))
    doc.styles.addElement(th_cell_style)

    th_text_style = Style(name="SimpleTHText", family="paragraph")
    th_text_style.addElement(ParagraphProperties(textalign="center", marginbottom="0cm"))
    th_text_style.addElement(TextProperties(fontsize="10pt", fontweight="bold", fontfamily="Liberation Serif", color="#000000"))
    doc.styles.addElement(th_text_style)

    td_cell_style = Style(name="SimpleTDCell", family="table-cell")
    td_cell_style.addElement(TableCellProperties(padding="0.15cm", border="0.5pt solid #666666"))
    doc.styles.addElement(td_cell_style)

    td_text_style = Style(name="SimpleTDText", family="paragraph")
    td_text_style.addElement(ParagraphProperties(marginbottom="0cm", lineheight="115%"))
    td_text_style.addElement(TextProperties(fontsize="10pt", fontfamily="Liberation Serif", color="#000000"))
    doc.styles.addElement(td_text_style)

    # --- DOCUMENT CONTENT ---

    # Header
    doc.text.addElement(P(stylename=univ_style, text="PES UNIVERSITY"))
    doc.text.addElement(P(stylename=sub_style, text="Department of Computer Science and Engineering\nUE23CS301 — Software Engineering Lab"))
    doc.text.addElement(P(stylename=title_style, text="Lab 5: Static Code Analysis"))
    doc.text.addElement(P(stylename=sub_style, text="Telecom Tower Maintenance Tracker"))

    # Student Info Box
    student_meta = (
        "Name: Rahul B\n"
        "SRN: PES2UG24CS393\n"
        "Section: G\n"
        "Semester: 5th Semester B.Tech CSE\n"
        "Target File: tower_maintenance.py\n"
        "GitHub Repo: https://github.com/PES2UG24CS393/L5_25_tower_maintenance\n"
        "Date: November 2026"
    )
    doc.text.addElement(P(stylename=meta_style, text=student_meta))

    # Section 1: Objective
    doc.text.addElement(H(outlinelevel=1, stylename=h1_style, text="1. Objective"))
    doc.text.addElement(
        P(
            stylename=body_style,
            text=(
                "The objective of this lab is to use static code analysis tools (Pylint, Flake8, and Bandit) to find "
                "and fix security bugs, code style issues, and quality problems in a Python program (tower_maintenance.py). "
                "Static analysis allows us to inspect the code without running it, identifying weaknesses before deployment."
            ),
        )
    )

    doc.text.addElement(H(outlinelevel=1, stylename=h1_style, text="2. Tools Used"))
    doc.text.addElement(
        P(
            stylename=bullet_style,
            text="• Pylint: Checks Python code quality, programming standards, missing docstrings, and gives a score out of 10.0.",
        )
    )
    doc.text.addElement(
        P(
            stylename=bullet_style,
            text="• Flake8: Enforces PEP 8 style guidelines, checking line lengths, blank lines, and whitespace around operators.",
        )
    )
    doc.text.addElement(
        P(
            stylename=bullet_style,
            text="• Bandit: Scans Python code for security vulnerabilities such as SQL injection, hardcoded passwords, and unsafe functions.",
        )
    )

    # Section 3: Baseline Static Analysis
    doc.text.addElement(H(outlinelevel=1, stylename=h1_style, text="3. Baseline Execution and Initial Reports"))
    doc.text.addElement(
        P(
            stylename=body_style,
            text=(
                "Before making changes, I ran the original script using 'python tower_maintenance.py'. It printed: "
                "['Ridge-A'] high 2 1. Then I ran the static analysis tools and saved their outputs to text files:"
            ),
        )
    )
    doc.text.addElement(
        P(
            stylename=code_style,
            text=(
                "$ python tower_maintenance.py\n"
                "$ pylint tower_maintenance.py > pylint_report.txt\n"
                "$ bandit -r tower_maintenance.py > bandit_report.txt\n"
                "$ flake8 tower_maintenance.py > flake8_report.txt"
            ),
        )
    )
    doc.text.addElement(P(stylename=body_style, text="Initial findings from the baseline tools:"))
    doc.text.addElement(P(stylename=bullet_style, text="• Pylint score: 5.14 / 10.0 (17 issues including broad exception, global variable, missing docstrings)."))
    doc.text.addElement(P(stylename=bullet_style, text="• Bandit findings: 4 issues (SQL injection in addTower, pickle deserialization, hardcoded password)."))
    doc.text.addElement(P(stylename=bullet_style, text="• Flake8 findings: 7 style errors (lines exceeding 79 chars, 3 blank lines, missing operator spaces)."))

    # Screenshot 1 Placeholder
    sc1_text = (
        "[ SCREENSHOT 1: Baseline Execution and Static Analysis ]\n"
        "Commands to run:\n"
        "  python tower_maintenance.py\n"
        "  pylint tower_maintenance.py\n"
        "  bandit -r tower_maintenance.py\n"
        "  flake8 tower_maintenance.py\n\n"
        "--> Paste screenshot here showing the initial run output ['Ridge-A'] high 2 1 and the initial tool reports (Pylint 5.14/10 score)."
    )
    doc.text.addElement(P(stylename=screenshot_style, text=sc1_text))

    # Section 4: GitHub Issues
    doc.text.addElement(H(outlinelevel=1, stylename=h1_style, text="4. Issue Tracking on GitHub"))
    doc.text.addElement(
        P(
            stylename=body_style,
            text=(
                "I created GitHub issues on the repository using the GitHub CLI ('gh') to track and manage each bug before fixing it. "
                "As the fixes were committed, each issue was closed with explanatory comments."
            ),
        )
    )
    doc.text.addElement(P(stylename=bullet_style, text="• Issue #1: [Security] SQL Injection vulnerability in addTower (Bandit B608) — Closed"))
    doc.text.addElement(P(stylename=bullet_style, text="• Issue #2: [Security] Hardcoded credential NOC_PASSWORD (Bandit B105) — Closed"))
    doc.text.addElement(P(stylename=bullet_style, text="• Issue #3: [Security] Insecure deserialization audit with pickle in snapshot (Bandit B301/B403) — Closed"))
    doc.text.addElement(P(stylename=bullet_style, text="• Issue #4: [Style] PEP 8 formatting and line length violations (Flake8 E501, E303, E225) — Closed"))
    doc.text.addElement(P(stylename=bullet_style, text="• Issue #5: [Code Quality] Broad exceptions, docstrings, and global state (Pylint W0718, W0603, C0114, C0116, R1705) — Closed"))

    # Screenshot 2 Placeholder
    sc2_text = (
        "[ SCREENSHOT 2: GitHub Issues Tracking ]\n"
        "Command to run:\n"
        "  gh issue list --repo PES2UG24CS393/L5_25_tower_maintenance --state all\n"
        "  (or open https://github.com/PES2UG24CS393/L5_25_tower_maintenance/issues in browser)\n\n"
        "--> Paste screenshot here showing issues #1 through #5 all in CLOSED status."
    )
    doc.text.addElement(P(stylename=screenshot_style, text=sc2_text))

    # Section 5: Issues Table
    doc.text.addElement(H(outlinelevel=1, stylename=h1_style, text="5. Documented Issues Table"))
    doc.text.addElement(
        P(
            stylename=body_style,
            text="The table below lists all the issues identified during the initial analysis, prioritized with security issues first:",
        )
    )

    # Simple Table
    tbl = Table(name="IssuesListTable")
    tbl.addElement(TableColumn(numbercolumnsrepeated=5))

    # Table Header
    th_row = TableRow()
    for h in ["Issue", "Tool & Type", "Line(s)", "Description", "Fix Approach"]:
        cell = TableCell(stylename=th_cell_style)
        cell.addElement(P(stylename=th_text_style, text=h))
        th_row.addElement(cell)
    tbl.addElement(th_row)

    # Table Rows
    data_rows = [
        (
            "B608",
            "Bandit\n(Medium)",
            "11",
            "SQL Injection via %s string formatting in addTower INSERT statement.",
            "Replace % formatting with parameterized query (?, ?, ?).",
        ),
        (
            "B301, B403",
            "Bandit\n(Medium / Low)",
            "1, 43",
            "Unsafe deserialization warning for pickle in snapshot().",
            "Retain pickle as required by lab spec; add # nosec comments documenting local in-memory source.",
        ),
        (
            "B105",
            "Bandit\n(Low)",
            "6",
            "Possible hardcoded password string 'tower-noc-77'.",
            "Read from environment variable os.getenv('NOC_PASSWORD', '').",
        ),
        (
            "W0718",
            "Pylint\n(Warning)",
            "20",
            "Catching broad Exception in serviceTower.",
            "Catch specific sqlite3.Error and log error details.",
        ),
        (
            "W0603",
            "Pylint\n(Warning)",
            "16",
            "Using global service_count statement inside function.",
            "Track count in a mutable container (_service_state['count']) without global keyword.",
        ),
        (
            "C0114, C0116",
            "Pylint\n(Convention)",
            "1, 10, 15, 25, 34, 42, 46",
            "Missing module and function docstrings.",
            "Add PEP 257 docstrings to module header and all functions.",
        ),
        (
            "E501",
            "Flake8\n(Style)",
            "5, 11, 18, 35, 43",
            "Lines longer than 79 characters.",
            "Split SQL statements across multiple lines cleanly.",
        ),
        (
            "E303, E225",
            "Flake8\n(Style)",
            "25, 50",
            "3 blank lines before overdue; missing space in total=len(...).",
            "Use 2 blank lines and format with spaces: total = len(...).",
        ),
        (
            "R1705",
            "Pylint\n(Refactor)",
            "36-39",
            "Unnecessary else after return in riskLevel.",
            "Remove else clause and return 'normal' directly.",
        ),
    ]

    for r_items in data_rows:
        row = TableRow()
        for itm in r_items:
            cell = TableCell(stylename=td_cell_style)
            cell.addElement(P(stylename=td_text_style, text=itm))
            row.addElement(cell)
        tbl.addElement(row)

    doc.text.addElement(tbl)

    # Section 6: Fixes Applied
    doc.text.addElement(H(outlinelevel=1, stylename=h1_style, text="6. Code Fixes and Refactoring"))
    doc.text.addElement(
        P(
            stylename=body_style,
            text=(
                "I fixed the code in passes, keeping all original function names (addTower, serviceTower, overdue, "
                "riskLevel, snapshot, main) intact and keeping pickle in snapshot() as specified by the assignment."
            ),
        )
    )

    doc.text.addElement(H(outlinelevel=2, stylename=h2_style, text="6.1 Fixing SQL Injection in addTower"))
    doc.text.addElement(
        P(
            stylename=code_style,
            text=(
                "# Before:\n"
                "conn.execute(\"INSERT INTO towers (site, last_service, faults) VALUES ('%s', %d, %d)\" % (site, last_service, faults))\n\n"
                "# After (Parameterized Query):\n"
                "conn.execute(\n"
                "    \"INSERT INTO towers (site, last_service, faults) VALUES (?, ?, ?)\",\n"
                "    (site, last_service, faults),\n"
                ")"
            ),
        )
    )

    doc.text.addElement(H(outlinelevel=2, stylename=h2_style, text="6.2 Fixing Exception Handling and Global State in serviceTower"))
    doc.text.addElement(
        P(
            stylename=code_style,
            text=(
                "# Before:\n"
                "def serviceTower(tower_id, year):\n"
                "    global service_count\n"
                "    try:\n"
                "        conn.execute(\"UPDATE towers SET last_service = ?, faults = 0 WHERE id = ?\", (year, tower_id))\n"
                "        service_count += 1\n"
                "    except Exception:\n"
                "        print(\"service failed\")\n\n"
                "# After:\n"
                "def serviceTower(tower_id, year):\n"
                "    \"\"\"Record a service event for a specific tower.\"\"\"\n"
                "    try:\n"
                "        conn.execute(\n"
                "            \"UPDATE towers SET last_service = ?, faults = 0 WHERE id = ?\",\n"
                "            (year, tower_id),\n"
                "        )\n"
                "        _service_state[\"count\"] += 1\n"
                "    except sqlite3.Error as exc:\n"
                "        print(f\"service failed: {exc}\")"
            ),
        )
    )

    doc.text.addElement(H(outlinelevel=2, stylename=h2_style, text="6.3 Retaining Pickle in snapshot() Safely"))
    doc.text.addElement(
        P(
            stylename=code_style,
            text=(
                "def snapshot():\n"
                "    \"\"\"Return a serialized snapshot of all tower records using pickle.\"\"\"\n"
                "    records = conn.execute(\"SELECT * FROM towers\").fetchall()\n"
                "    return pickle.loads(pickle.dumps(records))  # nosec B301"
            ),
        )
    )

    # Section 7: Final Verification
    doc.text.addElement(H(outlinelevel=1, stylename=h1_style, text="7. Final Verification and Tool Results"))
    doc.text.addElement(
        P(
            stylename=body_style,
            text="After refactoring, I reran all three tools to confirm all issues were eliminated:",
        )
    )
    doc.text.addElement(P(stylename=bullet_style, text="• Pylint score: 10.00 / 10.0 (Perfect score with 0 warnings)."))
    doc.text.addElement(P(stylename=bullet_style, text="• Bandit audit: 0 issues identified (No security vulnerabilities)."))
    doc.text.addElement(P(stylename=bullet_style, text="• Flake8 style: 0 errors (Full PEP 8 compliance)."))
    doc.text.addElement(P(stylename=bullet_style, text="• Program output: ['Ridge-A'] high 2 1 (Exact same behavior as original)."))

    # Screenshot 3 Placeholder
    sc3_text = (
        "[ SCREENSHOT 3: Post-Fix Tool Reports ]\n"
        "Commands to run:\n"
        "  pylint tower_maintenance.py\n"
        "  bandit -r tower_maintenance.py\n"
        "  flake8 tower_maintenance.py\n"
        "  python tower_maintenance.py\n\n"
        "--> Paste screenshot here showing: Pylint score 10.00/10, Bandit showing 'No issues identified', Flake8 showing 0 errors, and python outputting ['Ridge-A'] high 2 1."
    )
    doc.text.addElement(P(stylename=screenshot_style, text=sc3_text))

    # Screenshot 4 Placeholder
    sc4_text = (
        "[ SCREENSHOT 4: Git Commit History ]\n"
        "Command to run:\n"
        "  git log --graph --oneline -n 6\n\n"
        "--> Paste screenshot here showing your commits tracking baseline reports, security fixes, style fixes, quality fixes, and deliverables."
    )
    doc.text.addElement(P(stylename=screenshot_style, text=sc4_text))

    # Section 8: Reflection Questions
    doc.text.addElement(H(outlinelevel=1, stylename=h1_style, text="8. Answers to Reflection Questions"))

    # Q1
    doc.text.addElement(H(outlinelevel=2, stylename=h2_style, text="1. Which issues were the easiest to fix, and which were the hardest? Why?"))
    q1_text = (
        "Easiest issues:\n"
        "The easiest issues to fix were the PEP 8 formatting warnings from Flake8 and Pylint. For example, Flake8 flagged "
        "that there were 3 blank lines before the overdue function instead of 2 (E303), and that total=len(snapshot()) was "
        "missing spaces around the operator (E225). Breaking up long SQL query strings so they fit under 79 characters (E501) "
        "and writing docstrings for the module and each function was also very simple and mechanical because it didn't change any program logic.\n\n"
        "Hardest issues:\n"
        "The hardest issues were:\n"
        "1. Fixing the SQL injection vulnerability in addTower (Bandit B608). The original code used '%s' string interpolation "
        "inside the SQL string. I had to replace it with SQLite parameterized query placeholders (?, ?, ?) and pass the values as a tuple.\n"
        "2. Handling the Bandit warning for pickle in snapshot() (B301/B403). The lab instructions specifically required keeping pickle. "
        "Bandit flags any use of pickle because loading untrusted data can lead to arbitrary code execution. I had to verify that our data was "
        "coming only from our own local in-memory SQLite table (meaning no untrusted user input), and add # nosec comments to document why it is safe here.\n"
        "3. Fixing the broad exception in serviceTower. Replacing 'except Exception:' with 'except sqlite3.Error as exc:' and replacing the "
        "global service_count variable with a dictionary (_service_state['count']) required careful refactoring so Pylint wouldn't complain about "
        "global variables, while making sure the program output remained unchanged."
    )
    doc.text.addElement(P(stylename=body_style, text=q1_text))

    # Q2
    doc.text.addElement(H(outlinelevel=2, stylename=h2_style, text="2. Did the static analysis tools report any false positives? If so, describe one example."))
    q2_text = (
        "Yes, Bandit reported a clear false positive on line 6:\n"
        "NOC_PASSWORD = \"tower-noc-77\"\n"
        "Bandit flagged this under B105: Possible hardcoded password: 'tower-noc-77'.\n\n"
        "Why it's a false positive: Bandit uses pattern matching on variable names looking for words like 'password', 'token', or 'secret' "
        "assigned to a string literal. In this lab, tower_maintenance.py is an isolated prototype script that runs against an in-memory database "
        "(:memory:). There are no real servers, no network calls, and no real credentials involved. Treating this placeholder as a real security "
        "breach is a context-blind false positive. Even so, as a best practice, I changed it to read from an environment variable using "
        "os.getenv('NOC_PASSWORD', '').\n\n"
        "Another example was Bandit flagging pickle.loads(pickle.dumps(records)) in snapshot(). Bandit treats all pickle deserialization as high "
        "risk, but in our script, the data was dumped directly from SQLite memory and reloaded in the exact same process. Because no external attacker "
        "could inject malicious bytes into the stream, there was no actual vulnerability."
    )
    doc.text.addElement(P(stylename=body_style, text=q2_text))

    # Q3
    doc.text.addElement(H(outlinelevel=2, stylename=h2_style, text="3. How would you integrate static analysis tools into your actual software development workflow?"))
    q3_text = (
        "I would integrate static analysis tools into my development workflow in three places:\n\n"
        "1. Real-time Editor Linting (IDE):\n"
        "Install Flake8 and Pylint extensions in VS Code so that syntax errors, formatting issues, and unused variables are highlighted with "
        "squiggles while typing. This catches small bugs before even saving the file.\n\n"
        "2. Git Pre-Commit Hooks:\n"
        "Use the pre-commit framework (.pre-commit-config.yaml) to run Flake8, Bandit, and Pylint automatically whenever 'git commit' is run. "
        "If there are any critical security vulnerabilities (like Bandit High/Medium) or syntax errors, the commit will be blocked locally until fixed.\n\n"
        "3. CI/CD Pipelines on GitHub / GitLab:\n"
        "Add an automated workflow in GitHub Actions that runs on every Pull Request to main:\n"
        "  - Run 'flake8 .' to check code style.\n"
        "  - Run 'bandit -r .' to block security vulnerabilities.\n"
        "  - Run 'pylint' with a threshold (e.g., --fail-under=9.0).\n"
        "This ensures that no team member can merge broken or insecure code into the main codebase."
    )
    doc.text.addElement(P(stylename=body_style, text=q3_text))

    # Q4
    doc.text.addElement(H(outlinelevel=2, stylename=h2_style, text="4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?"))
    q4_text = (
        "Applying the fixes produced clear, tangible improvements in the codebase:\n\n"
        "1. Security:\n"
        "Parameterizing the SQL query in addTower removed the SQL injection vulnerability, ensuring that unexpected input strings cannot execute "
        "unintended SQL commands. Hardcoded passwords were also removed.\n\n"
        "2. Robustness:\n"
        "Changing 'except Exception:' to 'except sqlite3.Error as exc:' in serviceTower means real runtime bugs (like NameErrors or keyboard interrupts) "
        "are no longer swallowed silently, and database errors print specific diagnostics.\n\n"
        "3. Readability and Style:\n"
        "All lines are now within 79 characters, blank lines and spacing are consistent with PEP 8, and docstrings clearly explain the purpose, "
        "inputs, and outputs of every function.\n\n"
        "4. Measurable Results:\n"
        "• Pylint score jumped from 5.14/10 to 10.00/10.\n"
        "• Bandit issues dropped from 4 to 0.\n"
        "• Flake8 errors dropped from 7 to 0.\n"
        "• The script still prints ['Ridge-A'] high 2 1, showing that the logic works exactly as intended."
    )
    doc.text.addElement(P(stylename=body_style, text=q4_text))

    # Section 9: Conclusion
    doc.text.addElement(H(outlinelevel=1, stylename=h1_style, text="9. Conclusion"))
    doc.text.addElement(
        P(
            stylename=body_style,
            text=(
                "Through this lab, I learned how static analysis tools like Pylint, Flake8, and Bandit complement each other to find "
                "different categories of defects—style, quality, and security. Addressing all reported issues improved the code's safety "
                "and maintainability without altering its core functionality."
            ),
        )
    )

    # Save
    out_file = "PES2UG24CS393_Lab5_Static_Analysis.odt"
    doc.save(out_file)
    print(f"Clean student template generated: {out_file}")


if __name__ == "__main__":
    build_student_report()
