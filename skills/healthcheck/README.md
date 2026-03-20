# healthcheck Skill Reference

**Source:** OpenClaw built-in skill  
**Location:** `~/AppData/Roaming/npm/node_modules/openclaw/skills/healthcheck/`

## Quick Reference

| Aspect | Details |
|--------|---------|
| **Purpose** | Host security hardening and risk configuration |
| **Use case** | Security audits, firewall hardening, SSH hardening |
| **Target** | Laptops, workstations, Pi, VPS running OpenClaw |

## Core Rules

- Require explicit approval before state-changing actions
- Never modify remote access without confirming connection method
- Prefer reversible, staged changes
- OpenClaw does NOT change host firewall/SSH/OS updates
- Format choices as numbered options

## Workflow

### Phase 0: Model Self-Check
Recommend state-of-the-art model (Opus 4.5+, GPT 5.2+)

### Phase 1: Establish Context
Determine:
1. OS and version (Linux/macOS/Windows), container vs host
2. Privilege level (root/admin vs user)
3. Access path (local, SSH, RDP, tailnet)
4. Network exposure (public IP, reverse proxy, tunnel)
5. OpenClaw gateway status and bind address
6. Backup system status
7. Deployment context
8. Disk encryption status
9. OS automatic security updates status
10. Usage mode (personal workstation vs headless/remote)

### Phase 2: OpenClaw Security Audits
```bash
# Run audit
openclaw security audit
openclaw security audit --deep

# Apply safe defaults (requires approval)
openclaw security audit --fix
```

**Note:** `--fix` only tightens OpenClaw defaults and permissions. Does NOT change host firewall, SSH, or OS policies.

### Phase 3: Version Check
```bash
openclaw update status
```

### Phase 4: Risk Tolerance Profiles

| Profile | Description |
|---------|-------------|
| **1. Home/Workstation Balanced** | Firewall on, remote access restricted to LAN/tailnet |
| **2. VPS Hardened** | Deny-by-default, minimal ports, key-only SSH, no root login |
| **3. Developer Convenience** | More local services allowed, explicit exposure warnings |
| **4. Custom** | User-defined constraints |

### Phase 5: Remediation Plan
Includes:
- Target profile
- Current posture summary
- Gaps vs target
- Step-by-step remediation with exact commands
- Access-preservation strategy and rollback
- Risks and potential lockout scenarios
- Least-privilege notes
- Credential hygiene notes

### Phase 6: Execution Options
1. **Do it for me** — Guided, step-by-step approvals
2. **Show plan only** — View without executing
3. **Fix only critical issues** — Minimal hardening
4. **Export commands for later** — Save for manual execution

### Phase 7: Execute with Confirmations
For each step:
- Show exact command
- Explain impact and rollback
- Confirm access remains available
- Stop on unexpected output

### Phase 8: Verify and Report
Re-check:
- Firewall status
- Listening ports
- Remote access works
- OpenClaw security audit

## Periodic Checks

### Baseline Audit
```bash
openclaw security audit
openclaw security audit --deep
openclaw update status
```

### Cron Scheduling
```bash
# Schedule periodic audits
openclaw cron add --name healthcheck:security-audit \
  --command "openclaw security audit" \
  --schedule "0 9 * * 1"  # Weekly Monday 9 AM

# Schedule update checks
openclaw cron add --name healthcheck:update-status \
  --command "openclaw update status" \
  --schedule "0 9 * * *"  # Daily 9 AM
```

Use exact job names for deterministic updates.

## Required Confirmations

Always require approval for:
- Firewall rule changes
- Opening/closing ports
- SSH/RDP configuration changes
- Installing/removing packages
- Enabling/disabling services
- User/group modifications
- Scheduling tasks
- Update policy changes
- Access to sensitive files

## Supported Commands

- `openclaw security audit [--deep] [--fix] [--json]`
- `openclaw status [--deep]`
- `openclaw health [--json]`
- `openclaw update status`
- `openclaw cron add|list|runs|run`

## Memory Writes

Only write to memory files when:
- User explicitly opts in
- Session is private/local workspace

Write to `memory/YYYY-MM-DD.md`:
- What was checked
- Key findings
- Actions taken
- Scheduled cron jobs
- Key decisions
- Commands executed (redacted)

Update `MEMORY.md` for durable preferences (risk posture, allowed ports, update policy).

## Common OS Checks

### Linux
```bash
# OS version
cat /etc/os-release

# Listening ports
ss -ltnup

# Firewall
ufw status
firewall-cmd --state
nft list ruleset
```

### macOS
```bash
# OS version
sw_vers

# Listening ports
lsof -nP -iTCP -sTCP:LISTEN

# Firewall
/usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate
pfctl -s info

# Backups
tmutil status
```

## Security Notes

- Never log tokens or full credentials
- Redact: usernames, hostnames, IPs, serials, service names
- Verify backup status before hardening
- Always have rollback plan for remote access changes
