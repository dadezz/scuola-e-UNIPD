# 1pc = 3,26 al

def conversione (a, b, step):
    pct = []
    alt = []
    for pc in range (a, b, step):
        al=pc*3.26
        pct.append(pc)
        alt.append(al)
    return alt
