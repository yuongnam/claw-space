# openai-whisper-api Skill Reference

**Source:** OpenClaw built-in skill  
**Location:** `~/AppData/Roaming/npm/node_modules/openclaw/skills/openai-whisper-api/`

## Quick Reference

| Aspect | Details |
|--------|---------|
| **Purpose** | Transcribe audio via OpenAI Whisper API |
| **Model** | whisper-1 |
| **Input** | Audio files (m4a, ogg, mp3, wav, etc.) |
| **Output** | Plain text or JSON |
| **Emoji** | 🌐 |

## Requirements

- `OPENAI_API_KEY` environment variable
- `curl`

## Configuration

### Environment Variable
```bash
export OPENAI_API_KEY="your-key-here"
```

### OpenClaw Config
```json5
{
  skills: {
    "openai-whisper-api": {
      apiKey: "your-key-here",
    },
  },
}
```

## Usage

### Basic Transcription
```bash
{baseDir}/scripts/transcribe.sh /path/to/audio.m4a
```

Output: `/path/to/audio.txt`

### With Options

```bash
# Specify output file
{baseDir}/scripts/transcribe.sh /path/to/audio.ogg --out /tmp/transcript.txt

# Specify model
{baseDir}/scripts/transcribe.sh /path/to/audio.m4a --model whisper-1

# Specify language
{baseDir}/scripts/transcribe.sh /path/to/audio.m4a --language en

# Add context prompt (speaker names, terminology)
{baseDir}/scripts/transcribe.sh /path/to/audio.m4a \
  --prompt "Speaker names: Peter, Daniel"

# JSON output (with timestamps)
{baseDir}/scripts/transcribe.sh /path/to/audio.m4a \
  --json --out /tmp/transcript.json
```

## Supported Formats

Whisper supports most common audio formats:
- `.m4a` (iPhone voice memos)
- `.ogg`
- `.mp3`
- `.wav`
- `.webm`
- `.mp4` (extracts audio)

## Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `--model` | whisper-1 | Model to use |
| `--language` | auto-detect | Language code (en, zh, ko, etc.) |
| `--prompt` | none | Context to improve accuracy |
| `--json` | false | Output JSON with segments |
| `--out` | `{input}.txt` | Output file path |

## Use Cases

### Meeting Notes
```bash
{baseDir}/scripts/transcribe.sh meeting-recording.m4a --out meeting-notes.txt
```

### Voice Messages
```bash
{baseDir}/scripts/transcribe.sh voice-message.ogg
```

### Multi-language Content
```bash
# Specify language for better accuracy
{baseDir}/scripts/transcribe.sh korean-audio.m4a --language ko
```

### Named Speakers
```bash
{baseDir}/scripts/transcribe.sh interview.mp3 \
  --prompt "Speakers: interviewer, candidate"
```

### Timestamped Output
```bash
{baseDir}/scripts/transcribe.sh podcast.mp3 --json --out podcast.json
# JSON includes: text, segments (with start/end timestamps)
```

## Output Format

### Text Output (default)
```
This is the transcribed text from the audio file...
```

### JSON Output
```json
{
  "text": "Full transcript...",
  "segments": [
    {
      "id": 0,
      "start": 0.0,
      "end": 5.5,
      "text": "First segment..."
    }
  ]
}
```

## Tips

- **Prompts help** — Speaker names, technical terms, context
- **Language hint** — Specify for better accuracy on short files
- **JSON for editing** — Timestamps useful for video subtitles
- **Long files** — May take 1-2 minutes for hour-long content
