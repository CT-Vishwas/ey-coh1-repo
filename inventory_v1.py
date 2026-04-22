d1 = {
    987:23,988:67,989:56,900:32,892:25,765:45,566:90
}

l1 = []
for k,v in d1.items():
    l1.append((v,k))

l2 = sorted(l1)

d2 = {}
for k,v in l2:
    if k < 40:
        d2[v] = "LOW"
    elif k > 40 and k <=60:
        d2[v] = "APT"
    else:
        d2[v] = "HIGH"

print(d2)