from protocol_framework.core import ProtocolTestFramework

def test_sequence_validation():
    tester = ProtocolTestFramework()
    test_messages = [
        {'sequence': 1}, {'sequence': 2}, {'sequence': 4},
        {'sequence': 4}, {'sequence': 3}
    ]
    result = tester.validate_message_sequence(test_messages)
    assert result['sequence_gaps'] == [3]
    assert result['duplicate_sequences'] == [4]
    assert result['out_of_order'] == [3]
