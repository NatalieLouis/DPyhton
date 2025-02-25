import threading

# 共享变量
counter = 0


def increment():
    global counter
    for _ in range(1000000):
        counter += 1


def decrement():
    global counter
    for _ in range(1000000):
        counter -= 1


# 创建线程
threads = []
for _ in range(5):
    t1 = threading.Thread(target=increment)
    t2 = threading.Thread(target=decrement)
    t1.start()
    t2.start()
    threads.append(t1)
    threads.append(t2)

# 等待所有线程完成
for t in threads:
    t.join()

print(f"Final counter value: {counter}")
