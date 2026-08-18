# Request examples

## System prompt only

> I want an internal agent that answers HR questions from SharePoint. It performs no action. Here are the sources and the limits. Challenge my architecture, then produce only the system prompt.

## System prompt + simple skill

> I want an agent that analyzes access requests received by email. It must verify that the application name and the person's address are present, then produce a JSON `is_complete`. I plan to use Outlook as a tool and a workflow to create the request. Produce the system prompt and the Markdown skill.

## System prompt + complex skill

> I process documents in batches of five. The agent must preserve identifiers, produce a strict JSON, and pass it to a Dataverse Writer. I want a validation script and non-regression examples. Challenge the agent / workflow separation, then produce the system prompt and the ZIP.

## Review / Repair

> Here is the ZIP actually deployed and an output that fails. Inspect the package first. Distinguish facts and hypotheses. Propose the minimal correction and do not rebuild the whole skill without proof.
