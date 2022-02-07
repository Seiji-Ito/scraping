
"""
[description] : insert line break after specific character.
[argument]
target        : target string.
token         : Which character insert a line break.
"""
def insert_break_after_token(target, token):
    print(target.index('\''))

def write_dirdata_to_textfile(filename, dirdata):
    f = open(filename, 'w')

    for data in dirdata:
        f.write(data + '\n')

    f.close()