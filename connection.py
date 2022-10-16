from script import connect

with open("password", "r") as f:
    PASSWORD = f.read()

result = connect(PASSWORD)

print(result)