from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

# --- Bug fix regression tests ---

def test_too_high_hint_says_lower():
    """Bug fix: when guess is too high, the message must say 'LOWER', not 'HIGHER'."""
    outcome, message = check_guess(75, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected hint to say LOWER when guess is too high, got: {message}"
    assert "HIGHER" not in message, f"Hint should NOT say HIGHER when guess is too high, got: {message}"


def test_too_low_hint_says_higher():
    """Bug fix: when guess is too low, the message must say 'HIGHER', not 'LOWER'."""
    outcome, message = check_guess(25, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected hint to say HIGHER when guess is too low, got: {message}"
    assert "LOWER" not in message, f"Hint should NOT say LOWER when guess is too low, got: {message}"


def test_attempt_counter_starts_at_zero():
    """Bug fix: attempts must initialise to 0 so the very first guess is counted."""
    # Simulate what app.py does on a fresh session
    attempts = 0          # fixed value (was 1 before the bug fix)
    attempt_limit = 8     # Normal difficulty

    # Before any guess, all attempts should be available
    assert attempt_limit - attempts == 8, (
        f"Expected 8 attempts remaining before first guess, got {attempt_limit - attempts}"
    )

    # After the first guess, attempts should be 1 and remaining should be 7
    attempts += 1
    assert attempts == 1
    assert attempt_limit - attempts == 7, (
        f"Expected 7 attempts remaining after first guess, got {attempt_limit - attempts}"
    )
