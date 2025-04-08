#!/bin/bash
echo "#############################"
echo "STARTING TEST ${TEST}"
echo "BROWSER NAME ${BROWSER}"
echo "#############################"
# clean results folder from previous runs
rm -rf results/*

TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
# execute pytest to run an existing test in this project
poetry run pytest \
    --qase-mode=testops \
    --qase-testops-api-token=$QASE_API_TOKEN \
    --qase-testops-project=SL \
    --qase-testops-run-title="${TEST} tests - ${TIMESTAMP}" \
    --alluredir=./results \
    --strict-markers -s --verbose --browser ${BROWSER} -m ${TEST}