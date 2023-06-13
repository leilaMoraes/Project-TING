from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    if instance.is_duplicate(path_file):
        return

    file = txt_importer(path_file)
    if file:
        data = {
            'nome_do_arquivo': path_file,
            'qtd_linhas': len(file),
            'linhas_do_arquivo': file,
        }

        instance.enqueue(data)
        instance.add(data)
        print(data)


def remove(instance):
    if len(instance) == 0:
        return print("Não há elementos")
    file = instance.dequeue()
    path_file = file['nome_do_arquivo']
    return print(f"Arquivo {path_file} removido com sucesso")


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        return print(file)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
