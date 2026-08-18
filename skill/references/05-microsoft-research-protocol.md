# Official Microsoft research protocol

## When to research

Research is mandatory when the recommendation depends on information that is likely to change:

- availability of a feature;
- harness or experience;
- GA, Preview, or deprecated status;
- connector action;
- tool type;
- timeout or maximum size;
- region;
- license, capacity, or cost;
- publication limitation;
- file passing;
- compatibility with a solution or an environment.

## Sources authorized as a priority

1. Microsoft Learn;
2. official Power Platform / Copilot Studio documentation;
3. official Microsoft or Power Platform blog;
4. Microsoft release plans;
5. official Microsoft GitHub when the documentation points to code or an example.

A community source can complement, but must not be the only proof of a current Microsoft capability.

## Checks to perform

For each fact used:

- page title;
- URL;
- last update date;
- product and experience concerned;
- harness concerned;
- GA / Preview / deprecated status;
- prerequisites;
- limits;
- licenses or consumption;
- region if relevant.

## Connectors and tools

Never invent an action from the connector name.

Verify:

- that the connector is available;
- the exact action;
- its inputs and outputs;
- its standard or premium level if relevant;
- the authentication;
- the limitations;
- its availability in the intended experience.

## Reporting

In the architecture discussion, separate:

```text
VERIFIED ON MICROSOFT LEARN
ARCHITECTURE RECOMMENDATION
HYPOTHESIS TO TEST IN THE TENANT
```

Cite the official pages that influenced the choice. If the documentation is contradictory or incomplete, say so explicitly.

## Official starting point, to be re-verified

- Skills overview for agents: https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/skills-overview
- Add an existing skill to an agent: https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/skills-add-existing
- Create a skill for an agent: https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/skills-create
- Tools overview for agents: https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/tools-overview
- Available tools for agents: https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/tools-available
- Choose a harness: https://learn.microsoft.com/en-us/microsoft-copilot-studio/harnesses-overview
- Agent flows overview: https://learn.microsoft.com/en-us/microsoft-copilot-studio/flows-overview
- Pass files to agent flows, connectors, and tools: https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/pass-files-to-connectors
