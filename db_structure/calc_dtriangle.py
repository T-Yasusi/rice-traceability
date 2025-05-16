import numpy as np

def calc_dtriangle(x, y, size):
    """下向き正三角形の3頂点を返す（中心座標と一辺の長さから）"""
    h = np.sqrt(3) / 2 * size  # 正三角形の高さ
    return [
        [x - size / 2, y ],
        [x + size / 2, y ],
        [x,           y - h ]
    ]
