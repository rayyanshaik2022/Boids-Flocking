# Boids-Flocking
- My implementation of the boids flocking algorithm in pygame. It uses arrows - representative of birds - as enties that move around and account for each other’s positions.
The boids flocking algorithm in its self is a representation of how birds and other herds of animals move together.
- What do "Boids" account for?
  - Separation: Steer to avoid contact with other entities
  - Alignment: Steer towards the average direction of nearby entities
  - Cohesion: Steer towards the average position of all entities

## Primary Dependencies
- numpy
  - Used for specific math operations such as normalization functions
- pygame
  - Used to draw the graphics
  
## My Implementation
- Object Oriented Approach
  - The primary class is `Boids`. An object of this class represents one specific entity that has attributes for its velocity (speed and direction), position, and color.
  The `main.py` file instantiates a number of these objects and then updates them relative to one another.
- Coloration
  - All boids "spawn" with random color values, but when they come together and create a flock, boids start to assume the average color value of the flock.
  For example, if a flock consisted of two natively red boids, and one natively yellow boid, the flock would be seen to the viewer as orange. (Only the hue component of the color changes)
- "Infinite Borders"
  - When a boid travels in a direction off the screen, they are teleported to the opposite of the exceeded value.
