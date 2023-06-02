from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match='tipo inválido para key'):
        encrypt_message("minimalist", 'string')

    with pytest.raises(TypeError, match='tipo inválido para message'):
        encrypt_message(5, 3)

    # Test case for key being out of range
    result = encrypt_message("minimalist", 10)
    assert result == "tsilaminim"

    # Test case for key being within the range
    result = encrypt_message("minimalist", 3)
    assert result == "nim_tsilami"

    # Test case for even key value
    result = encrypt_message("minimalist", 6)
    assert result == "tsil_aminim"

    # Test case for empty message
    result = encrypt_message("", 3)
    assert result == ""

    # Test case for key equal to message length
    result = encrypt_message("minimalist", 10)
    assert result == "tsilaminim"

    # Test case for key equal to 1
    result = encrypt_message("minimalist", 1)
    assert result == "m_tsilamini"
