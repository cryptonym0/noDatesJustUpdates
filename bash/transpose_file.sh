#!/bin/bash
# https://leetcode.com/problems/transpose-file/submissions/
seq "$(awk '{print NF}' file.txt| head -n 1)" | xargs -r -I {} sh -c "awk '{print \${}}' file.txt | xargs -r"