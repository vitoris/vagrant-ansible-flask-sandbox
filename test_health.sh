#!/bin/bash

host='10.2.2.25'

for i in {1..10}
do
echo "LB Check $i"
curl $host
echo
done
