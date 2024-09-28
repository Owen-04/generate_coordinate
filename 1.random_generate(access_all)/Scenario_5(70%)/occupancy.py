import random
import csv
import os


file_2 = r"C:\Users\ongwe\Documents\ITP Job\Coding\1.random_generate(access_all)\Scenario_5(70%)\final_list.csv"  
filename = r"C:\Users\ongwe\Documents\ITP Job\Coding\1.random_generate(access_all)\Scenario_5(70%)\export.csv"  

max_bay = 56
max_aisle = 24
max_level = 10
id_list = []

def read_csv():
   
    with open(filename, mode="r") as file:
        reader = csv.reader(file)
        next(reader) 
        
        for row in reader:

            data_str = row[0].strip("()")  
            data = data_str.split(",") 
            if len(data) == 3: 
                bay_id = int(data[0].strip())
                aisle_id = int(data[1].strip())
                level_id = int(data[2].strip())
                pallet_id = int(row[1].strip())

                current = (bay_id, aisle_id, level_id, pallet_id)
                id_list.append(current)
    
    return id_list


def check_occupancy():
   
  
    occupancy_grid = [[[(0, 0) for _ in range(max_level)] for _ in range(max_aisle)] for _ in range(max_bay)]
    
    for bay_id, aisle_id, level_id, pallet_id in id_list:

        if 1 <= bay_id <= max_bay and 1 <= aisle_id <= max_aisle and 1 <= level_id <= max_level:
           
            occupancy_grid[bay_id-1][aisle_id-1][level_id-1] = (1, pallet_id)  # Mark as occupied with pallet_id
    
    return occupancy_grid


def record_all_coordinates(occupancy_grid):

    all_coordinates = []
    
    for bay_id in range(1, max_bay + 1):
        for aisle_id in range(1, max_aisle + 1):
            for level_id in range(1, max_level + 1):
                occupancy, pallet_id = occupancy_grid[bay_id-1][aisle_id-1][level_id-1]
                print(f"BayID: {bay_id}, AisleID: {aisle_id}, LevelID: {level_id}, Occupancy: {occupancy}, PalletID: {pallet_id}")
                all_coordinates.append((bay_id, aisle_id, level_id, occupancy, pallet_id))
    
    return all_coordinates


def export_all_coordinates(all_coordinates):

    with open(file_2, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["(Bay_id, Aisle_id, Level_id)", "Occupancy", "Pallet_id"])  
        
        for bay_id, aisle_id, level_id, occupancy, pallet_id in all_coordinates:
           
            writer.writerow([f"({bay_id}, {aisle_id}, {level_id})", occupancy, pallet_id])


read_csv()
occupancy_grid = check_occupancy()
all_coordinates = record_all_coordinates(occupancy_grid)  
export_all_coordinates(all_coordinates)  
