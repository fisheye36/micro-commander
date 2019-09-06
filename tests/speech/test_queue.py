
from speech.response_queue import PriorityQueue


def test_queue_waits_for_missing_response():
    first_request = 1
    first_message = "this is the first message"
    second_request = 2
    second_message = "this is the second message"
    queue = PriorityQueue()
    queue.push(second_request, second_message)
    # should be an empty list because previous req was not received
    assert queue.pull() == []
    queue.push(first_request, first_message)
    assert queue.pull() == first_message.split()
    assert queue.pull() == second_message.split()
    assert queue.pull() == []


def test_available_resources_in_queue():
    queue = PriorityQueue()
    assert queue.is_response_available() is False
    queue.push(1, "first message")
    assert queue.is_response_available() is True
    queue.pull()  # pulling 1st
    assert queue.is_response_available() is False
    queue.push(3, "third message")
    assert queue.is_response_available() is False
    queue.push(2, "second message")
    assert queue.is_response_available() is True
    queue.pull()  # pulling 2nd
    assert queue.is_response_available() is True
    queue.pull()  # pulling 3rd
    assert queue.is_response_available() is False
