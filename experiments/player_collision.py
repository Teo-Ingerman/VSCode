def player_movement(player_position, player_surface, level_objects, x_change=0, y_change=0, screensize=(1080,1920)):
    x, y = player_position
    
    if level_objects != 0:
        
        for entities in level_objects:
            
            size = entities.size
            pos = entities.position
        
            
            player_size = player_surface.get_size()
            
            right_edge = x + player_size[0]
            down_edge = y + player_size[1]
            
            #*left
            if x <= pos[0] + size[0] + 2 and x_change == -1:
                
                if x >= pos[0] + size[0] - 2:
                    
                    if y <= pos[1] + size[1] + 2:
                        
                        if down_edge >= pos[1] - 2:
                            x_change = 0
                        
                        
            #*right
            if right_edge >= pos[0] - 2 and x_change == 1:
                
                if right_edge <= pos[0] + 2:
                
                    if y <= pos[1] + size[1] + 2:
                        
                        if down_edge >= pos[1] - 2:
                            x_change = 0
                        
                        
            #*up    
            if y <= pos[1] + size[1] + 2 and y_change == -1:
                
                if y >= pos[1] + size[1] - 2:
                    
                    if x <= pos[0] + size[0] + 2:
                        
                        if right_edge >= pos[0] - 2:
                            y_change = 0
                        
                        
            #*down
            if down_edge >= pos[1] - 2 and y_change == 1:
                
                if down_edge <= pos[1] + 2:
                
                    if x <= pos[0] + size[0] + 2:
                        
                        if right_edge >= pos[0] - 2:
                            y_change = 0
                        
    
    size = player_surface.get_size()
    
    right_edge = x + size[0]
    down_edge = y + size[1]
    
    size = player_surface.get_size()
    
    if x <= 2 and x_change == -1:
        x_change = 0
        
    if right_edge >= screensize[0] - 2 and x_change == 1:
        x_change = 0
        
    if y <= 2 and y_change == -1:
        y_change = 0
        
    if down_edge >= screensize[1] - 2 and y_change == 1:
        y_change = 0
    
    
    x += 2*x_change
    y += 2*y_change
    player_position = (x, y)
    return player_position