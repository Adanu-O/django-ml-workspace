# LeetCode problem 3: Longest substring without repeating characters


def substring(s: str) -> int:

        seen = set()
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            while char in seen:
                seen.remove(s[left])
                left += 1

            seen.add(char)
            max_len = max(max_len, right - left + 1)

        return max_len