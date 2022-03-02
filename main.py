#!/bin/env python
from predictor import predictValue
from search import search
from radar import plot
from similar import similarPlayers
import settings

def main():
    search()
    plot(predictValue(settings.currentPlayer.get('short_name')))
    similarPlayers()


# if __name__ == '__main__':
#     main()

main()