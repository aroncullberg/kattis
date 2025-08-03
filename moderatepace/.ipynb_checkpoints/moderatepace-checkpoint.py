from statistics import median
import sys

n = int(input())
mystat = map(int, input().split())
firstcoleguqestat = map(int, input().split())
secondcoleguqestat = map(int, input().split())
for t in zip(mystat,firstcoleguqestat,secondcoleguqestat):
    print(median(t))