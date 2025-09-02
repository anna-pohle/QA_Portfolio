from count_word_matches import count_word_matches
import pytest

TEST_CASES = [("The cat sat on the mat", "cat", 1), ("Dog dog DOG dOg", "dog", 4), ("Hello world", "world", 1), ("hello hello HELLO", "hello", 3), ("No matches here", "yes", 0), ("catcat cat catdog", "cat", 1), ("a a a", "a", 3)]
EDGE_CASES = [("", "word", 0), ("hello world", "", 0), ("hello  world", "world", 1), (" cat ", "cat", 1), ("cat,dog cat", "cat", 2), ("x y z", "x", 1)]
NEGATIVE_CASES = [(None, "word", TypeError), ("hello world", None, TypeError), (123, "word", TypeError), (["hello", "world"], "world", TypeError), ("hello world", ["world"], TypeError)]


# Part 1: Test Cases

@pytest.mark.parametrize("text, target, expected", TEST_CASES)
def test_count_word_matches(text, target, expected):
    assert count_word_matches(text, target) == expected


# Part 2: Edge Cases

@pytest.fixture
def edge_cases():
    return EDGE_CASES

def test_edge_cases(edge_cases):
    @pytest.mark.parametrize("text, target, expected", EDGE_CASES)
    def test_count_word_matches(text, target, expected):
        assert count_word_matches(text, target) == expected


# Part 3: Invalid Cases

@pytest.fixture
def invalid_cases():
    return INVALID_CASES

def test_invalid_cases(invalid_cases):
    @pytest.mark.parametrize("text, target, expected", INVALID_CASES)
    def test_count_word_matches(text, target, expected):
        with pytest.raises(TypeError):
            assert count_word_matches(text, target) == expected
