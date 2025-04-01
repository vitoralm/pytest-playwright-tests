#!/bin/bash
echo "#############################"
echo "STARTING TEST"
echo "#############################"
# clean results folder from previous runs
rm -rf results/*
# execute poetry task to run all existing tests in this project
poetry run task test_all