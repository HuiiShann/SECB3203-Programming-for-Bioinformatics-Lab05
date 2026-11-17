import pytest
from sequence_utils import reverse_complement, find_motif
from normalize import proportions, cpm

def test_proportions_input_unchanged():
    """Prove that proportions() returns a new list and leaves the input alone."""
    raw = [10.0, 30.0]
    result = proportions(raw)
    
    assert raw == [10.0, 30.0]  
    assert result == [0.25, 0.75] 

def test_proportions_zero_total():
    """Prove that passing a list of zeros raises a ValueError."""
    with pytest.raises(ValueError):
        proportions([0, 0, 0])

def test_reverse_complement_valid():
    """Prove that reverse complement correctly swaps and reverses bases."""
    assert reverse_complement("ATGC") == "GCAT"
    assert reverse_complement("aAac") == "GTTT" 
def test_find_motif_overlaps():
    """Prove that find_motif catches overlapping sequences."""
    assert find_motif("AAAA", "AA") == [0, 1, 2]

def test_cpm_custom_library_size():
    """Prove that cpm calculates correctly with an explicit library size."""
    assert cpm([10, 20], library_size=100) == [100000.0, 200000.0]