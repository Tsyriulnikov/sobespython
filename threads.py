from time import sleep, perf_counter
from threading import Thread

def task(id):
    print(f'Start task {id}...')
    sleep(1)
    print(f'Task {id} finished')

start_time = perf_counter()

# create and run 10 threads
threads = []
for n in range(1,11):
    t = Thread(target=task, args=(n,))
    threads.append(t)
    t.start()
# await
for t in threads:
    t.join()
end_time = perf_counter()
print(f'All time {end_time - start_time: 0.2f}seconds.')