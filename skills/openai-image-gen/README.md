# openai-image-gen Skill Reference

**Source:** OpenClaw built-in skill  
**Location:** `~/AppData/Roaming/npm/node_modules/openclaw/skills/openai-image-gen/`

## Quick Reference

| Aspect | Details |
|--------|---------|
| **Purpose** | Batch-generate images via OpenAI Images API |
| **Models** | GPT Image 1, DALL-E 3, DALL-E 2 |
| **Output** | Images + `prompts.json` + `index.html` gallery |
| **Emoji** | 🎨 |

## Requirements

- `OPENAI_API_KEY` environment variable
- `python3`

## Usage

### Basic Generation
```bash
# Random prompts (default)
python3 {baseDir}/scripts/gen.py

# Custom prompt
python3 {baseDir}/scripts/gen.py --prompt "ultra-detailed studio photo of a lobster astronaut"
```

### GPT Image Models

```bash
# GPT Image 1 (best quality)
python3 {baseDir}/scripts/gen.py --count 16 --model gpt-image-1

# GPT Image 1 Mini (faster, cheaper)
python3 {baseDir}/scripts/gen.py --count 32 --model gpt-image-1-mini

# GPT Image 1.5 (latest)
python3 {baseDir}/scripts/gen.py --model gpt-image-1.5
```

### DALL-E Models

```bash
# DALL-E 3 (single image only)
python3 {baseDir}/scripts/gen.py --model dall-e-3 --quality hd --style vivid
python3 {baseDir}/scripts/gen.py --model dall-e-3 --style natural

# DALL-E 2 (batch supported)
python3 {baseDir}/scripts/gen.py --model dall-e-2 --size 512x512 --count 4
```

## Parameters

### Size Options

| Model | Available Sizes | Default |
|-------|-----------------|---------|
| GPT Image 1/1.5 | `1024x1024`, `1536x1024`, `1024x1536` | `1024x1024` |
| DALL-E 3 | `1024x1024`, `1792x1024`, `1024x1792` | `1024x1024` |
| DALL-E 2 | `256x256`, `512x512`, `1024x1024` | `1024x1024` |

### Quality Options

| Model | Options | Default |
|-------|---------|---------|
| GPT Image | `auto`, `high`, `medium`, `low` | `high` |
| DALL-E 3 | `hd`, `standard` | `standard` |
| DALL-E 2 | `standard` only | `standard` |

### GPT Image Special Parameters

```bash
# Transparent background
python3 {baseDir}/scripts/gen.py --background transparent

# Output format
python3 {baseDir}/scripts/gen.py --output-format webp  # png, jpeg, webp
```

### DALL-E 3 Special Parameters

```bash
# Style
python3 {baseDir}/scripts/gen.py --model dall-e-3 --style vivid   # hyper-real, dramatic
python3 {baseDir}/scripts/gen.py --model dall-e-3 --style natural # natural looking
```

## Common Patterns

### Batch Generation
```bash
# Generate 16 random images
python3 {baseDir}/scripts/gen.py --count 16

# Generate variations of a theme
python3 {baseDir}/scripts/gen.py \
  --prompt "cyberpunk cityscape" \
  --count 8 \
  --model gpt-image-1
```

### High Quality Single Image
```bash
python3 {baseDir}/scripts/gen.py \
  --model dall-e-3 \
  --quality hd \
  --size 1792x1024 \
  --style vivid \
  --prompt "detailed fantasy landscape with floating islands"
```

### Custom Output Directory
```bash
python3 {baseDir}/scripts/gen.py \
  --out-dir ./my-images \
  --count 4
```

## Output Files

After generation, find in output directory:
- `*.png`, `*.jpeg`, or `*.webp` — Generated images
- `prompts.json` — Mapping of prompts to files
- `index.html` — Thumbnail gallery (open in browser)

## Model Comparison

| Model | Speed | Quality | Cost | Best For |
|-------|-------|---------|------|----------|
| GPT Image 1 | Medium | Excellent | Higher | Professional use, detailed images |
| GPT Image 1 Mini | Fast | Good | Lower | Quick generation, prototyping |
| GPT Image 1.5 | Medium | Excellent | Higher | Latest features |
| DALL-E 3 | Slower | Very Good | Medium | Artistic, vivid imagery |
| DALL-E 2 | Fast | Good | Lower | Simple images, batch generation |

## Notes

- DALL-E 3 only supports `count=1` (enforced automatically)
- GPT Image models support more advanced features (transparency, formats)
- Image generation can take 30+ seconds per image
- Set exec timeout to 300+ seconds when running via OpenClaw
