class Solution:
    def decodeString(self, s: str) -> str:
        # Time O(N), Space O(N)
        stack = []
        current_count = 0
        current_string = ''        
        for char in s:
            if char.isdigit():
                current_count = current_count * 10 + int(char)
            elif char == '[':
                stack.append((current_string, current_count))
                current_string = ''
                current_count = 0
            elif char == ']':
                prev_string, count = stack.pop()
                current_string = prev_string + current_string * count
            else:
                current_string += char        
        return current_string

                    
def test_answer():
    S = Solution()
    assert S.decodeString("3[a]2[bc]") == "aaabcbc"
    assert S.decodeString("3[a2[c]]") == "accaccacc"
    assert S.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
    assert S.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef") == "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"

def debug():
    S = Solution()
    # S.decodeString("3[a]2[bc]")
    # S.decodeString("3[a2[c]]")
    S.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef")

debug()