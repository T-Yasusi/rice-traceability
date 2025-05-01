import math

def connect_to_circle(ax, start, end, radius, **kwargs):
    """
    円のふちに接続する線を描く関数
    """
    start_x, start_y = start
    end_x, end_y = end

    dx = end_x - start_x
    dy = end_y - start_y
    length = math.hypot(dx, dy)

    if length == 0:
        adjusted_x, adjusted_y = end_x, end_y
    else:
        adjusted_x = end_x - radius * dx / length
        adjusted_y = end_y - radius * dy / length

    ax.plot([start_x, adjusted_x], [start_y, adjusted_y], **kwargs)



