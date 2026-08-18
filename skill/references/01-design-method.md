# Design method

## 1. Minimal intake

The consultant often already provides a macro architecture. Start by extracting the elements that are present, without asking again for what they already provided.

Information that can change the deliverable:

1. business objective and target user;
2. entry point of the agent;
3. data, knowledge, and documents;
4. actions to perform;
5. intended tools, connectors, MCP, APIs, or workflows;
6. inputs and outputs;
7. volume, duration, frequency, and parallelism;
8. expected reliability level;
9. POC or production;
10. human validation or irreversible decision.

If four pieces of information or fewer are genuinely blocking, ask them in a single turn. If nothing is blocking, move forward.

## 2. Architecture challenge

Do not challenge to show expertise. Challenge when a decision can cause:

- a non-deterministic output while a strict contract is required;
- processing that is too long or too large;
- data loss between the agent and a tool;
- a partial transaction;
- unnecessary consumption;
- a skill that is impossible to maintain;
- an unacknowledged Preview dependency;
- an absence of resume;
- ambiguity about the identity or the authorizations of the connection;
- confusion between knowledge, skill, tool, and workflow.

## 3. Deliverable decision tree

### System prompt only

Choose this level when the need mainly comes down to:

- a role;
- a tone;
- a scope;
- a response policy;
- a few orchestration rules;
- the simple use of already-configured tools.

Do not create a skill if the instructions are not reusable or specialized.

### System prompt + Markdown skill

Choose this level when the agent must activate a specialized procedure that includes:

- an analysis sequence;
- a decision grid;
- a response format;
- edge cases;
- textual business rules;
- tool usage instructions.

The skill remains a single `.md` file if no support file is genuinely necessary.

### System prompt + complex ZIP skill

Choose this level when the capability requires:

- a validation or transformation script;
- a large schema or contract;
- distinct references;
- a template;
- a test set;
- numerous examples;
- file generation;
- deterministic construction of an output.

Do not build a ZIP that contains only a `SKILL.md` and empty files.

### Multiple skills

Create multiple skills only if:

- each responsibility has a distinct trigger;
- each skill can be described clearly;
- the capabilities are separately reusable;
- data sharing between skills stays under control;
- a single skill would become confusing or contradictory.

Do not artificially split a linear procedure into multiple skills.

## 4. Skill, tool, or workflow

### Skill

A reusable procedure, reasoning, or behavior.

### Tool

An external capability that reads, writes, calls an API, performs an action, or obtains current data.

### Workflow

A deterministic, repeatable, multi-step, or transactional sequence. To be favored for:

- data creation and update;
- approvals;
- structured loops;
- transformations;
- notifications;
- resume or compensation;
- operations that must produce the same result for the same input.

### Script in a complex skill

Local transformation or validation tightly linked to the skill's capability. Never assume that a tool result is automatically available as a local file for the script.

## 5. POC and production

### POC

Can explicitly accept:

- a few rare errors;
- manual resume;
- limited monitoring;
- long processing time;
- Preview features;
- test data.

The POC must nevertheless measure the errors and identify what remains to be industrialized.

### Production

Must generally handle:

- idempotency;
- resume;
- partial processing;
- logging;
- supervision;
- security and connections;
- timeout;
- limits and costs;
- non-regression tests;
- human validation;
- versioning and deployment.
