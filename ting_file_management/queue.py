from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._queue = list()
        self._processed_files = set()

    def __len__(self):
        return len(self._queue)

    def enqueue(self, value):
        self._queue.append(value)

    def dequeue(self):
        if len(self._queue) == 0:
            raise IndexError("A fila está vazia")
        return self._queue.pop(0)

    def search(self, index):
        if index >= 0 and index < len(self._queue):
            return self._queue[index]
        raise IndexError("Índice Inválido ou Inexistente")

    def is_duplicate(self, file_name):
        return file_name in self._processed_files

    def add(self, data):
        file_name = data['nome_do_arquivo']
        self._processed_files.add(file_name)
