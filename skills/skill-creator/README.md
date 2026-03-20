# skill-creator Skill Reference

**Source:** OpenClaw built-in skill  
**Location:** `~/AppData/Roaming/npm/node_modules/openclaw/skills/skill-creator/`

## Quick Reference

| Aspect | Details |
|--------|---------|
| **Purpose** | Create, edit, improve, audit AgentSkills |
| **Triggers** | "create a skill", "improve this skill", "audit the skill" |
| **Output** | `.skill` package (zip with .skill extension) |

## What are Skills?

Skills = Modular packages that extend Codex capabilities

Think of them as "onboarding guides" for specific domains. They transform Codex from general-purpose to specialized.

### What Skills Provide

1. **Specialized workflows** — Multi-step procedures
2. **Tool integrations** — Instructions for APIs, file formats
3. **Domain expertise** — Company-specific knowledge
4. **Bundled resources** — Scripts, references, assets

## Skill Anatomy

```
skill-name/
├── SKILL.md              # Required: Metadata + instructions
├── scripts/              # Optional: Executable code
├── references/           # Optional: Documentation
└── assets/               # Optional: Templates, images, fonts
```

### SKILL.md Structure

```yaml
---
name: skill-name
description: "What it does and when to use it"
---

# Body: Instructions for using the skill
```

**Frontmatter (YAML):**
- `name` — Skill identifier
- `description` — Primary trigger mechanism (be comprehensive!)

**Body (Markdown):**
- Instructions for using the skill
- When to use, how to use
- Examples and patterns

### Resource Types

#### scripts/
- **When:** Same code rewritten repeatedly
- **Examples:** `rotate_pdf.py`, `deploy_script.sh`
- **Benefits:** Token efficient, deterministic

#### references/
- **When:** Documentation Codex should reference
- **Examples:** `schema.md`, `api_docs.md`, `policies.md`
- **Benefits:** Loaded only when needed

#### assets/
- **When:** Files for output (not loaded into context)
- **Examples:** `logo.png`, `template.pptx`, `boilerplate/`
- **Benefits:** Used without context bloat

## Core Principles

### 1. Concise is Key

Context window is a public good.

**Ask for every paragraph:**
- "Does Codex really need this explanation?"
- "Does this justify its token cost?"

**Default assumption:** Codex is already very smart.

### 2. Progressive Disclosure

Three-level loading:

1. **Metadata** (name + description) — Always in context (~100 words)
2. **SKILL.md body** — When skill triggers (<5k words)
3. **References** — As needed (unlimited)

### 3. Appropriate Freedom

| Freedom Level | When |
|---------------|------|
| **High** (text instructions) | Multiple approaches valid, context-dependent |
| **Medium** (pseudocode/script params) | Preferred pattern exists |
| **Low** (specific scripts) | Fragile, consistency critical |

## Skill Creation Workflow

### Step 1: Understand with Examples

Ask:
- "What functionality should this skill support?"
- "Can you give examples of how it would be used?"
- "What would trigger this skill?"

**Don't skip** unless usage patterns are already clear.

### Step 2: Plan Resources

Analyze each example:
1. How would Codex execute this from scratch?
2. What scripts/references/assets would help?

**Examples:**
- PDF rotation → `scripts/rotate_pdf.py`
- Webapp builder → `assets/hello-world/` template
- BigQuery queries → `references/schema.md`

### Step 3: Initialize

```bash
scripts/init_skill.py <skill-name> --path <output-dir> [options]
```

Options:
- `--resources scripts,references,assets` — Create directories
- `--examples` — Add example files

**Example:**
```bash
scripts/init_skill.py my-skill --path skills/public --resources scripts,references
```

### Step 4: Edit

1. **Start with resources** — scripts/, references/, assets/
2. **Update SKILL.md** — Frontmatter + body
3. **Test scripts** — Actually run them

### Step 5: Package

```bash
scripts/package_skill.py <path/to/skill-folder> [output-dir]
```

This:
- Validates the skill
- Creates `.skill` file (zip with .skill extension)

### Step 6: Iterate

Use → Notice issues → Improve → Test again

## Naming Conventions

- **Format:** lowercase letters, digits, hyphens
- **Length:** Under 64 characters
- **Style:** Short, verb-led phrases
- **Namespacing:** By tool when helpful
  - `gh-address-comments`
  - `linear-address-issue`

## Writing Guidelines

### Frontmatter Description

**Include:**
- What the skill does
- Specific triggers/contexts for when to use it

**Example:**
```yaml
description: "Comprehensive document creation and editing. Use when working with .docx files for: (1) Creating documents, (2) Modifying content, (3) Tracked changes, (4) Adding comments."
```

### Body Content

**Use imperative/infinitive form:**
- ✅ "Run the script"
- ✅ "Set the environment variable"
- ❌ "You should run the script"

**Progressive Disclosure Patterns:**

**Pattern 1: High-level with references**
```markdown
## Quick start
Extract text with pdfplumber: [code example]

## Advanced features
- **Form filling**: See [FORMS.md](FORMS.md)
- **API reference**: See [REFERENCE.md](REFERENCE.md)
```

**Pattern 2: Domain-specific organization**
```
bigquery-skill/
├── SKILL.md (overview)
└── reference/
    ├── finance.md
    ├── sales.md
    └── product.md
```

**Pattern 3: Conditional details**
```markdown
## Creating documents
Use docx-js. See [DOCX-JS.md](DOCX-JS.md).

**For tracked changes**: See [REDLINING.md](REDLINING.md)
```

## What NOT to Include

❌ **Never create:**
- README.md
- INSTALLATION_GUIDE.md
- QUICK_REFERENCE.md
- CHANGELOG.md
- etc.

Only essential files. No auxiliary documentation.

## Best Practices

- **Keep SKILL.md under 500 lines**
- **Avoid deeply nested references** — Keep one level deep
- **Structure long references** — TOC for files >100 lines
- **No duplication** — Info lives in SKILL.md OR references, not both
- **Test scripts** — Actually run before packaging

## Iteration

**Workflow:**
1. Use skill on real tasks
2. Notice struggles or inefficiencies
3. Identify SKILL.md/resource updates needed
4. Implement changes
5. Test again

Often happens right after first use when context is fresh.
