import os

def handle_command(command):
    if command == "move_mouse_up":
        os.system("xdotool mousemove_relative 0 -10")
        print("Move up")
        return {'message': 'Command executed successfully'}
    elif command == "move_mouse_down":
        os.system("xdotool mousemove_relative 0 10")
        print('Move down')
        return {'message': 'Command executed successfully'}
    elif command == "move_mouse_left":
        os.system("xdotool mousemove_relative -10 0")
        print("Move left")
        return {'message': 'Command executed successfully'}
    elif command == "move_mouse_right":
        os.system("xdotool mousemove_relative 10 0")
        print("Move right")
        return {'message': 'Command executed successfully'}
    elif command == "left_click":
        os.system("xdotool click 1")
        print("Left click")
        return {'message': 'Command executed successfully'}
    elif command == "right_click":
        os.system("xdotool click 3")
        print("Right click")
        return {'message': 'Command executed successfully'}
    else:
        print(f"Unknown command: {command}")
        return {'error': 'Unknown command'}
