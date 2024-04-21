import json
from json import JSONDecodeError,JSONEncoder

# json to python
jsonString='{"a":"apple","b":"ball"}'
try:
    jb=json.loads(jsonString)
    print(jb) 
except JSONDecodeError:
    print("could not decode the error")
    
#python to json   
pythondict={"a":"apple","b":"ball"}
json.dump(pythondict)

#custom jason
class Animal:
    def __int__(self,name):
        self.name=name
        
class AnimalEncoder(JSONEncoder):
    def default(self,o):
        if type(o)==Animal:
            return o.name
        return super().default(o)
    
pythoDict={"a":Animal("cat"),"b":Animal("buffalloo")}

json.dumps(pythondict,cls=AnimalEncoder)