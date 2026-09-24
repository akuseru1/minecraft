mountains = {
    "岩手山":2038,
    "富士山":3776,
    "八幡平":1613,
    "函館山":334,
    "箱根山":1438
}

takasa = 1500
yama_list = ["岩手山", "富士山", "八幡平", "函館山", "箱根山"]
result = []

for i in yama_list:
    if takasa <= mountains[i]:
        result.append(i)
print(result)