import json
import pandas as pd
import numpy as np

import requests
import random
import time
from tqdm import tqdm, trange
from utils.generate_phoenix import get_model_outputs, load_model_and_tokenizer, OmegaConf
from utils.utils import add_prompt
from datetime import datetime, timedelta




##### jialin's part #####
def get_names():
    url = 'https://raw.githubusercontent.com/aruljohn/popular-baby-names/master/2021/girl_boy_names_2021.csv'
    res = requests.get(url, allow_redirects=True)
    with open('girl_boy_names_2021.csv','wb') as file:
        file.write(res.content)
    df = pd.read_csv('girl_boy_names_2021.csv')    
    return df

def get_names_list():
    names_df = pd.read_csv("girl_boy_names_2021.csv")
    name_lst = []
    name_lst += names_df["Girl Name"].to_list()
    name_lst += names_df["Boy Name"].to_list()
    name_lst = list(set(name_lst))
    name_lst.sort()
    return name_lst

def get_user(N: int, save: bool) ->  pd.DataFrame:
    random.seed(151)
    name_lst = get_names_list()
    user_df = pd.DataFrame(columns=['USER_ID', 'USER_NAME', 'AGE'])

    for row_num in range(N):
        # generate ID
        id = random.randint(1e9, (1e10-1))
        while id in user_df['USER_ID'].to_list():
            id = random.randint(1e9, (1e10-1))
        # generate Name
        idx = random.randint(0, (len(name_lst)-1))
        name = name_lst[idx]
        # generate Age
        prob = random.randint(1, 100)
        if prob < 80:
            age = random.randint(20, 50)
        elif (prob >= 80) & (prob < 85):
            age = random.randint(12, 19)
        else:
            age = random.randint(51, 70)
        # insert to user table
        new_row = [id, name, age]
        user_df.loc[row_num] = new_row

    user_df.set_index("USER_ID", inplace=True)
    if save:
        user_df.to_csv('user.csv')
    return user_df


def get_complaint(N: int, save: bool) -> pd.DataFrame:
    random.seed(150)
    complaint_df = pd.DataFrame(columns=['COMPLAINT_ID', 'STATUS', 'COMPLAINT_DATE', 
                                         'RESOLUTION_DATE', 'USER_ID', 'BRAND_NAME'])
    dates = pd.date_range(datetime.strptime("2018-01-01", "%Y-%m-%d"),
                    datetime.strptime("2023-04-19", "%Y-%m-%d")-timedelta(days=1), 
                    freq='d')
    user_id_list = pd.read_csv("user.csv")
    user_id_list = user_id_list['USER_ID'].to_list()
    brand_list = pd.read_csv("brand.csv")
    brand_list = brand_list["BRAND_NAME"].to_list()

    for row_num in range(N):
        # Complaint ID
        c_id = random.randint(1e9, (1e10-1))
        while c_id in complaint_df['COMPLAINT_ID'].to_list():
            c_id = random.randint(1e9, (1e10-1))
        # Status
        status = random.randint(0,1)
        # Complaint Date & Resolution Date
        start = random.randint(0, (len(dates)-1))
        complaint_date = dates[start]
        if status == 1:
            interval = random.randint(0, 100)
            resolution_date = complaint_date + timedelta(days=interval)
        elif status == 0:
            resolution_date = None
        # User ID
        user = random.randint(0, (len(user_id_list)-1))
        user_id = user_id_list[user]
        # Brand Name
        brand = random.randint(0, (len(brand_list)-1))
        brand_name = brand_list[brand]

        new_row = [c_id, status, complaint_date, resolution_date, user_id, brand_name]
        complaint_df.loc[row_num] = new_row

    complaint_df.set_index("COMPLAINT_ID", inplace=True)

    if save:
        complaint_df.to_csv('complaint.csv')
    return complaint_df


##### kexuan & guiming's part #####

def get_time():
    a1=(2022,1,1,0,0,0,0,0,0)              
    a2=(2023,4,1,23,59,59,0,0,0)   
    
    start=time.mktime(a1)    
    end=time.mktime(a2)
    
    date_list = []
    for i in range(20000):      
        t=random.randint(start,end)
        date_touple=time.localtime(t)
        date=time.strftime("%Y-%m-%d",date_touple)
        date_list.append(date)
    return np.array(date_list)

def get_brand():
    sephora = pd.read_csv('sephora_website_dataset.csv')
    sephora = sephora.iloc[:9000, :]
    brand = sephora.iloc[:, 1:2]
    brand = brand.drop_duplicates().reset_index(drop = True)
    brand = brand.rename({'brand':'BRAND_NAME'}, axis = 1)
    brand.to_csv('output/brand.csv', index=False)
    return brand

