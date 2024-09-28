import random
import csv
import os

filename = r"C:\Users\ongwe\Documents\ITP Job\Coding\3.generate_start_from_front\Scenario_18(80%)\export.csv"
generated_list = []
max_bay = 56
max_aisle = 24
max_level = 10


def generate():
    total = int((max_level * max_aisle * max_bay) * 0.8)

    for bay_id in range(1,max_bay+1):
        if len(generated_list) == total :
            break
        for level_id in range(1,max_level+1):
            if len(generated_list) == total :
                break
            for aisle_id in range(1,max_aisle+1):
                id_tuple = (bay_id, aisle_id, level_id)
                if id_tuple not in generated_list:
                    generated_list.append(id_tuple)
                if len(generated_list) == total :
                    break

def find_outer():
    outer_list = []
    # if 8 , 1,4,5,8
    for coord in generated_list:
        bay_id, aisle_id, level_id = coord
        group_start = ((aisle_id - 1) // 4) * 4 + 1  
        group_end = group_start + 3
    
        if aisle_id == group_start or aisle_id == group_end:
            outer_list.append(coord)
    return outer_list

def find_inner():
    inner_list = []
    #if 8 , 2,3,6,7
    for coord in generated_list:
        bay_id, aisle_id, level_id = coord
        group_start = ((aisle_id - 1) // 4) * 4 + 1  
        group_end = group_start + 3 
        

        if group_start < aisle_id < group_end:
            inner_list.append(coord)
    return inner_list

def move_outer_to_inner():
    inner_list = find_inner()
    move_list = []
    outer_list = find_outer()
    for bay_id, aisle_id, level_id in inner_list:
        group_start = ((aisle_id - 1) // 4) * 4 + 1  
        group_end = group_start + 3

        if aisle_id == group_start + 1: 
            outer_coordinate = (bay_id, aisle_id - 1, level_id)  
        elif aisle_id == group_end - 1:  
            outer_coordinate = (bay_id, aisle_id + 1, level_id) 
        else:
            continue

        if outer_coordinate not in outer_list:
            move_list.append((outer_coordinate, (bay_id, aisle_id, level_id)))

    for new_coord, old_coord in move_list:
        generated_list.remove(old_coord)
        generated_list.append(new_coord)
        #print(f"Moved outer to inner: BayID: {old_coord[0]}, AisleID: {old_coord[1]}, LevelID: {old_coord[2]} -->  BayID: {new_coord[0]}, AisleID: {new_coord[1]}, LevelID: {new_coord[2]}")

def display_inner_outer():
    outer_list = find_outer()
    inner_list = find_inner()
    
    print("\nOuter Aisles:")
    for i, coord in enumerate(outer_list, 1):
        print(f"{i}. BayID: {coord[0]}, AisleID: {coord[1]}, LevelID: {coord[2]}")
    
    print("\nInner Aisles:")
    for i, coord in enumerate(inner_list, 1):
        print(f"{i}. BayID: {coord[0]}, AisleID: {coord[1]}, LevelID: {coord[2]}")

def export_to_csv():
    if os.path.exists(filename) and os.path.isfile(filename): 
        os.remove(filename)
        
    with open(filename, mode="w", newline="") as file:
        pallet_id = 0
        writer = csv.writer(file)
        writer.writerow(["( Bay_id , aisle_id , level_id )","Pallet_id"]) 
        for pallet_id,coord in enumerate(generated_list,1):
            writer.writerow([f"({coord[0]},{coord[1]},{coord[2]})",pallet_id])  

def display_list():
    count=0
    for i,coord in enumerate(generated_list,1):
         print(f"{i}. BayID: {coord[0]}, LevelID: {coord[2]} ,AisleID: {coord[1]}")
         count=i
    total=(count/(max_bay*max_level*max_aisle)) * 100
    print("Percent : ",int(total))

generate()
#display_inner_outer()
#move_outer_to_inner()
display_list()
export_to_csv()