import random
import math

def generate_node_points(x_range, y_range, num_points, min_distance):
    """重ならないランダム座標リストを作る関数"""
    x_min, x_max = x_range
    y_min, y_max = y_range
    points = []

    while len(points) < num_points:
        x = random.uniform(x_min, x_max)
        y = random.uniform(y_min, y_max)
        new_point = (x, y)

        # 既存ポイントとの距離チェック
        too_close = False
        for px, py in points:
            if math.hypot(x - px, y - py) < min_distance:
                too_close = True
                break

        if not too_close:
            points.append(new_point)

    points = sorted(points, key=lambda p: p[1], reverse=True)
    return points
