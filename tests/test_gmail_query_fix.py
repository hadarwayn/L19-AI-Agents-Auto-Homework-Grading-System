"""
Test the new Gmail query logic
"""

# Test cases
test_cases = [
    ("AI Development Expert course", 4),  # User's current search
    ("AI Development Expert course - Homework - L", 8),  # Previous working search
    ("awe1", 1),  # Short search
    ("homework", 1),  # Single word
    ("test one two three four five six seven", 7),  # Very long
]

print("Gmail Query Building Logic Test")
print("="*70)

for email_subject, word_count in test_cases:
    words = email_subject.split()

    if len(words) > 6:
        # For very long phrases (>6 words), use first 5 words
        key_words = ' '.join(words[:5])
        query = f'subject:{key_words}'
    else:
        # For short/medium search (≤6 words), use all words
        query = f'subject:{email_subject}'

    print(f"\nUser Search: '{email_subject}'")
    print(f"Word Count: {word_count}")
    print(f"Gmail Query: '{query}'")

print("\n" + "="*70)
print("\nKey Changes:")
print("- 1-6 words: Use ALL words in Gmail query")
print("- 7+ words: Use first 5 words in Gmail query")
print("- Post-filter: Always checks full user search term (case-insensitive)")
