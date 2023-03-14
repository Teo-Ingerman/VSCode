from PIL import Image
import pyautogui, time

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
        hex_color = '#{:02x}{:02x}{:02x}'.format(*color)
        
        if hex_color in ["1976D2"]:
            name = "one"
            
        elif hex_color in ["C9B491", "D6BD96", "D6B898", "E4C29E"]:
            name = "two"
        
        elif hex_color in []:
            name = "three"
        
        elif hex_color in []:
            name = "four"
        
        elif hex_color in []:
            name = "five"
        
        elif hex_color in []:
            name = "six"
            
        elif hex_color in []:
            name = "seven"
        
        elif hex_color in []:
            name = "eight"
        
        elif hex_color in []:
            name = "flag"
        
        elif hex_color in []:
            name = "empty"
        
        elif hex_color in []:
            name = "unknown"
        
        else:
            print("something went wrong!")
            quit()
        
        pixel_colors[pos] = name
    
    # Return the dictionary of pixel colors
    return pixel_colors



