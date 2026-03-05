import pytest
from app import get_range_for_difficulty, update_score

class TestGetRangeForDifficulty:
  def test_easy_difficulty(self):
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

  def test_normal_difficulty(self):
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

  def test_hard_difficulty(self):
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 50

  def test_unknown_difficulty_defaults_to_normal(self):
    low, high = get_range_for_difficulty("Unknown")
    assert low == 1
    assert high == 100


class TestUpdateScore:
  def test_win_first_attempt(self):
    score = update_score(0, "Win", 0)
    assert score == 90

  def test_win_multiple_attempts(self):
    score = update_score(0, "Win", 5)
    assert score == 40

  def test_win_score_minimum_threshold(self):
    score = update_score(0, "Win", 15)
    assert score == 10

  def test_too_high_even_attempt(self):
    score = update_score(100, "Too High", 0)
    assert score == 105

  def test_too_high_odd_attempt(self):
    score = update_score(100, "Too High", 1)
    assert score == 95

  def test_too_low(self):
    score = update_score(100, "Too Low", 0)
    assert score == 95

  def test_invalid_outcome(self):
    score = update_score(100, "Invalid", 0)
    class TestGetRangeForDifficulty:
      def test_easy_difficulty(self):
        low, high = get_range_for_difficulty("Easy")
        assert low == 1
        assert high == 20

      def test_normal_difficulty(self):
        low, high = get_range_for_difficulty("Normal")
        assert low == 1
        assert high == 100

      def test_hard_difficulty(self):
        low, high = get_range_for_difficulty("Hard")
        assert low == 1
        assert high == 50

      def test_unknown_difficulty_defaults_to_normal(self):
        low, high = get_range_for_difficulty("Unknown")
        assert low == 1
        assert high == 100


    class TestUpdateScore:
      def test_win_first_attempt(self):
        score = update_score(0, "Win", 0)
        assert score == 90

      def test_win_multiple_attempts(self):
        score = update_score(0, "Win", 5)
        assert score == 40

      def test_win_score_minimum_threshold(self):
        score = update_score(0, "Win", 15)
        assert score == 10

      def test_too_high_even_attempt(self):
        score = update_score(100, "Too High", 0)
        assert score == 105

      def test_too_high_odd_attempt(self):
        score = update_score(100, "Too High", 1)
        assert score == 95

      def test_too_low(self):
        score = update_score(100, "Too Low", 0)
        assert score == 95

      def test_invalid_outcome(self):
        score = update_score(100, "Invalid", 0)
        assert score == 100

      # Edge case: Negative current score
      def test_win_with_negative_score(self):
        score = update_score(-50, "Win", 0)
        assert score == 40

      # Edge case: Extremely large attempt number
      def test_win_very_large_attempt_number(self):
        score = update_score(0, "Win", 1000)
        assert score == 10

      # Edge case: Negative attempt number (shouldn't occur but test gracefully)
      def test_too_high_negative_attempt(self):
        score = update_score(100, "Too High", -1)
        assert score == 95

      # Edge case: Empty string outcome
      def test_empty_string_outcome(self):
        score = update_score(100, "", 0)
        assert score == 100

      # Edge case: None outcome
      def test_none_outcome(self):
        score = update_score(100, None, 0)
        assert score == 100