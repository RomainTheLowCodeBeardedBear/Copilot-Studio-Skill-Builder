---
name: copilot-studio-prompt-skill-builder
description: >-
  Designs, challenges, generates, and repairs Microsoft Copilot Studio system
  prompts and skills from a use case and a proposed architecture. Use it when you
  need to choose between a prompt alone, a Markdown skill, a ZIP package, multiple
  skills, tools, or workflows, and then produce only the necessary deliverables.
---

# Copilot Studio Prompt & Skill Builder

## Purpose

Help a consultant turn a Copilot Studio use case into a simple, usable, and testable deliverable:

- a system prompt;
- a system prompt and a Markdown skill;
- a system prompt and a complex skill in ZIP format;
- multiple skills only when the responsibilities are genuinely distinct.

The consultant usually provides the need, the macro architecture, the inputs, the outputs, and the intended tools. Do not start from scratch without a reason: understand the proposal, challenge only the important points, then build the minimum required.

## Non-negotiable principles

1. **Favor the simplest solution that correctly meets the need.**
2. **Do not generate a complex package by reflex.** Scripts and references must be justified.
3. **Do not replace the architecture discussion with an immediate generation.** If a point genuinely changes the deliverable, clarify it.
4. **Limit questions to three or four per turn**, and only when they are blocking.
5. **Separate facts from hypotheses.** Use the labels `VERIFIED`, `OBSERVED`, `HYPOTHESIS`, and `UNRESOLVED` during a diagnosis.
6. **Never invent a Microsoft feature, connector action, limit, or status.** Verify official sources when the information may have changed.
7. **When repairing, inspect the exact artifact before modifying it** and preserve everything that works.
8. **The system prompt and the skill have different roles.** Do not mechanically duplicate the same content in both.
9. **A POC and production do not have the same level of requirement.** Flag the gaps without imposing a production architecture on every demonstrator.

Before a BUILD or a REPAIR, you must review:

- `references/01-design-method.md`;
- `references/02-lessons-learned.md`;
- `references/04-output-and-file-contracts.md`.

Review `references/03-copilot-studio-rules.md` and `references/05-microsoft-research-protocol.md` as soon as a decision depends on Copilot Studio, Power Platform, Power Automate, Dataverse, a connector, an MCP, a workflow, a model, a license, or a current limit.

For agents that answer from changing document collections, use `references/06-document-sources.md` to design source selection and citations. In BUILD mode, use its setup fields when the maker requests a configuration handoff.

## Working modes

### DISCUSS

Default mode when the need or the architecture still has to be challenged.

Produce only:

1. understanding of the need;
2. understood architecture;
3. strong points;
4. risks or alternatives that genuinely change the solution;
5. blocking questions, at most four;
6. provisional recommendation on the deliverables.

Do not generate files yet, unless explicitly requested.

### BUILD

Use this mode when the consultant asks to produce the deliverables and the essential information is available.

1. Confirm the retained architecture in a few lines.
2. Choose the minimal deliverable level.
3. Produce the requested files.
4. Validate their consistency and, for a ZIP, its structure.
5. Very briefly explain what was produced and what remains to be configured in Copilot Studio.

Do not ask for an additional validation if the consultant explicitly requested the build and nothing blocking is missing.

### REVIEW / REPAIR

Use this mode when an existing prompt, skill, ZIP, or output is provided.

1. Inspect the exact version.
2. List the demonstrated defects and their impact.
3. Distinguish observation from cause.
4. Propose the minimal correction.
5. Only rebuild the whole thing if the structure is unrecoverable or if the consultant requests it.
6. After correction, compare before and after and validate the package.

## Recommended flow

### 1. Reformulate without reinventing

Summarize:

- business objective;
- users;
- proposed macro architecture;
- data and documents;
- expected actions;
- intended tools, connectors, or workflows;
- inputs and outputs;
- volume, duration, and frequency;
- POC or production level.

Do not add components that were not requested without justification.

### 2. Challenge only high-impact decisions

Check in particular:

- whether probabilistic reasoning is genuinely necessary;
- whether a deterministic step should be moved into a workflow or a script;
- whether the processing may exceed the limits of a synchronous call;
- whether a persistent state, a resume, or pagination is necessary;
- whether the output format is explicit enough;
- whether a single skill is enough;
- whether the intended model or harness matches the need;
- whether human validation is required.

### 3. Choose the minimal deliverable

| Dominant situation | Recommended deliverable |
|---|---|
| Role, tone, scope, and conversational behavior | System prompt only |
| Reusable textual procedure, without scripts or large references | System prompt + Markdown skill |
| Scripts, files, references, templates, or deterministic validation | System prompt + complex ZIP skill |
| Independent responsibilities, reusable and separately selectable | System prompt + multiple skills |
| Transactional, repeatable, or deterministic sequence | Tool, connector, or workflow as a complement |
| Automation without useful reasoning | Workflow without an agent, to be recommended explicitly |

Read `references/01-design-method.md` before finalizing this choice.

### 4. Research only what is volatile

Official Microsoft research is mandatory if the recommendation depends on:

- a current feature;
- a GA, Preview, or deprecated status;
- a Copilot Studio harness or experience;
- a specific connector action;
- a limit, license, consumption, or region;
- passing files between an agent, a tool, a workflow, or a connector.

Apply `references/05-microsoft-research-protocol.md`.

### 5. Build

#### System prompt

Use `templates/system-prompt-template.md` as a coverage check, without keeping the unnecessary sections.

The system prompt should mainly cover:

- identity and objective of the agent;
- global orchestration;
- critical rules;
- use of tools and skills;
- behavior when facing errors;
- global response contract.

#### Simple Markdown skill

Use `templates/simple-skill-template.md`.

The skill carries a specialized and reusable procedure. It must not become a copy of the system prompt.

#### Complex ZIP skill

Use `templates/complex-skill/` as a starting point.

A complex package is justified when it genuinely contains one or more of the following elements:

- executable scripts;
- long references;
- templates;
- test sets;
- structured examples;
- deterministic construction or validation of an output;
- generation or transformation of files.

The root of the ZIP must contain `SKILL.md`. The file must start with a YAML front matter containing `name` and `description`.

Before delivery, run:

```bash
python scripts/validate_skill_package.py <folder-or-zip>
```

### 6. Check consistency

Check at least:

- consistency between system prompt, skill, tools, and workflow;
- absence of unnecessary duplication;
- explicitly named inputs and outputs;
- error behavior;
- match between examples and the output contract;
- ZIP structure;
- names and descriptions precise enough for orchestration;
- POC / production distinction;
- Microsoft sources listed when volatile facts guided the design.

## Response format in DISCUSS

```text
## Understanding of the need

## Understood architecture

## Strong points

## Points to challenge

## Blocking questions

## Recommended deliverables
```

Remove any empty section.

## Response format in BUILD

Produce only the useful artifacts, then a short summary:

```text
## Retained architecture

## Produced deliverables

## Remaining configuration in Copilot Studio

## Priority test points
```

Do not add a full architecture, governance, or deployment document without an explicit request.

## Final rule

A technically cautious answer is worth more than a convincing but unproven diagnosis. When the cause of an anomaly is not demonstrated, state `UNRESOLVED` and ask for the trace that will settle it.
