import numpy as np
from logging import warning
import pprint

out_list_promotion_code = []
dict_phone_pro = {}
def g_code(numbers_phone):
    header_code=['PC']
    tail_code = list('0123456789')
    global out_list_promotion_code
    global dict_phone_pro
    header_code.append(''.join(np.random.choice(tail_code,6)))
    code_promotion = ''.join(header_code)
    if code_promotion not in out_list_promotion_code:
        out_list_promotion_code.append(code_promotion)
        dict_phone_pro.update({code_promotion:numbers_phone})
        return code_promotion
    else:
        return g_code(numbers_phone)
def input_refcode(numbers_phone,promotion_code,dic_data):
    global dict_phone_pro
    if dic_data['promotion_code'] == dic_data[dict_phone_pro[promotion_code]][promotion_code]:
        k = dic_data[dict_phone_pro[promotion_code]]['entered numbers']
        dic_data[dict_phone_pro[promotion_code]]['entered numbers'] = int(k)-1 if int(k)>0 else warning("OVER NUMBERS INPUT, CHECK CODE AGAIN")
        if k >= 1 :
            return save_ref_code_in_data(numbers_phone,promotion_code,dic_data)
        else:
            warning("OVER NUMBERS INPUT, CHECK CODE AGAIN")
    else:
        warning("NO EXISTS")

def save_ref_code_in_data(numbers_phone,promotion_code,dic_data):
    if dict_phone_pro[promotion_code] == str(numbers_phone):
        dic_data[dict_phone_pro[promotion_code]]['ref_code'] == str(promotion_code)
def dict_data_output(phone,k=5):
    dic_out={}
    dic_out[phone] = {
        'promotion_code': g_code(phone),
        'entered numbers': k,
        'ref_code': None
    }
    return dic_out
def dict_datas(list_data_input):
    list_phones=[]
    list_dic=[]
    for i in list_data_input:
        list_phones.append(i['phone'])
    for i in list_phones:
        list_dic.append(dict_data_output(i))
    return list_dic
def generate_user_code(list_input):
    dictionary_agents = dict_datas(list_input)
    for i in range(len(dictionary_agents)):
        for j in range(len(dictionary_agents)):
            try:
                list_input[i].update(dictionary_agents[j][list_input[i]['phone']])
            except Exception as e:
                warning(e)
                continue
    return list_input
