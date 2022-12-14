# Rubik's Cube rotations

This README only briefly tells about the task and shows some results. Longer
story appears in my blog post:
https://barahilia.github.io/blog/computers/2022/09/26/rubik-rotation.html

## About
This project was created to simulate a series of Rubic's cube rotations. A full
cycle runs in iterations to count the number to get back to the initial state.
The series comprises two actions: rotate right side clockwise, then rotate down
side clockwise. In common notation:
```
RD
```

The project features:
- 2D unfolded cube representation of 6 sides
- color output in terminal

## Show case
First, the start state:

![start](start.png)

Next rotate right side clockwise:

![rotate_right](rotate_right.png)

After that, rotate down side clockwise, completing one full cycle:

![right_down](right_down.png)
