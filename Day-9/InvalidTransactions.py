class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        ans, done = [], []
        for i_pos, i in enumerate(transactions):
            for j_pos, j in enumerate(transactions):
                if i_pos != j_pos:
                    name1, time1, amount1, city1 = i.split(",")
                    name2, time2, amount2, city2 = j.split(",")
                    if name1 == name2 and abs(int(time1)-int(time2)) <= 60 and city1 != city2:
                        if i_pos not in done:
                            ans.append(i)
                            done.append(i_pos)
                        if j_pos not in done:
                            ans.append(j)
                            done.append(j_pos)
                    elif int(amount2) > 1000:
                        if j_pos not in done:
                            ans.append(j)
                            done.append(j_pos)
        return ans
