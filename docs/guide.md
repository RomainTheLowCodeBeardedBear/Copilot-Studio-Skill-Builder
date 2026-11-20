# Copilot Studio Prompt & Skill Builder — User Guide

> **Skill version:** V1.1 — **updated on 20 November 2026.**
> Copilot Studio, its harnesses, its skills, and its billing evolve very quickly. Always check
> the creation date of this skill and re-verify the official Microsoft sources before presenting
> a point as current.

## About this skill and how it fits with official resources

The Microsoft **Power CAT team** publishes official, community catalogs of skills for AI agents
(Cowork, Copilot Studio, and Scout) at **https://microsoft.github.io/cat-agent-skills/**. Those
catalogs are the reference starting point for reusable, ready-to-use skills.

This project is a **personal contribution** that I use **in addition** to those official resources.
It is the skill I personally rely on when designing agents, because it packages:

- my own design methodology;
- the frequent mistakes that AIs make when building Copilot Studio agents;
- efficient, field-tested guidelines to avoid those mistakes.

It is not a replacement for the official catalogs. It is a complement, shaped by real project
experience, and shared openly with the community.

---

# 1. Introduction

## 1.1 — Purpose of the guide

This guide presents the Copilot Studio Prompt & Skill Builder V1.1 package and how to use it to
design, challenge, generate, or repair system prompts and skills intended for Microsoft Copilot
Studio. It is aimed primarily at consultants who already have a use case and an initial vision of
the architecture.

The goal is not to systematically produce a complete architecture. The expected deliverable is
most often limited to a system prompt, or a system prompt accompanied by a Markdown skill or a ZIP
package. The skill nevertheless helps identify the situations in which a tool, a connector, a
workflow, a script, or several skills genuinely become necessary.

Guiding principle: The skill must leverage the thinking already done by the consultant, challenge
only the high-impact decisions, and favor the simplest solution that correctly meets the need.

## 1.2 — Intended audience

- Copilot Studio and Power Platform consultants;
- functional or technical architects preparing an agent;
- makers who need a system prompt or a structured skill;
- teams that want to capitalize on mistakes encountered in previous projects.

## 1.3 — What the package produces

| Dominant need | Deliverable | Example |
|---|---|---|
| General behavior | System prompt | Documentary agent or internal assistant |
| Reusable textual procedure | Prompt + Markdown skill | Qualifying a request or an analysis grid |
| Scripts, references, or validation | Prompt + ZIP skill | Batch processing with a strict JSON contract |
| Independent responsibilities | Prompt + multiple skills | Separate extraction, control, and writing |

## 1.4 — What the package must not become

The package is neither an automatic generator of architecture documents dozens of pages long, nor
a frozen library of every Microsoft feature. It does not replace the consultant's judgment and must
not impose a multi-agent, Dataverse, or workflow approach when the need does not justify it.

Warning: A complex use case does not automatically require a complex skill. The complexity of the
deliverable must answer a demonstrated need: scripts, references, deterministic validation, file
generation, or independent reuse.

---

# 2. Package contents

## 2.1 — Tree structure

```text
copilot-studio-prompt-skill-builder-v1.1.zip
├── SKILL.md
├── host-system-prompt.md
├── README.md
├── references/
│   ├── 01-design-method.md
│   ├── 02-lessons-learned.md
│   ├── 03-copilot-studio-rules.md
│   ├── 04-output-and-file-contracts.md
│   ├── 05-microsoft-research-protocol.md
│   └── 06-document-sources.md
├── templates/
│   ├── system-prompt-template.md
│   ├── simple-skill-template.md
│   └── complex-skill/
├── scripts/
│   └── validate_skill_package.py
└── examples/
    └── request-examples.md
```

## 2.2 — Role of the main files

