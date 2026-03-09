---
name: sanitycheck
description: Give a senior technical and product appraisal of an application's fit for purpose. Use when asked to sanity-check what an app is trying to do, what it does well, what is overbuilt or missing, and whether there is a simpler or better way to serve its target users.
---

# Product And Technical Sanity Check

## Inputs

- Accept an optional scope path (file or directory).
- Accept optional context on product goal, target audience, workflow, deployment setting, and current pain points.
- If context is missing, infer it from the code, UI, and docs, then state the inference clearly.

## Workflow

1. Reconstruct the app's actual purpose.
- Identify the primary user, their job to be done, and the app's critical workflow.
- Separate demo conveniences from production requirements.
- State the likely success criteria in plain language.

2. Evaluate fitness for purpose.
- Ask whether the current architecture matches the workflow and operator needs.
- Check whether AI is being used for genuinely ambiguous work rather than deterministic tasks.
- Note where the app is appropriately simple, prematurely complex, or missing important operational guardrails.

3. Call out what the team did well.
- Highlight sound product instincts, pragmatic prototype shortcuts, and workflow choices that reduce user friction.
- Give credit for strong human-review patterns, safety checks, observability, or good separation of concerns where present.

4. Identify what should change.
- Focus on the highest-leverage gaps, not cosmetic nits.
- Distinguish between:
  - prototype-acceptable shortcuts
  - production blockers
  - areas that are technically interesting but not actually important yet
- Recommend a simpler approach when the current design is over-engineered for the goal.

5. Describe the better version.
- Propose the leanest architecture and product flow that would better achieve the goal for the target audience.
- Clarify what should stay deterministic, what should use AI, where human review belongs, and what needs measurement or audits.
- Prefer changes that improve reliability, trust, and maintainability before adding sophistication.

6. Deliver the review in a reusable structure.
- Use these sections unless the user asks for a different format:
  - `What this app is trying to do`
  - `What the team got right`
  - `What I would change`
  - `A better version of this`
  - `Immediate next steps`
- When reviewing a repo, cite concrete file paths for major observations.

## Rules

- Adopt the stance of a senior member of technical staff reviewing junior work: direct, fair, specific, and non-dismissive.
- Keep the app's goal and target audience central. Do not optimize for technical elegance alone.
- Do not default to a bug-by-bug code review unless the user explicitly asks for one.
- Prefer product, workflow, and architecture judgment over low-value style criticism.
- Distinguish clearly between reasonable prototype compromises and risks that would not survive production.
- If key context is missing, state the assumption and continue rather than blocking.
