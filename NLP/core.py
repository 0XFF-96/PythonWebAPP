

def process_data(data):

    l = len(data)

    if l < 5:
        return 'Good question '
    elif l < 10:
        return 'Not bad'
    else:
        return 'sorry , I can\'t full understand you'


