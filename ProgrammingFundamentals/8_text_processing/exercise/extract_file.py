path=rf'{input()}'
paths=path.split('\\')

name, extension=paths[len(paths)-1].split('.')

print(f'File name: {name}')
print(f'File extension: {extension}')


