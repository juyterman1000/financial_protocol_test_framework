import pytest
from protocol_framework.core import ProtocolTestFramework
from protocol_framework.enums import MessageType

@pytest.fixture
def framework():
    return ProtocolTestFramework()

def test_create_fix_message(framework):
    msg = framework.create_fix_message(
        MessageType.LOGIN,
        {'49': 'CLIENT1', '56': 'EXCHANGE'}
    )
    assert "8=FIX.4.4" in msg
    assert "35=A" in msg
    assert "49=CLIENT1" in msg
