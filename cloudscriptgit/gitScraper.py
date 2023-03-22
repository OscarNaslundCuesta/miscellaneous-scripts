"""
Scrapes previous git commits and searches for a string in all the files in that branch. In this case "flag{"
"""
import os

with open("input.txt", "r") as input:
    lines = input.readlines()

for line in lines:
    if line[:6] == "commit":
        commitline = line.strip().split(" ")
        commit = commitline[1]
        os.system(f"git checkout {commit}")
        os.system("cat * | grep flag{") #cat abuse