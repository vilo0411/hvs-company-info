---
name: content-feedback-loop
description: Automatically analyzes user feedback and revision logs to update Anti-AI rules and improve content quality over time.
---

# Skill: Content Feedback Learning Loop

## Overview
This skill acts as the "long-term memory" for the agent. It triggers after an article is finalized to ensure that user preferences and style corrections are captured and applied to future tasks.

## Workflow
1. **Trigger:** Triggered automatically after `/approve` or `pass` results in a file being moved to `3-finalized/`.
2. **Analysis:**
   - Read the **ENTIRE cumulative Revision Log** at the bottom of the finalized file.
   - Analyze the sequence of changes to identify evolving preferences or repeating errors.
   - Read user comments and feedback in the conversation history.
   - Identify patterns:
     - Specific words the user disliked (and what they replaced them with).
     - Tone adjustments (e.g., "too formal", "too robotic").
     - Structural preferences (e.g., "don't use sub-bullets").
3. **Consolidation:**
   - Compare findings with existing rules in `seo-strategy/resources/content-strategy/anti-ai-rules.md`.
   - Formulate new rules or vocabulary entries.
4. **User Confirmation:**
   - Present a summary of the learned patterns to the user.
   - Example: *"I noticed you consistently removed 'hành trình' and asked for more specific examples. Should I update the Anti-AI rules to reflect this?"*
5. **Update:**
   - Upon user approval, update `seo-strategy/resources/content-strategy/anti-ai-rules.md`.
   - Add an entry to the **Feedback Learning Log** section of that file.

## Rule for Future Content
- Every time `/write` or `/optimize` is triggered, the agent **MUST** read `anti-ai-rules.md` and adhere to its latest version.
- **Note:** Fresh articles without a Revision Log at the bottom of the file → skip this skill automatically.
