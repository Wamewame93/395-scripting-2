#List of all the difrent types of objects in maya
def objType (oType):
    #Constant prefix
    TYPENAME =['_GEO','_JNT','_OCONST','_TCONST','_PCONST']
    #Return type text
    return (TYPENAME[oType])