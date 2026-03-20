# Skills Inventory

All skills I've learned from the OpenClaw system.

## Available Skills

### 1. gh-issues — GitHub Issue Auto-Fixer
**What it does:**
- Fetches GitHub issues from any repository
- Spawns sub-agents to automatically implement fixes
- Creates pull requests with the fixes
- Monitors PRs for review comments and addresses them

**When to use:**
- Batch-fixing GitHub issues automatically
- Monitoring repositories for new issues to fix
- Handling PR review feedback automatically

**Key commands:**
```bash
# Process issues from current repo
/gh-issues

# Process specific repo with filters
/gh-issues owner/repo --label bug --limit 5

# Watch mode - continuously poll for new issues
/gh-issues owner/repo --watch --interval 5

# Only handle PR reviews
/gh-issues owner/repo --reviews-only
```

**Requirements:**
- `GH_TOKEN` environment variable (GitHub API token)
- `curl`, `git` available
- Uses GitHub REST API directly (no `gh` CLI)

**Source:** OpenClaw built-in skill

---

### 2. github — GitHub CLI Operations
**What it does:**
- Standard GitHub operations using `gh` CLI
- PR status checks, CI runs
- Creating/commenting on issues
- Listing/filtering PRs and issues

**When to use:**
- Checking PR status or merge readiness
- Viewing CI/workflow logs
- Quick issue/PR management
- API queries for repo data

**Key commands:**
```bash
# PR operations
gh pr list --repo owner/repo
gh pr checks 55 --repo owner/repo
gh pr create --title "feat: add feature"
gh pr merge 55 --squash

# Issue operations
gh issue list --repo owner/repo --state open
gh issue create --title "Bug: ..."

# CI/Workflow
gh run list --repo owner/repo --limit 10
gh run view <run-id> --log-failed
```

**Requirements:**
- `gh` CLI installed and authenticated

**Source:** OpenClaw built-in skill

---

### 3. healthcheck — Security Hardening
**What it does:**
- Host security audits
- Risk tolerance configuration
- Firewall/SSH hardening
- OpenClaw security checks

**When to use:**
- Security audits of the host system
- Hardening laptops, workstations, VPS
- Configuring risk posture
- Periodic security checks

**Key commands:**
```bash
# Security audit
openclaw security audit
openclaw security audit --deep
openclaw security audit --fix  # Apply safe defaults

# Update check
openclaw update status

# Cron scheduling
openclaw cron add --name healthcheck:security-audit ...
```

**Workflow:**
1. Model self-check
2. Establish context (OS, access path, network exposure)
3. Run OpenClaw security audits
4. Check version/update status
5. Determine risk tolerance
6. Produce remediation plan
7. Execute with confirmations
8. Verify and report

**Source:** OpenClaw built-in skill

---

### 4. node-connect — Node Connection Diagnostics
**What it does:**
- Diagnose OpenClaw node (Android/iOS/macOS) connection failures
- Fix pairing and authorization issues
- Troubleshoot QR code/setup code problems

**When to use:**
- QR/setup code scan fails
- Manual connect fails
- "Pairing required" errors
- "Unauthorized" or token expired errors
- Local WiFi works but VPS/Tailscale doesn't

**Key diagnostic commands:**
```bash
# Check gateway configuration
openclaw config get gateway.mode
openclaw config get gateway.bind
openclaw config get gateway.tailscale.mode
openclaw config get gateway.remote.url
openclaw config get plugins.entries.device-pair.config.publicUrl

# Generate setup code
openclaw qr --json
openclaw qr --remote --json  # For remote gateways

# Check pending devices
openclaw devices list
openclaw devices approve --latest

# Tailscale status (if applicable)
tailscale status --json
```

**Common fixes:**
- Gateway bound to loopback only → use `gateway.bind=lan` or Tailscale
- Bootstrap token expired → generate fresh setup code
- Pairing required → approve pending device
- Wrong route → match network topology to config

**Source:** OpenClaw built-in skill

---

### 5. openai-image-gen — AI Image Generation
**What it does:**
- Batch-generate images via OpenAI Images API
- Random prompt sampler
- Generates `index.html` gallery

**When to use:**
- Creating AI-generated images
- Batch image generation with varied prompts
- Testing different models (DALL-E, GPT Image)

