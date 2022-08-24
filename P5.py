def genParenthesis(n, Open, close, s, ans):
	if(Open == n and close == n):
		ans.append(s)
		return

	if(Open < n):
		genParenthesis(n, Open+1, close, s+"{", ans)

	if(close < Open):
		genParenthesis(n, Open, close + 1, s+"}", ans)

n = 3
ans = []
genParenthesis(n, 0, 0, "", ans)
print(ans)

