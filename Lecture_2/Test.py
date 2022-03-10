#This script will add a prefixes to the object name depending on what type of object there is

#IMPORTANT!!!
#The object list is still not done 

import maya.cmds as cmds


def sorter (objectList):
    x=0
    for each in objectList:
        #Sorting object types
        #First check for nondescendats
        child = cmds.listRelatives(each, c=1)
        if (cmds.objectType(each)=='joint'):
            cmds.rename(each, objRename(each,1))
        elif (cmds.objectType(each)=='orientConstraint'):
            cmds.rename(each, objRename(each,2))
        elif (cmds.objectType(each)=='pointConstraint'):
            cmds.rename(each, objRename(each,3))
        elif (cmds.objectType(each)=='parentConstraint'):
            cmds.rename(each, objRename(each,4))
        elif (cmds.objectType(child[x])=='mesh'):
            cmds.rename(each, objRename(each,0))

        x+1

#List of all the difrent types of objects in maya
def objType (oType):
    #Constant prefix
    TYPENAME =['_GEO','_JNT','_OCONST','_TCONST','_PCONST']
    #Return type text
    return (TYPENAME[oType])



def removeFromName(name):
    REMOVELIST = ['_GEO','_JNT','_OCONST','_TCONST','_PCONST','parent','orient','point','Constraint']
    for word in REMOVELIST:
        name = name.replace(word,'')
    print (name)
    return (name)

#Rename object and cleanup of old name 
#ex: old bad name: "Cube_GEO_Constraint_JNT_JNT_JNT" ---> remove old prefix: "Cube" ---> new name: "Cube_GEO"

def objRename (name, oType):
    #clean up old name
    #Add object type to the name 
    return (removeFromName(str(name)) + objType(oType))

sorter(cmds.ls(sl=1))