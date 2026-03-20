# github Skill Reference

**Source:** OpenClaw built-in skill  
**Location:** `~/AppData/Roaming/npm/node_modules/openclaw/skills/github/`

## Quick Reference

| Aspect | Details |
|--------|---------|
| **Purpose** | GitHub operations via `gh` CLI |
| **Tool** | `gh` command (not curl/API) |
| **Auth** | `gh auth login` (one-time) |
| **Emoji** | 🐙 |

## When to Use vs Not Use

**✅ USE for:**
- Checking PR status, reviews, merge readiness
- Viewing CI/workflow run status and logs
- Creating/closing/commenting on issues
- Creating or merging pull requests
- Querying GitHub API for repo data

**❌ DON'T USE for:**
- Local git operations (commit/push/pull) → use `git`
- Non-GitHub repos → different CLIs
- Cloning → use `git clone`
- Code review → use coding-agent
- Complex multi-file diffs → use coding-agent

## Setup

```bash
# Authenticate (one-time)
gh auth login

# Verify
gh auth status
```

## Pull Requests

```bash
# List PRs
gh pr list --repo owner/repo

# View PR details
gh pr view 55 --repo owner/repo

# Check CI status
gh pr checks 55 --repo owner/repo

# Create PR
gh pr create --title "feat: add feature" --body "Description"

# Merge PR
gh pr merge 55 --squash --repo owner/repo
```

## Issues

```bash
# List issues
gh issue list --repo owner/repo --state open

# Create issue
gh issue create --title "Bug: something broken" --body "Details..."

# Close issue
gh issue close 42 --repo owner/repo
```

## CI/Workflow Runs

```bash
# List recent runs
gh run list --repo owner/repo --limit 10

# View specific run
gh run view <run-id> --repo owner/repo

# View failed step logs only
gh run view <run-id> --repo owner/repo --log-failed

# Re-run failed jobs
gh run rerun <run-id> --failed --repo owner/repo
```

## API Queries

```bash
# Get PR with specific fields
gh api repos/owner/repo/pulls/55 --jq '.title, .state, .user.login'

# List all labels
gh api repos/owner/repo/labels --jq '.[].name'

# Get repo stats
gh api repos/owner/repo --jq '{stars: .stargazers_count, forks: .forks_count}'
```

## JSON Output & Filtering

```bash
# Structured output with jq filtering
gh issue list --repo owner/repo --json number,title \
  --jq '.[] | "\(.number): \(.title)"'

gh pr list --json number,title,state,mergeable \
  --jq '.[] | select(.mergeable == "MERGEABLE")'
```

## Templates

### PR Review Summary
```bash
PR=55 REPO=owner/repo
echo "## PR #$PR Summary"
gh pr view $PR --repo $REPO --json title,body,author,additions,deletions,changedFiles \
  --jq '"**\(.title)** by @\(.author.login)\n\n\(.body)\n\n📊 +\(.additions) -\(.deletions) across \(.changedFiles) files"'
gh pr checks $PR --repo $REPO
```

### Issue Triage
```bash
gh issue list --repo owner/repo --state open \
  --json number,title,labels,createdAt \
  --jq '.[] | "[\(.number)] \(.title) - \([.labels[].name] | join(", ")) (\(.createdAt[:10]))"'
```

## Notes

- Always specify `--repo owner/repo` when not in a git directory
- Can use URLs directly: `gh pr view https://github.com/owner/repo/pull/55`
- Rate limits apply; use `gh api --cache 1h` for repeated queries
