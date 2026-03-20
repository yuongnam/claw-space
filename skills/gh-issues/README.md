# gh-issues Skill Reference

**Source:** OpenClaw built-in skill  
**Location:** `~/AppData/Roaming/npm/node_modules/openclaw/skills/gh-issues/`

## Quick Reference

| Aspect | Details |
|--------|---------|
| **Purpose** | Auto-fetch GitHub issues, spawn sub-agents to fix, create PRs, handle reviews |
| **Trigger** | `/gh-issues [owner/repo] [flags]` |
| **API** | GitHub REST API via curl (NO gh CLI) |
| **Token** | `GH_TOKEN` env var |
| **Max concurrent** | 8 sub-agents |

## Usage Patterns

### Basic Usage
```bash
# Current repo
/gh-issues

# Specific repo
/gh-issues owner/repo

# With filters
/gh-issues owner/repo --label bug --limit 5
/gh-issues owner/repo --state open --assignee @me
```

### Watch Mode (Continuous)
```bash
# Poll every 5 minutes for new issues
/gh-issues owner/repo --watch --interval 5

# Poll for PR reviews only
/gh-issues owner/repo --watch --reviews-only
```

### Fork Mode
```bash
# Fork workflow: fetch from source, push to fork, PR to source
/gh-issues upstream/repo --fork myuser/repo
```

### Cron Mode (Headless)
```bash
# Fire-and-forget for scheduled runs
/gh-issues owner/repo --cron --yes
/gh-issues owner/repo --cron --reviews-only
```

## Key Flags Reference

| Flag | Default | Description |
|------|---------|-------------|
| `--label` | none | Filter by label |
| `--limit` | 10 | Max issues per poll |
| `--milestone` | none | Filter by milestone |
| `--assignee` | none | Filter by assignee (@me = self) |
| `--state` | open | open/closed/all |
| `--fork` | none | Your fork (user/repo) |
| `--watch` | false | Continuous polling |
| `--interval` | 5 | Minutes between polls |
| `--dry-run` | false | Preview only |
| `--yes` | false | Skip confirmation |
| `--reviews-only` | false | Skip issues, only handle PR reviews |
| `--cron` | false | Cron-safe mode (fire-and-forget) |
| `--model` | default | Model for sub-agents |
| `--notify-channel` | none | Telegram channel for notifications |

## Workflow Phases

1. **Parse Arguments** - Extract owner/repo, flags
2. **Fetch Issues** - GitHub API with filters
3. **Present & Confirm** - Show table, ask which to process
4. **Pre-flight Checks** - Dirty tree, remote access, existing PRs/branches
5. **Spawn Sub-agents** - Launch fix agents (up to 8 concurrent)
6. **PR Review Handler** - Check for review comments, spawn handlers

## Sub-agent Task Structure

Each sub-agent receives:
- Source repo (issues)
- Push repo (branches/PRs)
- Fork mode status
- Base branch
- Issue details (number, title, body, labels)

Sub-agent must:
1. Confidence check (skip if < 7/10)
2. Understand the issue
3. Create branch `fix/issue-{N}`
4. Analyze codebase
5. Implement minimal fix
6. Run tests
7. Commit and push
8. Create PR via API
9. Report results

## Review Handling

Reviews are checked from multiple sources:
- PR reviews (APPROVED, CHANGES_REQUESTED, COMMENTED)
- Inline/file-level comments
- General issue comments
- Embedded reviews in PR body (e.g., Greptile)

Actionable comments trigger review-fix sub-agents.

## In-Progress Tracking

Prevents duplicate work via:
- **PR check** - Skip if PR already exists
- **Branch check** - Skip if branch exists on push repo
- **Claims file** - Track recently claimed issues (2hr timeout)
- **Cursor file** (cron) - Sequential processing with state

## Common Patterns

### Pattern: Batch Fix
```bash
/gh-issues owner/repo --label "good first issue" --limit 10 --yes
```

### Pattern: Monitor & Fix
```bash
/gh-issues owner/repo --watch --interval 10 --label bug
```

### Pattern: Review Bot
```bash
/gh-issues owner/repo --watch --reviews-only
```

### Pattern: Cron Job
```bash
# Daily at 9 AM
openclaw cron add --name gh-issues-daily \
  --command "/gh-issues owner/repo --cron --label bug" \
  --schedule "0 9 * * *"
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "GitHub authentication failed" | Check GH_TOKEN env var or openclaw.json |
| "No issues found" | Check filters, try --state all |
| "PR already exists" | Normal - prevents duplicates |
| Sub-agent times out | Issue may be too complex |
| Branch exists but no PR | Sub-agent still working or failed |

## Security Notes

- Never log full GH_TOKEN
- Use x-access-token auth for git push
- Claims file prevents duplicate processing
- Check PR existence before creating
