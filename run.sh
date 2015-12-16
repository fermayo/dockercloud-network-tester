#!/bin/sh

python -mSimpleHTTPServer > /dev/null 2>&1 &
exec python test.py