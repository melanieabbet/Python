class Car:

    RIGHT_TURN = {"up": "right", "right": "down", "down": "left", "left": "up"}
    LEFT_TURN = {"up": "left", "left": "down", "down": "right", "right": "up"}

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
    def state(self):
        print(f"Car: x={self.x} y={self.y} direction={self.direction}")
    
    def forward(self, distance=1):
        if distance >= 0:
            if self.direction == "up":
                self.y += distance
            if self.direction == "down":
                self.y -= distance
            if self.direction == "right":
                self.x += distance
            if self.direction == "left":
                self.x -= distance
        else:
            raise ValueError("Going forward the distance value has to be positive")
    def right(self):
        self.direction = self.RIGHT_TURN[self.direction]
    def left(self):
        self.direction = self.LEFT_TURN[self.direction]

    