import os
import sys
import time

command = [
    "npm i styled-components",
    "npm i --save-dev @types/styled-components @types/styled-components-react-native",
    "npm i react-query",
    "npm i recoil",
    "npm i @react-navigation/native",
    "npm i @react-navigation/native-stack",
    "npm i @react-navigation/bottom-tabs",
    "npm i react-native-screens",
    "npm i react-native-safe-area-context",
    "npm i react-native-vector-icons",
    "npm i -D @types/react-native-vector-icons",
    "npm i react-native-svg",
    "npm i -D eslint-config-prettier",
    "npm i @gluestack-style/react",
    "npm i @gluestack-ui/config",
    "npm i @gluestack-ui/overlay",
    "npm i @gluestack-ui/themed",
    "npm i @gluestack-ui/toast",
    "npx pod-install ios",
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

os.system(f"npx react-native@latest init {NAME}")
print(f"{'*'*10} create react native application done. {'*'*10}")
time.sleep(1)

os.chdir(NAME)
print(f"{'*'*10} change directory to {NAME} done. {'*'*10}")
time.sleep(1)

print(f"{'*'*10} start to run commands. {'*'*10}")
for cmd in command:
    os.system(cmd)
    print(f"{'*'*10} {cmd} is done. {'*'*10}")
    time.sleep(0.5)

created_path = os.path.join(PATH, NAME)
os.chdir(created_path)
time.sleep(1)

app = "App.tsx"

replacement_app_code = """
import React from "react";
import {GluestackUIProvider, Heading} from "@gluestack-ui/themed";
import {config} from "@gluestack-ui/config";
import {ToastProvider} from "@gluestack-ui/toast";
import {OverlayProvider} from "@gluestack-ui/overlay";
import {SafeAreaProvider} from "react-native-safe-area-context";

function App(): JSX.Element {
    return (
        <GluestackUIProvider config={config}>
            <SafeAreaProvider>
                <ToastProvider>
                    <OverlayProvider>
                        <Heading>Hello world!</Heading>
                    </OverlayProvider>
                </ToastProvider>
            </SafeAreaProvider>
        </GluestackUIProvider>
    );
}

export default App;
"""

with open(app, "w") as app_file:
    app_file.write(replacement_app_code)

prettier = ".prettierrc.js"

replacement_prettier_code = """
module.exports = {
    arrowParens: 'avoid',
    bracketSameLine: true,
    bracketSpacing: false,
    singleQuote: false,
    trailingComma: 'all',
    tabWidth: 4,
};
"""

with open(prettier, "w") as prettier_file:
    prettier_file.write(replacement_prettier_code)

eslint = ".eslintrc.js"

replacement_eslint_code = """
module.exports = {
    root: true,
    extends: ["@react-native", "prettier"],
    rules: {
        "react-native/no-inline-styles": 0,
        "prettier/prettier": [
            "error",
            {
                "no-inline-styles": false,
            },
        ],
    },
};
"""

with open(eslint, "w") as eslint_file:
    eslint_file.write(replacement_eslint_code)

print(
    "react-native-vector-icons requires additional settings.\nPlease check docs and set it."
)
