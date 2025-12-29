---
id: 1
title: Update Constitution
stage: constitution
date: 2025-12-29
surface: agent
model: gpt-4
feature: todo-app
branch: main
user: user
command: /sp.constitution
labels: [constitution, todo-app, multi-level]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
 - README.md
tests:
 - null
---

## Prompt

```
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

You are updating the project constitution at `.specify/memory/constitution.md`. This file contains the core principles for the Todo In-Memory Python Console Application project. Your job is to ensure the constitution reflects the following key principles and that all dependent templates align with these principles.

The core principles for this project are:

1. Agent-First Development: All code must be written by the agent; the human must not write or edit implementation code.
2. Spec-First Development: Never write code before a specification exists; every feature must originate from a written spec.
3. Strict Agentic Workflow: Follow the exact sequence: Write specification → Generate implementation plan → Break into tasks → Implement incrementally → Validate against spec.
4. Functional Completeness: Implement all five core features: ADD, VIEW, UPDATE, DELETE, MARK COMPLETE.
5. Clean Architecture: Follow clean code principles with clear separation of concerns (Data models, Business logic, CLI interaction).
6. Memory-Only Data Storage: All task data must exist only in runtime memory; no persistent storage.

Follow this execution flow:

1. Load the existing constitution at `.specify/memory/constitution.md`.
   - Verify it reflects the core principles for the Todo In-Memory Python Console Application.

2. Consistency propagation checklist:
   - Read `.specify/templates/plan-template.md` and ensure "Constitution Check" section aligns with the six core principles.
   - Read `.specify/templates/spec-template.md` for scope/requirements alignment with the project principles.
   - Read `.specify/templates/tasks-template.md` and ensure task categorization reflects the principle-driven requirements.
   - Read command files in `.qwen/commands/*.toml` to verify no outdated references remain.
   - Read any runtime guidance docs (e.g., `README.md`, `docs/quickstart.md`) to update references to principles.

3. If updates are needed to the constitution:
   - Update the version according to semantic versioning rules:
     - MAJOR: Backward incompatible governance/principle removals or redefinitions.
     - MINOR: New principle/section added or materially expanded guidance.
     - PATCH: Clarifications, wording, typo fixes, non-semantic refinements.
   - Update the LAST_AMENDED_DATE to today's date.

4. Produce a Sync Impact Report (prepend as an HTML comment at top of the constitution file after update):
   - Version change: old → new
   - List of modified principles (old title → new title if renamed)
   - Added sections
   - Removed sections
   - Templates requiring updates (✅ updated / ⚠ pending) with file paths
   - Follow-up TODOs if any placeholders intentionally deferred.

5. Validation before final output:
   - No remaining unexplained bracket tokens.
   - Version line matches report.
   - Dates ISO format YYYY-MM-DD.
   - Principles are declarative, testable, and free of vague language.

6. Write the completed constitution back to `.specify/memory/constitution.md` (overwrite).

7. Output a final summary to the user with:
   - New version and bump rationale.
   - Any files flagged for manual follow-up.
   - Suggested commit message (e.g., `docs: amend constitution to vX.Y.Z (principle additions + governance update)`).

Formatting & Style Requirements:

- Use Markdown headings exactly as in the template (do not demote/promote levels).
- Wrap long rationale lines to keep readability (<100 chars ideally) but do not hard enforce with awkward breaks.
- Keep a single blank line between sections.
- Avoid trailing whitespace.

Do not create a new template; always operate on the existing `.specify/memory/constitution.md` file.

---

As the main request completes, you MUST create and complete a PHR (Prompt History Record) using agent‑native tools when possible.

1) Determine Stage
   - Stage: constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general

2) Generate Title and Determine Routing:
   - Generate Title: 3–7 words (slug for filename)
   - Route is automatically determined by stage:
     - `constitution` → `history/prompts/constitution/`
     - Feature stages → `history/prompts/<feature-name>/` (spec, plan, tasks, red, green, refactor, explainer, misc)
     - `general` → `history/prompts/general/`

3) Create and Fill PHR (Shell first; fallback agent‑native)
   - Run: `.specify/scripts/bash/create-phr.sh --title "<title>" --stage <stage> [--feature <name>] --json`
   - Open the file and fill remaining placeholders (YAML + body), embedding full PROMPT_TEXT (verbatim) and concise RESPONSE_TEXT.
   - If the script fails:
     - Read `.specify/templates/phr-template.prompt.md` (or `templates/…`)
     - Allocate an ID; compute the output path based on stage from step 2; write the file
     - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT

4) Validate + report
   - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.
   - On failure: warn, don't block. Skip only for `/sp.phr`.


/sp.constitution 
AGENTIC DEV STACK CONSTITUTION
Todo Application (Basic → Intermediate → Advanced Levels)

==================================================
ROLE & IDENTITY
==================================================

You are an autonomous senior-level software engineering agent.

You operate under a strict Agentic Dev Stack workflow and are responsible for designing, planning, and implementing a multi-level Todo application without any manual human coding.

The human provides intent, constraints, and evaluation criteria only.

==================================================
ABSOLUTE RULES
==================================================

1. NO MANUAL CODING
- All implementation code must be generated by the agent.
- Human input is limited to specifications, reviews, and approval.
- Any change in behavior must originate from an updated specification.

2. STRICT SPEC-FIRST DEVELOPMENT
- Never implement functionality before a written and approved spec exists.
- Each development level (Basic, Intermediate, Advanced) must have its own versioned specification.
- Specs must be preserved in a specs history folder.

3. MANDATORY AGENTIC WORKFLOW
The following workflow must be followed without exception:

1. Write Specification
2. Generate Implementation Plan
3. Break Plan into Atomic Tasks
4. Implement Tasks Incrementally
5. Validate Against Spec

Skipping, merging, or reordering steps is forbidden.

==================================================
PROJECT OBJECTIVE
==================================================

Build a progressively evolving Todo application that demonstrates increasing levels of software maturity:

- Basic Level: Core CRUD functionality
- Intermediate Level: Organization, usability, and productivity enhancements
- Advanced Level: Intelligent and time-aware features

The project emphasizes agent autonomy, architectural clarity, and disciplined process over feature speed.

==================================================
APPLICATION LEVELS & SCOPE
==================================================

------------------------------
BASIC LEVEL (CORE ESSENTIALS)
------------------------------

The Basic Level establishes the foundation and must be completed and validated before higher levels.

Required features:
- Add Task
- View Task List
- Update Task
- Delete Task
- Mark Task as Complete / Incomplete

Data storage is in-memory only.

------------------------------
INTERMEDIATE LEVEL
(ORGANIZATION & USABILITY)
------------------------------

The Intermediate Level enhances task organization and user efficiency.

Required features:

1. Priorities and Tags / Categories
- Tasks may be assigned a priority level:
  - High
  - Medium
  - Low
- Tasks may include one or more tags or categories
  (e.g., work, personal, home).

2. Search and Filter
- Search tasks by keyword (title or description).
- Filter tasks by:
  - Completion status
  - Priority level
  - Tag or category
  - Date (if applicable).

3. Sort Tasks
- Allow task ordering by:
  - Alphabetical order (title)
  - Priority level
  - Due date (if present).

------------------------------
ADVANCED LEVEL
(INTELLIGENT FEATURES)
------------------------------

The Advanced Level introduces time-aware and automated behavior.

Required features:

1. Recurring Tasks
- Support tasks that repeat on a defined schedule
  (e.g., daily, weekly, monthly).
- Automatically reschedule the next occurrence upon completion.

2. Due Dates and Time Reminders
- Tasks may include a due date and time.
- The system must track upcoming deadlines.
- Notifications may be implemented using appropriate runtime mechanisms
  suitable for a console or environment-aware application.

==================================================
NON-FUNCTIONAL REQUIREMENTS
==================================================

- Language: Python
- Minimum Version: Python 3.13+
- Interface: Command-line (CLI)
- Architecture must support incremental feature expansion.
- Clean code principles must be followed at all levels.
- Separation of concerns is mandatory:
  - Data models
  - Business logic
  - Interface layer

==================================================
DATA & STORAGE CONSTRAINTS
==================================================

- Default storage remains in-memory.
- Persistence may only be introduced if explicitly specified in a future spec.
- External services or databases are not allowed unless approved via spec.

==================================================
VERSIONING & EVOLUTION RULES
==================================================

- Each level must have:
  - Its own specification
  - Its own implementation plan
  - Its own task breakdown
- Existing functionality must not be broken when adding new levels.
- Backward compatibility must be preserved unless explicitly stated otherwise.

==================================================
SUCCESS CRITERIA
==================================================

The project is successful if:

- Each level is fully implemented and validated before advancing.
- All features behave as specified.
- The agent strictly follows the Agentic Dev Stack workflow.
- The codebase remains readable, modular, and maintainable.
- The system demonstrates clear architectural evolution across levels.

Process discipline, clarity, and correctness are more important than feature count or speed.

You must behave as a disciplined autonomous engineer at all times.
```

## Response snapshot

I've successfully updated the project constitution to include the multi-level todo application structure (Basic → Intermediate → Advanced). Here's what was accomplished:

1. Updated the constitution file (.specify/memory/constitution.md) to version 2.0.0, incorporating:
   - The multi-level application structure (Basic, Intermediate, Advanced)
   - Detailed requirements for each level
   - Non-functional requirements
   - Data & storage constraints
   - Versioning & evolution rules

2. Updated the README.md file to reflect the multi-level structure

3. Verified that all templates (plan, spec, tasks) already aligned with the core principles

4. Updated the sync impact report in the constitution file

The constitution now properly reflects the multi-level todo application structure as specified in the user's input, while maintaining all the core principles of agent-first development, spec-first development, and clean architecture.

## Outcome

- ✅ Impact: Constitution updated to version 2.0.0 with multi-level todo application structure
- 🧪 Tests: N/A (documentation update only)
- 📁 Files: .specify/memory/constitution.md, README.md updated
- 🔁 Next prompts: Ready for feature specification based on updated constitution
- 🧠 Reflection: The update successfully incorporated the multi-level structure while preserving all core principles

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin implementing basic level features per updated constitution