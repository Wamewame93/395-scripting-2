from RemoveText import removeFromName
from Typelist import objType

#Rename object and cleanup of old name 
#ex: old bad name: "Cube_GEO_Constraint_JNT_JNT_JNT" ---> remove old prefix: "Cube" ---> new name: "Cube_GEO"

def objRename (name, oType):
    #Cleanup old name and add object type name
    return (removeFromName(str(name)) + objType(oType))