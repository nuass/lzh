# coding=utf-8
import collections
import os
import sys
import numpy as np

start_token = "G"
end_token="E"

def process_poems(file_name):
    #诗集
    poems=[]
    with open(file_name,'r',encoding='utf-8') as f:
        for line in f.readlines():
            try:
                title,content=line.strip().split(':')
                content = content.replace(' ','')
                if '_' in content or "(" in content or "{" in content or "{" in content \
                    or "<<" in content or "[" in content or start_token in content or\
                    end_token in content:
                    continue
                if len(content) <5 or len(content) >79:
                    continue
                content=start_token+content+end_token
                poems.append(content)
            except ValueError as e:

                pass
    #按诗的字数排序
    print(poems)
    poems = sorted(poems,key = lambda line:len(line))
    all_words = []
    for poem in poems:
        all_words+=poem
    counter = collections.Counter(all_words)
    count_pairs = sorted(counter.items(),key=lambda x:-x[-1])
    words,_=zip(*count_pairs)

    words = words[:len(words)]+("",)

    words_int_map=dict(zip(words,range(len(words))))
    poems_vector = [list(map(lambda word:words_int_map.get(word,len(words)),poem))for poem in poems]
    print(poems_vector[1])
    print(np.array(poems_vector).shape)
    return poems_vector,words_int_map,words

def generate_batch(batch_size,poems_vec,word_to_int):
    n_chunk=len(poems_vec)//batch_size
    x_batches=[]
    y_batches=[]

    for i in range(n_chunk):
        start_index=i*batch_size
        end_index = start_index+batch_size
        batches=poems_vec[start_index:end_index]
        #找到最长的长度
        length=max(map(len,batches))
        x_data=np.full((batch_size,length),word_to_int[''],np.int32)

        for row in range(batch_size):
            x_data[row,:len(batches[row])]=batches[row]
        y_data=np.copy(x_data)
        y_data[:,:-1]=x_data[:,1:]
        x_batches.append(x_data)
        y_batches.append(y_data)
    return x_batches,y_batches
    pass

process_poems("./data/poetry.txt")
