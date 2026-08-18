# Copilot Studio rules to take into account

These rules provide a starting point. Copilot Studio evolves quickly: verify the official Microsoft sources before presenting a point as current.

## Components

- **Agent instructions**: general behavior, role, tone, scope, and orchestration.
- **Knowledge**: reference information used to answer.
- **Skills**: reusable capabilities, described by a name, a description, and Markdown instructions.
- **Tools**: external actions via connectors, APIs, MCP, or workflows.
- **Workflows / agent flows**: multi-step and deterministic processes.
- **Connected agents**: specialized agents, only when the delegation brings a real benefit.

## Skill package

The format expected in the new experience includes:

- a `SKILL.md` file;
- a YAML front matter with `name` and `description`;
- Markdown instructions;
- optionally scripts, templates, and references in a ZIP.

The `name` must use lowercase letters, digits, and hyphens. The `description` must explain what the skill does and when to activate it, because the orchestrator relies on it.

## Tools

Choose according to the need:

- **Connector**: a known service with Power Platform actions;
- **MCP**: an internal or custom service exposed through the MCP protocol;
- **Workflow**: a multi-step and deterministic process;
- **API or custom tool**: a specific contract not cleanly covered by the previous options.

Tool names and descriptions are critical for their selection by the orchestrator.

## Workflows and agent flows

A workflow is preferable when the processing must be:

- repeatable;
- deterministic;
- transactional;
- observable;
- resumed after an error;
- composed of several actions;
- separated from conversational reasoning.

For a flow called synchronously by an agent, verify the current trigger, response, and timeout requirements on Microsoft Learn. Do not memorize them as permanent.

## Files

Before recommending a file passing:

1. identify the type of value actually provided by the agent;
2. identify the type expected by the tool;
3. check the name and content fields;
4. check the current maximum size;
5. check whether the value can be used by a local script;
6. plan a strategy if the file is too large.

## Harness, experience, and billing

The choice of harness influences reasoning, files, skills, workflows, and billing. Always verify the current documentation when this choice is part of the architecture.

Do not mix instructions or limitations coming from different experiences without identifying them.
