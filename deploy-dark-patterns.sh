#!/bin/sh

docker build -t jcgardey/dark-patterns ./dark-patterns-api --no-cache
docker push jcgardey/dark-patterns

docker build -t jcgardey/dark-patterns-front ./dark-patterns --no-cache
docker push jcgardey/dark-patterns-front