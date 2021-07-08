# Algorithms_Visualiser
Python code for visualising Graph algorithms
The algorithms included are 
1) Dijkstra's shortest path algorithm 
2) Bellmann-Ford algorithm 
3) Breadth-First Search

Each of these is combined into a single .py file.
The visualisation is done using PyGame; a small PyGame window allows the user to choose the intial point and the target point in a grid of cells.
The user can also create a wall (cells which are exluded from the grid). The path-finding algorithm shall find the shortest path (if it exists) from the initial to the target cell, finding a way around the wall.

1) To start, run the code.
2) Once you see a grid of cells, you can select the starting point by left-clicking on the cell. This point will be highlighted in blue.
3) Once the initial cell has been chosen, you can choose the endpoint by clicking on another cell in the grid. This is highlighted in red.
4) Now, you can create a wall (black cells). If you want to make individual cells black, you can click on that cell; however, since the grid is quite large, you can keep the mouse clicked, a drag the mouse to create the wall; this is much faster that clicking one at a time.
5) If you are not satisfied with the cells, you can reset the cells by left-clicking on them (note that dragging while left-clicking will still work).
6) Once you are satisfied, click the space bar to run the visualiser. 
7) Now, wait and see the magic!
8) Additionaly, the algorithm also prints out the path, but in terms of the (x,y) co-ordinates of the cells.
