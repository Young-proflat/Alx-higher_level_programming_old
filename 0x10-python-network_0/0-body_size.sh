#!/bin/bash

# Curl using bash script to response in size bytes
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
