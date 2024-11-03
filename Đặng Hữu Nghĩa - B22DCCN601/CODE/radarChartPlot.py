import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import argparse

def load_data(file_path):
    return pd.read_csv(file_path)

def radar_chart(data, player1, player2, attributes):
    # Lọc dữ liệu cho từng cầu thủ
    p1_data = data[data['Player'] == player1]
    p2_data = data[data['Player'] == player2]
    # Kiểm tra nếu không tìm thấy cầu thủ
    if p1_data.empty or p2_data.empty:
        print("Không tìm thấy cầu thủ.")
        return

    # Lấy giá trị các thuộc tính
    p1_values = p1_data[attributes].values.flatten()
    p2_values = p2_data[attributes].values.flatten()

    # Xây dựng góc của biểu đồ radar
    num_vars = len(attributes)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    # Hoàn thành vòng radar
    p1_values = np.concatenate((p1_values, [p1_values[0]]))
    p2_values = np.concatenate((p2_values, [p2_values[0]]))
    angles += angles[:1]

    # Vẽ biểu đồ
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, p1_values, color='blue', alpha=0.25)
    ax.fill(angles, p2_values, color='red', alpha=0.25)
    ax.plot(angles, p1_values, color='blue', linewidth=2, label=player1)
    ax.plot(angles, p2_values, color='red', linewidth=2, label=player2)

    # Cấu hình các nhãn thuộc tính
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(attributes)
    plt.title(f"So sánh chỉ số giữa {player1} và {player2}")
    plt.legend(loc='upper right')
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Vẽ biểu đồ radar so sánh cầu thủ")
    parser.add_argument("--p1", type=str, required=True, help="Tên cầu thủ thứ nhất")
    parser.add_argument("--p2", type=str, required=True, help="Tên cầu thủ thứ hai")
    parser.add_argument("--Attribute", type=str, required=True, help="Danh sách các chỉ số cần so sánh, cách nhau bởi dấu phẩy")
    args = parser.parse_args()
    attributes = [attr.strip() for attr in args.Attribute.split(",")]
    # Đọc dữ liệu và vẽ biểu đồ
    data = load_data("results.csv")
    radar_chart(data, args.p1, args.p2, attributes)
