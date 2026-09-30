# -------------------- Sequential Process --------------------


# import time

# def work():
#     time.sleep(2)

# start = time.time()
# for i in range(4):
#     work()

# end = time.time()
# seq_time = end - start
# print("Sequential Time: ", seq_time)




# -------------------- Parallel Process --------------------


# import time
# import threading

# def task1():
#     print("Task1 Started")
#     time.sleep(2)
#     print("Task1 Ended")

# def task2():
#     print("Task2 Started")
#     time.sleep(2)
#     print("Task2 Ended")

# start = time.time()

# t1 = threading.Thread(target=task1)
# t2 = threading.Thread(target=task2)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# end = time.time()
# par_time = end - start
# print("Parallel Time: ", par_time)