def get_order():
    prod = pd.read_csv('product.csv')
    user = pd.read_csv('user.csv')
    address1 = pd.read_csv('testdata1.csv', header = None)
    address2 = pd.read_csv('testdata2.csv', header = None)
    address3 = pd.read_csv('testdata3.csv', header = None)
    address4 = pd.read_csv('testdata4.csv', header = None)
    address = pd.concat([address1, address2, address3, address4])
    address = address.to_numpy()
    user = user[['USER_ID']]
    
    order = prod[['PRODUCT_ID','PRODCUT_NAME','PRICE']]
    order_id = np.random.randint(1000000000, 2000000000, size = (21000, ), dtype = int)
    order_id = np.random.choice(order_id, 20000, replace = False)
    item_quant = np.random.randint(1, 100, size = (20000, ))
    shipping_cost = np.random.randint(50, 200, size = (20000, )).astype(np.float64)
    shipping_prec = np.round(np.random.random((20000, )), 2)
    shipping_cost += shipping_prec
    
    timestamp = get_time()
    user_id = np.random.choice(user['USER_ID'].to_numpy(), size = (20000, ))
    order_att = np.column_stack((order_id, item_quant, address, shipping_cost, timestamp, user_id))
    
    order_att = pd.DataFrame(order_att, columns = ['ORDER_ID','ITEM_QUANTITY','SHIPPING_ADDRESS','TOTAL_SHIPPING_COST','TIMESTAMP','USER_ID'])
    order = pd.concat([order, order_att], axis = 1)
    namelist = {'PRODCUT_NAME':'PRODUCT_NAME','PRICE':'ITEM_PRICE'}
    order = order.rename(namelist, axis = 1)
    order['ITEM_PRICE'] = order['ITEM_PRICE']/20
    order['ITEM_PRICE'] = order['ITEM_PRICE'].round(2)
    order['TOTAL_COST'] = order['ITEM_PRICE']*order['ITEM_QUANTITY'] + order['TOTAL_SHIPPING_COST']
    order = order[['ORDER_ID','ITEM_PRICE','ITEM_QUANTITY','SHIPPING_ADDRESS','TOTAL_SHIPPING_COST', 'TOTAL_COST','TIMESTAMP','PRODUCT_NAME','USER_ID']]
    
    prod = pd.read_csv('product.csv')
    prod = prod[['PRODUCT_ID','PRODCUT_NAME','PRICE']]
    prod_new = np.random.choice(prod['PRODCUT_NAME'].to_numpy(), size = (20000, ))
    prod_new = pd.DataFrame(prod_new, columns = ['PRODUCT_NAME'])
    prod_new = pd.merge(prod_new, prod, how = 'left', left_on = 'PRODUCT_NAME', right_on = 'PRODCUT_NAME')
    prod_new = prod_new.drop_duplicates()
    prod_new = prod_new[['PRODUCT_NAME','PRICE']]
    prod_name = np.random.choice(prod_new['PRODUCT_NAME'], 20000)
    prod_name = pd.DataFrame(prod_name, columns = ['PRODUCT_NAME'])
    prod_final = pd.merge(prod_name, prod_new, how = 'left', on = 'PRODUCT_NAME')
    prod_new = prod_final
    order['ITEM_PRICE'] = prod_new['PRICE']
    order['ITEM_PRICE'] = order['ITEM_PRICE']/20
    order['ITEM_PRICE'] = order['ITEM_PRICE'].round(2)
    order['PRODUCT_NAME'] = prod_new['PRODUCT_NAME']
    order['TOTAL_COST'] = order['ITEM_PRICE']*order['ITEM_QUANTITY'] + order['TOTAL_SHIPPING_COST']
    
    prod = pd.read_csv('product.csv')
    order_cate = pd.merge(order, prod, how = 'left', left_on = ['PRODUCT_NAME'], right_on = ['PRODCUT_NAME'])
    order_cate = order_cate[['ORDER_ID','ITEM_PRICE','ITEM_QUANTITY','SHIPPING_ADDRESS','TOTAL_SHIPPING_COST', 'TOTAL_COST','TIMESTAMP','PRODUCT_NAME', 'PRODUCT_ID','USER_ID','CATEGORY']]
    order_cate = order_cate.drop_duplicates()
    order_cate[['ITEM_QUANTITY']] = order_cate[['ITEM_QUANTITY']].astype(int)
    order_cate[['TOTAL_SHIPPING_COST','TOTAL_COST']] = order_cate[['TOTAL_SHIPPING_COST','TOTAL_COST']].astype(float)
    
    order_cate['TIMESTAMP'] = pd.to_datetime(order_cate['TIMESTAMP']).dt.strftime("%Y-%m-%d")
    mask = (order_cate['TIMESTAMP'] > '2022-12-01') & (order_cate['TIMESTAMP'] < '2023-03-20') & (order_cate['CATEGORY'] == 'Skincare')
    new_quant = order_cate.loc[mask, 'ITEM_QUANTITY'] + 50
    mask = (order_cate['TIMESTAMP'] > '2022-01-01') & (order_cate['TIMESTAMP'] < '2022-03-20') & (order_cate['CATEGORY'] == 'Skincare')
    new_quant = order_cate.loc[mask, 'ITEM_QUANTITY'] + 50
    order_cate.loc[mask, 'ITEM_QUANTITY'] = new_quant
    
    order_output = order_cate.iloc[:, :10]
    order_output = order_output.drop_duplicates(subset = 'ORDER_ID')
    order_output = order_output.drop('PRODUCT_NAME', axis = 1)
    order_output.to_csv('output/order.csv', index=False)
    return order_output
    
    



