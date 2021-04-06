#!/bin/bash

for i in 1 2
do
	python3 stochastic_engine.py $1 $i
done
