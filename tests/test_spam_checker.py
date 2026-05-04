from tools.spam_checker_tool import SpamCheckerTool, SpamCheckResult

def test_clean_email_scores_low():
    """Clean email scores low (< 30)"""
    checker = SpamCheckerTool()
    result = checker.check_spam_score(
        subject="Meeting request",
        body="Hi John, I hope you're doing well. Let's schedule a meeting next week."
    )
    assert isinstance(result, SpamCheckResult)
    assert result.spam_score <= 0.3, f"Expected score <=0.3, got {result.spam_score}"

def test_body_with_free_scores_high():
    """Body with 'FREE!!!' scores high (> 50)"""
    checker = SpamCheckerTool()
    result = checker.check_spam_score(
        subject="Special Offer!!!",
        body="GET FREE!!! LIMITED TIME OFFER!!! CLICK HERE NOW TO WIN CASH!!!!"
    )
    assert result.spam_score > 0.5, f"Expected score >0.5, got {result.spam_score}"

def test_all_caps_subject_increases_score():
    """ALL CAPS subject increases score"""
    checker = SpamCheckerTool()
    normal_result = checker.check_spam_score(
        subject="Normal subject",
        body="Regular email body"
    )
    caps_result = checker.check_spam_score(
        subject="ALL CAPS SUBJECT",
        body="Regular email body"
    )
    assert caps_result.spam_score > normal_result.spam_score, \
        f"ALL CAPS should increase score: {caps_result.spam_score} vs {normal_result.spam_score}"

def test_recommendations_list_returned():
    """Recommendations list returned"""
    checker = SpamCheckerTool()
    result = checker.check_spam_score(
        subject="Test",
        body="Test body"
    )
    assert isinstance(result.recommendations, list)
    assert len(result.recommendations) > 0

def test_empty_subject_handled_without_crash():
    """Empty subject handled without crash"""
    checker = SpamCheckerTool()
    try:
        result = checker.check_spam_score(
            subject="",
            body="Test body"
        )
        assert isinstance(result, SpamCheckResult)
    except Exception as e:
        assert False, f"Empty subject caused crash: {e}"

def test_is_likely_spam_true_when_score_high():
    """`is_likely_spam` True when score > 70"""
    checker = SpamCheckerTool()
    result = checker.check_spam_score(
        subject="FREE MONEY!!! WIN BIG NOW!!!",
        body="CLICK HERE FOR FREE CASH!!! BUY NOW!!! LIMITED TIME OFFER!!! ACT NOW OR LOSE OUT!!!"
    )
    assert result.is_likely_spam is True, \
        f"Expected is_likely_spam=True for high score {result.spam_score}"
    assert result.spam_score > 0.7, f"Expected score >0.7, got {result.spam_score}"
