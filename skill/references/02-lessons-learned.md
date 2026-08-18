# Lessons learned and anti-patterns

This document captures real incidents encountered while building complex Copilot Studio agents. The rules are generalized so they remain useful for other use cases.

## 1. Honest diagnosis

Always distinguish:

- **VERIFIED**: demonstrated by a file, a test, a trace, or a reproduced output;
- **OBSERVED**: visible, but the cause is not established;
- **HYPOTHESIS**: a plausible explanation to test;
- **UNRESOLVED**: the available elements do not allow a conclusion.

Never turn a correlation into a cause. A displayed JSON can differ from the value actually passed to another agent or to a tool.

## 2. Targeted repair

Before any modification:

1. open the exact version actually deployed;
2. list its structure;
3. identify the functional behavior to preserve;
4. reproduce the error;
5. modify the minimum;
6. compare before and after;
7. validate the final package.

Do not regenerate a whole ZIP from a memory or an excerpt.

## 3. System prompt and skill

The system prompt carries the identity, the orchestration, and the global rules.

The skill carries a specialized procedure, references, and possibly scripts.

Anti-patterns:

- copying the same block entirely into both;
- putting the whole technical procedure into the system prompt;
- reducing the system prompt to a sentence that no longer drives the agent;
- introducing two contradictory rules in different locations.

## 4. JSON contracts

For a strict output:

- define all fields;
- specify the allowed values;
- distinguish root fields and per-item fields;
- validate the cardinalities;
- check, for example, `count == len(results)`;
- use a construction and validation script when exact fidelity is critical;
- forbid the model from manually rebuilding the output after validation;
- keep at least one example known to work.

Native citations such as `[1]`, `[2]`, `[source]`, or markers injected by the environment can break a JSON consumer. In a strict contract, write the sources as ordinary data or isolate them in a dedicated field.

## 5. File passing

Always distinguish:

- URL;
- a connector's file reference;
- binary content;
- Base64 string;
- truncated Base64 text;
- the sandbox local path;
- conversational attachment.

Anti-patterns:

- assuming a tool response automatically exists in a skill's filesystem;
- manually re-typing a large output into a local file;
- sending a Base64 preview with `...` as file content;
- confusing the local path created by a script and the file type expected by a connector.

## 6. Large-volume processing

For hundreds of items:

- paginate;
- limit the batches;
- persist the state;
- make the writes idempotent;
- plan for resume;
- avoid a final synthesis that re-reads and reasons over the entire corpus if the results can be accumulated progressively;
- measure time, consumption, and error rate per model.

An incomplete result after a six-hour limit is not necessarily a model error: document the execution limit and distinguish quality, coverage, duration, and cost.

## 7. Tools and workflows

Do not invent the name of a connector action.

For each tool, clarify:

- name and description;
- authentication;
- inputs;
- outputs;
- timeout;
- error behavior;
- connection identity;
- idempotency;
- current status and limits.

Move deterministic, transactional, or repetitive steps to a workflow when it improves reliability.

## 8. Packaging

Before delivering a complex skill:

- `SKILL.md` at the root;
- valid YAML front matter;
- `name` and `description` present;
- name in lowercase, digits, and hyphens;
- no unnecessary wrapper folder in the ZIP;
- no `__pycache__`, `.pyc`, temporary files, or test outputs;
- all referenced files exist;
- scripts executed at least on one nominal case and one error case.

## 9. Do not over-architect

A complex use case does not automatically justify:

- multiple agents;
- multiple skills;
- a ZIP skill;
- a workflow;
- Dataverse;
- asynchronous processing.

Complexity must meet a measurable need.
