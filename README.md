# Mock Reasoning — Group Assignment

192-211 Automated Software Testing · Siam University

This repository is the starting point for the group assignment described in
`Mock_reasoning_group_assignment.pdf`. The eight production modules and the
eight tests are given to you. Your group produces the predictions, the
experiment files, and the report.

## 1. Set up the repository (owner, once)

One member is the owner. The others are collaborators. Nobody forks.

Owner, on GitHub:

1. Create a new **public** repository named `mock-reasoning-group-<NN>`.
2. Create it empty: no README, no .gitignore, no license.
3. Open Settings -> Collaborators -> Add people, and add every teammate by
   their GitHub username.

Owner, in this folder:

    git init
    git add .
    git commit -m "Starter files for the mock reasoning assignment"
    git branch -M main
    git remote add origin https://github.com/<owner>/mock-reasoning-group-<NN>.git
    git push -u origin main

Then tell your teammates the repository URL.

## 2. Join the repository (every collaborator, once)

Accept the invitation email or open the repository URL while signed in. Then:

    git clone https://github.com/<owner>/mock-reasoning-group-<NN>.git
    cd mock-reasoning-group-<NN>
    git log --oneline

**Checkpoint.** Every member must see the same first commit in `git log`. Do
not continue until that is true for everyone.

## 3. Set up Python (every member)

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    pytest -q

You must see `8 passed`. Paste that summary line as your answer to Q0.1.

## 4. Work

- Answer the questions in `REPORT_template.md`. Keep the question numbers.
- Create each `exp_*.py` file by typing it from the handout, into the repository
  root. Write your prediction down before you run it.
- Run an experiment by naming it, because `pytest -q` on its own collects only
  `test_*.py`:

      pytest -q exp_spec.py --tb=line

- Commit after each example, not once at the end:

      git add -A
      git commit -m "Example 3: experiment output and answers"
      git pull --rebase
      git push

If a push is rejected, a teammate pushed first. Run `git pull --rebase`, then
push again. This is normal.

## 5. Rules

- Do not edit the eight given modules or the eight given tests, except where a
  question tells you to change something. Put that change back afterwards, so
  `pytest -q` still reports `8 passed` when you submit.
- Some experiment files contain a deliberate mistake. That is the point of the
  experiment. Do not correct it.
- Paste output as text. Screenshots are not accepted.
- Output that cannot be reproduced from the files in this repository is marked
  as absent.

## 6. Submit

Export the finished `REPORT_template.md` to `MockReasoning_Group<NN>.pdf`,
commit the PDF to the repository, and push. Check the repository on GitHub
before the deadline, because the pushed state is what is marked.

## What is in here

| Path | Purpose |
|---|---|
| `weather.py` `weather_api.py` | Example 1 |
| `login.py` | Example 2 |
| `verification.py` | Example 3 |
| `idgen.py` | Example 4 |
| `filesvc.py` | Example 5 |
| `tax.py` | Example 6 |
| `date_utils.py` `report.py` | Example 7 |
| `greetings.py` | Example 8 |
| `test_*.py` | the eight given tests |
| `REPORT_template.md` | your report, 44 questions |
| `requirements.txt` | pytest |
