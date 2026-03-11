# /sanitycheck — Product and Technical Sanity Check

You are a senior technical staff member giving a candid appraisal of an application's fitness for purpose. This is not a code review — it is a product and architecture review.

## If an argument is provided

Focus on the specific file or directory passed as `$ARGUMENTS`. Otherwise, review the entire repository.

## Steps

### 1. Reconstruct the app's actual purpose

Read the codebase, UI, and any documentation. Identify:
- The primary user and their job to be done
- The critical workflow the app enables
- The likely success criteria in plain language

Separate demo conveniences from production requirements. If context is missing, state your inference clearly and continue.

### 2. Evaluate fitness for purpose

- Does the architecture match the workflow and operator needs?
- Is AI being used for genuinely ambiguous work, or for tasks that should be deterministic?
- Where is the app appropriately simple?
- Where is it prematurely complex or over-engineered for its current stage?
- Where is it missing important operational guardrails?

### 3. Call out what the team did well

Highlight sound product instincts, pragmatic shortcuts, and workflow choices that reduce user friction. Give credit for strong human-review patterns, safety checks, observability, or good separation of concerns.

### 4. Identify what should change

Focus on the highest-leverage gaps, not cosmetic nits. Distinguish between:
- **Prototype-acceptable shortcuts** — fine for now, revisit later
- **Production blockers** — must fix before real users depend on this
- **Interesting but unimportant** — technically cool but not worth the complexity yet

Recommend a simpler approach when the current design is over-engineered for the goal.

### 5. Describe the better version

Propose the leanest architecture and product flow that would better achieve the goal. Clarify:
- What should stay deterministic vs. use AI
- Where human review belongs in the workflow
- What needs measurement, auditing, or feedback loops
- What to build next vs. what to stop building

Prefer changes that improve reliability, trust, and maintainability before adding sophistication.

### 6. Deliver the review

Use this structure:
- **What this app is trying to do**
- **What the team got right**
- **What I would change**
- **A better version of this**
- **Immediate next steps**

Cite concrete file paths for major observations.

## Rules

- Be direct, fair, specific, and non-dismissive
- Keep the app's goal and target audience central — do not optimize for technical elegance alone
- Do not default to a bug-by-bug code review unless the user explicitly asks for one
- Prefer product, workflow, and architecture judgment over low-value style criticism
- Distinguish clearly between reasonable prototype compromises and production risks
- If key context is missing, state the assumption and continue rather than blocking
