
def extract_lines(file):
    with open(file) as f:
        return [i.replace('\n', '') for i in f.readlines()]

