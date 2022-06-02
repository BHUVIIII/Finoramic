from pip._internal import main
import pip
import json

uninstalled = []
with open ("dependencies.json") as jfile:
    data = json.load(jfile)
    for i in data["dependencies"]:
        pip.main(["install", i])
        if ImportError:
            uninstalled.append(i)

if(len(uninstalled)==0):
    print("success")

else:
    print("Failed to install packages")
    for j in uninstalled:
        print(j)
