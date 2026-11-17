# AI USE LOG


- Course: SECB3203
- Assessment: Lab 5
- Student name: Tan Hui Shan
- Matric no: A24CS0197
- Group ID: n/a
- AI level: 1
- Tools cited: Google (2026). Gemini. Retrieved 17 November 2026 from https://gemini.google.com

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [x] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: 17 November 2026, 11:30 AM
- Tool: Google (2026). Gemini. Retrieved 17 November 2026 from https://gemini.google.com
- Purpose: explain
- Prompt: Explain to me why need to check the subset using set(sequence)<=allowed
- Output: The AI explained that `set(sequence) <= allowed` is a mathematical subset check that instantly verifies if all unique characters exist in the allowed bases, avoiding the need for a slower `for` loop.
- Verified by: ran pytest and reviewed Python documentation on set operations.
- My change: Accepted the explanation and kept the subset logic because it successfully passed all sequence validation tests efficiently.
- Used in: src/sequence_utils.py inside the is_valid_dna function.

## Entry 2

- Date: 17 November 2026, 11:45 AM
- Tool: Google (2026). Gemini. Retrieved 17 November 2026 from https://gemini.google.com
- Purpose: explain
- Prompt: what is the function of translate(complement)?
- Output: The AI explained that `.translate()` uses a mapping table to swap multiple characters simultaneously, which is more efficient and prevents accidental overwriting bugs that happen when chaining `.replace()` calls.
- Verified by: ran pytest to ensure the DNA was properly reversed and complemented without losing bases.
- My change: Accepted the logic and used it to generate the complementary strand before reversing it.
- Used in: src/sequence_utils.py inside the reverse_complement function.

## Entry 3

- Date: 17 November 2026, 11:55 AM
- Tool: Google (2026). Gemini. Retrieved 17 November 2026 from https://gemini.google.com
- Purpose: explain
- Prompt: what is cpm
- Output: The AI explained that CPM (Counts Per Million) is calculated by dividing each sequence count by the total library size, and then multiplying by 1,000,000 to normalize the data.
- Verified by: compared with the formula provided in the lab sheet and ran pytest.
- My change: Implemented the mathematical formula inside a list comprehension to ensure a new list was generated without mutating the original data.
- Used in: src/normalize.py inside the cpm function.

## Entry 4

- Date: 17 November 2026, 12:05 PM
- Tool: Google (2026). Gemini. Retrieved 17 November 2026 from https://gemini.google.com
- Purpose: generate-text
- Prompt: What is the design decisions I used here
- Output: The AI summarized my code logic into clear sentences, explaining the ValueError policy for zero totals, the use of list comprehensions to avoid side effects, and the efficiency of mathematical subset checking.
- Verified by: cross-referenced with the actual code written in normalize.py and sequence_utils.py, and checked against the lab sheet instructions.
- My change: Write the design decisions entirely by adding my actual logic for handling empty lists and CPM library sizes.
- Used in: README.md under the "Design Decisions" section.
