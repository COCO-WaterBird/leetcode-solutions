class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:


        items = ['A', 'C', 'G', 'T']

        bank_set = set(bank)
        queue = deque([startGene])
        visited = {startGene: 0}

        while queue:
            gene = queue.popleft()
            step = visited[gene]

            chars = list(gene)

            for i in range(8):
                for c in items:
                    if chars[i] == c:
                        continue

                    new_chars = chars.copy()
                    new_chars[i] = c
                    next_gene = ''.join(new_chars)

                    if next_gene not in bank_set:
                        continue

                    if next_gene in visited:
                        continue

                    if next_gene == endGene:
                        return step + 1

                    visited[next_gene] = step + 1
                    queue.append(next_gene)

        return -1       