def podpis(datoteka):
    with open(datoteka, 'w') as f:
        print('France', 'Pesnik', file=f)
    return True
