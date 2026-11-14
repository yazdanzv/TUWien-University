# TU Wien — MSc Data Science Workspace

This workspace organizes coursework for the Master's in Data Science at TU Wien.
The current semester is Winter Semester 2026/27 (`2026-WS`).

## Courses

- Information Visualization
- Visual Data Science
- Machine Learning
- Experiment Design & Experiment
- Introduction to Semantic System

Course folders contain `lectures/`, `projects/`, `notes/`, and `resources/`, with
`assignments/` where applicable. The Green Decoupling team project is in
`2026-WS/visual-data-science/projects/green-decoupling/`.
Shared report templates, references, and study notes belong in `shared-resources/`.

## Public copy

This public repository contains the student's working files and selected outputs.
Course lecture slides, assignment handouts, other students' individual work, and
shared group submissions are kept locally because publication rights have not
been established. They are excluded from this repository and its Git history.
Some local workflows therefore require files obtained through the relevant
course platform or from the project team.

## Working conventions

- Open `~/University` as the Codex project when working across courses.
- Open a course directory for focused work only when `~/University` remains the
  project root, so its root `AGENTS.md` is inherited.
- Create assignments as numbered directories such as
  `assignments/assignment-01/`; keep the original brief separate from working
  files and final submissions.
- Create substantial programming work under a dedicated `projects/<name>/`
  directory with its own README, suitable `.gitignore`, and clear separation of
  source code, tests, configuration, data, outputs, and reports.
- Course documents and assignment briefs always take precedence over general
  workspace guidance.

## Codex instructions

The root `AGENTS.md` contains workspace-wide academic and engineering rules.
Each course has a shorter `AGENTS.md` containing only subject-specific guidance.
Codex loads applicable instructions from the project root down to the current
working directory; the more specific course file is applied after the root file.

