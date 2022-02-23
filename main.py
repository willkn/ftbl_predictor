#!/bin/env python
# Messi isn't in the csv for some reason. Needs to be added. 
from search import search
from radar import plot
from similar import similarPlayers
import settings

def main():
    search()
    plot()
    similarPlayers()


# if __name__ == '__main__':
#     main()

main()