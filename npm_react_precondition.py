import os
import sys
import time

command = [
    "npm i styled-components",
    "npm i --save-dev @types/styled-components",
    "npm i react-router-dom@6.4",
    "npm i --save-dev @types/react-router-dom",
    "npm i react-query",
    "npm i react-helmet",
    "npm i --save-dev @types/react-helmet",
    "npm install recoil",
    "npm install react-hook-form",
    "npm install framer-motion@10.12.4",
    "npm i @chakra-ui/react @emotion/react @emotion/styled framer-motion",
    "npm i @tanstack/react-query-devtools",
    "npm i styled-reset",
    "npm install react-icons --save",
]

# ChagkaUI Doc: https://chakra-ui.com/getting-started
# ReactQuery(TanStack Query) & Devtool Doc: https://tanstack.com/query/v4/docs/react/devtools

# Todo
"""
* npm install react-icons --save
* npm i @chakra-ui/react @emotion/react @emotion/styled framer-motion
"""

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
"""

for c in command:
    help += f" * {c}\n"

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