def get_comments(df_r, duplicated_indices):
    random.seed(0)
    df_product= pd.read_csv('output/product.csv')
    pid2NameandCat = {k: [v1, v2] for k,v1, v2 in zip(df_product['PRODUCT_ID'], df_product['PRODUCT_NAME'], df_product['CATEGORY'])}
    del df_product

    ratings = df_r['RATINGS']
        
    comments = []
    model_id = 'phoenix-inst-chat-7b'
    config = OmegaConf.load('utils/config_private.yaml')[model_id]
    prompt = "A chat between a curious human and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the human's questions.\n\nHuman: <s>{question}</s>Assistant: <s>"
    question_template = 'You have bought a product. \
You have rated the product using a scale of 5 and the rating information is provided. A rating of 0~1 means disappointing, 2 means mediocre, 3 means okay, 4 means satisfying and 5 means perfect. \
Write a short and emotional review within 50 words with the following information: \
\nName of product: {name}\nOrder price: {order_price}\nOrder quantity: {order_quantity}\nCategory: {category}\nRating: {rating}/5\
\n\nDo not include too many details but the rating of your purchase.'
    model, tokenizer = load_model_and_tokenizer(config['model_id'], 'cuda', 1, 'fp16', config['config_dir'])
    generation_config = config['generation_config']
    
    generation_config['pad_token_id'] = tokenizer.pad_token_id

    df_order = pd.read_csv('output/order.csv')
    for i in trange(len(df_order)):
        if i in duplicated_indices:
            continue
        if random.random() < 0.6: # comment
            raw_question = question_template.format(
                name=pid2NameandCat[df_r.loc[i, 'PRODUCT_ID']][0], 
                order_price=df_order.loc[i, 'ITEM_PRICE'],
                order_quantity=df_order.loc[i, 'ITEM_QUANTITY'],
                category=pid2NameandCat[df_r.loc[i, 'PRODUCT_ID']][1],
                rating=round(ratings[i]),
            )
            inputs = add_prompt(raw_question, prompt)
            comment = get_model_outputs(
                model_id = model_id, 
                model = model, 
                tokenizer= tokenizer, 
                prompts=[inputs], 
                generation_config=generation_config, 
                texts = [], 
                device = 'cuda'
            )[0]
            print(ratings[i])
            print(comment)
            print('-'*20)
        else:
            comment = ''

        comments.append(comment)
    return comments


def get_review_date_and_productid_and_userid():
    df = pd.read_csv('output/order.csv')
    order_date = df['TIMESTAMP'] # a series of str
    today = '2023-4-20'
    review_date = []
    for od in order_date:
        rd = str_time_prop(od, today, '%Y-%m-%d', random.random())
        review_date.append(rd)
    productid = df['PRODUCT_ID'].to_list()
    user_ids = df['USER_ID'].to_list()
    
    return review_date, productid, user_ids


def str_time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def get_product(n):
    random.seed(0)
    inventory = random.choices(range(3000, 90000), k=n)
    name = pd.read_csv('sephora_website_dataset.csv')['name'][:n]
    price = np.random.random(n).round(2) + np.random.randint(3000, 10000, size=n)
    # category = random.choices(['Perfume', 'Cologne', 'Concealer', 'Lipstick', 'Moisturizers', 'Value & Gift Sets', 'Fragrance', 'Body Mist & Hair Mist', 'Others'], k=n)
    category = random.choices(
        ['Gift Sets', 'Hair & Body', 'Scents', 'Makeup', 'Tools', 'Skincare', 'Others'],
        weights=[0.2259, 0.2149, 0.1601, 0.1075, 0.1009, 0.1009, 0.0899],
        k=n)
    brands = pd.read_csv('output/brand.csv')['BRAND_NAME']
    brand_names = random.choices(brands, k=n)
    df = pd.DataFrame({
        'PRODUCT_ID': list(range(n)),
        'INVENTORY': inventory,
        'PRODUCT_NAME': name,
        'PRICE': price,
        'CATEGORY': category,
        'BRAND_NAME': brand_names,
    })
    o = 'output/product.csv'
    df.to_csv(o, index=False)
    print(f'output to {o}')


