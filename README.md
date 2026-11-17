# SECB3203 Lab 5 - Functions and modules: sequence_utils.py and normalize.py

Student: Tan Hui Shan, A24CS0197

## Setup
    python -m venv .venv
    source .venv/bin/activate        # Windows: .venv\Scripts\activate
    pip install -r requirements.txt

## Run
    python -m pytest                 # all tests
    ruff check src                   # style check

## What is in this repository
- `src/sequence_utils.py` : clean_sequence, is_valid_dna, gc_content, reverse_complement, find_motif
- `src/normalize.py` : proportions, cpm (never change the caller's data)
- `tests/` : visible tests and my own tests (test_lab05_own.py)
- `AI_USE_LOG.md` : my AI prompt log (or nil return)

## Design decisions
**Error Policy:** The `proportions() `function raises a ValueError when the total is zero instead of returning a list of zeros. 

**Side Effects:** Functions in `normalize.py` never mutate the original input list. The line return `[count / total for count in counts]` builds and returns a brand-new list using a list comprehension, ensuring the caller's original data remains completely unchanged.

**Sequence Validation:** The `is_valid_dna()` function uses mathematical subset checking `(set(sequence) <= allowed) `because it is safer and much more efficient than writing a loop to check every single character.