from count_word_matches import count_word_matches
import pytest

TEST_CASES = [("The cat sat on the mat", "cat", 1), ("Dog dog DOG dOg", "dog", 4), ("Hello world", "world", 1), ("hello hello HELLO", "hello", 3), ("No matches here", "yes", 0), ("catcat cat catdog", "cat", 1), ("a a a", "a", 3)]

@pytest.mark.parametrize("text, target, expected", TEST_CASES)
def test_count_word_matches(text, target, expected):
    assert count_word_matches(text, target) == expected
