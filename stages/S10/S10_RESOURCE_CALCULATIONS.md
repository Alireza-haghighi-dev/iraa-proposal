# S10_RESOURCE_CALCULATIONS

| Field | Value |
|---|---|
| Document ID | S10_RESOURCE_CALCULATIONS |
| Version | 0.2 |
| Status | DRAFT |
| Stage | S10 |
| Date | 2026-11-21 |
| Depends on | DEC-042; S11_EFFORT_AND_SCHEDULE; stages/S11/qc/S11_EFFORT_MODEL.py; REF-02 §§14–16 |

- **Purpose:** the fixed quantities of the approved baseline (DEC-042) and the formulas that turn the owner's remaining inputs into Sections 14, 15 and 16. Nothing here sets a rate, cost, name or availability.
- **Fixed by DEC-042:** 1,291 person-hours; WP1 150, WP2 168, WP3 210, WP4 138, WP5 226, WP6 267, WP7 132; six months; the month distribution in S11_EFFORT_AND_SCHEDULE §4.

## 1. Quantities from the approved baseline

| WP | Lead hours | Contributor hours (combined) | Total | Share of total effort |
|---|---|---|---|---|
| 1 | 74 | 76 | 150 | 11.6% |
| 2 | 62 | 106 | 168 | 13.0% |
| 3 | 83 | 127 | 210 | 16.3% |
| 4 | 61 | 77 | 138 | 10.7% |
| 5 | 85 | 141 | 226 | 17.5% |
| 6 | 107 | 160 | 267 | 20.7% |
| 7 | 54 | 78 | 132 | 10.2% |
| Total | 526 | 765 | 1,291 | 100.0% |

Lead share of total effort: 40.7%; contributors combined: 59.3%. Average monthly hours over six months: lead 87.7 (planned peak 108 in month 3, a scheduling assumption under DEC-042 item 9); contributors combined 127.5; each contributor 42.5.

## 2. Section 14 (team table)

Share of total effort for a member = member hours ÷ 1,291; monthly hours = member hours ÷ 6. Rows use neutral labels until the local details are supplied.

| Case | Member 1 (technical lead) | Members 2, 3, 4 |
|---|---|---|
| Contributor hours shared equally (255 h each; DEC-043) | 526 h; 87.7 h per month; 40.7% | 255 h each; 42.5 h per month; 19.8%, 19.8%, 19.7% (largest-remainder rounding to one decimal so the column totals 100.0%; exact values 40.74% and 19.75%) |
| Unequal shares | As above | Hours per member from the owner; shares and monthly hours recomputed by the formula |

## 3. Section 15 (budget table)

Personnel cost = Σ (member hours × member hourly rate). Unit costs and totals are local-only columns in the form; the English master records cost types, item descriptions and quantities (hours, units). Non-personnel lines are added only if the owner includes them: reference evaluation environment (existing equipment, purchase or rental), patent-service access above the free tier, and any other item the sponsor's rules allow.

## 4. Section 16 (activity cost and weight)

Activity cost = lead hours × lead rate + contributor hours × contributor rate (+ any non-personnel cost assigned to the activity). Weight = activity cost ÷ total cost.

- If all members have the same rate and no non-personnel cost is assigned to activities, the weights equal the effort shares of §1 (11.6, 13.0, 16.3, 10.7, 17.5, 20.7, 10.2%).
- If the lead's rate is k times the contributors' rate, weight of activity i = (k·Lᵢ + Cᵢ) ÷ (526·k + 765), using the hours in §1; only the ratio k is needed, not the amounts.
- Non-personnel costs need either an assignment to activities or an amount relative to one personnel hour, so that weights can be computed without local currency.
