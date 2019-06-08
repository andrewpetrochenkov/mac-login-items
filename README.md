<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/badge/OS-macOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/mac-login-items.svg?maxAge=3600)](https://pypi.org/project/mac-login-items/)
[![](https://img.shields.io/npm/v/mac-login-items.svg?maxAge=3600)](https://www.npmjs.com/package/mac-login-items)
[![Travis](https://api.travis-ci.org/looking-for-a-job/mac-login-items.svg?branch=master)](https://travis-ci.org/looking-for-a-job/mac-login-items/)

#### Installation
```bash
$ [sudo] npm i -g mac-login-items
```
```bash
$ [sudo] pip install mac-login-items
```

#### Scripts usage
command|`usage`
-|-
`login-items` |`usage: login-items command [args]`
`login-items-add` |`usage: login-items-add path ...`
`login-items-names` |`usage: login-items-names`
`login-items-paths` |`usage: login-items-paths`
`login-items-rm` |`usage: login-items-rm`

#### Examples
```bash
$ login-items names
Google Chrome
Windscribe
```

```bash
$ login-items paths
/Users/username/Applications/Google Chrome.app
/Applications/Windscribe.app
```

```bash
$ login-items add /Applications/CCMenu.app
```

```bash
$ login-items rm CCMenu
```

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>