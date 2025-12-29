---

description: "Task list for implementing Intermediate and Advanced levels of Todo application"
---

# Tasks: Todo In-Memory Python Console Application (Intermediate & Advanced Levels)

**Input**: Design documents from `/specs/002-todo-intermediate-advanced/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

<!--
  ============================================================================
  IMPORTANT: The tasks below are SAMPLE TASKS for illustration purposes only.

  The /sp.tasks command MUST replace these with actual tasks based on:
  - User stories from spec.md (with their priorities P1, P2, P3...)
  - Feature requirements from plan.md
  - Entities from data-model.md
  - Endpoints from contracts/

  Tasks MUST be organized by user story so each story can be:
  - Implemented independently
  - Tested independently
  - Delivered as an MVP increment

  DO NOT keep these sample tasks in the generated tasks.md file.
  ============================================================================
-->

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan ensuring separation of concerns
- [X] T002 Initialize Python 3.13+ project with proper type hints and documentation
- [X] T003 [P] Configure linting and formatting tools for clean code principles

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [X] T004 Extend in-memory data storage structure to support new task properties (no database)
- [X] T005 [P] Implement extended task model with priority, tags, due date, and recurrence pattern in src/models/task.py
- [X] T006 [P] Update CLI interface structure with command parsing for new features in src/cli/cli.py
- [X] T007 Create base models/entities that all stories depend on in src/models/task_list.py
- [X] T008 Configure error handling and input validation for new features in src/lib/utils.py
- [X] T009 Update application entry point and main loop to support new functionality in src/cli/cli.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Set Task Priority & Tags (Priority: P1) 🎯 MVP

**Goal**: Enable users to assign priority levels and tags to tasks for better organization

**Independent Test**: Can be fully tested by creating a task, assigning priority and tags, and then viewing the task to confirm the priority and tags are displayed correctly.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T010 [P] [US1] Contract test for priority setting in tests/contract/test_priority.py
- [X] T011 [P] [US1] Contract test for tag management in tests/contract/test_tags.py
- [X] T012 [P] [US1] Integration test for priority and tag functionality in tests/integration/test_priority_tags.py

### Implementation for User Story 1

- [X] T013 [P] [US1] Extend Task model with priority field in src/models/task.py
- [X] T014 [P] [US1] Extend Task model with tags field in src/models/task.py
- [X] T015 [US1] Implement priority setting in TaskService in src/services/task_service.py
- [X] T016 [US1] Implement tag management in TaskService in src/services/task_service.py
- [X] T017 [US1] Add CLI command for setting priority in src/cli/cli.py
- [X] T018 [US1] Add CLI command for managing tags in src/cli/cli.py
- [X] T019 [US1] Add validation and error handling for priority and tags in src/lib/utils.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Search & Filter Tasks (Priority: P1)

**Goal**: Enable users to search and filter tasks to quickly find specific tasks

**Independent Test**: Can be fully tested by creating multiple tasks with different properties, then using search and filter functions to locate specific subsets of tasks.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [X] T020 [P] [US2] Contract test for search functionality in tests/contract/test_search.py
- [X] T021 [P] [US2] Contract test for filter functionality in tests/contract/test_filter.py
- [X] T022 [P] [US2] Integration test for search and filter in tests/integration/test_search_filter.py

### Implementation for User Story 2

- [X] T023 [P] [US2] Implement search method in TaskList model in src/models/task_list.py
- [X] T024 [P] [US2] Implement filter method in TaskList model in src/models/task_list.py
- [X] T025 [US2] Implement search functionality in TaskService in src/services/task_service.py
- [X] T026 [US2] Implement filter functionality in TaskService in src/services/task_service.py
- [X] T027 [US2] Add CLI command for search in src/cli/cli.py
- [X] T028 [US2] Add CLI command for filter in src/cli/cli.py
- [X] T029 [US2] Add validation and error handling for search and filter in src/lib/utils.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Sort Tasks (Priority: P2)

**Goal**: Enable users to sort tasks by different criteria for better organization

**Independent Test**: Can be fully tested by creating multiple tasks with different properties, then using sort functions to reorder the task list by various criteria.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [X] T030 [P] [US3] Contract test for sort functionality in tests/contract/test_sort.py
- [X] T031 [P] [US3] Integration test for sort functionality in tests/integration/test_sort.py

### Implementation for User Story 3

- [X] T032 [P] [US3] Implement sort method in TaskList model in src/models/task_list.py
- [X] T033 [US3] Implement sort functionality in TaskService in src/services/task_service.py
- [X] T034 [US3] Add CLI command for sort in src/cli/cli.py
- [X] T035 [US3] Add validation and error handling for sort operations in src/lib/utils.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Recurring Tasks (Priority: P2)

**Goal**: Enable users to create recurring tasks that automatically reschedule upon completion

**Independent Test**: Can be fully tested by creating a recurring task, completing it, and verifying that a new instance is automatically created according to the recurrence pattern.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [X] T036 [P] [US4] Contract test for recurring task creation in tests/contract/test_recurring.py
- [X] T037 [P] [US4] Contract test for recurring task scheduling in tests/contract/test_recurring.py
- [X] T038 [P] [US4] Integration test for recurring task functionality in tests/integration/test_recurring.py

### Implementation for User Story 4

- [X] T039 [P] [US4] Extend Task model with recurrence pattern field in src/models/task.py
- [X] T040 [US4] Implement RecurrenceService in src/services/recurrence_service.py
- [X] T041 [US4] Update TaskService to handle recurring tasks in src/services/task_service.py
- [X] T042 [US4] Add CLI command for setting recurrence in src/cli/cli.py
- [X] T043 [US4] Add validation and error handling for recurrence patterns in src/lib/utils.py

**Checkpoint**: Recurring task functionality should be working independently

---

## Phase 7: User Story 5 - Due Dates & Reminders (Priority: P3)

**Goal**: Enable users to set due dates for tasks and receive reminders for upcoming deadlines

**Independent Test**: Can be fully tested by creating tasks with due dates, checking reminders, and verifying that overdue tasks are properly identified.

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [X] T044 [P] [US5] Contract test for due date setting in tests/contract/test_due_dates.py
- [X] T045 [P] [US5] Contract test for reminder functionality in tests/contract/test_reminders.py
- [X] T046 [P] [US5] Integration test for due dates and reminders in tests/integration/test_reminders.py

### Implementation for User Story 5

- [X] T047 [P] [US5] Extend Task model with due date field in src/models/task.py
- [X] T048 [US5] Implement ReminderService in src/services/reminder_service.py
- [X] T049 [US5] Update TaskService to handle due dates in src/services/task_service.py
- [X] T050 [US5] Add CLI command for setting due dates in src/cli/cli.py
- [X] T051 [US5] Add CLI command for viewing reminders in src/cli/cli.py
- [X] T052 [US5] Add validation and error handling for due dates in src/lib/utils.py

**Checkpoint**: All user stories should now be functional

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] TXXX [P] Documentation updates in docs/ ensuring clean architecture principles
- [X] TXXX Code cleanup and refactoring for readability and maintainability
- [X] TXXX Performance optimization ensuring memory-only storage efficiency
- [X] TXXX [P] Additional unit tests (if requested) in tests/unit/
- [X] TXXX Input validation and error handling improvements
- [X] TXXX Run quickstart.md validation ensuring all new features work correctly

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1-3 but should be independently testable
- **User Story 5 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1-4 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Contract test for priority setting in tests/contract/test_priority.py"
Task: "Contract test for tag management in tests/contract/test_tags.py"

# Launch all models for User Story 1 together:
Task: "Extend Task model with priority field in src/models/task.py"
Task: "Extend Task model with tags field in src/models/task.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Priority & Tags)
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Agent Implementation Strategy

Following the strict agentic workflow:

1. Agent completes Setup + Foundational sequentially
2. Once Foundational is done:
   - Agent implements User Story 1 (Priority & Tags functionality)
   - Agent validates implementation against spec
   - Agent implements User Story 2 (Search & Filter functionality)
   - Agent validates implementation against spec
   - Continue with remaining stories following spec-first approach
3. All implementation follows clean architecture principles with separation of concerns

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
- Adhere to agent-first development: all code written by agent
- Follow spec-first development: verify specification exists before implementation
- Maintain clean architecture with separation of data models, business logic, and CLI interaction
- Ensure memory-only storage constraint is maintained throughout implementation