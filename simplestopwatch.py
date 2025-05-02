import time
input("Press Enter to start")
start = time.time()
input("Press Enter to stop")
end = time.time()
elapsed = end - start
print(f"Elapsed time: {elapsed:.2f} seconds")