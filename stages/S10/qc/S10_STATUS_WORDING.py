"""Approval-status wording corrections (S10 correction pass, 2026-11-22), shared by the master and the Word form.
DEC-042 approved the S11 test-set sizes, the 0.05 margin and the two corpus sizes; the response-time value,
absolute floors and agreement threshold remain open (ISS-039)."""
SUBS = [
 ("The margin of 0.05, the response-time value, the corpus sizes and the test-set sizes are planning values that await owner confirmation before the evaluation protocol is frozen.",
  "The test-set sizes, the margin of 0.05 and the corpus sizes of 10,000 and 100,000 items are fixed for this project. The response-time value of 5 seconds, the absolute floors and the judge-agreement threshold are planning values that remain to be confirmed before the evaluation protocol is frozen."),
 ("For the two ranking tasks the margin is 0.05, a planning value:", "For the two ranking tasks the margin is 0.05:"),
 ("at 10,000 and 100,000 items, the planning sizes;", "at 10,000 and 100,000 items, the specified corpus sizes;"),
]
if __name__ == "__main__":
    import sys, pathlib
    p = pathlib.Path(sys.argv[1]) / "proposal/IRAA_PROPOSAL_EN_MASTER.md"; s = p.read_text()
    for a, b in SUBS:
        assert s.count(a) == 1, a[:60]; s = s.replace(a, b)
    s = s.replace("| Version | 0.6 |", "| Version | 0.7 |", 1)
    p.write_text(s); print("master wording corrected")
