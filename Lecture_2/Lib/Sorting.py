import maya.cmds as cmds
from RenameObject import objRename
def sorter (objectList):
    x=0
    for each in objectList:
        #Sorting object types
        #First check for nondescendents so it dosen't search for transforms
        child = cmds.listRelatives(each, c=1)
        print (cmds.objectType(each))
        if (cmds.objectType(each)=='joint'):
            cmds.rename(each, objRename(each,1))
        elif (cmds.objectType(each)=='orientConstraint'):
            cmds.rename(each, objRename(each,2))
        elif (cmds.objectType(each)=='pointConstraint'):
            cmds.rename(each, objRename(each,3))
        elif (cmds.objectType(each)=='parentConstraint'):
            cmds.rename(each, objRename(each,4))
        #descendents to search for
        elif (cmds.objectType(child[x])=='mesh'):
            cmds.rename(each, objRename(each,0))

        x+1