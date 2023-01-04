import tarfile, yaml, json, os
import datetime


class DateTimeEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, datetime.datetime):
            return (str(z))
        else:
            return super().default(z)

# extrahiert die Daten aus der tgz-Datei
def extract_from_tarfile():
    tgz = tarfile.open('download.tgz', 'r')
    tgz.extractall()
    tgz.close()


def convert_yaml_to_json_files(source_file:str, target_dir:str):
    if target_dir not in os.listdir():
        os.mkdir(target_dir)
    with open(source_file, 'r', encoding='utf-8') as file:
        textcontent = file.read()
        for conf in textcontent.split('---\n'):
            if conf == '':
                continue
            jsoncontent = yaml.safe_load(conf)
            # Dateinamen können keine Slashes enthalten!
            with open(f'{target_dir}/{target_dir}_' + str(jsoncontent['_id']).replace('/', '++') + '.json', 'w', encoding='utf-8') as json_file:
                json.dump(jsoncontent, json_file, cls=DateTimeEncoder)


if __name__ == '__main__':
    target_dir = input('Bitte geben Sie das Zielverzeichnis ein: ')
    source_file = input('Bitte geben Sie den Pfad zur Quelldatei ein: ')
    convert_yaml_to_json_files(source_file, target_dir)