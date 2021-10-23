import raylibpy;

#Raylib.InitWindow(width, height, title);
#Raylib.SetTargetFPS(frameRate);

raylibpy.init_window(800, 600, "Test Game")
raylibpy.set_target_fps(30)


while (True):
    raylibpy.begin_drawing()
    raylibpy.clear_background(raylibpy.WHITE)

    raylibpy.draw_circle(100, 100, 30, raylibpy.BLUE)

    raylibpy.end_drawing()