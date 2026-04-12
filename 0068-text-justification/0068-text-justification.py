class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        n = len(words)
        i = 0

        while i < n:
            # 找当前行能放哪些单词
            j = i
            words_len = 0  # 当前行所有单词长度之和

            while j < n and words_len + len(words[j]) + (j - i) <= maxWidth:
                words_len += len(words[j])
                j += 1

            num_words = j - i
            num_gaps = num_words - 1

            # 最后一行 or 这一行只有一个单词：左对齐
            if j == n or num_words == 1:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                total_spaces = maxWidth - words_len
                base_spaces = total_spaces // num_gaps
                extra_spaces = total_spaces % num_gaps

                parts = []
                for k in range(i, j - 1):
                    parts.append(words[k])
                    spaces = base_spaces
                    if k - i < extra_spaces:
                        spaces += 1
                    parts.append(" " * spaces)

                parts.append(words[j - 1])
                line = "".join(parts)

            res.append(line)
            i = j

        return res       