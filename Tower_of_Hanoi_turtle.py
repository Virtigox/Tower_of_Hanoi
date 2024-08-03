import turtle


# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Tower of Hanoi Puzzle")


class Disk():
    def __init__(self, disk_name, tower_info, disk_color, disk_measurement):
        self.t = turtle.Turtle() # each disk have different turtle object
        # Hide the turtle
        self.t.hideturtle()
        self.t.speed(1)


        self.disk_type = disk_name
        self.pre_disk_pos = [0,0]
        self.width, self.height = disk_measurement
        self.tower = tower_info
        self.tower_name,self.pos = tower_info.tower_type, tower_info.pos
        self.color = disk_color
        self.actions = 0  # Track the number of actions
        


    def draw_disks(self, other_tower = None):
        
        if other_tower is not None:
            other_tower.no_of_disks += 1
            placing = self.tower.no_of_disks  - other_tower.no_of_disks
            self.tower.no_of_disks -= 1
            other_tower.add_disk(self.tower.disks_holder.pop())
            self.pos = other_tower.pos # change tower position
            self.tower = other_tower # tower also changed
            
        else:
            self.tower.no_of_disks += 1
            self.tower.add_disk(self) # adding a disk onto tower
            
         
        print(self.tower.disks_holder[-1].disk_type, " : ",self.tower.disks_holder[-1].tower_name )
        self.height, self.width, self.color = self.tower.disks_holder[-1].height,self.tower.disks_holder[-1].width,self.tower.disks_holder[-1].color # new disck from tower.
       
       # Calculate vertical position
        vertical_position = (self.tower.no_of_disks - 1) * self.height

        # Calculate horizontal position
        tower_center_x = self.tower.pos[0] + (self.tower.width / 2)
        disk_start_x = tower_center_x - (self.width / 2)

        # Set the final position
        x = disk_start_x
        y =  -190  + vertical_position

        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()
        self.t.color(self.color)
        self.t.begin_fill()
        for _ in range(2):
            self.t.forward(self.width)
            self.t.right(90)
            self.t.forward(self.height)
            self.t.right(90)
        self.t.end_fill()
        self.actions += 1  # Increment the action count
        

    def move_disk_to(self, other_tower):
        self.erase_disk()  # Erase the disk from its current position
        self.draw_disks(other_tower)

    def erase_disk(self):
        self.t.clear()
        
  



class Tower():
    def __init__(self,measurement, tower_name,starting_pos, tower_color):
        self.tower_type = tower_name
        self.width, self.height = measurement
        self.color = tower_color
        self.pos  = starting_pos
        self.no_of_disks = 0
        self.disks_holder = [] # a stack like list to hold the disk in decending order, only smaller disck can put top of the big one.
        self.t = turtle.Turtle()
        # Hide the turtle
        self.t.hideturtle()
        self.t.speed(10)

    # Function to draw a rectangle
    def draw_rectangle(self):

        self.t.penup()
        self.t.goto(self.pos[0],self.pos[1])
        self.t.pendown()
        self.t.color(self.color)
        self.t.begin_fill()
        for _ in range(2):
            self.t.forward(self.width)
            self.t.right(90)
            self.t.forward(self.height)
            self.t.right(90)
        self.t.end_fill()

    def add_disk(self, disk):
        self.disks_holder.append(disk)
        self.no_of_disks += 1


def set_setting(num_disks=3):
    # three towers standing points 
    towers_pos = [(-200,0),(0,0),(200,0)]
    floor_pos = (-300,-200)

    # Create towers
    floor = Tower((600,20),"Floor", floor_pos,"black")
    tower_A = Tower((20,200),"Tower_A",towers_pos[0], "black")
    tower_B = Tower((20,200),"Tower_B",towers_pos[1], "black")
    tower_C = Tower((20,200),"Tower_C",towers_pos[2], "black")

    # Draw towers
    floor.draw_rectangle()
    tower_A.draw_rectangle()
    tower_B.draw_rectangle()
    tower_C.draw_rectangle()

    # Create disks
    colors = ["orange", "purple", "cyan", "yellow", "pink"]  # Add more colors if needed
    base_width = 100
    width_decrement = 10
    height = 10

    for i in range(num_disks):
        disk_width = base_width - (i * width_decrement)
        disk_color = colors[i % len(colors)]  # Cycle through colors if more disks than colors
        disk = Disk(f"Disk_{num_disks-i}", tower_A, disk_color, (disk_width, height))
        disk.draw_disks()

    return tower_A, tower_B, tower_C

def hanoiTower(num_disks, source, auxiliary, destination):
    if num_disks == 1:
        print(f"Move disk 1 from {source.tower_type} to {destination.tower_type}")
        source.disks_holder[-1].move_disk_to(destination)
    else:
        hanoiTower(num_disks - 1, source, destination, auxiliary)
        print(f"Move disk {num_disks} from {source.tower_type} to {destination.tower_type}")
        source.disks_holder[-1].move_disk_to(destination)
        hanoiTower(num_disks - 1, auxiliary, source, destination)

# Create a function to get user input and start the game
def start_game():
    # Use turtle's textinput function to get user input
    disk_input = screen.textinput("Tower of Hanoi", "Enter the number of disks (1-8):")
    
    try:
        num_disks = int(disk_input)
        if 1 <= num_disks <= 8:
            # Clear any existing drawings
            screen.clear()
            screen.bgcolor("white")
            
            # Set up the game with user-specified number of disks
            tower_A, tower_B, tower_C = set_setting(num_disks)
            
            # Solve the puzzle
            hanoiTower(num_disks, tower_A, tower_B, tower_C)
        else:
            screen.textinput("Error", "Please enter a number between 1 and 8. Click OK to try again.")
            start_game()
    except ValueError:
        screen.textinput("Error", "Invalid input. Please enter a number. Click OK to try again.")
        start_game()

# Start the game
start_game()

# Keep the window open until clicked
screen.exitonclick()



