import os as os

authDict = {}
with open("auth/alpacaAuth.text") as authFile:
    for line in authFile:
        name,var = line.partition(": ")[::2]
        authDict[name.strip()] = str(var)
print(authDict["alpacaEndPoint"])
