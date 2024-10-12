from datetime import date
import time

curr = time.time()
print(f'Seconds since January 1, 1970: {curr:.4f} or {curr:.2e} in scientific notation')
print(date.fromtimestamp(curr).strftime("%b %d %Y"))
