---
title: "API reference"
description: "Scope every call to one organization."
---

# API reference

Scope every call to one organization.

## List boundaries


```bash
curl https://api.boundarykit.com/v2/boundaries -H "X-API-Key: $BKIT_KEY" -H "X-Organization-Id: $BKIT_ORG"
```

## Handle cancellation


```go
req, err := http.NewRequestWithContext(ctx, http.MethodGet, endpoint, nil)
if err != nil { return err }
req.Header.Set("X-API-Key", key)
```
