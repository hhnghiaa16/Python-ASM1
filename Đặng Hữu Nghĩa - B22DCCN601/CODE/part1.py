from functools import reduce
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = 'https://fbref.com/en/comps/9/2023-2024/2023-2024-Premier-League-Stats'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    table = soup.find('table', {
        'class': 'stats_table sortable min_width force_mobilize',
        'id': 'results2023-202491_overall'
    })

    # Danh sách chứa các đội bóng kèm url
    teams_data = []
    # Tìm các thẻ <a> trong <tbody> của table
    tbody = table.find('tbody')
    teams = tbody.find_all('a', href=True)

    # Lấy dữ liệu về tên và link đội bóng, đưa vào danh sách
    for team in teams:
        if "squads" in team['href']:
            team_name = team.text.strip()
            team_url = "https://fbref.com" + team['href']
            teams_data.append([team_name, team_url])
    #df = pd.DataFrame(teams_data[1:], columns=teams_data[0])
    #df.to_csv('team_data.csv', index=False, encoding='utf-8-sig')

    ok = 1  # Check header
    # Tạo danh sách chữa dữ liệu
    base_data = []
    goalkeep_data = []
    shooting_data = []
    passing_data = []
    passtype_data = []
    goalshot_data = []
    defensive_data = []
    possess_data = []
    playtime_data = []
    miscell_data = []

    # Xử lí dữ liệu cho từng mục
    for team in teams_data:
        print(f"dang xu li du lieu doi {team[0]}..")
        r = requests.get(team[1])
        soup = BeautifulSoup(r.content, 'html.parser')

        # Tìm bảng chứa dữ liệu base_data
        table = soup.find('table', {
            'class': 'stats_table sortable min_width',
            'id': 'stats_standard_9'
        })
        # Tìm tên các cột
        if ok == 1:
            b = []
            b.append("Team")
            thead = table.find('thead').find_all('tr')
            for x in thead[1]:
                if x.text.strip() != "":
                    b.append(x.text.strip())
            base_data.append(b)
        # TÌm các dữ liệu còn lại của bảng
        tbody = table.find('tbody').find_all('tr')
        for y in tbody:
            tmp = []
            tmp.append(team[0])
            for x in y:
                if (x.text.strip() == ""):
                    tmp.append("N/a")
                else:
                    tmp.append(x.text.strip())
            base_data.append(tmp)
        # kết thúc base_data

        # Bắt đầu tìm goalkeep_data
        table = soup.find('table', {
            'class': 'stats_table sortable min_width',
            'id': 'stats_keeper_9'
        })
        if ok == 1:
            b = []
            thead = table.find('thead').find_all('tr')
            for x in thead[1]:
                if x.text.strip() != "":
                    b.append(x.text.strip())
            goalkeep_data.append(b)
        tbody = table.find('tbody').find_all('tr')
        for y in tbody:
            tmp = []
            for x in y:
                if (x.text.strip() == ""):
                    tmp.append("N/a")
                else:
                    tmp.append(x.text.strip())
            goalkeep_data.append(tmp)
        # kết thúc goalkeep_data

        # Bắt đầu tìm shooting_data
        table = soup.find('table', {
            'class': 'stats_table sortable min_width',
            'id': 'stats_shooting_9'
        })
        if ok == 1:
            b = []
            thead = table.find('thead').find_all('tr')
            for x in thead[1]:
                if x.text.strip() != "":
                    b.append(x.text.strip())
            shooting_data.append(b)
        tbody = table.find('tbody').find_all('tr')
        for y in tbody:
            tmp = []
            for x in y:
                if (x.text.strip() == ""):
                    tmp.append("N/a")
                else:
                    tmp.append(x.text.strip())
            shooting_data.append(tmp)
        # kết thúc shooting_data

        # Bắt đầu tìm passing_data
        table = soup.find('table', {
            'class': 'stats_table sortable min_width',
            'id': 'stats_passing_9'
        })
        if ok == 1:
            b = []
            thead = table.find('thead').find_all('tr')
            for x in thead[1]:
                if x.text.strip() != "":
                    b.append(x.text.strip())
            passing_data.append(b)
        tbody = table.find('tbody').find_all('tr')
        for y in tbody:
            tmp = []
            for x in y:
                if (x.text.strip() == ""):
                    tmp.append("N/a")
                else:
                    tmp.append(x.text.strip())
            passing_data.append(tmp)
        # kết thúc passing_data

        # Bắt đầu tìm passtype_data
        table = soup.find('table', {
            'class': 'stats_table sortable min_width',
            'id': 'stats_passing_types_9'
        })
        if ok == 1:
            b = []
            thead = table.find('thead').find_all('tr')
            for x in thead[1]:
                if x.text.strip() != "":
                    b.append(x.text.strip())
            passtype_data.append(b)
        tbody = table.find('tbody').find_all('tr')
        for y in tbody:
            tmp = []
            for x in y:
                if (x.text.strip() == ""):
                    tmp.append("N/a")
                else:
                    tmp.append(x.text.strip())
            passtype_data.append(tmp)
        # kết thúc passtype_data

        # Bắt đầu tìm goalshot_data
        table = soup.find('table', {
            'class': 'stats_table sortable min_width',
            'id': 'stats_gca_9'
        })
        if ok == 1:
            b = []
            thead = table.find('thead').find_all('tr')
            for x in thead[1]:
                if x.text.strip() != "":
                    b.append(x.text.strip())
            goalshot_data.append(b)
        tbody = table.find('tbody').find_all('tr')
        for y in tbody:
            tmp = []
            for x in y:
                if (x.text.strip() == ""):
                    tmp.append("N/a")
                else:
                    tmp.append(x.text.strip())
            goalshot_data.append(tmp)
        # kết thúc goalshot_data

        # Bắt đầu tìm defensive_data
        table = soup.find('table', {
            'class': 'stats_table sortable min_width',
            'id': 'stats_defense_9'
        })
        if ok == 1:
            b = []
            thead = table.find('thead').find_all('tr')
            for x in thead[1]:
                if x.text.strip() != "":
                    b.append(x.text.strip())
            defensive_data.append(b)
        tbody = table.find('tbody').find_all('tr')
        for y in tbody:
            tmp = []
            for x in y:
                if (x.text.strip() == ""):
                    tmp.append("N/a")
                else:
                    tmp.append(x.text.strip())
            defensive_data.append(tmp)
        # kết thúc defensive_data

        # Bắt đầu tìm possess_data
        table = soup.find('table', {
            'class': 'stats_table sortable min_width',
            'id': 'stats_possession_9'
        })
        if ok == 1:
            b = []
            thead = table.find('thead').find_all('tr')
            for x in thead[1]:
                if x.text.strip() != "":
                    b.append(x.text.strip())
            possess_data.append(b)
        tbody = table.find('tbody').find_all('tr')
        for y in tbody:
            tmp = []
            for x in y:
                if (x.text.strip() == ""):
                    tmp.append("N/a")
                else:
                    tmp.append(x.text.strip())
            possess_data.append(tmp)
        # kết thúc possess_data

        # Bắt đầu tìm playtime_data
        table = soup.find('table', {
            'class': 'stats_table sortable min_width',
            'id': 'stats_playing_time_9'
        })
        if ok == 1:
            b = []
            thead = table.find('thead').find_all('tr')
            for x in thead[1]:
                if x.text.strip() != "":
                    b.append(x.text.strip())
            playtime_data.append(b)
        tbody = table.find('tbody').find_all('tr')
        for y in tbody:
            tmp = []
            for x in y:
                if (x.text.strip() == ""):
                    tmp.append("N/a")
                else:
                    tmp.append(x.text.strip())
            playtime_data.append(tmp)
        # kết thúc playtime_data

        # Bắt đầu tìm miscell_data
        table = soup.find('table', {
            'class': 'stats_table sortable min_width',
            'id': 'stats_misc_9'
        })
        if ok == 1:
            b = []
            thead = table.find('thead').find_all('tr')
            for x in thead[1]:
                if x.text.strip() != "":
                    b.append(x.text.strip())
            miscell_data.append(b)
        tbody = table.find('tbody').find_all('tr')
        for y in tbody:
            tmp = []
            for x in y:
                if (x.text.strip() == ""):
                    tmp.append("N/a")
                else:
                    tmp.append(x.text.strip())
            miscell_data.append(tmp)
        # kết thúc miscell_data
        print(f'da xu li xong doi {team[0]}...')
        ok += 1
        time.sleep(2)

    # Tạo 1 list chứa tất cả các df
    all_df = []
    # Chuyển đổi list thành Dataframe và loại bộ những hàng không cần thiết
    base_data_df = pd.DataFrame(base_data[1:], columns=base_data[0])
    base_data_df = base_data_df.drop(['90s', 'Gls', 'G+A', 'PK', 'npxG+xAG', 'Matches'], axis=1)
    all_df.append(base_data_df.drop_duplicates(subset='Player'))

    goalkeep_data_df = pd.DataFrame(goalkeep_data[1:], columns=goalkeep_data[0])
    goalkeep_data_df = goalkeep_data_df.drop(['Nation', 'Pos', 'Age', 'MP', 'Starts', 'Min', '90s', 'Matches'], axis=1)
    all_df.append(goalkeep_data_df.drop_duplicates(subset='Player'))

    shooting_data_df = pd.DataFrame(shooting_data[1:], columns=shooting_data[0])
    shooting_data_df = shooting_data_df.drop(['Nation', 'Pos', 'Age', '90s', 'Matches'], axis=1)
    all_df.append(shooting_data_df.drop_duplicates(subset='Player'))

    passing_data_df = pd.DataFrame(passing_data[1:], columns=passing_data[0])
    passing_data_df = passing_data_df.drop(['Nation', 'Pos', 'Age', '90s', 'Matches'], axis=1)
    all_df.append(passing_data_df.drop_duplicates(subset='Player'))

    passtype_data_df = pd.DataFrame(passtype_data[1:], columns=passtype_data[0])
    passtype_data_df = passtype_data_df.drop(['Nation', 'Pos', 'Age', '90s', 'Att', 'Matches'], axis=1)
    all_df.append(passtype_data_df.drop_duplicates(subset='Player'))

    goalshot_data_df = pd.DataFrame(goalshot_data[1:], columns=goalshot_data[0])
    goalshot_data_df = goalshot_data_df.drop(['Nation', 'Pos', 'Age', '90s', 'Matches'], axis=1)
    all_df.append(goalshot_data_df.drop_duplicates(subset='Player'))

    defensive_data_df = pd.DataFrame(defensive_data[1:], columns=defensive_data[0])
    defensive_data_df = defensive_data_df.drop(['Nation', 'Pos', 'Age', '90s', 'Matches'], axis=1)
    all_df.append(defensive_data_df.drop_duplicates(subset='Player'))

    possess_data_df = pd.DataFrame(possess_data[1:], columns=possess_data[0])
    possess_data_df = possess_data_df.drop(['Nation', 'Pos', 'Age', '90s', 'Matches'], axis=1)
    all_df.append(possess_data_df.drop_duplicates(subset='Player'))

    playtime_data_df = pd.DataFrame(playtime_data[1:], columns=playtime_data[0])
    playtime_data_df = playtime_data_df.drop(
        ['Nation', 'Pos', 'Age', '90s', 'Matches', 'MP', 'Min', 'Mn/MP', 'Min%', '+/-', '+/-90', 'On-Off', 'xG+/-',
         'xG+/-90', 'On-Off'], axis=1)
    all_df.append(playtime_data_df.drop_duplicates(subset='Player'))

    miscell_data_df = pd.DataFrame(miscell_data[1:], columns=miscell_data[0])
    miscell_data_df = miscell_data_df.drop(
        ['Nation', 'Pos', 'Age', '90s', 'Matches', 'CrdY', 'CrdR', '2CrdY', 'Int', 'TklW', 'PKwon', 'PKcon'], axis=1)
    all_df.append(miscell_data_df.drop_duplicates(subset='Player'))

    # Outer join hết tất cả các df trong list all_df
    result = reduce(lambda left, right: pd.merge(left, right, on=['Player'], how='outer'), all_df)
    result = result.drop_duplicates()
    result = result.groupby('Player').first().reset_index()
    result = result.T.drop_duplicates().T


    # Loc theo điều kiện
    def check(a: str):
        if a == 'N/a':
            return 0
        return int(a.replace(',', ''))


    a = result['Min'].to_list()
    b = [x for x in a if check(x) > 90]
    result = result[result['Min'].isin(b)].reset_index(drop=True)
    print(result)
    # Đưa thông tin vào file csv
    result.to_csv("results.csv",index=False)