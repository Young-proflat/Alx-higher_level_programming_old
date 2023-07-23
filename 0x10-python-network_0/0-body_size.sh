#!/bin/bash

#curl using bash script to send,request and display
curl -sI "$1" | grep 'Content-length' | awk '{print $2}'
