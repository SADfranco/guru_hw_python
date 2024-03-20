from datetime import datetime

now = datetime.now().time()
print(f'{now.hour}:{now.minute}')