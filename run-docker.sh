#!/usr/bin/sh
app="mindset.docker"
docker build -t ${app} .
docker run -dp 5000:5000 --rm --name=${app} --network=host ${app}
