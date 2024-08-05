import requests
import pandas as pd
from datetime import datetime
import time

def hot_search():
    url = 'https://weibo.com/ajax/side/hotSearch'
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()['data']

def fetch_and_append_data(df):
    data = hot_search()
    if not data:
        print('获取微博热搜榜失败')
        return df

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    hot_search_list = []
    
    for rs in data['realtime'][:50]:
        title = rs['word']
        try:
            label = rs['label_name']
            if label in ['新', '爆', '沸']:
                title = title.rstrip(label)
        except:
            pass
        hot_search_list.append((timestamp, title))

    new_df = pd.DataFrame(hot_search_list, columns=['Timestamp', 'Hot Search'])
    df = pd.concat([df, new_df], ignore_index=True)
    return df

def main():
    df = pd.DataFrame(columns=['Timestamp', 'Hot Search'])

    for _ in range(24):  # Run the job 24 times, once per hour
        df = fetch_and_append_data(df)
        df.to_csv('F:/weibo_hot_searches_new2.csv', index=False)
        print(f"Data saved at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        time.sleep(3600)  # Wait for one hour

if __name__ == '__main__':
    main()
