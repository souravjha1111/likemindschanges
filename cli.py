
resourcesTable2 = [
    {
    "image":{
            "userdata":{
                "1":"read",
                "2":"write"
            },
            "accessType":"none"
        }
       } ]

usersTable = [
    {
        "1":"user",
        "2":"none"
    }
]

def addResource(name):
    print(resourcesTable2)
    resourcesTable2[0][name] = {}
    print(resourcesTable2)

# def addAccessOnResourceToRole(accessType, resource, role):
#     if usersTable[0][]

def checkAccess(user, resource, accessType):
    for resourceValue in resourcesTable2:
        if resourceValue[resource]:
            for usersdata in resourceValue[resource]['userdata']:
                if user == usersdata:
                    if resourceValue[resource]['userdata'][user] == accessType:
                        return "yes"
                    else:
                        return "no" 
        #     return "usernotfound"
        # else:
        #     return "resource not found"

def addRoleToUser(role,userId):
    print(usersTable)
    for users in usersTable:
        if users[userId]:
            usersTable[0][userId] = role
    print(usersTable)

def addUser(user):
    usersTable[0][user] = "user"


def addAccess(type):
    for resourceValue in resourcesTable2:
        if resourceValue["image"]:
            resourceValue["image"]['accessType']  = type         

addUser(3)

addRoleToUser("admin","2")
# for val in usersTable:
#     print(val)
print(checkAccess("1","image","read"))
addResource("iamge2")