import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(message="Rafael", key="string")
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(message=123, key=1)
    assert encrypt_message(message="Rafael", key=7) == "leafaR"
    assert encrypt_message(message="Rafael", key=4) == "le_afaR"
    assert encrypt_message(message="Rafael", key=3) == "faR_lea"
