#!/bin/bash

#curl using bash script to send,request and display
curl -sI "$1"| grep 'Content-layer' | awk '{print $2}'
