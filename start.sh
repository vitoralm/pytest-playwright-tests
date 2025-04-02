#!/bin/bash
echo "#############################"
echo "STARTING TEST ${TEST}"
echo "BROWSER NAME ${BROWSER}"
echo "#############################"
# clean results folder from previous runs
rm -rf results/*
# execute pytest to run an existing test in this project
poetry run pytest --alluredir=./results --strict-markers -s --verbose --browser ${BROWSER} -m ${TEST}