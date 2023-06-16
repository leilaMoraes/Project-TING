def exists_word(word, instance):
    result = []

    for i in range(len(instance)):
        file = instance.search(i)
        info = {
            'palavra': word,
            'arquivo': file['nome_do_arquivo'],
            'ocorrencias': []
        }
        for phrase in file['linhas_do_arquivo']:
            if word.lower() in phrase.lower():
                info['ocorrencias'].append({
                    'linha': file['linhas_do_arquivo'].index(phrase) + 1
                })
        if info["ocorrencias"]:
            result.append(info)

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
