"""
Unit tests for the generate_otp function from the otp module.
"""

import pytest
from otp import generate_otp  # Replace with the actual file/module name

def test_generate_otp_length():
    """
    Test if the generate_otp function generates OTPs of the correct length.
    Validates for lengths 4 and 6 and checks for invalid input (length > 8).
    """
    otp = generate_otp(6)
    assert len(otp) == 6

    otp = generate_otp(4)
    assert len(otp) == 4

    with pytest.raises(ValueError):
        generate_otp(9)  # Length exceeds 8

def test_generate_otp_content():
    """
    Test if the generate_otp function generates OTPs consisting only of digits.
    """
    otp = generate_otp(6)
    assert otp.isdigit()

# Final newline added to adhere to PEP 8 formatting standards.
