# Org-City Patterns

> **Organizational Architecture Based on Christopher Alexander's Pattern Language**

This directory contains the pattern language framework for structuring the org-regima organization as an "Org-City" - applying architectural design patterns to organizational and software architecture.

## Contents

```
org-city-patterns/
├── README.md                    # This file
├── ORG_CITY_MAPPING.md         # Complete mapping of APL-253 to org structure
├── schemas/
│   ├── pattern_schema.json     # JSON Schema for pattern definitions
│   └── archetypal_pattern_schema.json  # Schema for archetypal patterns
└── sequences/
    └── pattern_sequences.json  # 36 pattern sequences with emergent phenomena
```

## Pattern Categories

| Category | Patterns | Organizational Mapping |
|----------|----------|----------------------|
| **Towns** | 1-94 | Enterprise & Organization Structure |
| **Buildings** | 95-204 | Repositories & Projects |
| **Construction** | 205-253 | Code, Workflows & Implementation |

## Quick Start

### 1. Understanding the Mapping

Read `ORG_CITY_MAPPING.md` for the complete mapping of architectural patterns to organizational structures.

### 2. Using Pattern Schemas

The schemas in `schemas/` can be used to:
- Validate pattern definitions
- Generate pattern documentation
- Build pattern-aware tooling

```python
import json

with open('schemas/pattern_schema.json') as f:
    schema = json.load(f)

# Use with jsonschema for validation
from jsonschema import validate
validate(instance=your_pattern, schema=schema)
```

### 3. Exploring Sequences

The `sequences/pattern_sequences.json` contains 36 pattern sequences, each describing:
- Pattern groupings
- Emergent phenomena
- Category mappings

## Integration with OrgimA

This pattern framework integrates with:

1. **OrgimA Introspector App** - Uses patterns to analyze org structure
2. **RegimA Learning Cycle** - Applies patterns to organizational learning
3. **Repository Generation** - Creates repos following pattern principles

## Key Patterns for GitHub Organizations

### Essential Organizational Patterns

| Pattern # | Name | GitHub Implementation |
|-----------|------|----------------------|
| 1 | Independent Regions | Enterprise autonomy |
| 12 | Community of 7000 | Organization size limits |
| 14 | Identifiable Neighborhood | Repository topics/collections |
| 95 | Building Complex | Monorepo structure |
| 99 | Main Building | Core repository |
| 100 | Pedestrian Street | Documentation paths |
| 205 | Structure Follows Social Spaces | Architecture follows use cases |

### Pattern Application Process

1. **Identify the Scale** - Enterprise, Org, Repo, or Code level
2. **Select Relevant Patterns** - Choose from appropriate category
3. **Apply Pattern Principles** - Implement the pattern's solution
4. **Connect Patterns** - Link to broader and narrower patterns
5. **Evaluate Emergence** - Assess emergent organizational properties

## Extended Patterns (1001-1253)

The APL-253 archive includes extended patterns for organizational consciousness:
- Located in `.github/agents/apl0/dim4/`
- Cover meta-organizational concepts
- Support cognitive architecture implementations

## References

- [A Pattern Language](https://www.patternlanguage.com/) - Original source
- [Extended Patterns](https://kairos.laetusinpraesens.org/84patlan_8_h_1) - Patterns 1001-1253
- [APL-253 Repository](../APL-253-main.zip) - Full pattern archive

## License

Pattern Language concepts by Christopher Alexander.
Org-City mapping and implementation by org-regima.
