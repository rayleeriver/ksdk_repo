def make_tree(path):
    tree = dict(name=os.path.basename(path), children=[])
    print os.path.basename(path)
    open(name + '/index.html','w') 
    try: lst = os.listdir(path)
    except OSError:
        pass #ignore errors
    else:
        for name in lst:
            fn = os.path.join(path, name)
            if os.path.isdir(fn):
                tree['children'].append(make_tree(fn))
            else:
                tree['children'].append(dict(name=name))
    return tree


