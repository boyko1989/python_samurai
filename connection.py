import os
from script import connect

PASSWORD = os.getenv("PASSWORD")
print(PASSWORD)
result = connect(PASSWORD)

print(result)