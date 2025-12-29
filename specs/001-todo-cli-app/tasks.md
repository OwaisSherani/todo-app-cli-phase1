---

description: "Task list for Todo In-Memory Python Console Application implementation"
---

# Tasks: Todo In-Memory Python Console Application

**Input**: Design documents from `/specs/001-todo-cli-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are included as specified in the requirements.

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

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure per implementation plan ensuring separation of concerns
- [x] T002 Initialize Python 3.13+ project with proper type hints and documentation
- [x] T003 [P] Configure linting and formatting tools for clean code principles

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 Create in-memory data storage structure (no database)
- [x] T005 [P] Implement task model with ID, title, description, and completion status in src/models/task.py
- [x] T006 [P] Setup CLI interface structure with command parsing in src/cli/main.py
- [x] T007 Create base models/entities that all stories depend on
- [x] T008 Configure error handling and input validation
- [x] T009 Setup application entry point and main loop

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Task (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks via the command line with required title and optional description

**Independent Test**: Can be fully tested by running the application and adding a new task with a title and optional description. The task should appear in the task list with a unique ID and pending status.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

- [x] T010 [P] [US1] Contract test for add task functionality in tests/contract/test_add_task.py
- [x] T011 [P] [US1] Unit test for Task model in tests/unit/models/test_task.py
- [x] T012 [P] [US1] Unit test for TaskManager add_task method in tests/unit/services/test_task_manager.py
- [x] T013 [P] [US1] Integration test for add task feature in tests/integration/test_cli_integration.py

### Implementation for User Story 1

- [x] T014 [P] [US1] Create Task model in src/models/task.py
- [x] T015 [US1] Implement TaskManager service with add_task functionality in src/services/task_manager.py
- [x] T016 [US1] Implement add task CLI command in src/cli/main.py
- [x] T017 [US1] Add validation for required title when adding tasks
- [x] T018 [US1] Add unique ID assignment for new tasks
- [x] T019 [US1] Add graceful error handling for invalid inputs

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Task List (Priority: P1)

**Goal**: Enable users to view all their tasks with ID, title, and completion status

**Independent Test**: Can be fully tested by adding one or more tasks and then viewing the task list. The list should display all tasks with their ID, title, and completion status.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [x] T020 [P] [US2] Contract test for view task list functionality in tests/contract/test_view_tasks.py
- [x] T021 [P] [US2] Unit test for TaskManager get_all_tasks method in tests/unit/services/test_task_manager.py
- [x] T022 [P] [US2] Integration test for view task list feature in tests/integration/test_cli_integration.py

### Implementation for User Story 2

- [x] T023 [US2] Implement TaskManager get_all_tasks method in src/services/task_manager.py
- [x] T024 [US2] Implement view task list CLI command in src/cli/main.py
- [x] T025 [US2] Add proper formatting for task display
- [x] T026 [US2] Handle empty task list scenario with clear message

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Existing Task (Priority: P2)

**Goal**: Enable users to update existing tasks by providing the task ID and new information

**Independent Test**: Can be fully tested by creating a task, updating its title or description, and then viewing the task to confirm the changes were applied.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [x] T027 [P] [US3] Contract test for update task functionality in tests/contract/test_update_task.py
- [x] T028 [P] [US3] Unit test for TaskManager update_task method in tests/unit/services/test_task_manager.py
- [x] T029 [P] [US3] Integration test for update task feature in tests/integration/test_cli_integration.py

### Implementation for User Story 3

- [x] T030 [US3] Implement TaskManager update_task method in src/services/task_manager.py
- [x] T031 [US3] Implement update task CLI command in src/cli/main.py
- [x] T032 [US3] Add validation to ensure task ID exists before updating
- [x] T033 [US3] Add validation for required title when updating tasks

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Delete Task (Priority: P2)

**Goal**: Enable users to delete tasks by providing the task ID

**Independent Test**: Can be fully tested by creating a task, deleting it by its ID, and then viewing the task list to confirm it's no longer present.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [x] T034 [P] [US4] Contract test for delete task functionality in tests/contract/test_delete_task.py
- [x] T035 [P] [US4] Unit test for TaskManager delete_task method in tests/unit/services/test_task_manager.py
- [x] T036 [P] [US4] Integration test for delete task feature in tests/integration/test_cli_integration.py

### Implementation for User Story 4

- [x] T037 [US4] Implement TaskManager delete_task method in src/services/task_manager.py
- [x] T038 [US4] Implement delete task CLI command in src/cli/main.py
- [x] T039 [US4] Add validation to ensure task ID exists before deleting
- [x] T040 [US4] Add confirmation message after successful deletion

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Mark Task Complete/Incomplete (Priority: P2)

**Goal**: Enable users to toggle a task's completion status between pending and completed

**Independent Test**: Can be fully tested by creating a task, marking it as complete, viewing the list to confirm the status change, and then marking it as incomplete again.

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [x] T041 [P] [US5] Contract test for toggle task status functionality in tests/contract/test_toggle_status.py
- [x] T042 [P] [US5] Unit test for TaskManager toggle_task_status method in tests/unit/services/test_task_manager.py
- [x] T043 [P] [US5] Integration test for toggle task status feature in tests/integration/test_cli_integration.py

### Implementation for User Story 5

- [x] T044 [US5] Implement TaskManager toggle_task_status method in src/services/task_manager.py
- [x] T045 [US5] Implement toggle task status CLI command in src/cli/main.py
- [x] T046 [US5] Add validation to ensure task ID exists before toggling status
- [x] T047 [US5] Add proper status display in task list

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T048 [P] Documentation updates in README.md ensuring clean architecture principles
- [x] T049 Code cleanup and refactoring for readability and maintainability
- [x] T050 Performance optimization ensuring memory-only storage efficiency
- [x] T051 [P] Additional unit tests (if requested) in tests/unit/
- [x] T052 Input validation and error handling improvements
- [x] T053 Run quickstart.md validation ensuring all five core features work correctly

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
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 5 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories

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
Task: "Contract test for add task functionality in tests/contract/test_add_task.py"
Task: "Unit test for Task model in tests/unit/models/test_task.py"
Task: "Unit test for TaskManager add_task method in tests/unit/services/test_task_manager.py"
Task: "Integration test for add task feature in tests/integration/test_cli_integration.py"

# Launch all models for User Story 1 together:
Task: "Create Task model in src/models/task.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
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
   - Agent implements User Story 1 (ADD TASK functionality)
   - Agent validates implementation against spec
   - Agent implements User Story 2 (VIEW TASK LIST functionality)
   - Agent validates implementation against spec
   - Continue with remaining stories following spec-first approach
3. All implementation follows clean architecture principles with separation of data models, business logic, and CLI interaction

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