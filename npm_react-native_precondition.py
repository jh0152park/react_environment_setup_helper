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

# App.tsx, prettier, eslint setting

print(f"{'*'*10} App.tsx, prettier, eslint start to set. {'*'*10}")
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

print(f"{'*'*10} App.tsx, prettier, eslint set is done. {'*'*10}")

# ios react-native-vector-icons setting
print(
    f"{'*'*10} ios Info.plist start to set for using react-native-vector-icons. {'*'*10}"
)

ios_project_path = os.path.join("ios", NAME)
info_plist_path = os.path.join(created_path, ios_project_path)

os.chdir(info_plist_path)
time.sleep(1)

# Info.plist 파일 읽기
info_plist = "Info.plist"

with open(info_plist, "r", encoding="utf-8") as file:
    lines = file.readlines()

# 찾을 문자열
search_string = "</dict>"

# 찾은 문자열의 인덱스
index = None

# 뒤에서부터 역순으로 검색하여 가장 끝에 있는 </dict> 찾기
for i in range(len(lines) - 1, -1, -1):
    if search_string in lines[i]:
        index = i
        break

# 추가할 Key-Values 선언
new_key_values = """
    <key>UIAppFonts</key>
    <array>
		<string>AntDesign.ttf</string>
		<string>Entypo.ttf</string>
		<string>EvilIcons.ttf</string>
		<string>Feather.ttf</string>
		<string>FontAwesome.ttf</string>
		<string>FontAwesome5_Brands.ttf</string>
		<string>FontAwesome5_Regular.ttf</string>
		<string>FontAwesome5_Solid.ttf</string>
		<string>FontAwesome6_Brands.ttf</string>
		<string>FontAwesome6_Regular.ttf</string>
		<string>FontAwesome6_Solid.ttf</string>
		<string>Foundation.ttf</string>
		<string>Ionicons.ttf</string>
		<string>MaterialIcons.ttf</string>
		<string>MaterialCommunityIcons.ttf</string>
		<string>SimpleLineIcons.ttf</string>
		<string>Octicons.ttf</string>
		<string>Zocial.ttf</string>
		<string>Fontisto.ttf</string>
	</array>
"""

# 해당 라인 뒤에 새로운 Key-Values 추가
lines.insert(index, new_key_values)

# 수정된 내용을 파일에 쓰기
with open(info_plist, "w", encoding="utf-8") as file:
    file.writelines(lines)

print(f"{'*'*10} ios Info.plist set is done. {'*'*10}")

# android react-native-vector-icons setting
print(
    f"{'*'*10} android build.gradle start to set for using react-native-vector-icons. {'*'*10}"
)

android_app_path = os.path.join(created_path, "android/app")

os.chdir(android_app_path)
time.sleep(1)

build_gradle = "build.gradle"

add_android_method = (
    "apply from: file('../../node_modules/react-native-vector-icons/fonts.gradle')"
)

with open(build_gradle, "a") as build_gradle_file:
    build_gradle_file.write(add_android_method)

print(f"{'*'*10} android build.gradle set is done. {'*'*10}")

print(f"{'*'*10} ios pod install start to run commands. {'*'*10}")

os.chdir(created_path)
time.sleep(1)

os.system("npx pod-install ios")
time.sleep(0.5)

print(f"{'*'*10} ios pod install is done. {'*'*10}")
