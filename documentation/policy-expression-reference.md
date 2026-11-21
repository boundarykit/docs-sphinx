---
title: "Policy expression reference"
description: "Use this reference when reviewing a pinned policy revision or reconstructing an audit trail."
---

# Policy expression reference

Use this reference when reviewing a pinned policy revision or reconstructing an audit trail.

## Expression grammar

An expression returns a typed value. A policy predicate must return Bool. Missing and null are distinct. See [String comparisons](#string-comparisons).

```ebnf
expr = literal | field | call | expr operator expr ;
call = identifier '(' [expr {',' expr}] ')' ;
field = identifier {'.' identifier} ;
```

## String comparisons

### eq

True for equal values of the same type. The string comparisons overload of `eq` accepts operands of the declared type. Resolve the left operand in the current decision context before evaluating the comparison.

### Examples

| Expression | Evaluation |
| --- | --- |
| `eq(request.label, rule.label)` | Resolve request.label from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `eq(session.label, rule.label)` | Resolve session.label from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `eq(principal.label, rule.label)` | Resolve principal.label from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `eq(resource.label, rule.label)` | Resolve resource.label from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `eq(organization.label, rule.label)` | Resolve organization.label from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |

### Edge cases

| Input at eq | Result | Diagnostic |
| --- | --- | --- |
| Missing left operand | unknown | Record the unresolved path and skip this allow branch. |
| Explicit null | type error | Select the null overload or guard the expression with is_null. |
| Mixed operand types | compile error | A string comparisons expression requires compatible types on both sides. |
### ne

True for distinct values of the same type. The string comparisons overload of `ne` accepts operands of the declared type. Resolve the left operand in the current decision context before evaluating the comparison.

### Examples

| Expression | Evaluation |
| --- | --- |
| `ne(request.label, rule.label)` | Resolve request.label from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `ne(session.label, rule.label)` | Resolve session.label from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `ne(principal.label, rule.label)` | Resolve principal.label from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `ne(resource.label, rule.label)` | Resolve resource.label from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `ne(organization.label, rule.label)` | Resolve organization.label from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |

### Edge cases

| Input at ne | Result | Diagnostic |
| --- | --- | --- |
| Missing left operand | unknown | Record the unresolved path and skip this allow branch. |
| Explicit null | type error | Select the null overload or guard the expression with is_null. |
| Mixed operand types | compile error | A string comparisons expression requires compatible types on both sides. |
### starts_with

Match a literal prefix starting at offset zero. The string comparisons overload of `starts_with` accepts operands of the declared type. Resolve the left operand in the current decision context before evaluating the comparison.

### Examples

| Expression | Evaluation |
| --- | --- |
| `starts_with(request.label, rule.label)` | Resolve request.label from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `starts_with(session.label, rule.label)` | Resolve session.label from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `starts_with(principal.label, rule.label)` | Resolve principal.label from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `starts_with(resource.label, rule.label)` | Resolve resource.label from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `starts_with(organization.label, rule.label)` | Resolve organization.label from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |

### Edge cases

| Input at starts_with | Result | Diagnostic |
| --- | --- | --- |
| Missing left operand | unknown | Record the unresolved path and skip this allow branch. |
| Explicit null | type error | Select the null overload or guard the expression with is_null. |
| Mixed operand types | compile error | A string comparisons expression requires compatible types on both sides. |
### ends_with

Match a literal suffix ending at the last code point. The string comparisons overload of `ends_with` accepts operands of the declared type. Resolve the left operand in the current decision context before evaluating the comparison.

### Examples

| Expression | Evaluation |
| --- | --- |
| `ends_with(request.label, rule.label)` | Resolve request.label from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `ends_with(session.label, rule.label)` | Resolve session.label from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `ends_with(principal.label, rule.label)` | Resolve principal.label from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `ends_with(resource.label, rule.label)` | Resolve resource.label from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `ends_with(organization.label, rule.label)` | Resolve organization.label from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |

### Edge cases

| Input at ends_with | Result | Diagnostic |
| --- | --- | --- |
| Missing left operand | unknown | Record the unresolved path and skip this allow branch. |
| Explicit null | type error | Select the null overload or guard the expression with is_null. |
| Mixed operand types | compile error | A string comparisons expression requires compatible types on both sides. |
### contains

Check literal membership without case folding. The string comparisons overload of `contains` accepts operands of the declared type. Resolve the left operand in the current decision context before evaluating the comparison.

### Examples

| Expression | Evaluation |
| --- | --- |
| `contains(request.label, rule.label)` | Resolve request.label from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `contains(session.label, rule.label)` | Resolve session.label from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `contains(principal.label, rule.label)` | Resolve principal.label from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `contains(resource.label, rule.label)` | Resolve resource.label from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `contains(organization.label, rule.label)` | Resolve organization.label from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |

### Edge cases

| Input at contains | Result | Diagnostic |
| --- | --- | --- |
| Missing left operand | unknown | Record the unresolved path and skip this allow branch. |
| Explicit null | type error | Select the null overload or guard the expression with is_null. |
| Mixed operand types | compile error | A string comparisons expression requires compatible types on both sides. |
### matches

Match a compiled regular expression against the input. The string comparisons overload of `matches` accepts operands of the declared type. Resolve the left operand in the current decision context before evaluating the comparison.

### Examples

| Expression | Evaluation |
| --- | --- |
| `matches(request.label, rule.label)` | Resolve request.label from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `matches(session.label, rule.label)` | Resolve session.label from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `matches(principal.label, rule.label)` | Resolve principal.label from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `matches(resource.label, rule.label)` | Resolve resource.label from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `matches(organization.label, rule.label)` | Resolve organization.label from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |

### Edge cases

| Input at matches | Result | Diagnostic |
| --- | --- | --- |
| Missing left operand | unknown | Record the unresolved path and skip this allow branch. |
| Explicit null | type error | Select the null overload or guard the expression with is_null. |
| Mixed operand types | compile error | A string comparisons expression requires compatible types on both sides. |
### equals_fold

Compare identifiers after case folding. The string comparisons overload of `equals_fold` accepts operands of the declared type. Resolve the left operand in the current decision context before evaluating the comparison.

### Examples

| Expression | Evaluation |
| --- | --- |
| `equals_fold(request.label, rule.label)` | Resolve request.label from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `equals_fold(session.label, rule.label)` | Resolve session.label from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `equals_fold(principal.label, rule.label)` | Resolve principal.label from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `equals_fold(resource.label, rule.label)` | Resolve resource.label from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `equals_fold(organization.label, rule.label)` | Resolve organization.label from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |

### Edge cases

| Input at equals_fold | Result | Diagnostic |
| --- | --- | --- |
| Missing left operand | unknown | Record the unresolved path and skip this allow branch. |
| Explicit null | type error | Select the null overload or guard the expression with is_null. |
| Mixed operand types | compile error | A string comparisons expression requires compatible types on both sides. |

## Numeric comparisons

### eq

True for equal values of the same type. The numeric comparisons overload of `eq` accepts operands of the declared type. Resolve the left operand in the current decision context before evaluating the comparison.

### Examples

| Expression | Evaluation |
| --- | --- |
| `eq(request.quota, rule.quota)` | Resolve request.quota from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `eq(session.quota, rule.quota)` | Resolve session.quota from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `eq(principal.quota, rule.quota)` | Resolve principal.quota from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `eq(resource.quota, rule.quota)` | Resolve resource.quota from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `eq(organization.quota, rule.quota)` | Resolve organization.quota from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |

### Edge cases

| Input at eq | Result | Diagnostic |
| --- | --- | --- |
| Missing left operand | unknown | Record the unresolved path and skip this allow branch. |
| Explicit null | type error | Select the null overload or guard the expression with is_null. |
| Mixed operand types | compile error | A numeric comparisons expression requires compatible types on both sides. |
### ne

True for distinct values of the same type. The numeric comparisons overload of `ne` accepts operands of the declared type. Resolve the left operand in the current decision context before evaluating the comparison.

### Examples

| Expression | Evaluation |
| --- | --- |
| `ne(request.quota, rule.quota)` | Resolve request.quota from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `ne(session.quota, rule.quota)` | Resolve session.quota from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `ne(principal.quota, rule.quota)` | Resolve principal.quota from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `ne(resource.quota, rule.quota)` | Resolve resource.quota from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `ne(organization.quota, rule.quota)` | Resolve organization.quota from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |

### Edge cases

| Input at ne | Result | Diagnostic |
| --- | --- | --- |
| Missing left operand | unknown | Record the unresolved path and skip this allow branch. |
| Explicit null | type error | Select the null overload or guard the expression with is_null. |
| Mixed operand types | compile error | A numeric comparisons expression requires compatible types on both sides. |
### lt

Exclude the upper bound. The numeric comparisons overload of `lt` accepts operands of the declared type. Resolve the left operand in the current decision context before evaluating the comparison.

### Examples

| Expression | Evaluation |
| --- | --- |
| `lt(request.quota, rule.quota)` | Resolve request.quota from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `lt(session.quota, rule.quota)` | Resolve session.quota from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `lt(principal.quota, rule.quota)` | Resolve principal.quota from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `lt(resource.quota, rule.quota)` | Resolve resource.quota from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `lt(organization.quota, rule.quota)` | Resolve organization.quota from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |

### Edge cases

| Input at lt | Result | Diagnostic |
| --- | --- | --- |
| Missing left operand | unknown | Record the unresolved path and skip this allow branch. |
| Explicit null | type error | Select the null overload or guard the expression with is_null. |
| Mixed operand types | compile error | A numeric comparisons expression requires compatible types on both sides. |
### le

Include the upper bound. The numeric comparisons overload of `le` accepts operands of the declared type. Resolve the left operand in the current decision context before evaluating the comparison.

### Examples

| Expression | Evaluation |
| --- | --- |
| `le(request.quota, rule.quota)` | Resolve request.quota from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `le(session.quota, rule.quota)` | Resolve session.quota from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `le(principal.quota, rule.quota)` | Resolve principal.quota from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `le(resource.quota, rule.quota)` | Resolve resource.quota from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `le(organization.quota, rule.quota)` | Resolve organization.quota from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |

### Edge cases

| Input at le | Result | Diagnostic |
| --- | --- | --- |
| Missing left operand | unknown | Record the unresolved path and skip this allow branch. |
| Explicit null | type error | Select the null overload or guard the expression with is_null. |
| Mixed operand types | compile error | A numeric comparisons expression requires compatible types on both sides. |
### gt

Exclude the lower bound. The numeric comparisons overload of `gt` accepts operands of the declared type. Resolve the left operand in the current decision context before evaluating the comparison.

### Examples

| Expression | Evaluation |
| --- | --- |
| `gt(request.quota, rule.quota)` | Resolve request.quota from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `gt(session.quota, rule.quota)` | Resolve session.quota from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `gt(principal.quota, rule.quota)` | Resolve principal.quota from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `gt(resource.quota, rule.quota)` | Resolve resource.quota from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `gt(organization.quota, rule.quota)` | Resolve organization.quota from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |

### Edge cases

| Input at gt | Result | Diagnostic |
| --- | --- | --- |
| Missing left operand | unknown | Record the unresolved path and skip this allow branch. |
| Explicit null | type error | Select the null overload or guard the expression with is_null. |
| Mixed operand types | compile error | A numeric comparisons expression requires compatible types on both sides. |
### ge

Include the lower bound. The numeric comparisons overload of `ge` accepts operands of the declared type. Resolve the left operand in the current decision context before evaluating the comparison.

### Examples

| Expression | Evaluation |
| --- | --- |
| `ge(request.quota, rule.quota)` | Resolve request.quota from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `ge(session.quota, rule.quota)` | Resolve session.quota from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `ge(principal.quota, rule.quota)` | Resolve principal.quota from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `ge(resource.quota, rule.quota)` | Resolve resource.quota from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `ge(organization.quota, rule.quota)` | Resolve organization.quota from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |

### Edge cases

| Input at ge | Result | Diagnostic |
| --- | --- | --- |
| Missing left operand | unknown | Record the unresolved path and skip this allow branch. |
| Explicit null | type error | Select the null overload or guard the expression with is_null. |
| Mixed operand types | compile error | A numeric comparisons expression requires compatible types on both sides. |
### between

Accept values inside the inclusive interval supplied on the right. The numeric comparisons overload of `between` accepts operands of the declared type. Resolve the left operand in the current decision context before evaluating the comparison.

### Examples

| Expression | Evaluation |
| --- | --- |
| `between(request.quota, rule.quota)` | Resolve request.quota from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `between(session.quota, rule.quota)` | Resolve session.quota from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `between(principal.quota, rule.quota)` | Resolve principal.quota from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `between(resource.quota, rule.quota)` | Resolve resource.quota from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `between(organization.quota, rule.quota)` | Resolve organization.quota from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |

### Edge cases

| Input at between | Result | Diagnostic |
| --- | --- | --- |
| Missing left operand | unknown | Record the unresolved path and skip this allow branch. |
| Explicit null | type error | Select the null overload or guard the expression with is_null. |
| Mixed operand types | compile error | A numeric comparisons expression requires compatible types on both sides. |

## Set predicates

### contains

Check literal membership without case folding. The set predicates overload of `contains` accepts operands of the declared type. Resolve the left operand in the current decision context before evaluating the comparison.

### Examples

| Expression | Evaluation |
| --- | --- |
| `contains(request.scopes, rule.scopes)` | Resolve request.scopes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `contains(session.scopes, rule.scopes)` | Resolve session.scopes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `contains(principal.scopes, rule.scopes)` | Resolve principal.scopes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `contains(resource.scopes, rule.scopes)` | Resolve resource.scopes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `contains(organization.scopes, rule.scopes)` | Resolve organization.scopes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |

### Edge cases

| Input at contains | Result | Diagnostic |
| --- | --- | --- |
| Missing left operand | unknown | Record the unresolved path and skip this allow branch. |
| Explicit null | type error | Select the null overload or guard the expression with is_null. |
| Mixed operand types | compile error | A set predicates expression requires compatible types on both sides. |
### contains_all

Require every member of the right set. The set predicates overload of `contains_all` accepts operands of the declared type. Resolve the left operand in the current decision context before evaluating the comparison.

### Examples

| Expression | Evaluation |
| --- | --- |
| `contains_all(request.scopes, rule.scopes)` | Resolve request.scopes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `contains_all(session.scopes, rule.scopes)` | Resolve session.scopes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `contains_all(principal.scopes, rule.scopes)` | Resolve principal.scopes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `contains_all(resource.scopes, rule.scopes)` | Resolve resource.scopes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `contains_all(organization.scopes, rule.scopes)` | Resolve organization.scopes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |

### Edge cases

| Input at contains_all | Result | Diagnostic |
| --- | --- | --- |
| Missing left operand | unknown | Record the unresolved path and skip this allow branch. |
| Explicit null | type error | Select the null overload or guard the expression with is_null. |
| Mixed operand types | compile error | A set predicates expression requires compatible types on both sides. |
### overlaps

Require at least one common member. The set predicates overload of `overlaps` accepts operands of the declared type. Resolve the left operand in the current decision context before evaluating the comparison.

### Examples

| Expression | Evaluation |
| --- | --- |
| `overlaps(request.scopes, rule.scopes)` | Resolve request.scopes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `overlaps(session.scopes, rule.scopes)` | Resolve session.scopes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `overlaps(principal.scopes, rule.scopes)` | Resolve principal.scopes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `overlaps(resource.scopes, rule.scopes)` | Resolve resource.scopes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `overlaps(organization.scopes, rule.scopes)` | Resolve organization.scopes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |

### Edge cases

| Input at overlaps | Result | Diagnostic |
| --- | --- | --- |
| Missing left operand | unknown | Record the unresolved path and skip this allow branch. |
| Explicit null | type error | Select the null overload or guard the expression with is_null. |
| Mixed operand types | compile error | A set predicates expression requires compatible types on both sides. |
### disjoint

Return true when the intersection is empty. The set predicates overload of `disjoint` accepts operands of the declared type. Resolve the left operand in the current decision context before evaluating the comparison.

### Examples

| Expression | Evaluation |
| --- | --- |
| `disjoint(request.scopes, rule.scopes)` | Resolve request.scopes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `disjoint(session.scopes, rule.scopes)` | Resolve session.scopes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `disjoint(principal.scopes, rule.scopes)` | Resolve principal.scopes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `disjoint(resource.scopes, rule.scopes)` | Resolve resource.scopes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `disjoint(organization.scopes, rule.scopes)` | Resolve organization.scopes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |

### Edge cases

| Input at disjoint | Result | Diagnostic |
| --- | --- | --- |
| Missing left operand | unknown | Record the unresolved path and skip this allow branch. |
| Explicit null | type error | Select the null overload or guard the expression with is_null. |
| Mixed operand types | compile error | A set predicates expression requires compatible types on both sides. |
### equals

Ignore insertion order when comparing membership. The set predicates overload of `equals` accepts operands of the declared type. Resolve the left operand in the current decision context before evaluating the comparison.

### Examples

| Expression | Evaluation |
| --- | --- |
| `equals(request.scopes, rule.scopes)` | Resolve request.scopes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `equals(session.scopes, rule.scopes)` | Resolve session.scopes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `equals(principal.scopes, rule.scopes)` | Resolve principal.scopes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `equals(resource.scopes, rule.scopes)` | Resolve resource.scopes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `equals(organization.scopes, rule.scopes)` | Resolve organization.scopes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |

### Edge cases

| Input at equals | Result | Diagnostic |
| --- | --- | --- |
| Missing left operand | unknown | Record the unresolved path and skip this allow branch. |
| Explicit null | type error | Select the null overload or guard the expression with is_null. |
| Mixed operand types | compile error | A set predicates expression requires compatible types on both sides. |

## Timestamp comparisons

### before

Compare normalized UTC instants using a strict upper bound. The timestamp comparisons overload of `before` accepts operands of the declared type. Resolve the left operand in the current decision context before evaluating the comparison.

### Examples

| Expression | Evaluation |
| --- | --- |
| `before(request.deadline, rule.deadline)` | Resolve request.deadline from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `before(session.deadline, rule.deadline)` | Resolve session.deadline from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `before(principal.deadline, rule.deadline)` | Resolve principal.deadline from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `before(resource.deadline, rule.deadline)` | Resolve resource.deadline from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `before(organization.deadline, rule.deadline)` | Resolve organization.deadline from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |

### Edge cases

| Input at before | Result | Diagnostic |
| --- | --- | --- |
| Missing left operand | unknown | Record the unresolved path and skip this allow branch. |
| Explicit null | type error | Select the null overload or guard the expression with is_null. |
| Mixed operand types | compile error | A timestamp comparisons expression requires compatible types on both sides. |
### after

Compare normalized UTC instants using a strict lower bound. The timestamp comparisons overload of `after` accepts operands of the declared type. Resolve the left operand in the current decision context before evaluating the comparison.

### Examples

| Expression | Evaluation |
| --- | --- |
| `after(request.deadline, rule.deadline)` | Resolve request.deadline from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `after(session.deadline, rule.deadline)` | Resolve session.deadline from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `after(principal.deadline, rule.deadline)` | Resolve principal.deadline from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `after(resource.deadline, rule.deadline)` | Resolve resource.deadline from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `after(organization.deadline, rule.deadline)` | Resolve organization.deadline from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |

### Edge cases

| Input at after | Result | Diagnostic |
| --- | --- | --- |
| Missing left operand | unknown | Record the unresolved path and skip this allow branch. |
| Explicit null | type error | Select the null overload or guard the expression with is_null. |
| Mixed operand types | compile error | A timestamp comparisons expression requires compatible types on both sides. |
### within

Check membership in the supplied time interval. The timestamp comparisons overload of `within` accepts operands of the declared type. Resolve the left operand in the current decision context before evaluating the comparison.

### Examples

| Expression | Evaluation |
| --- | --- |
| `within(request.deadline, rule.deadline)` | Resolve request.deadline from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `within(session.deadline, rule.deadline)` | Resolve session.deadline from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `within(principal.deadline, rule.deadline)` | Resolve principal.deadline from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `within(resource.deadline, rule.deadline)` | Resolve resource.deadline from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `within(organization.deadline, rule.deadline)` | Resolve organization.deadline from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |

### Edge cases

| Input at within | Result | Diagnostic |
| --- | --- | --- |
| Missing left operand | unknown | Record the unresolved path and skip this allow branch. |
| Explicit null | type error | Select the null overload or guard the expression with is_null. |
| Mixed operand types | compile error | A timestamp comparisons expression requires compatible types on both sides. |
### expired

Compare the deadline to the evaluation timestamp. The timestamp comparisons overload of `expired` accepts operands of the declared type. Resolve the left operand in the current decision context before evaluating the comparison.

### Examples

| Expression | Evaluation |
| --- | --- |
| `expired(request.deadline, rule.deadline)` | Resolve request.deadline from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `expired(session.deadline, rule.deadline)` | Resolve session.deadline from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `expired(principal.deadline, rule.deadline)` | Resolve principal.deadline from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `expired(resource.deadline, rule.deadline)` | Resolve resource.deadline from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `expired(organization.deadline, rule.deadline)` | Resolve organization.deadline from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |

### Edge cases

| Input at expired | Result | Diagnostic |
| --- | --- | --- |
| Missing left operand | unknown | Record the unresolved path and skip this allow branch. |
| Explicit null | type error | Select the null overload or guard the expression with is_null. |
| Mixed operand types | compile error | A timestamp comparisons expression requires compatible types on both sides. |

## Map predicates

### has_key

Look up the exact key, including case. The map predicates overload of `has_key` accepts operands of the declared type. Resolve the left operand in the current decision context before evaluating the comparison.

### Examples

| Expression | Evaluation |
| --- | --- |
| `has_key(request.attributes, rule.attributes)` | Resolve request.attributes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `has_key(session.attributes, rule.attributes)` | Resolve session.attributes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `has_key(principal.attributes, rule.attributes)` | Resolve principal.attributes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `has_key(resource.attributes, rule.attributes)` | Resolve resource.attributes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `has_key(organization.attributes, rule.attributes)` | Resolve organization.attributes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |

### Edge cases

| Input at has_key | Result | Diagnostic |
| --- | --- | --- |
| Missing left operand | unknown | Record the unresolved path and skip this allow branch. |
| Explicit null | type error | Select the null overload or guard the expression with is_null. |
| Mixed operand types | compile error | A map predicates expression requires compatible types on both sides. |
### has_value

Search the map values using typed equality. The map predicates overload of `has_value` accepts operands of the declared type. Resolve the left operand in the current decision context before evaluating the comparison.

### Examples

| Expression | Evaluation |
| --- | --- |
| `has_value(request.attributes, rule.attributes)` | Resolve request.attributes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `has_value(session.attributes, rule.attributes)` | Resolve session.attributes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `has_value(principal.attributes, rule.attributes)` | Resolve principal.attributes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `has_value(resource.attributes, rule.attributes)` | Resolve resource.attributes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `has_value(organization.attributes, rule.attributes)` | Resolve organization.attributes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |

### Edge cases

| Input at has_value | Result | Diagnostic |
| --- | --- | --- |
| Missing left operand | unknown | Record the unresolved path and skip this allow branch. |
| Explicit null | type error | Select the null overload or guard the expression with is_null. |
| Mixed operand types | compile error | A map predicates expression requires compatible types on both sides. |
### empty

Compare the collection size to zero. The map predicates overload of `empty` accepts operands of the declared type. Resolve the left operand in the current decision context before evaluating the comparison.

### Examples

| Expression | Evaluation |
| --- | --- |
| `empty(request.attributes, rule.attributes)` | Resolve request.attributes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `empty(session.attributes, rule.attributes)` | Resolve session.attributes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `empty(principal.attributes, rule.attributes)` | Resolve principal.attributes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `empty(resource.attributes, rule.attributes)` | Resolve resource.attributes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `empty(organization.attributes, rule.attributes)` | Resolve organization.attributes from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |

### Edge cases

| Input at empty | Result | Diagnostic |
| --- | --- | --- |
| Missing left operand | unknown | Record the unresolved path and skip this allow branch. |
| Explicit null | type error | Select the null overload or guard the expression with is_null. |
| Mixed operand types | compile error | A map predicates expression requires compatible types on both sides. |

## Operand compatibility

| Left | Right | Resolution |
| --- | --- | --- |
| String comparisons | String comparisons | Use the declared overload. |
| String comparisons | Numeric comparisons | Require an explicit checked conversion before comparison. |
| String comparisons | Set predicates | Require an explicit checked conversion before comparison. |
| String comparisons | Timestamp comparisons | Require an explicit checked conversion before comparison. |
| String comparisons | Map predicates | Require an explicit checked conversion before comparison. |
| String comparisons | Boolean logic | Require an explicit checked conversion before comparison. |
| String comparisons | Duration comparisons | Require an explicit checked conversion before comparison. |
| Numeric comparisons | String comparisons | Require an explicit checked conversion before comparison. |
| Numeric comparisons | Numeric comparisons | Use the declared overload. |
| Numeric comparisons | Set predicates | Require an explicit checked conversion before comparison. |
| Numeric comparisons | Timestamp comparisons | Require an explicit checked conversion before comparison. |
| Numeric comparisons | Map predicates | Require an explicit checked conversion before comparison. |
| Numeric comparisons | Boolean logic | Require an explicit checked conversion before comparison. |
| Numeric comparisons | Duration comparisons | Require an explicit checked conversion before comparison. |
| Set predicates | String comparisons | Require an explicit checked conversion before comparison. |
| Set predicates | Numeric comparisons | Require an explicit checked conversion before comparison. |
| Set predicates | Set predicates | Use the declared overload. |
| Set predicates | Timestamp comparisons | Require an explicit checked conversion before comparison. |
| Set predicates | Map predicates | Require an explicit checked conversion before comparison. |
| Set predicates | Boolean logic | Require an explicit checked conversion before comparison. |
| Set predicates | Duration comparisons | Require an explicit checked conversion before comparison. |
| Timestamp comparisons | String comparisons | Require an explicit checked conversion before comparison. |
| Timestamp comparisons | Numeric comparisons | Require an explicit checked conversion before comparison. |
| Timestamp comparisons | Set predicates | Require an explicit checked conversion before comparison. |
| Timestamp comparisons | Timestamp comparisons | Use the declared overload. |
| Timestamp comparisons | Map predicates | Require an explicit checked conversion before comparison. |
| Timestamp comparisons | Boolean logic | Require an explicit checked conversion before comparison. |
| Timestamp comparisons | Duration comparisons | Require an explicit checked conversion before comparison. |
| Map predicates | String comparisons | Require an explicit checked conversion before comparison. |
| Map predicates | Numeric comparisons | Require an explicit checked conversion before comparison. |
| Map predicates | Set predicates | Require an explicit checked conversion before comparison. |
| Map predicates | Timestamp comparisons | Require an explicit checked conversion before comparison. |
| Map predicates | Map predicates | Use the declared overload. |
| Map predicates | Boolean logic | Require an explicit checked conversion before comparison. |
| Map predicates | Duration comparisons | Require an explicit checked conversion before comparison. |
| Boolean logic | String comparisons | Require an explicit checked conversion before comparison. |
| Boolean logic | Numeric comparisons | Require an explicit checked conversion before comparison. |
| Boolean logic | Set predicates | Require an explicit checked conversion before comparison. |
| Boolean logic | Timestamp comparisons | Require an explicit checked conversion before comparison. |
| Boolean logic | Map predicates | Require an explicit checked conversion before comparison. |
| Boolean logic | Boolean logic | Use the declared overload. |
| Boolean logic | Duration comparisons | Require an explicit checked conversion before comparison. |
| Duration comparisons | String comparisons | Require an explicit checked conversion before comparison. |
| Duration comparisons | Numeric comparisons | Require an explicit checked conversion before comparison. |
| Duration comparisons | Set predicates | Require an explicit checked conversion before comparison. |
| Duration comparisons | Timestamp comparisons | Require an explicit checked conversion before comparison. |
| Duration comparisons | Map predicates | Require an explicit checked conversion before comparison. |
| Duration comparisons | Boolean logic | Require an explicit checked conversion before comparison. |
| Duration comparisons | Duration comparisons | Use the declared overload. |

## Boolean logic

### and

Require both operands to be true. The boolean logic overload of `and` accepts operands of the declared type. Resolve the left operand in the current decision context before evaluating the comparison.

### Examples

| Expression | Evaluation |
| --- | --- |
| `and(request.enabled, rule.enabled)` | Resolve request.enabled from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `and(session.enabled, rule.enabled)` | Resolve session.enabled from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `and(principal.enabled, rule.enabled)` | Resolve principal.enabled from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `and(resource.enabled, rule.enabled)` | Resolve resource.enabled from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `and(organization.enabled, rule.enabled)` | Resolve organization.enabled from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |

### Edge cases

| Input at and | Result | Diagnostic |
| --- | --- | --- |
| Missing left operand | unknown | Record the unresolved path and skip this allow branch. |
| Explicit null | type error | Select the null overload or guard the expression with is_null. |
| Mixed operand types | compile error | A boolean logic expression requires compatible types on both sides. |
### or

Require at least one true operand. The boolean logic overload of `or` accepts operands of the declared type. Resolve the left operand in the current decision context before evaluating the comparison.

### Examples

| Expression | Evaluation |
| --- | --- |
| `or(request.enabled, rule.enabled)` | Resolve request.enabled from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `or(session.enabled, rule.enabled)` | Resolve session.enabled from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `or(principal.enabled, rule.enabled)` | Resolve principal.enabled from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `or(resource.enabled, rule.enabled)` | Resolve resource.enabled from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `or(organization.enabled, rule.enabled)` | Resolve organization.enabled from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |

### Edge cases

| Input at or | Result | Diagnostic |
| --- | --- | --- |
| Missing left operand | unknown | Record the unresolved path and skip this allow branch. |
| Explicit null | type error | Select the null overload or guard the expression with is_null. |
| Mixed operand types | compile error | A boolean logic expression requires compatible types on both sides. |
### xor

Require exactly one true operand. The boolean logic overload of `xor` accepts operands of the declared type. Resolve the left operand in the current decision context before evaluating the comparison.

### Examples

| Expression | Evaluation |
| --- | --- |
| `xor(request.enabled, rule.enabled)` | Resolve request.enabled from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `xor(session.enabled, rule.enabled)` | Resolve session.enabled from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `xor(principal.enabled, rule.enabled)` | Resolve principal.enabled from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `xor(resource.enabled, rule.enabled)` | Resolve resource.enabled from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `xor(organization.enabled, rule.enabled)` | Resolve organization.enabled from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |

### Edge cases

| Input at xor | Result | Diagnostic |
| --- | --- | --- |
| Missing left operand | unknown | Record the unresolved path and skip this allow branch. |
| Explicit null | type error | Select the null overload or guard the expression with is_null. |
| Mixed operand types | compile error | A boolean logic expression requires compatible types on both sides. |
### implies

Reject only a true premise with a false conclusion. The boolean logic overload of `implies` accepts operands of the declared type. Resolve the left operand in the current decision context before evaluating the comparison.

### Examples

| Expression | Evaluation |
| --- | --- |
| `implies(request.enabled, rule.enabled)` | Resolve request.enabled from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `implies(session.enabled, rule.enabled)` | Resolve session.enabled from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `implies(principal.enabled, rule.enabled)` | Resolve principal.enabled from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `implies(resource.enabled, rule.enabled)` | Resolve resource.enabled from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `implies(organization.enabled, rule.enabled)` | Resolve organization.enabled from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |

### Edge cases

| Input at implies | Result | Diagnostic |
| --- | --- | --- |
| Missing left operand | unknown | Record the unresolved path and skip this allow branch. |
| Explicit null | type error | Select the null overload or guard the expression with is_null. |
| Mixed operand types | compile error | A boolean logic expression requires compatible types on both sides. |

## Duration comparisons

### lt

Exclude the upper bound. The duration comparisons overload of `lt` accepts operands of the declared type. Resolve the left operand in the current decision context before evaluating the comparison.

### Examples

| Expression | Evaluation |
| --- | --- |
| `lt(request.lease, rule.lease)` | Resolve request.lease from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `lt(session.lease, rule.lease)` | Resolve session.lease from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `lt(principal.lease, rule.lease)` | Resolve principal.lease from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `lt(resource.lease, rule.lease)` | Resolve resource.lease from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `lt(organization.lease, rule.lease)` | Resolve organization.lease from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |

### Edge cases

| Input at lt | Result | Diagnostic |
| --- | --- | --- |
| Missing left operand | unknown | Record the unresolved path and skip this allow branch. |
| Explicit null | type error | Select the null overload or guard the expression with is_null. |
| Mixed operand types | compile error | A duration comparisons expression requires compatible types on both sides. |
### le

Include the upper bound. The duration comparisons overload of `le` accepts operands of the declared type. Resolve the left operand in the current decision context before evaluating the comparison.

### Examples

| Expression | Evaluation |
| --- | --- |
| `le(request.lease, rule.lease)` | Resolve request.lease from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `le(session.lease, rule.lease)` | Resolve session.lease from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `le(principal.lease, rule.lease)` | Resolve principal.lease from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `le(resource.lease, rule.lease)` | Resolve resource.lease from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `le(organization.lease, rule.lease)` | Resolve organization.lease from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |

### Edge cases

| Input at le | Result | Diagnostic |
| --- | --- | --- |
| Missing left operand | unknown | Record the unresolved path and skip this allow branch. |
| Explicit null | type error | Select the null overload or guard the expression with is_null. |
| Mixed operand types | compile error | A duration comparisons expression requires compatible types on both sides. |
### eq

True for equal values of the same type. The duration comparisons overload of `eq` accepts operands of the declared type. Resolve the left operand in the current decision context before evaluating the comparison.

### Examples

| Expression | Evaluation |
| --- | --- |
| `eq(request.lease, rule.lease)` | Resolve request.lease from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `eq(session.lease, rule.lease)` | Resolve session.lease from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `eq(principal.lease, rule.lease)` | Resolve principal.lease from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `eq(resource.lease, rule.lease)` | Resolve resource.lease from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `eq(organization.lease, rule.lease)` | Resolve organization.lease from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |

### Edge cases

| Input at eq | Result | Diagnostic |
| --- | --- | --- |
| Missing left operand | unknown | Record the unresolved path and skip this allow branch. |
| Explicit null | type error | Select the null overload or guard the expression with is_null. |
| Mixed operand types | compile error | A duration comparisons expression requires compatible types on both sides. |
### ge

Include the lower bound. The duration comparisons overload of `ge` accepts operands of the declared type. Resolve the left operand in the current decision context before evaluating the comparison.

### Examples

| Expression | Evaluation |
| --- | --- |
| `ge(request.lease, rule.lease)` | Resolve request.lease from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `ge(session.lease, rule.lease)` | Resolve session.lease from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `ge(principal.lease, rule.lease)` | Resolve principal.lease from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `ge(resource.lease, rule.lease)` | Resolve resource.lease from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `ge(organization.lease, rule.lease)` | Resolve organization.lease from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |

### Edge cases

| Input at ge | Result | Diagnostic |
| --- | --- | --- |
| Missing left operand | unknown | Record the unresolved path and skip this allow branch. |
| Explicit null | type error | Select the null overload or guard the expression with is_null. |
| Mixed operand types | compile error | A duration comparisons expression requires compatible types on both sides. |
### gt

Exclude the lower bound. The duration comparisons overload of `gt` accepts operands of the declared type. Resolve the left operand in the current decision context before evaluating the comparison.

### Examples

| Expression | Evaluation |
| --- | --- |
| `gt(request.lease, rule.lease)` | Resolve request.lease from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `gt(session.lease, rule.lease)` | Resolve session.lease from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `gt(principal.lease, rule.lease)` | Resolve principal.lease from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `gt(resource.lease, rule.lease)` | Resolve resource.lease from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |
| `gt(organization.lease, rule.lease)` | Resolve organization.lease from the signed evaluation snapshot. Check the result against the expected predicate for the pinned rule revision. |

### Edge cases

| Input at gt | Result | Diagnostic |
| --- | --- | --- |
| Missing left operand | unknown | Record the unresolved path and skip this allow branch. |
| Explicit null | type error | Select the null overload or guard the expression with is_null. |
| Mixed operand types | compile error | A duration comparisons expression requires compatible types on both sides. |

## Built-in functions

### is_null

Return true for explicit null. Evaluate the argument against the current revision. Record a type diagnostic when the input fails validation.

### exists

Test whether a path resolves. Evaluate the argument against the current revision. Record a type diagnostic when the input fails validation.

### length

Count Unicode code points or collection elements. Evaluate the argument against the current revision. Record a type diagnostic when the input fails validation.

### lower

Fold an ASCII identifier to lowercase. Evaluate the argument against the current revision. Record a type diagnostic when the input fails validation.

### keys

Return the key set of a map. Evaluate the argument against the current revision. Record a type diagnostic when the input fails validation.

### now

Read the snapshot timestamp. Evaluate the argument against the current revision. Record a type diagnostic when the input fails validation.

### duration

Parse an ISO duration. Evaluate the argument against the current revision. Record a type diagnostic when the input fails validation.

### decimal

Parse a base-ten numeric string. Evaluate the argument against the current revision. Record a type diagnostic when the input fails validation.
