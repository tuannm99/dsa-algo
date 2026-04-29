package stringsx

func IsPalindromeAlphaNumeric(s string) bool {
	left, right := 0, len(s)-1
	for left < right {
		for left < right && !isAlphaNum(s[left]) {
			left++
		}
		for left < right && !isAlphaNum(s[right]) {
			right--
		}
		if toLower(s[left]) != toLower(s[right]) {
			return false
		}
		left++
		right--
	}
	return true
}

func GroupAnagrams(words []string) map[[26]int][]string {
	result := map[[26]int][]string{}
	for _, word := range words {
		var key [26]int
		for i := 0; i < len(word); i++ {
			key[word[i]-'a']++
		}
		result[key] = append(result[key], word)
	}
	return result
}

func LongestPalindromeExpand(s string) string {
	if len(s) < 2 {
		return s
	}

	start, end := 0, 0
	for i := 0; i < len(s); i++ {
		l1, r1 := expand(s, i, i)
		l2, r2 := expand(s, i, i+1)
		if r1-l1 > end-start {
			start, end = l1, r1
		}
		if r2-l2 > end-start {
			start, end = l2, r2
		}
	}
	return s[start : end+1]
}

func expand(s string, left, right int) (int, int) {
	for left >= 0 && right < len(s) && s[left] == s[right] {
		left--
		right++
	}
	return left + 1, right - 1
}

func isAlphaNum(c byte) bool {
	return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9')
}

func toLower(c byte) byte {
	if c >= 'A' && c <= 'Z' {
		return c + ('a' - 'A')
	}
	return c
}
