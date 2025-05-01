import math
from matplotlib.patches import FancyArrowPatch

def connect_to_circle_by_arr(ax, start, end, radius, arrow_at="end", **kwargs):
    x1, y1 = start
    x2, y2 = end

    dx = x2 - x1
    dy = y2 - y1
    distance = math.hypot(dx, dy)

    if distance == 0:
        return  # 始点と終点が同じなら描画しない

    ux = dx / distance
    uy = dy / distance

    if arrow_at == "end":
        start_adj = (x1, y1)
        end_adj = (x2 - ux * radius, y2 - uy * radius)
    elif arrow_at == "start":
        start_adj = (x1, y1)
        end_adj = (x2 - ux * radius, y2 - uy * radius)
        # 向きを逆転
        start_adj, end_adj = end_adj, start_adj
    else:
        raise ValueError("arrow_at must be 'start' or 'end'")

    arrow = FancyArrowPatch(
        start_adj,
        end_adj,
        arrowstyle='-|>',
        **kwargs
    )
    ax.add_patch(arrow)
