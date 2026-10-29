"""
ALGORITHM: String Pattern Matching (Knuth-Morris-Pratt / KMP)

WHAT IT DOES (SIMPLY):
Imagine you are searching for a word in a huge 1,000-page book. If you are halfway through
matching the word and get one letter wrong, a naive search resets all the way back to the start.
KMP pre-analyzes the word you are looking for so that when a mismatch happens, it knows exactly
how much of the word is already partially matched, jumping forward without ever re-reading
a single letter of the book.

REAL-LIFE USE CASES:
- DNA & Genome Analysis: Searching for exact gene sequences inside billions of DNA base pairs.
- Antivirus & Intrusion Detection: Scanning live network packets for virus signatures without stalling internet speeds.
- Text Editors & Search Tools: The underlying engine for "Find & Replace" and tools like grep.
"""

# Computes the Longest Proper Prefix which is also a Suffix (LPS) table
def compute_lps_array(pattern):
    m = len(pattern)
    lps = [0] * m
    prev_len = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[prev_len]:
            prev_len += 1
            lps[i] = prev_len
            i += 1
        else:
            if prev_len != 0:
                prev_len = lps[prev_len - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


# Knuth-Morris-Pratt pattern search algorithm
def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0:
        return []

    lps = compute_lps_array(pattern)
    matches = []
    i = j = 0

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            matches.append(i - j)
            j = lps[j - 1]
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches


if __name__ == "__main__":
    txt = "ABABDABACDABABCABAB"
    pat = "ABABCABAB"
    print(f"Matches at indices: {kmp_search(txt, pat)}")
