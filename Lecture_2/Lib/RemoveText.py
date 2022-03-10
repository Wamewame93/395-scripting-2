
def removeFromName(name):
    REMOVELIST = ['_GEO','_JNT','_OCONST','_TCONST','_PCONST','parent','orient','point','Constraint']
    for word in REMOVELIST:
        name = name.replace(word,'')
    print (name)
    return (name)