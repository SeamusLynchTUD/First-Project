def setup():
    size(500, 500)

def draw():
    colorMode(HSB)
    fill(25, 150, 150)
    circle(mouseX, mouseY, mouseX-mouseY)
