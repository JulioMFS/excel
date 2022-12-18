def isfloat(num):
    num = num.replace('.', '')
    num = num.replace(',', '.')
    try:
        float(num)
        return True
    except ValueError:
        return False