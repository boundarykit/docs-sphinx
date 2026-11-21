---
title: "Make your first decision"
description: "Allow five minutes and use a disposable workspace."
---

# Make your first decision

Allow five minutes and use a disposable workspace.

## Initialize the workspace


```bash
bkit init --workspace demo
# Created boundary.yaml for demo
```

## Preview the rule


```yaml
effect: allow
capability: ticket.read
```

```bash
bkit evaluate --manifest boundary.yaml --capability ticket.read --output json > decision.json
```

## Inspect the receipt


```json
{"effect":"allow","capability":"ticket.read","revision":"rev_31"}
```

```typescript
import { readFileSync } from "node:fs";
console.log(JSON.parse(readFileSync("decision.json","utf8")).effect);
```

```python
import json
from pathlib import Path
assert json.loads(Path("decision.json").read_text())["effect"] == "allow"
```