| File | Role |
|---|---|
| SKILL.md | Central method: modes, decisions, generation, and repair. |
| host-system-prompt.md | Optional base for the general instructions of the host agent. |
| 01-design-method.md | Minimal questionnaire, architecture challenge, and decision tree. |
| 02-lessons-learned.md | Encountered mistakes and rules meant to prevent repeating them. |
| 04-output-and-file-contracts.md | JSON, tools, files, and deterministic validation contracts. |
| 06-document-sources.md | Folder descriptions, evidence checks and configuration handoff for evolving collections. |
| templates/ | Starting points for the produced prompts and skills. |
| validate_skill_package.py | Structure check of a folder or a ZIP before delivery. |

## 2.3 — Why the package is a complex skill

The central capability remains a design method, but it relies on several references, templates, and
a validation script. A single Markdown file would become hard to maintain and would force the AI to
constantly load details that are only useful in certain contexts.

Modular design: The SKILL.md file contains the general flow. The references are consulted as needed:
architecture, known mistakes, output contracts, or Microsoft research.

---

# 3. Installation and prerequisites

## 3.1 — Use in Copilot Studio

As of 6 August 2026, Microsoft documents skills in the experience based on the GitHub Copilot
harness. A skill can be imported as a Markdown file or as a ZIP containing SKILL.md at the root,
with a YAML front matter including `name` and `description`.

1. Create or open the host agent in the experience that supports skills.
2. Open the Build tab, then the Skills component.
3. Choose Upload a skill and import the V1.1 ZIP.
4. Use host-system-prompt.md as the base for the host agent's general instructions.
5. Add the tools required for Microsoft research and file generation, depending on the environment.
6. Test at least one DISCUSS scenario, one BUILD, and one REVIEW / REPAIR.

Consumption: Microsoft indicates that building, testing, and evaluating agents based on the GitHub
Copilot harness can consume Copilot Credits. Check the tenant documentation and governance before
intensive use.

## 3.2 — Use with another AI

The package can also be attached to a conversation with an AI that can read files. You must then
explicitly ask the AI to start with SKILL.md. The ability to produce a ZIP, a Word document, or a
script depends on the tools actually available in that AI.

Important limitation: The skill can define a file-generation method, but it does not create a
technical capability absent from the host agent. Without a filesystem, Python execution, or a
file-creation tool, the AI must provide the textual content without pretending to have created a ZIP.

## 3.3 — Access to Microsoft documentation

The research protocol requires official Microsoft sources when the recommendation depends on a
current feature, a connector, a harness, a limit, a license, or a Preview status. The host agent
must therefore have a browsing or web-search tool. Otherwise, it must declare the verification
impossible and must not invent the answer.

---

# 4. Working modes

## 4.1 — DISCUSS mode

DISCUSS is the default mode when the consultant presents a use case and a macro architecture. The
skill reformulates the need, identifies the strong points, challenges the choices that can change
reliability or cost, then proposes the deliverable level.

- no file is generated if the request only concerns the discussion;
- three or four blocking questions maximum per turn;
- no reset of the architecture without justification;
- clear distinction between a Microsoft fact, a recommendation, and a hypothesis.

## 4.2 — BUILD mode

BUILD is used when the consultant explicitly requests the deliverables and the essential information
is available. The skill briefly confirms the retained architecture, produces the prompt and the
necessary skills, then validates the consistency and the structure.

Rule: If the consultant has requested the build and no blocking information is missing, the AI must
not impose a new validation step before generating the files.

## 4.3 — REVIEW / REPAIR mode

This mode applies when an existing prompt, skill, or ZIP is provided. The goal is to correct the
artifact that is actually deployed without repeating the full-rebuild mistakes encountered on
complex projects.

1. Inspect the exact version and its structure.
2. Reproduce or characterize the error.
3. Separate the observation from the cause.
4. Propose the minimal correction.
5. Compare before and after.
6. Run the package validator.

## 4.4 — Usage cycle

| 1. Explain | 2. Challenge | 3. Choose | 4. Build |
|---|---|---|---|
| Use case, architecture, inputs, outputs, and tools | Only the choices that change the solution | Prompt, simple skill, ZIP, or workflow | Usable files, tests, and validation |

Recommended cycle for using the skill.

---

# 5. Preparing a request

## 5.1 — Useful information

