#!/bin/bash

#curl using bash script to send,request and display
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
