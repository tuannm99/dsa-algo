def is_palindrome_alphanumeric(text: str) -> bool:
    left, right = 0, len(text) - 1
    while left < right:
        while left < right and not text[left].isalnum():
            left += 1
        while left < right and not text[right].isalnum():
            right -= 1
        if text[left].lower() != text[right].lower():
            return False
        left += 1
        right -= 1
    return True


def group_anagrams(words: list[str]) -> dict[tuple[int, ...], list[str]]:
    result: dict[tuple[int, ...], list[str]] = {}
    for word in words:
        key = [0] * 26
        for ch in word:
            key[ord(ch) - ord("a")] += 1
        frozen = tuple(key)
        result.setdefault(frozen, []).append(word)
    return result


def longest_palindrome_expand(text: str) -> str:
    if len(text) < 2:
        return text

    start = end = 0
    for i in range(len(text)):
        left1, right1 = _expand(text, i, i)
        left2, right2 = _expand(text, i, i + 1)
        if right1 - left1 > end - start:
            start, end = left1, right1
        if right2 - left2 > end - start:
            start, end = left2, right2
    return text[start : end + 1]


def _expand(text: str, left: int, right: int) -> tuple[int, int]:
    while left >= 0 and right < len(text) and text[left] == text[right]:
        left -= 1
        right += 1
    return left + 1, right - 1
