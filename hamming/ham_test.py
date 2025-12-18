import pytest
from ham import encode_hamming_block, decode_hamming_block 

def test_encode_block():
    assert encode_hamming_block("1011") == "0110011"

def test_decode_block():
    code = "0110011"
    assert decode_hamming_block(code) == 0