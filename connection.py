import os
from dotenv import load_dotenv
from script import connect

load_dotenv()

PASSWORD = os.getenv("PASSWORD")
print(PASSWORD)
result = connect(PASSWORD)

print(result)
