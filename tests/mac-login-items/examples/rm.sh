#!/usr/bin/env bash
{ set +x; } 2>/dev/null

set -- Calendar Growl

( set -x; login-items rm "$@" )
