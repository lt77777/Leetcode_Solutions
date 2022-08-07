class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip() + ' '                                             # Remove surrounding whitespaces, add an extra space: avoid empty string
        sign = -1 if s[0] == '-' else 1                                 # Capture the sign
        left = right = 1 if s[0] in ('-', '+') else 0                   # If there was a sign, start looking for digits from the next character
        while right < len(s) and s[right].isdigit(): right += 1         # Scan the characters to the right till all are digits
        num = sign * int(s[left:right]) if (right > left) else 0        # Number is the digits portion with the sign or 0 if there were no digits
        return max(-2**31, min(num, 2**31 - 1))                         # Clamp the number to the given range
