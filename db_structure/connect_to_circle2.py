import math

def connect_to_circle2(ax, start, end, radius, **kwargs):
    x1, y1 = start
    x2, y2 = end

    dx = x2 - x1
    dy = y2 - y1
    distance = math.hypot(dx, dy)

    if distance == 0:
        return  # 始点と終点が同じなら描画しない

    # 単位ベクトル
    ux = dx / distance
    uy = dy / distance

    # 両端の円の外周に接する位置を計算
    start_adjusted = (x1 + ux * radius, y1 + uy * radius)
    end_adjusted = (x2 - ux * radius, y2 - uy * radius)

    ax.plot(
        [start_adjusted[0], end_adjusted[0]],
        [start_adjusted[1], end_adjusted[1]],
        **kwargs
    )
