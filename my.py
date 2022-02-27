def printprojs(projects):
    for p in projects:
        print(p.name,p.totalDays,p.score,p.bbDays,p.noOfRoles)
        for r in p.roles:
            print(r.name,r.level)
def printconts():            
    for c in conts:
        print(c.name,c.noOfSkills)
        for s in c.skills:
            print(s.name, s.level)

def printroles():
    for r,cs in allRoles.items():
        print("-",r)
        for c in cs:
            print(c.name)

class Project:
    def __init__(self, newName, newDays, newScore, newbb, newRoles):
        self.name = newName
        self.totalDays = newDays
        self.score = newScore
        self.bbDays = newbb
        self.noOfRoles = newRoles
        self.roles = []
        
class Contributor:
    def __init__(self, c_name, c_skills):
        self.name = c_name
        self.noOfSkills = c_skills
        self.skills = []
    


class Skill:
    def __init__(self, s_name, s_level):
        self.name = s_name
        self.level = s_level
        
        
conts = []
projects = []
allRoles = {}
with open("e.txt", mode='r', encoding='utf-8') as f:
    line = f.readline()
    noOfC, noOfP = line.split()
    noOfC = int(noOfC)
    noOfP = int(noOfP)
    for i in range(noOfC):
        line = f.readline()
        name, noOfSkills = line.split()
        noOfSkills = int(noOfSkills)
        contributor = Contributor(name,noOfSkills)
        conts.append(contributor)
        for j in range(noOfSkills):
            line = f.readline()
            name, level = line.split()
            level = int(level)
            skill = Skill(name, level)
            contributor.skills.append(skill)
    for i in range(noOfP):
        line = f.readline()
        name, days, score, bbdays, roles = line.split()
        project = Project(name,int(days),int(score),int(bbdays),int(roles))
        projects.append(project)
        for j in range(int(roles)):
            line = f.readline()
            name, level = line.split()
            role = Skill(name,int(level))
            project.roles.append(role)
            
for p in projects:
    for r in project.roles:
        if r.name not in allRoles.keys():
            allRoles[r.name] = []

for c in conts:
    for s in c.skills:
        if s.name in allRoles.keys():
            allRoles[s.name].append(c)
        else:
            allRoles[s.name] = []
            allRoles[s.name].append(c)

assignedcs= set()
tickprojects = []
projects.sort(key=lambda x: x.noOfRoles)
for p in projects:
    p.roles.sort(key=lambda x: x.level, reverse = True)
conts.sort(key=lambda x: x.noOfSkills, reverse = True)

for clist in allRoles.values():
    clist.sort(key=lambda x: x.noOfSkills, reverse =True)

for p in projects:
    line = p.name + "\n"
    assigned = False
    assignedRoles = 0
    projectconts = set()
    for r in p.roles:
        if assigned == True:
            continue
        assigned = False
        for c in allRoles[r.name]:
            #if c in assignedcs:
            #    continue
            if assigned == True:
                break;
            for s in c.skills:
                if assigned == True:
                    break;
                if r.name == s.name:
                    if r.level <= s.level:
                        line = line + c.name + " "
                        assigned = True
                        projectconts.add(c)
                        assignedRoles = assignedRoles + 1
                else:
                    continue
        if assigned == True:
            continue
        for c in allRoles[r.name]:
            #if c in assignedcs:
            #    continue
            if assigned == True:
                break;
            for s in c.skills:
                if assigned == True:
                    break;
                if r.name == s.name:
                    if r.level == 0:
                        line = line + c.name + " "
                        assigned = True
                        projectconts.add(c)
                        assignedRoles = assignedRoles + 1
    if p.noOfRoles == assignedRoles:
        tickprojects.append(p)
        print(line)
        for c in projectconts:
            assignedcs.add(c)
    
            

n = len(tickprojects)
print(n)
# project with least roles
 # roles with least contrs
    # contr with smallest skill that fulfills the role
