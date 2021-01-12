from datetime import datetime

print("PRINT FROM PYTHON: ACTION 1.2 - STARTED")

timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
with open('/variable.txt', 'r') as file:
    user_input = file.read().replace('\n', '')

with open('log.md', 'w') as f:
    f.write(f'# {user_input}  {timestamp} ')

print("PRINT FROM PYTHON: ACTION 1.2 - COMPLETED")

