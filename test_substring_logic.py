"""
Test to verify substring matching logic
"""

def test_substring_matching():
    """Test the substring matching logic"""

    # Simulating the search
    email_subject_search = "awe1"  # User searches for this

    # Test cases: (subject, should_match)
    test_cases = [
        ("rawe1", True),   # Contains "awe1" as substring
        ("awe1r", True),   # Contains "awe1" as substring
        ("awe", False),    # Does NOT contain "awe1"
        ("AWE1", True),    # Case insensitive match
        ("RAWE1", True),   # Case insensitive match
        ("AI Development Expert course - Homework - L17 - GradingL19", False),  # Does not contain "awe1"
        ("AI Development Expert course - Homework - L18 - GradingL19", False),  # Does not contain "awe1"
        ("Test awe1 here", True),  # Contains "awe1"
    ]

    print(f"Search term: '{email_subject_search}'")
    print("="*70)

    all_passed = True
    for subject, expected_match in test_cases:
        # This is the actual logic from agent_runner.py line 285
        actual_match = email_subject_search.lower() in subject.lower()

        status = "[PASS]" if actual_match == expected_match else "[FAIL]"
        if actual_match != expected_match:
            all_passed = False

        print(f"{status} Subject: '{subject}'")
        print(f"       Expected: {expected_match}, Got: {actual_match}")
        print()

    print("="*70)
    if all_passed:
        print("[+] All tests PASSED!")
    else:
        print("[!] Some tests FAILED!")

    return all_passed


def test_your_example():
    """Test with the user's actual search query"""
    email_subject_search = "AI Development Expert course - Homework - L"

    test_subjects = [
        "AI Development Expert course - Homework - L17 - GradingL19",
        "AI Development Expert course - Homework - L18 - GradingL19",
        "AI Development Expert course - Homework - L11 - Generate Overlapping Gaussian Distribution Groups",
        "Something else entirely",
        "AI Course",
    ]

    print(f"\nUser's search: '{email_subject_search}'")
    print("="*70)

    for subject in test_subjects:
        matches = email_subject_search.lower() in subject.lower()
        status = "[MATCH]" if matches else "[SKIP]"
        print(f"{status} {subject}")

    print("="*70)


if __name__ == "__main__":
    test_substring_matching()
    test_your_example()
