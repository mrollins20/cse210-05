# CSE210-05: greed game

# TODO 
    -write program including at least 8 classes

## Overview: 
    Greed is a game where the player seeks to gather as many falling gems as possible. 
    The game continues until the player wishes to stop (or runs out of lives?).

## Running the Game:
To start the game, begin by running the "__main__.py" file. 

## Help/Information:
    directory:
        root (main folder/parent folder)
        |
        \---greed
        |   |    __main__.py
        |   \---game
        |       |
        |       \---directing
        |       |   |
        |       |   |   director.py
        |       |
        |       \---services
        |       |
        |       \---shared
        |
        \---__main__.py
    
    ```
    root                            (project root folder)
    +-- greed                       (source code for game)
      +-- game                      (specific game classes)
        +-- casting                 (contains classes for entities)
            +-- ?
        +-- directing               (contains director class)
            +-- director.py
        +-- services                (contains keyboard and video classes borrowed from "BYUI's, rfk game" code)
            +-- keyboard_service.py 
            +-- video_service.py
        +-- shared                  (contains color and point classes borrowed from "BYUI's, rfk game" code)
            +-- color.py
            +-- point.py
      +-- __main__.py               (entry point for program)
    +-- README.md                   (general info)
    ```

To find more information, you can see the base code in the repository at https://github.com/mrollins20/cse210-05

## Contributers:
    Helaman Cristian Pinheiro Ewerton - 
    Lorenzo Tarati - 
    Marc Rollins - 
    Robbie Platt - 
