import threading, queue

input_q = queue.Queue()
output_q = queue.Queue()

def split_args(args, slices):
    slices_size = len(args) // slices
    return [args[slices_size * i : (slices_size*i)+slices_size if i < slices-1 else -1] for i in range(slices)]

def split_and_merge(nthreads, merge_function):
    def decorator(F):
        def wrapper(*args):
            lists = split_args(args[0], nthreads)
            for el in lists:
                input_q.put(el)
                t = threading.Thread(target=runner)
                t.start()
            input_q.join()
            return merge_function([output_q.get() for i in range(nthreads)])

        def runner():
            arg = input_q.get()
            print("Runner started on: {}".format(arg))
            output_q.put(F(arg))
            input_q.task_done()

        return wrapper
    return decorator
