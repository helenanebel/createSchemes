import os, json


def get_keys_recursive(possible_dictionary, indent: str, dictionary):
    if isinstance(possible_dictionary, dict):
        for key in possible_dictionary.keys():
            if key not in dictionary and isinstance(possible_dictionary[key], dict):
                dictionary[key] = {}
            elif isinstance(possible_dictionary[key], str) or isinstance(possible_dictionary[key], list):
                if key not in dictionary:
                    dictionary[key] = []
            get_keys_recursive(possible_dictionary[key], indent + '    ', dictionary[key])
    else:
        if isinstance(possible_dictionary, str) or isinstance(possible_dictionary, list):
            if possible_dictionary not in dictionary:
                dictionary.append(possible_dictionary)



def get_json_scheme(source_dir: str):
    complete_scheme = {}
    for file in os.listdir(source_dir):
        try:
            with open(f'{source_dir}/{file}', 'r') as json_file:
                data = json.load(json_file)
                get_keys_recursive(data, '', complete_scheme)
        except Exception as e:
            print(file)
            print("ERROR:", e)
            # Doppelpunkte in Keys sind in YAML nicht erlaubt, das führt zu einem Fehler!
            # das kann aber nicht automatisiert korrigiert werden, sondern muss händisch geändert werden.
    print(complete_scheme)


if __name__ == '__main__':
    get_json_scheme('area')
