def comb(s, res):
    if not s: return
    res.add(s)
    for i in range(0, len(s)):
        t = s[0:i] + s[i + 1:]
        comb(t, res)

res = set()
comb('shahrukh', res) 

print(res)