| Information | Why it matters | Example |
|---|---|---|
| Business objective | Determines the expected result | Qualify an access request |
| Macro architecture | Avoids starting from scratch | Agent + Dataverse workflow |
| Inputs | Defines the available context | Email and attachment |
| Outputs | Determines the contract | Strict JSON or user response |
| Intended tools | Allows validating the integration | Outlook, SharePoint, Dataverse |
| Volume and duration | Influences batches, resume, and cost | 200 documents, 6-hour run |
| Reliability level | Determines the controls | POC with manual resume |
| Requested deliverable | Avoids unnecessary documents | Prompt + Markdown skill |

## 5.2 — Example of a complete request

> Here is my use case: I want to analyze the access requests received by email. I plan to use a
> main agent, Outlook as a tool, and a Power Automate workflow to create the request. Inputs: the
> email body, the sender, and a possible attachment. Expected output: a JSON with `is_complete`,
> `missing_information`, and `proposed_reply`. It is a POC, but the writing workflow must be
> deterministic. Challenge the architecture, then produce the system prompt and the necessary
> skill(s).

## 5.3 — Blocking questions

The skill must not turn every request into a questionnaire. It only asks the questions whose answer
changes the deliverable, for example the existence of a Dataverse write, the need for a strict JSON,
the volume, or the need for human validation.

Good practice: When the answers are already present in the message, do not ask for them again. When
four questions or fewer are blocking, group them in a single turn.

---

# 6. Choosing the right deliverable

## 6.1 — System prompt only

Choose a system prompt when the need is mainly about the role, the tone, the scope, the response
rules, and the general orchestration of already-configured tools. An additional skill brings nothing
if the procedure is neither specialized nor reusable.

## 6.2 — System prompt and Markdown skill

This level suits a textual business procedure: analysis grid, qualification sequence, escalation
rules, response format, or precise instructions for using a tool. The skill remains a single file
when no script, template, or reference corpus is necessary.

## 6.3 — System prompt and complex ZIP skill

The ZIP is justified by concrete needs: deterministic validation, file generation, scripts, long
references, templates, multiple examples, or test sets. It must not be chosen only because the use
case is important.

- SKILL.md at the root;
- YAML front matter with `name` and `description`;
- single-responsibility scripts;
- references separated from the global instructions;
- ZIP validation before delivery.

## 6.4 — Multiple skills

Multiple skills are relevant only if their responsibilities, descriptions, and triggers are
distinct. A linear procedure must not be split artificially, because it increases the risk of
incorrect selection and loss of context.

## 6.5 — Tool or workflow as a complement

| Need | Preferred component | Reason |
|---|---|---|
| Read or write in a known service | Connector | Existing Power Platform actions |
| Internal or custom service | MCP or API | Specific contract |
| Repeatable multi-step process | Workflow / agent flow | Deterministic and observable execution |
| Automation without reasoning | Workflow without an agent | Less cost and variability |

---

# 7. Challenging the Copilot Studio architecture

## 7.1 — Distinguish instructions, knowledge, skills, and tools

The skill checks that each responsibility is placed at the right level. Instructions define the
general behavior; knowledge provides information; a skill describes a reusable capability; a tool
acts on an external system; a workflow runs a deterministic sequence.

## 7.2 — Verify the description of skills and tools

The orchestrator selects a skill or a tool based on its name, its description, and the context. A
vague description reduces the selection quality. The skill builder therefore requires a description
that specifies the produced result and the situations in which the capability must be activated.

## 7.3 — Harness, experience, and model

The harness influences the type of reasoning, file handling, skills, workflows, and billing. The
model influences quality, speed, and cost. These elements evolve quickly: the skill does not freeze
a catalog, it imposes an official Microsoft research at design time.

Example: Two models can produce similar quality with very different durations. During a POC, compare
coverage, relevance, time, cost, and error rate instead of choosing only the most recent model.

## 7.4 — Long or large processing

An agent that analyzes hundreds of items over several hours generally requires batches, a persistent
state, a resume, and a coverage measurement. An execution limited to six hours can produce a partial
file without the quality of the already-obtained results being necessarily poor.

