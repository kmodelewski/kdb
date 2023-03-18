
import time
todo: list = ['first job', 'second job', 'third job ']
done: list = []
def manufacturing_process(todo: list, done: list) -> list:
    print("---------Starting process----------")
    print(f"todo list: {todo}, done list: {done}")


    while todo:
        removed_item = todo.pop()
        print(f"---removing item: {removed_item}")
        time.sleep(1)
        done.append(removed_item)
        print(f" added to done list {removed_item}")
        time.sleep(1)
    print(f"todo list: {todo}, done list: {done}")
manufacturing_process(todo, done)
