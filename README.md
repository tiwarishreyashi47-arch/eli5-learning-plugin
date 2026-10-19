# ELI5 Learning Companion

ELI5 Learning Companion is a lightweight technical learning companion for non-technical professionals who want usable technical fluency without needing a computer-science background.

It is designed for a practical outcome: helping someone understand a technical topic well enough to ask better questions, work with technical teammates, manage dependencies, and make informed decisions.

## The learning model

- **ELI5 — understand what it is:** approachable first principles and plain-language explanations.
- **ELI15 — understand how it works:** real terminology, components, and end-to-end flow.
- **ELI30 — understand how to work with it:** practical trade-offs, risks, dependencies, and questions to ask.

The companion scopes a topic into a **1–7 day learning sprint**, then uses a short 10-question diagnostic to recommend a starting depth. The learner can accept or override that recommendation.

## Core experience

Learners can move between:

- **Explain:** a direct explanation at the selected depth;
- **Q&A:** follow-up questions driven by the learner’s curiosity;
- **Question-led:** learning through guided questions rather than a lecture;
- **Practice:** optional checks that ask the learner to recall, explain, or apply an idea;
- **Parking:** save exact wording that genuinely clicked, without paraphrasing it;
- **Booklet output:** end a session with a structured, booklet-ready summary that preserves parked text exactly.

The intended loop is short enough to use between meetings, while still encouraging the learner to explain a concept in their own words.

## How to try it

This repository contains the early V0.1 plugin package and tester guidance. Start with a topic you actually want to understand, such as APIs, cloud systems, databases, AI agents, authentication, system design, DevOps, or security basics.

1. For local validation, run `python3 scripts/plugin_tool.py validate .`. To create the distributable archive, run `python3 scripts/plugin_tool.py package .`.
2. Say: `I want to learn [topic].`
3. Choose ELI5, ELI15, or ELI30, or let the diagnostic recommend one.
4. Ask for an explanation, use Q&A, or say `Teach me through questions.`
5. Optionally say `Test me` and choose a short practice set.
6. Say `Park this:` followed by exact text you want to keep.
7. Say `End session` when you want the booklet-ready output.

See [`START_HERE_FOR_TESTERS.md`](./START_HERE_FOR_TESTERS.md) for the short tester walkthrough and [`docs/testing/`](./docs/testing/) for the detailed plans.

The repository now includes a standard-library-only validator and packager in [`scripts/plugin_tool.py`](./scripts/plugin_tool.py). A passing static check confirms package structure and metadata only; it does not prove that a ChatGPT or Codex account can install or invoke the plugin.

## Current status: early V0.1

This is an early learning-behavior prototype. The current testing question is whether people with different starting points can choose an appropriate depth, learn through more than one interaction style, and explain or apply a concept afterward.

The package does not yet provide durable cross-chat storage. Testers should keep a topic in one conversation and copy or export the booklet output at the end of a session.

## Distribution constraint

An ordinary ChatGPT user cannot simply install an unpublished local plugin ZIP as a public plugin. Early testing therefore focuses on validating the learning behavior and session design in a supported development/plugin environment before solving broader distribution.

That constraint is an honest product-learning boundary, not a claim that the distribution model is finished. It helps keep the V0 question narrow: does the learning loop work before investing in packaging, persistence, and public availability?

## Repository contents

- `plugin.json` — package metadata and capability description;
- `START_HERE_FOR_TESTERS.md` — quick-start instructions;
- `docs/testing/` — friend-pilot and designer benchmark plans.

## Limitations and next questions

The prototype does not yet prove long-term retention, cross-chat memory, public distribution, or broad accessibility. Early feedback should focus on level fit, technical accuracy, question quality, usefulness of practice and parking, and whether learners would return for another topic.
