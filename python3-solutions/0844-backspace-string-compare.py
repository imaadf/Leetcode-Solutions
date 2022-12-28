class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        s_skip, t_skip = 0, 0
        s_index, t_index = len(s) - 1, len(t) - 1

        while s_index >= 0 or t_index >= 0:

            while s_index >= 0:
                if s[s_index] == '#':
                    s_skip += 1
                    s_index -= 1
                elif s_skip > 0:
                    s_skip -= 1
                    s_index -= 1
                else:
                    break

            while t_index >= 0:
                if t[t_index] == '#':
                    t_skip += 1
                    t_index -= 1
                elif t_skip > 0:
                    t_skip -= 1
                    t_index -= 1
                else:
                    break

            s_char = s[s_index] if s_index >= 0 else ''
            t_char = t[t_index] if t_index >= 0 else ''

            if s_char != t_char:
                return False

            s_index -= 1
            t_index -= 1

        return True
