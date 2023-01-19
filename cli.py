#resourcetable2 consist of a list of resources with userdata as a dict, which contains list of users with their access type on this resource, it alos has a value as universalAccessType 
#   which defines it's access type for all users

resourcesTable2 = [
    {
    "image":{
            "userdata":{
                "1":"read",
                "2":"write"
            },
            "universalAccessType":"none"
        }
       } ]


#usertable contains a list of users with their type that can be user or admin
usersTable = [
    {
        "1":"user",
        "2":"admin"
    }
]

def addAccess(type):# type is read or write
    for resourceValue in resourcesTable2:
        if resourceValue["image"]:
            resourceValue["image"]['universalAccessType']  = type         


def addResource(name): # name is resource name
    resourcesTable2[0][name] = {
        "userdata":{},
        "universalAccessType":"none"
    }
 
def addActionOnResource(accessType, resourceName):
    for resourceValue in resourcesTable2:
        if resourceValue[resourceName]:
            resourceValue[resourceName]['universalAccessType']  = accessType
         


def addAccessOnResourceToRole(access, resource, role):
    print("before addAccessOnResourceToRole",resourcesTable2)
    for users in usersTable:
        for val in users:
            if usersTable[0][val] == role:
                resourcesTable2[0][resource]['userdata'][val] = access
    print("after addAccessOnResourceToRole",resourcesTable2)


def checkAccess(user, resource, accessType):
    for resourceValue in resourcesTable2:
        if resourceValue[resource]:
            for usersdata in resourceValue[resource]['userdata']:
                if user == usersdata:
                    if resourceValue[resource]['userdata'][user] == accessType:
                        return "yes"
                    else:
                        return "no" 


def addUser(user):
    print("before addUser", usersTable)
    usersTable[0][user] = "user"
    print("after addUser", usersTable)




def addRoleToUser(role,userId):
    print(usersTable)
    for users in usersTable:
        if users[userId]:
            usersTable[0][userId] = role
    print(usersTable)

# addAccess("read")
# addResource("iamge2")
# addAccessOnResourceToRole("write","image")
# addAccessOnResourceToRole("read", "image","admin")
# checkAccess("1","image","read")