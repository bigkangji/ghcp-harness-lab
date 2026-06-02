# ADR 0001: Decision Log Format

## Status

Draft

## Context

The `decide` CLI needs a file format that is easy to inspect in git and simple
to update with the Python standard library.

## Decision

Start with a line-oriented markdown format. `/grill-with-docs` may refine the
exact line syntax before implementation begins.

## Consequences

- Tests should assert behavior through CLI output and file content.
- The format should avoid hidden metadata that a human reviewer cannot read.
- If future features need stable IDs, they should be added through a new ADR.