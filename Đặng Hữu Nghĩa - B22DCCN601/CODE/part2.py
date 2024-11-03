import os
import time
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#Hàm tìm kiếm top 3
def get_top_player(df):
    # #Tìm kiếm các cột kiểu số và đưa vào danh sách
    numeric_col = df.select_dtypes(include=['number'])
    numeric_columns_list = numeric_col.columns.tolist()

    def values(column:str):
        df_sorted = df.sort_values(by=column)
        a = list(df_sorted['Player'].head(3).values)
        b = list(df_sorted['Player'].tail(3).values)
        return (a + b)

    results = pd.DataFrame()
    for x in numeric_columns_list:
        results[x] = values(x)
    print(results)

#Tìm trung vị,trung bình,độ lệch chuẩn của từng chỉ số
def get_statistics(df):
    #Tìm kiếm các cột kiểu số và đưa vào danh sách
    numeric_col = df.select_dtypes(include=['number'])
    numeric_columns_list = numeric_col.columns.tolist()
    #Tìm trung vị,trung bình và độ lệch chuẩn mỗi chỉ số của toàn cầu thu
    median_all = numeric_col.median().round(2)
    mean_all = numeric_col.mean().round(2)
    std_all = numeric_col.std().round(2)
    #gôp thành 1 bảng
    overall_df = pd.DataFrame({
        'STT': [0],
        'Team': ['all'],
        **{f'Median of {col}': [median_all[col]] for col in numeric_col},
        **{f'Mean of {col}': [mean_all[col]] for col in numeric_col},
        **{f'Std of {col}': [std_all[col]] for col in numeric_col}
    })

    #Tìm trung vị , trung bình , độ lệch chuẩn của mỗi chỉ số theo đội
    median_team = df.groupby('Team')[numeric_columns_list].median().round(2)
    mean_team = df.groupby('Team')[numeric_columns_list].mean().round(2)
    std_team = df.groupby('Team')[numeric_columns_list].std().round(2)
    #Gộp các bảng này thành 1 bảng
    team_df = pd.DataFrame({
        'STT': range(1, len(median_team) + 1),
        'Team': median_team.index,
        **{f'Median of {col}': median_team[col].values for col in numeric_col},
        **{f'Mean of {col}': mean_team[col].values for col in numeric_col},
        **{f'Std of {col}': std_team[col].values for col in numeric_col}
    })

    #Gộp hai bảng thành 1 và ghi dữ liệu vào file results2.csv
    final_df = pd.concat([overall_df, team_df], ignore_index=True)
    final_df.to_csv('results2.csv', index=False)
    print(pd.read_csv("results2.csv"))

def historgram(df):
    # Thư mục lưu trữ các biểu đồ toàn giải
    output_folder_1 = "histograms_all"
    # Tạo nếu chưa tồn tại
    if not os.path.exists(output_folder_1):
        os.makedirs(output_folder_1)

    # Vẽ histogram cho toàn giải
    for col in df:
        plt.figure(figsize=(8, 6))
        sns.histplot(df[col], bins=20, kde=True, color='blue')
        plt.title(f'Histogram of {col} - Toàn Giải')
        plt.xlabel(col)
        plt.ylabel('Số lượng cầu thủ ')
        plt.grid(True, linestyle='--', alpha=0.5)
        # Lưu biểu đồ vào thư mục "histograms_all"
        plt.savefig(os.path.join(output_folder_1, f"{df.columns.get_loc(col)}.png"))
        plt.close()
    print("Đã vẽ xong biểu đồ cho toàn giải")

    # Thư mục để lưu trữ các biểu đồ các đội
    output_folder_2 = "histograms_teams"
    # Tạo nếu chưa tồn tại
    if not os.path.exists(output_folder_2):
        os.makedirs(output_folder_2)

    # Vẽ histogram cho từng đội
    teams = df['Team'].unique()
    for team in teams:
        # Tên thư mục của đội
        team_folder = os.path.join(output_folder_2, team)
        # Tạo thư mục nếu chưa tồn tại
        if not os.path.exists(team_folder):
            os.makedirs(team_folder)

        team_data = df[df['Team'] == team]
        for col in df:
            plt.figure(figsize=(8, 6))
            sns.histplot(team_data[col], bins=20, kde=True, color='green')
            plt.title(f'Histogram of {col} - {team}')
            plt.xlabel(col)
            plt.ylabel('Số lượng cầu thủ')
            plt.grid(True, linestyle='--', alpha=0.5)
            # Lưu biểu đồ vào thư mục của đội
            plt.savefig(os.path.join(team_folder, f"{df.columns.get_loc(col)}.png"))
            plt.close()
        print(f"Đã vẽ xong biểu đồ cho đội {team}")
        time.sleep(1)

    print("Đã vẽ xong biểu đồ cho toàn giải và từng đội")

def get_best_team(df):
    results=[]
    # Tìm kiếm các cột kiểu số và đưa vào danh sách
    numeric_columns = df.select_dtypes(include=['number'])
    numeric_columns_list = numeric_columns.columns.tolist()
    mean_team = df.groupby('Team')[numeric_columns_list].mean().round(2)
    for x in numeric_columns_list :
        team=mean_team[x].idxmax()
        value=mean_team[x].max()
        results.append([team,x,value])
    df_results = pd.DataFrame(results,columns=["Teams","Status","Value"])
    print(df_results)
    # Đếm tần suất của từng đội
    team_counts = Counter([row[0] for row in results])
    # Chuyển kết quả đếm tần suất thành dạng bảng và sắp xếp nó
    frequency_table = [[team, count] for team, count in team_counts.items()]
    frequency_table.sort(key=lambda x: x[1], reverse=True)
    #In ra Teams có điểm số cao nhất 
    print(frequency_table[0][0],frequency_table[0][1])

if __name__ == "__main__":
    df=pd.read_csv("results.csv")
    print("Chọn chức năng: ")
    print("1. Tìm Top 3 người có chỉ số cao nhất và thấp nhất")
    print("2. Tính trung vị, trung bình và độ lệch chuẩn của các chỉ số của toàn giải và các đội")
    print("3. Vẽ biểu đồ histogram cho toàn giải và từng đội")
    print("4. Tìm đội có giá trị cao nhất ở từng chỉ số và tần suất của từng đội")
    print("5. Thoát")
    while True:
        choice = int(input("Nhập lựa chọn: "))
        while choice < 1 or choice > 5:
            choice = int(input("Lỗi !!! Hãy nhập lại: "))
        if choice == 1:
            get_top_player(df)
        elif choice == 2:
            get_statistics(df)
        elif choice == 3:
            historgram(df)
        elif choice == 4:
            get_best_team(df)
        else:
            break
    
    
