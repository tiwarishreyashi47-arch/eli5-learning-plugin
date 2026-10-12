# ELI5 Plugin V0 — Shreyashi Test Plan

## Main question
Can one plugin help different non-technical people learn different technical concepts at an appropriate depth — and leave them better able to explain or apply the concept rather than merely enjoy the explanation?

## What V0 is testing
V0 tests six things:
1. **Scope:** Can the plugin turn a topic into a realistic 1-7 day learning sprint?
2. **Level:** Do ELI5 / ELI15 / ELI30 feel meaningfully different, and is the diagnostic recommendation useful?
3. **Conversation:** Can people move naturally among explanation, Q&A, and question-led learning?
4. **Practice:** Do optional 2-5 question checks improve thinking and recall?
5. **Parking:** Do learners naturally save wording that genuinely helped them understand something?
6. **Learning outcome:** Can they explain or reason about the concept afterwards?

V0 does **not** test durable cross-chat storage. That belongs in V0.5.

---

## Phase 0 — Your controlled benchmark
Before sending it to friends, use your API learning journey as the reference case.

Run the existing API benchmark prompts and score each response from 0-2 on:
- source fidelity;
- simplicity;
- technical accuracy;
- boundary awareness;
- useful structure.

**Pass condition:** no invented personal implementation claims, and an average of at least 8/10 across the benchmark.

Then use the plugin yourself on a fresh topic you currently do **not** know well — ideally cloud infrastructure, DevOps, or security basics — so you experience the plugin as a learner rather than as its designer.

---

## Phase 1 — Five-person pilot
Choose five people with deliberately different starting points.

| Tester | Profile to target | Example topic | Primary thing to observe |
|---|---|---|---|
| 1 | Complete beginner | APIs / cloud / databases | Does ELI5 remove jargon without becoming childish? |
| 2 | Curious non-tech professional | AI agents / authentication | Does ELI15 make end-to-end mechanics understandable? |
| 3 | Senior cross-functional stakeholder | system design / integrations | Does ELI30 translate tech into dependencies, risks and decisions? |
| 4 | Interview-driven learner | DevOps / security / webhooks | Can learning move from definition to articulation/application? |
| 5 | Question-first learner | topic of their choice | Can someone learn primarily through Q&A/Socratic interaction? |

Do not give everyone APIs. Cross-topic performance is part of the test.

---

## What to capture for every tester
### Before first session
- Topic
- Why they want to learn it
- Chosen level: ELI5 / ELI15 / ELI30
- Self-rated knowledge before session: 1-5

### Diagnostic
- Recommended level
- Did they accept it? Y/N
- Did the recommendation feel correct? 1-5
- Did any question feel badly calibrated?

### During each session
Capture only meaningful observations:
- Did they ask natural follow-ups?
- Did they switch between Learn / Q&A / question-led interaction?
- Did the plugin become too verbose or too shallow?
- Did they park anything? What kind of wording was parked — analogy, definition, flow, practical checklist?
- Did they choose optional practice?
- Were practice questions recall, explanation, or application heavy?
- Did a wrong answer lead to a useful correction?

### End of session
Ask the learner to explain **one important concept in their own words without looking back at the chat**. Record the answer or your assessment.

---

## Minimum test duration
Ask each friend for **2 sessions** on the same topic.

One session can show novelty. Two sessions begin to show whether the plugin supports actual learning and return behaviour.

A 3rd-5th session is useful but not required for V0.

---

## End-of-pilot interview — 10 questions
1. What did you learn?
2. What level did you choose initially?
3. What level did the plugin recommend?
4. Was the final depth too simple, right, or too technical?
5. Which did you use most: explanation, Q&A, or question-led learning?
6. Did answering questions make you think differently from just reading?
7. Did you park anything? What made that wording worth saving?
8. Can you explain the central concept now without reopening the chat?
9. What felt annoying, confusing, repetitive, or unnecessary?
10. Would you voluntarily use this for a different technical topic?

---

## Scorecard
Score 1-5 after at least two sessions.

| Dimension | What a 5 means |
|---|---|
| Level fit | Depth felt tailored to the learner and topic |
| Clarity | Difficult ideas became understandable without distortion |
| Technical accuracy | Correct, appropriately qualified, no invented facts |
| End-to-end reasoning | Learner understands relationships, not isolated definitions |
| Practice quality | Questions make the learner retrieve, explain, or apply knowledge |
| Conversation flexibility | Learner can drive the path without fighting the workflow |
| Parking usefulness | Saved text genuinely helps recall/understanding |
| Learning outcome | Learner can explain/apply the idea independently |
| Return intent | Learner would choose the plugin again for another topic |

---

## V0 success criteria
With five testers, call V0 promising if:
- **4/5** can start without you coaching them;
- **4/5** say the eventual level felt appropriate;
- **4/5** can explain at least one core concept in their own words after learning;
- **3/5** voluntarily use the optional practice feature;
- **3/5** park at least one explanation because the wording helped;
- **4/5** would use it again for another technical topic.

Do not use “they liked it” as the main success criterion. Evidence of independent explanation/application matters more.

---

## Feedback tags for this thread
When you bring feedback back here, prefix it with one tag:

- `LEVEL` — depth or recommendation problem
- `SCOPE` — topic plan too broad/narrow
- `EXPLAIN` — explanation/analogy issue
- `Q&A` — answer/follow-up issue
- `SOCRATIC` — question-led learning issue
- `PRACTICE` — practice question issue
- `PARK` — saving behaviour issue
- `BOOKLET` — summary/output issue
- `UX` — confusing interaction
- `ACCURACY` — technical error or unsupported claim

Example:

`PRACTICE — Tester 3 / System design / ELI30 / Session 2: questions were mostly definition recall; she wanted scenario-based trade-offs.`

That will let us turn feedback into product decisions rather than a pile of anecdotes.
