"""Reusable DNA sequence utilities for BioPyLearn."""

DNA_BASES = frozenset("ACGT")
COMPLEMENT = str.maketrans("ACGT", "TGCA")


def clean_sequence(raw: str) -> str:
    """Return a normalized DNA string with spaces removed and bases uppercased."""
    return "".join(ch for ch in raw.upper() if ch.isalpha())


def is_valid_dna(sequence: str, allow_n: bool = False) -> bool:
    """True for a non-empty string of A, C, G, T (N if allowed)."""
    if sequence == "":
        return False
    allowed = set(DNA_BASES)
    if allow_n:
        allowed.add("N")
    return set(sequence.upper()) <= allowed


def gc_content(sequence: str) -> float:
    """Return GC percentage (0-100); ValueError if invalid."""
    sequence = sequence.upper()
    if not is_valid_dna(sequence, allow_n=False):
        raise ValueError("Invalid DNA sequence.")
    return (sequence.count("C") + sequence.count("G")) / len(sequence) * 100.0


def reverse_complement(sequence: str) -> str:
    """Return the reverse complement; ValueError if invalid."""
    sequence = sequence.upper()
    if not is_valid_dna(sequence, allow_n=False):
        raise ValueError("Invalid DNA sequence.")
    return sequence[::-1].translate(COMPLEMENT)


def find_motif(sequence: str, motif: str) -> list[int]:
    """Return every 0-based start of motif (overlaps allowed)."""
    if not motif:
        raise ValueError("Motif cannot be empty.")
    
    sequence = sequence.upper()
    motif = motif.upper()
    
    return [
        index
        for index in range(len(sequence) - len(motif) + 1)
        if sequence[index : index + len(motif)] == motif
    ]
