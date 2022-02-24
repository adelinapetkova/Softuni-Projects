import os


def files_finder(start_directory, dictionary):
    for obj in os.listdir(start_directory):
        element = os.path.join(start_directory, obj)
        if os.path.isfile(element):
            name, extension= obj.split('.')
            extension='.'+extension
            if extension not in dictionary:
                dictionary[extension]=[]
            dictionary[extension].append(obj)
        elif os.path.isdir(element):
            files_finder(element, dictionary)
    print(dictionary)


files_dictionary = {}
files_finder(os.getcwd(), files_dictionary)

files_dictionary=dict(sorted(files_dictionary.items(), key=lambda x: x[0]))
with open('report.txt', 'w') as file:
    for key, value in files_dictionary.items():
        file.write(f'{key}\n')
        for f in value:
            file.write(f'- - - {f}\n')