- paginate the inputs;
- validate each batch;
- save the progress;
- make the writing idempotent;
- document the rare read or analysis errors;
- plan the automatic resume in production.

## 7.5 — POC and production

| Topic | POC | Production |
|---|---|---|
| Rare error | Can be observed and corrected manually | Resume or exception handling |
| Partial state | Acceptable if documented | Persisted and resumable |
| Monitoring | Targeted measurement | Logging and alerts |
| Preview | Possible if acknowledged | Explicit decision and alternative |
| Cost | Comparative estimate | Budget, limits, and tracking |
| Human validation | Depending on the risk | Mandatory for sensitive decisions |

---

# 8. Output contracts and file handling

## 8.1 — Textual or JSON output

The format must be decided before generation. A response intended for a human can stay in Markdown.
An output consumed by a Writer, a workflow, or Dataverse must precisely define its fields, its
allowed values, its cardinalities, and its error behavior.

```json
{
  "count": 5,
  "results": [ ... ]
}
```

Rule: `count == len(results)`.

## 8.2 — Deterministic construction

When identifiers, metadata, or a count must be preserved exactly, the model must not manually
rebuild the final envelope. A script can assemble the deterministic fields, validate the schema, and
emit the output.

Lesson learned: A validation does not protect the output if the agent then retypes the JSON. The
contract must specify that the final response is the validated output and that no reconstruction is
allowed.

## 8.3 — Citations in a strict JSON

Native citation markers such as `[1]` or `[2]` can be added by the environment and disrupt a
consumer. The sources must be described in dedicated fields or as ordinary text, then validated
before transmission.

## 8.4 — URL, reference, binary, and Base64

The skill requires documenting the exact nature of each file. A SharePoint URL, a connector
reference, a local path, a binary content, and a Base64 string are not interchangeable.

| Value | Question to ask |
|---|---|
| URL | Can the next component download the file? |
| Connector reference | Can it be passed as-is to the next tool? |
| Local path | Does the file really exist in the script's sandbox? |
| Base64 | Is the string complete, not truncated, and expected by the destination? |
| Bytes | Does the connector expect an object with `contentBytes` and `name`? |

---

# 9. Reviewing and repairing an artifact

## 9.1 — Inspect the exact version

Before any correction, the AI must open the ZIP or the file actually deployed. An old package, a
prompt excerpt, or a locally generated version is not enough to attribute the cause of an incident.

## 9.2 — Levels of proof

| Level | Meaning |
|---|---|
| VERIFIED | Demonstrated by a trace, a file, or a reproduced test. |
| OBSERVED | Visible in the output, but the cause is not demonstrated. |
| HYPOTHESIS | A plausible explanation to test. |
| UNRESOLVED | The current data does not allow a conclusion. |

## 9.3 — Minimal correction

1. Identify the rule or the file at fault.
2. Preserve the structure and the functional behaviors.
3. Modify only the necessary elements.
4. Run the nominal tests and the error cases.
5. Compare the final package with the source version.
6. Validate the ZIP with validate_skill_package.py.

## 9.4 — Validation command

```bash
python scripts/validate_skill_package.py <folder-or-zip>
```

The validator notably checks the presence of SKILL.md at the root, the front matter, the skill name,
UTF-8 encoding, and the absence of temporary files. It also flags ZIPs that contain a wrapper folder
above SKILL.md.

---

# 10. Anti-patterns to avoid

## 10.1 — Over-architecting

- creating multiple skills for a linear procedure;
- adding Dataverse or a workflow without a persistent or transactional need;
- producing a full folder when only a prompt is requested;
- turning every POC into a production architecture.

## 10.2 — Inventing or freezing the platform

- inventing a plausible connector action;
- using an old limit without checking its date;
- mixing experiences or harnesses;
- presenting a Preview feature as a production commitment;
- copying a connector catalog into the skill instead of researching at the time of need.

## 10.3 — Rebuilding instead of repairing

