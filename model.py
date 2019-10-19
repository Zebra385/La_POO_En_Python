#-*- coding: utf8 -*-#codage in french
import json# import the modul json

class Agent:# definition class Agen
    
    def __init__(self, **agent_attributes):# definition o a attribut to the class (the "**" for attribute parameter those a key in dyctionnary)
        for attr_name, attr_value in agent_attributes.items():# item to know the name and value of all keys
            setattr(self, attr_name, attr_value)#use a méthod name "setattr() " those take instance(self) in parameter  , le name o attribut et his value

def main():# definition a only fonction to recuper the total value of key agreeableness
    for agent_attributes in json.load(open("agents-100k.json")):# load the name et value of the key in the json file
        agent = Agent(**agent_attributes)#agent is a object of the class Agent whit the total parameters (all key of dictionnary)
        print(agent.age,agent.agreeableness)
		
        
main()