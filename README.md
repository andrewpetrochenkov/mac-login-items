<!--
https://pypi.org/project/readme-generator/
-->

[![](https://img.shields.io/badge/OS-MacOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/pyversions/mac-login-items.svg?longCache=True)](https://pypi.org/project/mac-login-items/)
[![](https://img.shields.io/pypi/v/mac-login-items.svg?maxAge=3600)](https://pypi.org/project/mac-login-items/)
[![](https://img.shields.io/npm/v/mac-login-items.svg?maxAge=3600)](https://www.npmjs.com/package/mac-login-items)
[![Travis](https://api.travis-ci.org/looking-for-a-job/mac-login-items.svg?branch=master)](https://travis-ci.org/looking-for-a-job/mac-login-items/)

#### Installation
```bash
$ [sudo] npm i -g mac-login-items
```
```bash
[sudo] pip install mac-login-items
```

#### CLI
```bash
usage: login-items command [args]

Available commands:
    add                    add login items
    list                   print login items names
    paths                  print login items paths
    rm                     remove login items

run `login-items COMMAND --help` for more infos
```

#### Examples
```bash
$ login-items names
Google Chrome
Windscribe
```

```bash
$ login-items paths
/Users/russianidiot/Applications/Google Chrome.app
/Applications/Windscribe.app
```

```bash
$ login-items add /Applications/CCMenu.app
```

```bash
$ login-items rm CCMenu
```

<p align="center">
    <a href="https://pypi.org/project/readme-generator/">readme-generator</a>
</p>