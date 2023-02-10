# Sort and Search Simulation

This repository aims to simulate many search and sort algorithms to better understand how they work, their differences, and best use cases using python [pygame](https://www.pygame.org/docs/) module

The covered sort algorithms are:
  - Selection Sort
  - Bubble Sort
  - Insertion Sort
  - Quick Sort
  - Counting Sort
  - Bucket Sort
  - Merge Sort
 
 Searching algorithms are yet to be implemented (Search list is empty for now)
 
 
## Setup
 
 1. Install python 3.xx [here](https://www.python.org/downloads/)
  
 2. Clone the repository:
 
```
 git clone https://github.com/KhaledR4/Sort-and-Search-Simulation.git
```

 3. In root directory where repository was cloned:
 
 ```
  pip install pygame
  python main.py
 ```
 
## Make changes

To add and try algorithms of your own define a new function in Sort_algos.py.

Note that some algorithms use previously implemented ones so don't hesitate to use them.

After successfully adding a new algorithm don't forget to add its legend in Drawing/objects.py DrawLegends class (add it as a static method as done with all other algorithms).

## Demo

A peak on two of the implemented algorithms:

<div>
<img src="https://user-images.githubusercontent.com/94381448/218177429-92dec52b-9861-427d-b8ee-e11ae41ed14a.png" height=500></img>
<img src="https://user-images.githubusercontent.com/94381448/218177886-f7c059b5-bdcd-40e1-b8ae-eb6a816c1181.png" height=500></img>
</div>

