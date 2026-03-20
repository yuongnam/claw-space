# node-connect Skill Reference

**Source:** OpenClaw built-in skill  
**Location:** `~/AppData/Roaming/npm/node_modules/openclaw/skills/node-connect/`

## Quick Reference

| Aspect | Details |
|--------|---------|
| **Purpose** | Diagnose OpenClaw node (Android/iOS/macOS) connection failures |
| **Issues fixed** | QR failures, pairing errors, auth problems |
| **Topology** | Same machine, LAN, Tailscale, public URL |

## Network Topology Types

**Must pick ONE and stick to it:**

1. **Same machine / emulator / USB tunnel** — Local development
2. **Same LAN / local Wi-Fi** — Home/office network
3. **Same Tailscale tailnet** — VPN mesh network
4. **Public URL / reverse proxy** — Internet accessible

**Rule:** Don't mix them. Fix the route first, then debug pairing.

## Diagnostic Commands

### Gateway Configuration
```bash
# Core settings
openclaw config get gateway.mode
openclaw config get gateway.bind
openclaw config get gateway.tailscale.mode
openclaw config get gateway.remote.url
openclaw config get gateway.auth.mode
openclaw config get gateway.auth.allowTailscale
openclaw config get plugins.entries.device-pair.config.publicUrl
```

### Setup Code Generation
```bash
# Local setup code
openclaw qr --json

# Remote gateway setup code
openclaw qr --remote --json
```

### Device Status
```bash
# List devices
openclaw devices list

# Approve latest pending device
openclaw devices approve --latest

# Node status
openclaw nodes status
```

### Tailscale (if applicable)
```bash
tailscale status --json
```

## Understanding `openclaw qr --json` Output

Key fields:
- `gatewayUrl` — Actual endpoint the app should use
- `urlSource` — Which config path won (tells you which mode is active)

### Good Sources

| Source | Meaning |
|--------|---------|
| `gateway.bind=lan` | Same Wi-Fi/LAN only |
| `gateway.bind=tailnet` | Direct tailnet access |
| `gateway.tailscale.mode=serve/funnel` | Tailscale route |
| `plugins.entries.device-pair.config.publicUrl` | Public/reverse-proxy route |
| `gateway.remote.url` | Remote gateway route |

## Error Messages & Fixes

### "Gateway is only bound to loopback"
**Cause:** Remote node can't connect  
**Fix:**
```bash
# Same LAN
openclaw config set gateway.bind lan

# Tailscale
openclaw config set gateway.tailscale.mode serve

# Public URL
openclaw config set plugins.entries.device-pair.config.publicUrl https://your-domain.com
```

Then: restart gateway, generate fresh QR, rescan

### "gateway.bind=tailnet set, but no tailnet IP was found"
**Cause:** Gateway host not on Tailscale  
**Fix:** Install and authenticate Tailscale on gateway host

### "qr --remote requires gateway.remote.url"
**Cause:** Remote-mode config incomplete  
**Fix:**
```bash
openclaw config set gateway.remote.url https://gateway.example.com
```

### "Pairing required"
**Cause:** Network/auth worked, device pending approval  
**Fix:**
```bash
openclaw devices list
openclaw devices approve --latest
```

### "Bootstrap token invalid or expired"
**Cause:** Old setup code  
**Fix:** Generate fresh setup code and rescan:
```bash
openclaw qr --json
```

### "Unauthorized"
**Cause:** Wrong token/password or Tailscale mismatch  
**Fix:**
- Check `gateway.auth.allowTailscale` matches intended flow
- Use explicit token/password if not using Tailscale

## Fast Heuristics

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| Same WiFi + gateway advertises `127.0.0.1` | Loopback-only config | Use `gateway.bind=lan` or Tailscale |
| Remote setup + setup uses private LAN IP | Wrong network topology | Use public URL or Tailscale |
| Tailnet setup + gateway advertises LAN IP | Wrong bind mode | Use `gateway.bind=tailnet` or Tailscale mode |
| Public URL set but QR shows something else | Check `urlSource` | Config priority issue |
| Pending devices in list | Need approval | `openclaw devices approve` |

## Fix Style

**Good diagnosis:**
> "The gateway is still loopback-only, so a node on another network can never reach it. Enable Tailscale Serve, restart the gateway, run `openclaw qr` again, rescan, then approve the pending device pairing."

**Bad diagnosis:**
> "Maybe LAN, maybe Tailscale, maybe port forwarding, maybe public URL."

## Workflow

1. **Identify topology** — Same machine, LAN, Tailscale, or public?
2. **Run diagnostics** — `openclaw qr --json`, check `urlSource`
3. **Match config to topology** — Fix bind mode, URLs, Tailscale
4. **Restart gateway** — Apply configuration changes
5. **Generate fresh QR** — `openclaw qr --json`
6. **Rescan with app** — Use new setup code
7. **Approve device** — `openclaw devices approve --latest`

## Key Configuration Paths

### For Local/LAN Access
```bash
openclaw config set gateway.bind lan
```

### For Tailscale Access
```bash
# Option A: Direct tailnet
openclaw config set gateway.bind tailnet

# Option B: Tailscale Serve (preferred for sharing)
openclaw config set gateway.tailscale.mode serve
# or
openclaw config set gateway.tailscale.mode funnel  # public internet via Tailscale
```

### For Public/Remote Access
```bash
# Via reverse proxy
openclaw config set plugins.entries.device-pair.config.publicUrl https://your-domain.com

# Via remote gateway
openclaw config set gateway.remote.url https://gateway.example.com
```

## Security Notes

- Verify the gateway URL is what you expect before scanning
- Don't approve unknown devices
- Tailscale auth is more secure than password tokens
- Funnel mode exposes to public internet — use with caution
