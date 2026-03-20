# weather Skill Reference

**Source:** OpenClaw built-in skill  
**Location:** `~/AppData/Roaming/npm/node_modules/openclaw/skills/weather/`

## Quick Reference

| Aspect | Details |
|--------|---------|
| **Purpose** | Get current weather and forecasts |
| **Source** | wttr.in (no API key needed) |
| **Emoji** | ☔ |
| **Requires** | `curl` only |

## When to Use

**✅ USE for:**
- "What's the weather?"
- "Will it rain today/tomorrow?"
- "Temperature in [city]"
- "Weather forecast for the week"
- Travel planning weather checks

**❌ DON'T USE for:**
- Historical weather data → use archives
- Climate analysis/trends → use specialized sources
- Hyper-local microclimate → use local sensors
- Severe weather alerts → check official sources
- Aviation/marine weather → use METAR/METEO

## Location Required

**Always include a location** — city, region, or airport code.

## Commands

### Current Weather

```bash
# One-line summary
curl "wttr.in/London?format=3"
# Output: London: ⛅️ +19°C

# Detailed current conditions
curl "wttr.in/London?0"

# Specific city (spaces become +)
curl "wttr.in/New+York?format=3"
```

### Forecasts

```bash
# 3-day forecast (default)
curl "wttr.in/London"

# Week forecast
curl "wttr.in/London?format=v2"

# Specific day
# 0 = today, 1 = tomorrow, 2 = day after
curl "wttr.in/London?0"  # Today
curl "wttr.in/London?1"  # Tomorrow
curl "wttr.in/London?2"  # Day after tomorrow
```

### Format Options

```bash
# One-liner custom format
curl "wttr.in/London?format=%l:+%c+%t+%w"

# JSON output (for parsing)
curl "wttr.in/London?format=j1"

# PNG image (for display)
curl "wttr.in/London.png" -o weather.png
```

## Format Codes

| Code | Meaning |
|------|---------|
| `%c` | Weather condition emoji |
| `%t` | Temperature |
| `%f` | "Feels like" temperature |
| `%w` | Wind |
| `%h` | Humidity |
| `%p` | Precipitation |
| `%l` | Location name |
| `%m` | Moon phase |
| `%M` | Moon day |
| `%u` | UV index |

## Quick Response Patterns

### "What's the weather?"
```bash
curl -s "wttr.in/London?format=%l:+%c+%t+(feels+like+%f),+%w+wind,+%h+humidity"
# London: ⛅️ +19°C (feels like +18°C), ↙15km/h wind, 64% humidity
```

### "Will it rain?"
```bash
curl -s "wttr.in/London?format=%l:+%c+%p"
# London: ⛅️ 0mm  (or shows precipitation amount)
```

### "Weekend forecast"
```bash
# Visual format with charts
curl "wttr.in/London?format=v2"
```

### "Detailed forecast"
```bash
# Full terminal output
curl "wttr.in/London"
# Shows: current conditions + 3-day forecast
#        + wind + temperature graph + precipitation
```

## Airport Codes

Use IATA airport codes for locations:

```bash
curl "wttr.in/JFK"    # New York JFK
curl "wttr.in/LHR"    # London Heathrow
curl "wttr.in/HND"    # Tokyo Haneda
curl "wttr.in/ICN"    # Seoul Incheon
```

## Special Options

```bash
# No colors (for scripts)
curl "wttr.in/London?u"    # u = US units (Fahrenheit, mph)
curl "wttr.in/London?m"    # m = metric (default)
curl "wttr.in/London?M"    # M = metric, no colors

# Narrow output
curl "wttr.in/London?n"

# Wide output
curl "wttr.in/London?2"
```

## Error Handling

If location not found:
```
Unknown location; please try ~51.5074,-0.1278
```

Try coordinates:
```bash
curl "wttr.in/~51.5074,-0.1278"
```

## Notes

- **No API key needed** — wttr.in is free
- **Rate limited** — Don't spam requests
- **Global coverage** — Works for most cities
- **Terminal-friendly** — Designed for CLI output
- **Weather icons** — Emoji work in most terminals
