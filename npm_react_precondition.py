import os
import sys
import time

help = """
Two parameters necessary to run this script work find.

Fisrt - The path of you want to create new react application
Seceond - The name of will be created new react application

How to use this script?
python npm_react_precondition.py [First] [Second]
                    or
npm_react_precondition.py [First] [Second]
                    or
./npm_react_precondition.py [First] [Second]

Commands to be executed.
 * npm i --save-dev @types/styled-components
 * npm i styled-components
 * npm i react-router-dom@5.3.4
 * npm i react-query
 * npm i --save-dev @types/react-router-dom
"""

try:
    helps = ("-h", "--help")
    INPUTS = sys.argv[1:]
    PATH = INPUTS[0]
    NAME = INPUTS[1]

    if PATH.endswith(helps) or len(INPUTS) < 2:
        print(help)
        exit(0)
except Exception as ex:
    print(help)
    exit(0)
    
command = [
    "npm i --save-dev @types/styled-components",
    "npm i styled-components",
    "npm i react-router-dom@5.3.4",
    "npm i react-query",
    "npm i --save-dev @types/react-router-dom"
]

os.chdir(PATH)
print(f"{'*'*10} change directory to {PATH} done. {'*'*10}")
time.sleep(1)

os.system(f"npx create-react-app {NAME} --template typescript")
print(f"{'*'*10} create react application done. {'*'*10}")
time.sleep(1)

os.chdir(NAME)
print(f"{'*'*10} change directory to {NAME} done. {'*'*10}")
time.sleep(1)

print(f"{'*'*10} start to run commands. {'*'*10}")
for cmd in command:
    os.system(cmd)
    print(f"{'*'*10} {cmd} is done. {'*'*10}")
    time.sleep(0.5)