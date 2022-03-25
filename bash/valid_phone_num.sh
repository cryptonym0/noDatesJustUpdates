#!/bin/bash
#https://leetcode.com/problems/valid-phone-numbers/submissions/
#grep -Po '^(?\d{3}\)\s{1}\d{3}\-\d{4}|\d{3}\-\d{3}\-\d{4}$' file.txt
grep -Po '^(\(\d{3}\) |\d{3}-)\d{3}-\d{4}$' file.txt