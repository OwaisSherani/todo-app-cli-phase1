# Implementation Plan: Todo In-Memory Python Console Application (Intermediate & Advanced Levels)

**Branch**: `002-todo-intermediate-advanced` | **Date**: Monday, December 29, 2025 | **Spec**: [link to spec]
**Input**: Feature specification from `/specs/002-todo-intermediate-advanced/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

This plan extends the existing Basic Level Todo application with Intermediate and Advanced features based on the architectural sketch. The Intermediate Level adds organization and usability features (priorities, tags, search, filter, sort), while the Advanced Level introduces intelligent and time-aware features (recurring tasks, due dates, reminders). The implementation will maintain backward compatibility with existing Basic Level functionality while extending the data model and CLI interface.

## Technical Context

**Language/Version**: Python 3.13+ (as specified in constitution)
**Primary Dependencies**: Standard Python libraries (datetime, re, etc.), existing Basic Level dependencies
**Storage**: In-memory only (as specified in constitution - no persistent storage)
**Testing**: pytest for unit and integration tests
**Target Platform**: Cross-platform CLI application (Windows, macOS, Linux)
**Project Type**: Single project with extended functionality
**Performance Goals**: Maintain responsive CLI interaction (sub-100ms response times)
**Constraints**: Memory-only storage, maintain backward compatibility with Basic Level
**Scale/Scope**: Individual user task management (single-user, local application)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- Agent-First Development: Ensure all code will be written by the agent
- Spec-First Development: Verify complete specification exists before implementation
- Strict Agentic Workflow: Confirm adherence to spec → plan → tasks → implementation sequence
- Clean Architecture: Verify separation of concerns (models, services, CLI)
- Memory-Only Storage: Confirm no persistent storage implementation

## Project Structure

### Documentation (this feature)

```text
specs/002-todo-intermediate-advanced/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
src/
├── models/
│   ├── __init__.py
│   ├── task.py          # Extended task model with priority, tags, due dates, recurrence
│   └── task_list.py     # Task collection with search, filter, sort capabilities
├── services/
│   ├── __init__.py
│   ├── task_service.py  # Business logic for task operations
│   └── reminder_service.py # Service for handling due dates and reminders
├── cli/
│   ├── __init__.py
│   └── cli.py           # Extended CLI interface with new commands
└── lib/
    ├── __init__.py
    └── utils.py         # Utility functions

tests/
├── contract/
├── integration/
└── unit/
```

**Structure Decision**: Single project structure extending the existing Basic Level implementation with new models, services, and CLI commands to support Intermediate and Advanced features.

## Architecture Implementation

### 1. Project Setup
- Confirm Basic Level code is intact
- Ensure folder structure supports multiple levels
- Verify existing functionality works before extending

### 2. Data Model Extension
- Extend Task entity to include:
  - Priority (High / Medium / Low)
  - Tags / Categories (list of strings)
  - Due date / due time
  - Recurrence pattern

### 3. Intermediate Business Logic
- Implement search, filter, and sort methods in TaskManager
- Ensure compatibility with existing CRUD methods
- Maintain performance with efficient algorithms

### 4. Advanced Business Logic
- Implement recurring task scheduling
- Implement deadline tracking and reminder triggering
- Ensure new methods integrate with existing TaskManager

### 5. CLI Interface Updates
- Add menu options for new features
- Handle input validation for priority, tags, due date, time, recurrence
- Display enhanced task listings (sorted, filtered, with priorities/tags)

### 6. Integration and Testing
- Verify Intermediate features do not break Basic Level
- Verify Advanced features integrate seamlessly
- Test search, filter, sort, recurrence, due dates, and reminders

## Decision Documentation

### 1. Data Structure Extensions
- Priority: Represented as string enum with values "High", "Medium", "Low"
- Tags: Stored as list of strings in each task
- Due date/time: Stored as datetime object in each task
- Recurrence: Stored as string enum with values "daily", "weekly", "monthly"

### 2. Search & Filter Implementation
- Option A: Linear search over task list (chosen for simplicity)
- Tradeoffs: Slight performance impact vs. simplicity and maintainability

### 3. Recurring Task Scheduling
- Option A: Store next occurrence only (chosen for simplicity)
- Tradeoffs: Limited history tracking vs. memory efficiency

### 4. Notification Mechanism
- Option A: Console-based alerts (chosen for portability)
- Tradeoffs: Basic user experience vs. cross-platform compatibility

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [None identified] | [N/A] | [N/A] |