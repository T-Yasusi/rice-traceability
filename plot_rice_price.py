import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 日本語フォント（Noto Sans CJK JP）を指定
plt.rcParams['font.family'] = 'Noto Sans CJK JP'
# タイトルサイズ設定
plt.rcParams.update({
    'font.size': 20,  # 基本のフォントサイズ
    'axes.titlesize': 20,
    'axes.labelsize': 18,
    'xtick.labelsize': 15,
    'ytick.labelsize': 15
})

# CSVファイルのパス
csv_path = "data/rice_price.csv"

# CSVの読み込み
df = pd.read_csv(csv_path)

# 日付として扱う
df["年月"] = pd.to_datetime(df["年月"], format="%Y-%m")

# 店頭価格をkgあたりに換算（5kgパック前提）
df["店頭価格(円/kg)"] = df["店頭価格(円/5kg)"] / 5

# プロット
plt.figure(figsize=(10, 6))
plt.plot(df["年月"], df["玄米価格(円/kg)"], label="玄米価格 (相対取引)", marker="o")
plt.plot(df["年月"], df["店頭価格(円/kg)"], label="店頭価格", marker="s")

# 注釈: 最近の店頭価格急騰を強調
# latest = df.iloc[-1]
# plt.annotate(
#     f"{latest['店頭価格(円/kg)']:.0f}円/kg",
#     xy=(latest["年月"], latest["店頭価格(円/kg)"]),
#     xytext=(-60, -30),
#     textcoords='offset points',
#     arrowprops=dict(arrowstyle="->", color="gray"),
#     fontsize=10,
#     bbox=dict(boxstyle="round,pad=0.3", edgecolor="gray", facecolor="#f9f9f9")
# )

# グラフの設定
plt.title("店頭価格と玄米価格の推移")
plt.xlabel("年月")
plt.ylabel("価格（円/kg）")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.xticks(rotation=45)

# 保存（任意）
plt.savefig("figs/rice_prices.png", dpi=300)

plt.show()
