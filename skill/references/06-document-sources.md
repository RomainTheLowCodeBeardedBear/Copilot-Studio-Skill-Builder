# Build a document-backed agent

Use this reference when the source collection changes over time or several collections answer different questions.

## Configure each knowledge source

Describe each folder by the questions its contents can answer. Record its coverage, the evidence to look for and the boundary that matters to the user. Use the folder address supplied by the maker. If the address is missing, mark the field for completion.

Example configuration for a fictional service desk:

| Field | Value |
| --- | --- |
| Name | Equipment maintenance manuals |
| Description | Use these manuals for service intervals and inspection procedures. Match the equipment model and revision and cite the applicable section. For the date an inspection actually took place, consult service records. |
| Knowledge URL | <folder URL supplied by the maker> |

## Write instructions that survive content changes

- Put source selection, conversation context and citation rules in the agent instructions. Put a repeatable task such as interpreting a maintenance log in a skill. Add a reference when interpreting the document structure requires more detail.
- Find the current document by subject, scope and effective date. Use filenames in citations after retrieval. Keep volatile filenames out of routing rules.
- Check the unit, revision, date and scope against the question. For a table, read its headers along with the selected row. Carry those selections into follow-up questions and update the dimension the user changes.
- A manual specifies an interval. A dated service record establishes when work occurred. If the available evidence answers only part of the question, give that part and identify the missing record.
- Cite the document actually read. Include the section, sheet or page when visible. When sources disagree, explain which revisions and scopes differ before choosing a value.

## Deliver the configuration when requested

In BUILD mode, provide the agent instructions, the Name and Description to paste for each source, the corresponding folder URL or placeholder, and each required skill in its usable format. Include short setup steps mapping each item to its destination. Keep tenant-specific values in the maker's private configuration.

For a quick check, use a copy of the collection. Rename a document and repeat the same question. Then ask about a different model whose record is absent. Check that the first answer cites the renamed source and the follow-up identifies the missing evidence.