- recreating a ZIP without reading the source structure;
- removing the front matter or the support files;
- modifying several scripts when a single defect is demonstrated;
- announcing the cause of an error without a trace;
- confusing the displayed JSON and the one actually received by the next component.

## 10.4 — Mishandling files

- assuming that a tool result exists on the local disk;
- saving a truncated Base64 string as an Excel file;
- passing a URL to an action that expects bytes;
- not checking the size or the MIME type;
- generating a file without providing a usable link or reference.

---

# 11. Usage examples

## 11.1 — System prompt only

> I want an internal agent that answers HR questions from SharePoint. It performs no action and must
> not invent a policy. Here are the sources and the limits. Challenge my architecture, then produce
> only the system prompt.

Expected result: a structured system prompt. No skill or workflow is generated if the procedure does
not require a distinct reusable capability.

## 11.2 — Prompt and simple skill

> I want to analyze the access requests received by email. The skill must verify the application name
> and the person's address. The output is a JSON `is_complete`, `missing_information`, and
> `proposed_reply`. Outlook is a tool and the workflow creates the request. Produce the system prompt
> and the Markdown skill.

## 11.3 — Prompt and complex skill

> I process documents in batches of five. The identifiers must be preserved and the JSON must be
> validated before a Dataverse Writer. I want construction and validation scripts, as well as
> non-regression cases. Challenge the agent / workflow separation, then produce the system prompt and
> the ZIP.

## 11.4 — Review / Repair

> Here is the ZIP actually deployed and the trace of a failing run. Inspect the package before any
> modification. Distinguish VERIFIED, OBSERVED, HYPOTHESIS, and UNRESOLVED. Propose the minimal
> correction and keep the rest of the package.

---

# 12. Checklists

## 12.1 — Before calling the skill

- [ ] The business result is described.
- [ ] The intended macro architecture is explained.
- [ ] The inputs and outputs are identified.
- [ ] The intended tools or workflows are named.
- [ ] The volume and the duration are approximately known.
- [ ] The POC or production level is indicated.
- [ ] The expected deliverable is specified.

## 12.2 — Before starting BUILD

- [ ] The genuinely blocking questions have been answered.
- [ ] The prompt / simple skill / ZIP choice is justified.
- [ ] The responsibilities of the workflow and the agent are separated.
- [ ] The volatile Microsoft information has been verified.
- [ ] The output contract is defined.
- [ ] The error cases are identified.

## 12.3 — Before delivering a complex skill

- [ ] SKILL.md is at the root of the ZIP.
- [ ] `name` and `description` are present and precise.
- [ ] The description indicates when to activate the skill.
- [ ] No temporary file is included.
- [ ] The scripts have been tested.
- [ ] The examples match the contract.
- [ ] The validator returns VALID.
- [ ] A short README explains the installation and the points left to configure.

## 12.4 — Success criteria for V1

V1 is successful if it allows consultants to start from their use case and their architecture, to
get a useful discussion without an interrogation, then to generate a coherent prompt or skill
without reproducing the packaging, JSON contract, file transport, and diagnosis problems already
encountered.

Continuous improvement: The skill must evolve from real cases. Any new rule added must correspond to
a reproducible incident or a recurring need, so that it does not become too large or too specific.

---

# 13. Official references

## 13.1 — Microsoft documentation used

- Skills overview for agents — consulted on 06/08/2026
- Add an existing skill to an agent — consulted on 06/08/2026
- Create a skill for an agent — consulted on 06/08/2026
- Tools overview for agents — consulted on 06/08/2026
- Available tools for agents — consulted on 06/08/2026
- Choose a harness — consulted on 06/08/2026
- Agent flows overview — consulted on 06/08/2026
- Pass files to agent flows, connectors, and tools — consulted on 06/08/2026

## 13.2 — Maintenance rule

Copilot Studio changes quickly. This guide and the skill are dated on purpose: whenever a
recommendation depends on a feature, a harness, a limit, a license, or a status, re-verify the
official Microsoft sources at the time of use, and update the skill from real, reproducible cases.
