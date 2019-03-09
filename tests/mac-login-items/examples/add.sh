#!/usr/bin/env bash
{ set +x; } 2>/dev/null

set --
[ -d /Applications/Übersicht.app ] && set -- "$@" /Applications/Übersicht.app
[ -d /Applications/Growl.app ] && set -- "$@" /Applications/Growl.app

( set -x; login-items add "$@" )
