from count_word_matches import count_word_matches
import pytest

TEST_CASES = [("The cat sat on the mat", "cat", 1), ("Dog dog DOG dOg", "dog", 4), ("Hello world", "world", 1), ("hello hello HELLO", "hello", 3), ("No matches here", "yes", 0), ("catcat cat catdog", "cat", 1), ("a a a", "a", 3)]
EDGE_CASES = [("", "word", 0), ("hello world", "", 0), ("hello  world", "world", 1), (" cat ", "cat", 1), ("cat,dog cat", "cat", 2), ("x y z", "x", 1)]

@pytest.mark.parametrize("text, target, expected", TEST_CASES)
def test_count_word_matches(text, target, expected):
    assert count_word_matches(text, target) == expected

@pytest.fixture
def edge_cases():
    return EDGE_CASES

def test_edge_cases(edge_cases):
    @pytest.mark.parametrize("text, target, expected", EDGE_CASES)
    def test_count_word_matches(text, target, expected):
        assert count_word_matches(text, target) == expected