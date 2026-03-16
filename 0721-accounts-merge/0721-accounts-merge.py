class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        n = len(accounts)

        #初始化 
        # 节点是账户下标 0 ~ n-1（不是邮箱字符串）
        father = list(range(n))
        size   = [1] * n

        def find(i):
            if father[i] != i:
                father[i] = find(father[i])
            return father[i]

        def union(x, y) -> bool:
            fx, fy = find(x), find(y)
            if fx == fy:
                return False
            if size[fx] >= size[fy]:
                size[fx] += size[fy]
                father[fy] = fx
            else:
                size[fy] += size[fx]
                father[fx] = fy
            return True

        # 第一步：合并
        # 建立 邮箱 → 第一次出现的账户下标 的映射
        email_to_id = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:             # account[0] 是名字，跳过
                if email not in email_to_id:
                    email_to_id[email] = i        # 第一次见到这个邮箱，记录账户下标
                else:
                    union(i, email_to_id[email])  # 已存在 → 两个账户有相同邮箱 → 合并

        # 第二步：收集结果
        # 把同一集合的邮箱归到根节点下
        from collections import defaultdict
        root_to_emails = defaultdict(set)
        for email, i in email_to_id.items():
            root_to_emails[find(i)].add(email)    # 用 find(i) 找根，归到同一组

        # 组装最终结果：名字 + 排序后的邮箱列表
        res = []
        for root, emails in root_to_emails.items():
            name = accounts[root][0]              # 根节点对应的账户名
            res.append([name] + sorted(emails))

        return res        