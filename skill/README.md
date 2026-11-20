# Copilot Studio Prompt & Skill Builder — V1.1

This package helps an AI discuss, design, produce, and repair Microsoft Copilot Studio system prompts and skills.

## Main usage

The consultant describes:

- their use case;
- their macro architecture;
- the inputs and outputs;
- the intended tools or workflows;
- the requested deliverable.

The skill challenges only the important choices, then recommends and produces the minimum required: prompt alone, Markdown skill, or ZIP package.

## Contents

- `SKILL.md`: main method;
- `host-system-prompt.md`: recommended prompt for the host agent;
- `references/`: method, lessons learned, Copilot Studio rules, contracts, and research protocol;
- `templates/`: prompt and skill templates;
- `scripts/validate_skill_package.py`: package validation;
- `examples/`: request examples.

For document-backed agents, [document source guidance](references/06-document-sources.md) covers folder selection, citations and ready-to-paste knowledge settings.

## Use in Copilot Studio

In the new experience that supports skills:

1. open the agent;
2. go to `Build`;
3. select `Skills`;
4. choose `Upload a skill`;
5. import this ZIP;
6. use the content of `host-system-prompt.md` as the base for the host agent instructions;
7. test the three modes DISCUSS, BUILD, and REVIEW / REPAIR.

Availability, harness, consumption, and limits must be re-verified on Microsoft Learn at deployment time.

## Use with another AI

Attach the ZIP or its content to the conversation, then explicitly ask the AI to use `SKILL.md`. The actual ability to create a ZIP or a document depends on the tools available in that AI's environment.
