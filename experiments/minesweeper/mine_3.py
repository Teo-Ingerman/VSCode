from PIL import Image
import pyautogui, time
import pynput





def get_total_grid(start_square):
    #skapar en grid för alla fyrkanter som går att klicka på
    all_positions = []
    x, y = start_square
    for height in range(20):
        
        x = start_square[0]
        if height > 0:
            #pixellängd av en fyrkant
            y += 25
        for width in range(24):
            if width > 0:
                x += 25
            all_positions.append((x,y))
    
    return all_positions

def get_pixel_colors(positions):
    
    color_map = {
    "1976D2": 1,
    "C9B491": 2,
    "D6BD96": 2,
    "D6B898": 2,
    "E4C29E": 2,
    "D75149": 3,
    "D44F47": 3,
    "D32F2F": 3,
    "D3A7A0": 4,
    "C89F9B": 4,
    "E3BFA0": 4,
    "D6B59A": 4,
    "FF8F00": 5,
    "119AA7": 6,
    "0097A7": 6,
    "E74E12": "flag",
    "E64D11": "flag",
    "E5C29F": "empty",
    "D7B899": "empty",
    "AAD751": "unknown",
    "A2D149": "unknown"
    }
    
    # Take a screenshot of the current screen
    screenshot = pyautogui.screenshot()
    
    # Convert the screenshot to an image object
    img = Image.frombytes('RGB', screenshot.size, screenshot.tobytes())
    
    # Create an empty dictionary to store the pixel colors
    pixel_colors = {}
    
    # Loop through each pixel position and get the color value
    for pos in positions:
        # Get the color value at the current position
        color = img.getpixel(pos)
        
        # Convert the color value to a hex string and add it to the dictionary
        hex_color = '{:02x}{:02x}{:02x}'.format(*color).upper()
        
        try:
            name = color_map[hex_color]
        except:
            print(f"unknown color: {hex_color}, position: {pos}")
            
            quit()
        
        
        if color_map[hex_color] in ["flag", "empty", "unknown"]:
            pixel_colors[pos] = name
        else:
            pixel_colors[pos] = name
    
    # Return the dictionary of pixel colors
    return pixel_colors

def check_surrounding_pixels(position, all_squares):
    if all_squares[position] in [1, 2, 3, 4, 5, 6, 7, 8]:
        x, y = position
        
        square_value = all_squares[position]
        flags = 0
        
        spacing = 25
        
        surrounding_pixels = [
            (x-spacing, y-spacing), # top left
            (x, y-spacing), # top
            (x+spacing, y-spacing), # top right
            (x-spacing, y), # left
            (x+spacing, y), # right
            (x-spacing, y+spacing), # bottom left
            (x, y+spacing), # bottom
            (x+spacing, y+spacing) # bottom right
        ]
        
        surrounding_colors = [
            all_squares[(x-spacing, y-spacing)], # top left
            all_squares[(x, y-spacing)], # top
            all_squares[(x+spacing, y-spacing)], # top right
            all_squares[(x-spacing, y)], # left
            all_squares[(x+spacing, y)], # right
            all_squares[(x-spacing, y+spacing)], # bottom left
            all_squares[(x, y+spacing)], # bottom
            all_squares[(x+spacing, y+spacing)] # bottom right
        ]
        
        
        unknown_list = []
        flag_list = []
        
        for i, color in enumerate(surrounding_colors):
            
            if color == "unknown":
                unknown_list.append(surrounding_pixels[i])
            
            elif color == "flag":
                flag_list.append(surrounding_pixels[i])
        
        if len(flag_list) == square_value and len(unknown_list) != 0:
            pyautogui.moveTo(position)
            mouse = pynput.mouse.Controller()

            # Click both left and right mouse buttons simultaneously
            mouse.press(pynput.mouse.Button.left)
            mouse.press(pynput.mouse.Button.right)
            mouse.release(pynput.mouse.Button.left)
            mouse.release(pynput.mouse.Button.right)

    

yes = {
    "no": 1,
    "yes":2
    
}

for x in yes:
    print(x)
    print(yes[x])


""" time.sleep(2)

positions = get_total_grid((672, 347))

print(get_pixel_colors(positions))
 """
 
while True:
    grid = get_total_grid((672, 347))
    
    color_grid = get_pixel_colors(grid)
    for pos in color_grid:
        check_surrounding_pixels(pos, color_grid)