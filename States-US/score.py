import turtle

class Score:
    def __init__(self):
        self.score = 0  # Initial score
        self.writer = turtle.Turtle()
        self.writer.hideturtle()  # Hide the turtle icon
        self.writer.penup()
        self.writer.goto(0, 250)  # You can adjust this position to fit your map
        self.update_score()

    def update_score(self):
        """Clear previous score and write new one."""
        self.writer.clear()  # Clear previous score
        self.writer.write(f"Score: {self.score}", align="center", font=("Arial", 16, "bold"))

    def increase_score(self):
        """Increase score and update display."""
        self.score += 1
        self.update_score()