def get_applicability():
    random.seed(0)
    #  Only hair&body, makeup, skincare have (random) skin_type
    df = pd.read_csv('output/product.csv')
    choices = ['dry', 'normal', 'oily']
    pid = df['PRODUCT_ID']
    pcat = df['CATEGORY']

    tgt_id = [] # target id
    tgt_type = [] # target type

    for i in range(len(pid)):
        if pcat[i] in ['Skincare', 'Makeup', 'Hair & Body']:
            t_li = random.sample(choices, k=random.choice([1,2,3])) # a list of skin_type
            for t in t_li:
                tgt_id.append(pid[i])
                tgt_type.append(t)
                
            # tgt_type.append(', '.join(t)) # can have multiple skin types

    new_df = pd.DataFrame({
        'PRODUCT_ID': tgt_id,
        'SKIN_TYPE': tgt_type
    })
    o = 'output/applicability.csv'

    new_df.to_csv(o, index=False)
    print(f'output to {o}')


def get_skin(n):
    random.seed(0)
    # skin = [
    #     ','.join(random.sample(['combination', 'dry', 'normal', 'oily'], k=random.choice(range(1,5))))
    #     for _ in range(n)
    # ]
    skin = [random.sample(['dry', 'normal', 'oily'], k=1)[0] for _ in range(n)]
    product_names = pd.read_csv('output/product.csv')['PRODUCT_NAME']
    df = pd.DataFrame({
        'SKIN_TYPE': skin,
        'PRODUCT_NAME': product_names,
    })
    o = 'output/skin.csv'
    df.to_csv(o, index=False)
    print(f'output to {o}')


def get_ratings(user_ids):
    random.seed(0)
    df_u = pd.read_csv('output/user.csv')
    user2age = {k: v for k, v in zip(df_u['USER_ID'], df_u['AGE'])}
    ratings = []
    for uid in user_ids:
        if 20 <=  user2age[uid] <= 40: # they tend to rate a product lower
            r = random.choices(range(0,6), weights=[.2, .25, .25, .15, .1, .05], k=1)[0]
        else: # otherwise, ratings are higher
            r = random.choices(range(0,6), weights=[.075, .1, .125, .25, .25, .2], k=1)[0]
        ratings.append(r)

    return ratings


def get_review():
    random.seed(0)
    print('generating review')
    

    # must be generated after order date is determined
    dates, product_ids, user_ids =  get_review_date_and_productid_and_userid()

    # ratings = np.random.randint(0, 4, len(dates)) + np.random.uniform(0,1,len(dates)).round(2)
    ratings = get_ratings(user_ids)
    # ratings = random.choices(
    #     range(0,6), 
    #     weights = [.075, .1, .125, .25, .25, .2],
    #     k = len(dates)
    # )

    # comments = get_comments(ratings)
    comments = ['' for _ in range(len(dates))]
    # with open('output/answer_phoenix-inst-chat-7b.jsonl', 'r+', encoding='utf-8') as f:
    #     for item in f:
    #         item = json.loads(item)
    #         comments.append(item['text'])


    df = pd.DataFrame({
        'USER_ID': user_ids,
        'PRODUCT_ID': product_ids,
        'RATINGS': ratings,
        'COMMENT': comments,
        'REVIEW_DATE': dates,
    })
    duplicated_indices = df[df.duplicated(subset=['USER_ID', 'PRODUCT_ID'], keep = 'first')].index.tolist()
    # print(duplicated_indices); exit()
    df = df.drop_duplicates(subset=['USER_ID', 'PRODUCT_ID'], keep='first') # only keep the first occurrance
    
    # comment this line to get empty comments 
    df['COMMENT'] = get_comments(df, duplicated_indices)

    df.to_csv('output/review.csv', index=False)

    print('output to output/review.csv')

def main():
    # get_user(10000, True)
    # get_complaint(10000, True)
    # get_brand()
    # get_product(n_product=9000)
    # get_order()
    # get_applicability()
    # get_skin(n_product=9000)
    # get_review()
    pass


if __name__ == '__main__':
    main()