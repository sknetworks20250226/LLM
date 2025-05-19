# 터미널에서 conda install datasets
from datasets import load_dataset, Dataset
from transformers import AutoTokenizer
import os
import datasets

# 파일 경로 check
file_path = 'train.json'
if not os.path.exists(file_path):
    print('train.json 파일 이 없습니다.')    

# json 데이터 로드
try:
    dataset = load_dataset('json', data_files=file_path,  cache_dir=None)
    print('데이터 로드 성공')
except Exception as e:
    print(f"에러 : {e}")
    raise

# 데이터 플랫화
def flatten_data(dataset):
    temp_datasets = []
    for items in dataset['train']:        
        for item in items['data']:
            for pragraph in item['paragraphs']:
                context = pragraph.get('context','')
                for qa in pragraph['qas']:
                    temp_datasets.append({
                        'question':qa['question'],
                        'context' : context,
                        'answer' : qa['answers'][0]['text']
                    })
    return temp_datasets

def main():
    if __name__ =='__main__':
        print(flatten_data(dataset))

main()