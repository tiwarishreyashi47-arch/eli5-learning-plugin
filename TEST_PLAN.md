# ELI5 Plugin V0 — Friend Test Plan

## Objective
Test whether one plugin can help different non-technical learners understand different technical topics at the right depth while preserving curiosity-led conversation.

This V0 primarily tests:
1. Topic scoping into a 1-7 day learning sprint.
2. ELI5 / ELI15 / ELI30 level selection and recommendation.
3. Quality of explanation, Q&A, and question-led learning.
4. Optional practice questions.
5. Whether people naturally use Parking and find the booklet-ready summary useful.

V0 does **not** yet test durable cross-chat storage. A persistent Pocket/Booklet store belongs in V0.5.

## Suggested tester mix
Use 5 people with deliberately different goals. Do not assign them all the same topic.

| Tester archetype | Example topic | What this tests |
|---|---|---|
| Complete beginner | APIs, cloud, databases | Can ELI5 make jargon approachable without becoming childish? |
| Curious non-tech professional | APIs, AI agents, authentication | Does ELI15 explain end-to-end mechanics clearly? |
| Senior cross-functional stakeholder | system design, integrations, cloud infrastructure | Does ELI30 translate technical concepts into decisions, risks, dependencies, and questions to ask? |
| Interview-driven learner | webhooks, DevOps, security basics | Can the plugin move from definitions to application and articulation? |
| Self-directed / question-first learner | any topic they choose | Can someone learn effectively through Q&A or question-led mode rather than a prescribed lesson? |

## What to tell testers
Keep the instruction intentionally short:

> Pick one technical topic you've wanted to understand. Use this plugin naturally for at least 2 sessions. Choose whichever level you think fits you. You can ask questions, ask it to teach you through questions, park explanations that click, and optionally test yourself. Don't try to please the tool — use it the way you would actually learn.

## Session 1 checklist
Record whether the tester:
- could start without extra explanation from you;
- chose a level confidently;
- completed the diagnostic;
- agreed or disagreed with the recommended level;
- understood why the plugin made that recommendation;
- got a topic scope that felt achievable in 1-7 days;
- asked at least one natural follow-up;
- used Explain, Q&A, or Question-led mode;
- parked at least one explanation, or consciously chose not to;
- tried 2-5 practice questions, or consciously skipped them.

## Session 2+ checklist
Look for evidence of learning rather than novelty:
- Does the learner use terminology more accurately?
- Can they explain the concept without copying the plugin?
- Do their follow-up questions become more specific?
- Can they reason through a simple scenario or failure?
- Does the selected level still feel right?
- Do they return to parked material?
- Does the booklet summary help them remember the thread of learning?

## End-of-test questions for each friend
Ask these after at least 2 sessions:

1. What topic did you learn?
2. Which level did you initially choose: ELI5, ELI15, or ELI30?
3. What level did the plugin recommend? Did you accept it?
4. Did the explanation depth feel too simple, right, or too technical?
5. Which learning style did you use most: direct explanation, Q&A, or question-led?
6. Did the optional questions make you think differently from simply reading the explanation?
7. Did you park anything? If yes, what made you choose that passage?
8. Could you explain the core concept now without reopening the chat?
9. What part of the experience felt annoying, confusing, or unnecessary?
10. Would you voluntarily use this again for another technical topic? Why or why not?

## Quick scoring rubric
Score each dimension 1-5 after a tester has completed at least 2 sessions.

| Dimension | 1 | 3 | 5 |
|---|---|---|---|
| Level fit | Clearly wrong | Mostly usable | Feels tailored |
| Simplicity | Still confusing | Understandable | Immediately clear |
| Technical accuracy | Misleading | Mostly correct | Correct + appropriately qualified |
| End-to-end reasoning | Definitions only | Some connections | Can reason through flow / scenario |
| Practice quality | Generic trivia | Useful recall | Makes learner explain/apply |
| Conversation flexibility | Feels scripted | Some freedom | Learner drives path naturally |
| Parking usefulness | Not used / unclear | Occasionally useful | Captures memorable explanations |
| Return intent | Would not reuse | Maybe | Would use for another topic |

## Core V0 success criteria
With 5 testers, V0 is promising if:
- 4/5 can begin without your help;
- 4/5 say their final level felt appropriate;
- 4/5 can explain at least one learned concept in their own words after the session;
- at least 3/5 voluntarily use optional practice questions;
- at least 3/5 park something because the wording genuinely helped them;
- at least 4/5 say they would use it for another technical topic.

Do not over-index on satisfaction alone. A learner saying "this was fun" is weaker evidence than being able to explain or apply the concept afterwards.

## Issues to tag in feedback
Use these tags when you add feedback to the project thread:
- `LEVEL` — wrong depth or recommendation
- `SCOPE` — topic too broad/narrow
- `EXPLAIN` — clarity/analogy issue
- `Q&A` — answer quality or follow-up behaviour
- `SOCRATIC` — question-led mode issue
- `PRACTICE` — question quality/difficulty
- `PARK` — saving/wording issue
- `BOOKLET` — summary usefulness
- `UX` — confusing interaction or discoverability
- `ACCURACY` — technical error or unsupported claim

## Suggested experiment log format
For each piece of feedback, capture:

- Tester:
- Topic:
- Chosen level:
- Recommended level:
- Accepted recommendation? Y/N
- Session number:
- Feedback tag:
- What happened:
- What the tester expected:
- Severity: Low / Medium / High
- Proposed change (optional):

## API learning benchmark
Use the user's existing API Learning Journey test suite as a controlled reference benchmark before friend testing. It already tests explanation quality, API vs webhook reasoning, end-to-end architecture, acknowledgement vs business completion, idempotency, failure diagnosis, architecture-pattern distinctions, source fidelity, and boundary awareness.
