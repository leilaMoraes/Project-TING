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
        print(data, sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
