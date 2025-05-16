import random
import math

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch

from db_structure.connect_to_circle import connect_to_circle
from db_structure.connect_to_circle2 import connect_to_circle2
from db_structure.connect_to_circle_by_arr import connect_to_circle_by_arr
from db_structure.generate_node_points import generate_node_points
from db_structure.calc_dtriangle import calc_dtriangle

# 日本語フォント（Noto Sans CJK JP）を指定
plt.rcParams['font.family'] = 'Noto Sans CJK JP'

fig, ax = plt.subplots(figsize=(8, 6))

rice_field_x = [ 0.1 + i * 0.18 for i in range(5) ]
rice_field_y = 2

for x in rice_field_x:
    rect = patches.Rectangle((x-0.075, rice_field_y), 0.15, 0.15, edgecolor='black', facecolor='lightgreen' )
    ax.add_patch(rect)
    
collection_point_x = [ -0.08 + i * 0.18 for i in range(7) ]
collection_point_y = 1.7
    
for x in collection_point_x:
    rect = patches.Rectangle((x-0.075, collection_point_y), 0.15, 0.15, edgecolor='black', facecolor='tan' )
    ax.add_patch(rect)

for i in range(5):
    for j in range(i, i+3):
        arrow = FancyArrowPatch((rice_field_x[i], rice_field_y), (collection_point_x[j], collection_point_y+0.15),
                                arrowstyle='-|>', linewidth=2, mutation_scale=20, color='green' )
        ax.add_patch(arrow)

node_points = [ (-0.24 + i * 0.18, 1.53 ) for i in range(9) ]
node_points = sorted(node_points, key=lambda p: p[0])
node_points.extend(generate_node_points((0, 0.91), (1.40, 0.5), 20, 0.15))
# print(node_points)
        
for x, y in node_points:
    circle = patches.Circle((x, y),radius=0.05, edgecolor='black',facecolor='lightblue')
    ax.add_patch(circle)
    
connect_to_circle(ax, start=(collection_point_x[0], collection_point_y), end=node_points[0], radius=0.05, color="blue", linewidth=2)
connect_to_circle(ax, start=(collection_point_x[6], collection_point_y), end=node_points[8], radius=0.05, color="blue", linewidth=2)

spend_points = [ (-0.35, 1.2), (1.37, 1.2) ]
for x, y in spend_points:
    triangle = patches.Polygon(calc_dtriangle(x, y, 0.25), closed=True, facecolor='salmon', edgecolor='black')
    ax.add_patch(triangle)    

connect_to_circle_by_arr(ax, spend_points[0], node_points[0], radius=0.05, arrow_at="start", color="blue", linewidth=2, mutation_scale=20)
connect_to_circle_by_arr(ax, spend_points[1], node_points[8], radius=0.05, arrow_at="start", color="blue", linewidth=2, mutation_scale=20)

for i in range(7):
    for _ in range(3):
        j = random.randint(0, 8)
        connect_to_circle(ax, start=(collection_point_x[i], collection_point_y), end=node_points[j], radius=0.05, color="blue", linewidth=2)

for i in range(9):
    j = random.randint(9, 13)
    connect_to_circle2(ax, node_points[i], node_points[j], radius=0.05, color="blue", linewidth=2)

for i in range(9, 24):
    for _ in range(2):
        j=random.randint(i-2, i+5)
        connect_to_circle2(ax, node_points[i], node_points[j], radius=0.05, color="blue", linewidth=2)

for i in range(24, 29):
    for _ in range(random.randint(1,2)):
        j=random.randint(i-3, 28)
        print(i, j)
        connect_to_circle2(ax, node_points[i], node_points[j], radius=0.05, color="blue", linewidth=2)

rice_polising_x = [ -0.42 + i * 0.12 for i in range(16) ]
rice_polising_y = 0.2

for x in rice_polising_x:
    rect = patches.Rectangle((x, rice_polising_y), 0.075, 0.075, edgecolor='black', linewidth=2 )
    ax.add_patch(rect)

connect_to_circle_by_arr(ax, (rice_polising_x[0]+0.0375, rice_polising_y+0.075), node_points[1], radius=0.05, arrow_at="start", 
                         color="blue", linewidth=2, mutation_scale=20)

connect_to_circle_by_arr(ax, (rice_polising_x[1]+0.0375, rice_polising_y+0.075), node_points[1], radius=0.05, arrow_at="start", 
                         color="blue", linewidth=2, mutation_scale=20)

connect_to_circle_by_arr(ax, (rice_polising_x[14]+0.0375, rice_polising_y+0.075), node_points[7], radius=0.05, arrow_at="start", 
                         color="blue", linewidth=2, mutation_scale=20)

connect_to_circle_by_arr(ax, (rice_polising_x[15]+0.0375, rice_polising_y+0.075), node_points[7], radius=0.05, arrow_at="start", 
                         color="blue", linewidth=2, mutation_scale=20)

for i in range(2, 14):
    j = random.randint(25, 28)
    connect_to_circle_by_arr(ax, (rice_polising_x[i]+0.0375, rice_polising_y+0.075), node_points[j], radius=0.05, arrow_at="start", 
                             color="blue", linewidth=2, mutation_scale=20)


node_point2_x = [ -0.30 + i * 0.24 for i in range(8) ]
node_point2_y = 0.0

for x in node_point2_x:
    circle = patches.Circle((x, node_point2_y),radius=0.05, edgecolor='black',facecolor='white', linewidth=2)
    ax.add_patch(circle)

for i in range(16):
    j = math.floor(i/2)
    connect_to_circle_by_arr(ax, (rice_polising_x[i]+0.0375, rice_polising_y), (node_point2_x[j], node_point2_y), radius=0.05, 
                             color="black", linewidth=2, mutation_scale=20)

spend_x = [ -0.30 + i * 0.24 for i in range(8) ]
spend_y = -0.2

for x in spend_x:
    triangle = patches.Polygon(calc_dtriangle(x, spend_y, 0.15), closed=True, facecolor='salmon', edgecolor='black')
    ax.add_patch(triangle)

for i in range(8):
    connect_to_circle_by_arr(ax, (spend_x[i], spend_y), (node_point2_x[i], node_point2_y), radius=0.05, arrow_at="start",
                             color="black", linewidth=2, mutation_scale=20)

rect = patches.Rectangle((1.7, 1.5), 0.15, 0.15, edgecolor='black', facecolor='lightgreen' )
ax.add_patch(rect)
ax.text(1.86, 1.54, '生産地', fontsize=12)
rect = patches.Rectangle((1.7, 1.2), 0.15, 0.15, edgecolor='black', facecolor='tan' )
ax.add_patch(rect)
ax.text(1.86, 1.24, '備蓄庫', fontsize=12)
rect = patches.Rectangle((1.75, 0.9), 0.075, 0.075, edgecolor='black', linewidth=2 )
ax.add_patch(rect)
ax.text(1.86, 0.91, '精米所', fontsize=12)
triangle = patches.Polygon(calc_dtriangle(1.75, 0.675, 0.15), closed=True, facecolor='salmon', edgecolor='black')
ax.add_patch(triangle)
ax.text(1.86, 0.6, '消費', fontsize=12)

ax.autoscale_view()    
plt.tight_layout()

# 軸非表示
ax.set_aspect('equal')
ax.axis('off')

plt.savefig("figs/db_structure.png", dpi=300)
plt.show()

