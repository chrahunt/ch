import multiprocessing
import signal
import time

from ch.debug import get_process_stack


def test_read_child_stack():
    def target():
        def bar():
            signal.pause()

        def foo():
            bar()

        foo()

    p = multiprocessing.Process(target=target)
    p.daemon = True
    p.start()
    time.sleep(1)
    print(get_process_stack(p.pid))
    p.terminate()
    p.join()
