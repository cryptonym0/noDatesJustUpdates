#!/bin/bash
#https://leetcode.com/problems/word-frequency/submissions/
cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -r | awk '{print $2" "$1}'