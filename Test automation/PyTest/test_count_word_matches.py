from count_word_matches import count_word_matches
import pytest

TEST_CASES = [("The cat sat on the mat", "cat", 1), ("Dog dog DOG dOg", "dog", 4), ("Hello world", "world", 1), ("hello hello HELLO", "hello", 3), ("No matches here", "yes", 0), ("catcat cat catdog", "cat", 1), ("a a a", "a", 3)]
EDGE_CASES = [("", "word", 0), ("hello world", "", 0), ("hello  world", "world", 1), (" cat ", "cat", 1), ("cat,dog cat", "cat", 2), ("x y z", "x", 1)]
INVALID_CASES = [(None, "word", TypeError), ("hello world", None, TypeError), (123, "word", TypeError), (["hello", "world"], "world", TypeError), ("hello world", ["world"], TypeError)]


# Part 1: Test Cases

@pytest.mark.parametrize("text, target, expected", TEST_CASES)
def test_count_word_matches_normal(text, target, expected):
    assert count_word_matches(text, target) == expected


# Part 2: Edge Cases

@pytest.mark.parametrize("text, target, expected", EDGE_CASES)
def test_count_word_matches_edge(text, target, expected):
    assert count_word_matches(text, target) == expected


# Part 3: Invalid Cases

@pytest.mark.parametrize("text, target, expected", INVALID_CASES)
def test_count_word_matches_invalid(text, target, expected):
    try:
        result = count_word_matches(text, target)
        assert result == 0
    except AttributeError:
        pass
