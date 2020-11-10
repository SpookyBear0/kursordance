if __name__ == "__main__":
    exit()
import pyglet
from osu import beatmap, objects

resource = pyglet.resource
image = resource.image
sound = pyglet.media
shapes = pyglet.shapes
sprites = pyglet.sprite
sprite = sprites.Sprite
window = pyglet.window.Window(fullscreen=False, caption="Kursordance", width=1600, height=900)
circles = []
sliders = []
spinners = []

boundaries = sprite(image("assets/boundaries.png"))
boundaries.update(scale=1.175)

def to_scale(cs):
    CSratio = [0.75, 2]
    return CSratio[0]/(cs/CSratio[1])

def draw_circle(x=0, y=0, number=1):
    cs = map.CS
    scale = to_scale(cs)
    x, y = x * 2 + window.width/6.5, y * 2.1
    circle = [image("assets/hitcircle.png"),
              image("assets/hitcircle-full.png"), 
              image("assets/hitcircleoverlay.png")]
    i = 0
    for c in circle:
        c = sprite(c, x=x, y=y)
        c.update(scale_y=scale, scale_x=scale)
        if not i == 2:
            c.color = (255, 100, 100)
        c.draw()
        i += 1
    
    # number renderer
    width, height = sprite(circle[0]).width/2, sprite(circle[0]).height/2
    if number < 10:
        num = sprite(image(f"assets/numbers/default-{number}.png"),
                     x=x+scale*width/1.5,
                     y=y+scale*height/2)
    else:
        if number > 99:
            number = 99
        number = str(number)
        num = sprite(image(f"assets/numbers/default-{number[0]}.png"),
                     x=x+scale*width/2.15,
                     y=y+scale*height/2)
        num1 = sprite(image(f"assets/numbers/default-{number[1]}.png"),
                      x=x+scale*width/1.15,
                      y=y+scale*height/2)
        num1.update(scale_y=scale*2, scale_x=scale*2)
        num1.draw()
    num.update(scale_y=scale*2, scale_x=scale*2)
    num.draw()
    circles.append(circle)
    
        
def draw_spinner(time):
    circle = sprite(image("assets/spinner-circle.png"), x=window.width/4, y=window.height/14)
    acircle = sprite(image("assets/spinner-approachcircle.png"), x=window.width/4, y=window.height/14)
    circle.update(scale_y=0.6, scale_x=0.6)
    acircle.update(scale_y=2, scale_x=2)
    circle.draw()
    acircle.draw()
    spinners.append([circle, acircle])
    
def draw_slider(x, y, scorepoints, number=1):
    # draw hitcircle
    draw_circle(x, y, number)
    # draw slider...

@window.event
def on_draw():
    window.clear()
    window.set_caption(map.artist + " - " + map.title + " [" + map.diffName + "]")
    boundaries.draw()
    combo = 1
    for o in map.hitObjects:
        if combo == 100:
            combo = 1
        if isinstance(o, objects.Circle):
            draw_circle(o.x, o.y, combo)
        elif isinstance(o, objects.Slider):
            draw_slider(o.x, o.y, combo)
        elif isinstance(o, objects.Spinner):
            draw_spinner(o.time - o.endTime)
        combo += 1
    draw_cursor()

def draw_cursor():
    cursorparts = [image("assets/cursor.png"),
                   image("assets/cursor-top.png")]
    for c in cursorparts:
        c = sprite(c)
        c.update(scale_x=0.5, scale_y=0.5)
        c.color = (255, 100, 100) 
        c.draw()

def init(bmap: str, difficulty: str, mirror: bool, download: bool):
    """
    Args:
    map: search query for map
    difficulty: search query for difficulty
    mirror: mirror mode
    download: if kursordance should download the map
    """
    global map
    map = beatmap.Beatmap("D:\\games\\osu!\\Songs\\Tokyo_machine_-_Bubbles\\Tokyo machine - Bubbles (UslessLmao) [spookybear0's difficult].osu")
    #audio = sound.load("D:\\games\\osu!\\Songs\\Tokyo_machine_-_Bubbles\\audio.mp3")
    #audio.play()
    pyglet.app.run()
    