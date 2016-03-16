import json
data = []
with open("aa5.dat") as f:
    content =  f.readlines()
    for one in content:
        try:
            phi,theta,Ek = one.split()
            data.append({'x':0,'y':0,"theta":float(theta),"phi":float(phi),"Ek":float(Ek),"charge":1,"mass":1,"B":2})
        except:
            continue
o = json.dumps(data)

with open("StartCondition5.json",'w') as f:
    f.write(o)
