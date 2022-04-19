def mr (v):
    if len(v)==1:
        return v[0]
    else:

        func=mr(v[1:])
        if v[0]<func:
            return v[0]
        else:
            return func

v=[12,6,2,8,4]
print(mr(v))
