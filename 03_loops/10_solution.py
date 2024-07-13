import time
wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
  attempts += 1
  print("Attempts ", attempts, " -wait  time", wait_time)
  time.sleep(wait_time)
  wait_time *= 2
  if  wait_time < 64:
    break