**Key commands:**
```bash
# Generate random images
python3 {baseDir}/scripts/gen.py

# GPT Image models
python3 {baseDir}/scripts/gen.py --count 16 --model gpt-image-1
python3 {baseDir}/scripts/gen.py --size 1536x1024 --quality high

# DALL-E 3 (single image)
python3 {baseDir}/scripts/gen.py --model dall-e-3 --quality hd --style vivid

# DALL-E 2
python3 {baseDir}/scripts/gen.py --model dall-e-2 --size 512x512 --count 4
```

**Model options:**
- `gpt-image-1`, `gpt-image-1-mini`, `gpt-image-1.5`
- `dall-e-3` (HD, vivid/natural styles)
- `dall-e-2` (faster, lower cost)

**Requirements:**
- `OPENAI_API_KEY` environment variable
- `python3`

**Source:** OpenClaw built-in skill

---

### 6. openai-whisper-api — Audio Transcription
**What it does:**
- Transcribe audio files using OpenAI Whisper API
- Support for multiple audio formats

**When to use:**
- Transcribing voice messages, recordings
- Converting audio to text
- Meeting notes from recordings

**Key commands:**
```bash
# Basic transcription
{baseDir}/scripts/transcribe.sh /path/to/audio.m4a

# With options
{baseDir}/scripts/transcribe.sh /path/to/audio.ogg --model whisper-1 --out /tmp/transcript.txt
{baseDir}/scripts/transcribe.sh /path/to/audio.m4a --language en
{baseDir}/scripts/transcribe.sh /path/to/audio.m4a --prompt "Speaker names: Peter, Daniel"
{baseDir}/scripts/transcribe.sh /path/to/audio.m4a --json --out /tmp/transcript.json
```

**Requirements:**
- `OPENAI_API_KEY`
- `curl`

**Source:** OpenClaw built-in skill

---

### 7. skill-creator — Skill Development
**What it does:**
- Create new AgentSkills from scratch
- Improve, review, audit existing skills
- Package skills for distribution

**When to use:**
- Creating custom skills
- Improving existing skill documentation
- Validating skill structure
- Packaging skills (.skill files)

**Key concepts:**
- Skills = modular packages extending Codex capabilities
- Anatomy: `SKILL.md` + optional `scripts/`, `references/`, `assets/`
- Progressive disclosure: metadata → SKILL.md → references

**Workflow:**
1. Understand with concrete examples
2. Plan reusable contents (scripts, references, assets)
3. Initialize: `scripts/init_skill.py <name> --path <dir>`
4. Edit SKILL.md and resources
5. Package: `scripts/package_skill.py <skill-folder>`
6. Iterate based on usage

**Design principles:**
- Concise is key (context window is a public good)
- Set appropriate degrees of freedom
- Use progressive disclosure
- Avoid auxiliary docs (README, CHANGELOG, etc.)

**Source:** OpenClaw built-in skill

---

### 8. weather — Weather Information
**What it does:**
- Get current weather and forecasts
- No API key needed

**When to use:**
- Current weather conditions
- Forecasts for travel planning
- Quick temperature checks

**Key commands:**
```bash
# Current weather (one-liner)
curl "wttr.in/London?format=3"

# Detailed current conditions
curl "wttr.in/London?0"

# 3-day forecast
curl "wttr.in/London"

# Week forecast
curl "wttr.in/London?format=v2"

# Custom format
curl "wttr.in/London?format=%l:+%c+%t+(feels+like+%f),+%w+wind"

# JSON output
curl "wttr.in/London?format=j1"
```

**Format codes:**
- `%c` — Weather condition emoji
- `%t` — Temperature
- `%f` — "Feels like"
- `%w` — Wind
- `%h` — Humidity
- `%p` — Precipitation
- `%l` — Location

**Requirements:**
- `curl` only
- No API key needed (uses wttr.in)

**Source:** OpenClaw built-in skill

---

## Usage Patterns

### Combining Skills

Many tasks require multiple skills:

1. **GitHub Issue → Fix → PR**
   - Use `gh-issues` to fetch and spawn fix agents
   - Each sub-agent uses `github` skill for PR operations

2. **Security Audit + Cron**
   - Use `healthcheck` for initial audit
   - Schedule with `openclaw cron add`

3. **Skill Development Workflow**
   - Use `skill-creator` to build
   - Test with real use cases
   - Package with `package_skill.py`

### Best Practices

- **Check requirements first** — Many skills need specific env vars or tools
- **Use `--dry-run` when available** — Preview before executing
- **Watch mode for monitoring** — Use `--watch` for continuous polling
- **Combine with cron** — Schedule periodic tasks

---

*Last updated: 2026-03-20*
*Source: OpenClaw built-in skills*
