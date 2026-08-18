# Output and file contracts

## 1. Textual output contract

Specify:

- language;
- tone;
- length;
- structure;
- citations;
- forbidden elements;
- behavior when information is missing.

## 2. JSON contract

Define explicitly:

- the root object;
- the mandatory fields;
- the types;
- the allowed values;
- the cardinality rules;
- the fields that can be empty;
- a nominal example;
- an error example.

For a batch:

```text
count must equal the actual number of items in results.
```

Do not ask the model to produce a strict JSON and then rephrase it in natural language in the same response.

## 3. Deterministic construction

Use a script if the output must:

- preserve identifiers exactly;
- merge metadata and a verdict;
- validate a schema;
- compute a count;
- guarantee a file name;
- produce a binary.

The model can produce the semantic fields. The script must produce the deterministic fields.

## 4. Citations and sources

In a JSON consumed by another component:

- avoid native citation markers added automatically;
- store the title, publisher, URL, and excerpt in fields or as ordinary text;
- validate that characters added by the interface do not modify the transmitted string.

## 5. Tool contract

For each tool, document:

```text
Functional name:
Technology:
Exact action:
Description for the orchestrator:
Authentication:
Inputs:
Outputs:
Timeout:
Errors:
Resume:
Idempotency:
User or service connection:
Microsoft status verified on:
Official source:
```

## 6. File contract

Document:

```text
Name:
Extension:
MIME type:
Source:
Received value: URL | connector reference | bytes | Base64 | local path
Destination:
Value expected by the destination:
Maximum size:
Encoding:
Integrity validation:
Behavior if the file is missing or too large:
```

Never let the AI silently infer that a URL is a local path or that a Base64 string is a binary file.
