import numpy as np
from logging import warning

out_list_promotion_code = []
dict_promotion_phone = {} 
'''
    {
        promotion_code : phone
    }
'''

def generate_code(phone_numbers):
    '''
        Generate code following one phone_numbers
    '''

    header_code = ['PC']
    tail_code = list('0123456789')
    global out_list_promotion_code
    global dict_promotion_phone
    header_code.append(''.join(np.random.choice(tail_code,6)))
    promotion_code = ''.join(header_code)
    if promotion_code not in out_list_promotion_code:
        out_list_promotion_code.append(promotion_code)
        dict_promotion_phone.update({promotion_code:phone_numbers})

        return promotion_code
    else:

        return generate_code(phone_numbers)


def input_refcode(phone_numbers, promotion_code, dic_data):
    '''
        Enter REF-CODE - > SAVE in Data
    '''

    global dict_promotion_phone, out_list_promotion_code

    if promotion_code in out_list_promotion_code:
        if promotion_code!=dic_data[phone_numbers]['promotion_code']:
            k = dic_data[dict_promotion_phone[promotion_code]]['entered numbers']
            if k>=1 :
                new_dic_data, key = save_ref_code_in_data(phone_numbers, promotion_code, dic_data)
                if key:
                    new_dic_data[dict_promotion_phone[promotion_code]]['entered numbers'] = int(k)-1
                    
                    return new_dic_data
            else:
                warning("OVER NUMBERS INPUT, CHECK CODE AGAIN")
        else:
            warning("DO NOT ENTER YOUR CODE")
    else:
        warning("NO EXISTS")

    return dic_data


def save_ref_code_in_data(phone_numbers, promotion_code, dic_data):
    '''
        SAVE REF_CODE in DATA
    '''

    if dic_data[phone_numbers]['ref_code'] is None:
        dic_data[phone_numbers]['ref_code'] = str(promotion_code)
        warning("INPUT SUCCESSFULL")
        return dic_data,1

    warning("FAILED - YOUR REF-CODE EXISTS")
    return dic_data,0

def dict_data_output(phone_numbers, k=5):
    '''
        Dict return format std
    '''

    dic_out = {}
    dic_out[phone_numbers] = {
        'promotion_code': generate_code(phone_numbers),
        'entered numbers': k,
        'ref_code': None
    }

    return dic_out


def dict_datas(list_data_input):
    '''
        return list dict multiple database
    '''
    list_phones=[]
    list_dic=[]
    for i in list_data_input:
        list_phones.append(i['phone'])

    for i in list_phones:
        list_dic.append(dict_data_output(i))

    return list_dic


def generate_user_code(nodes):
    '''
        Generate user nodes in elder nodes
    '''
    dictionary_agents = dict_datas(nodes)
    for i in range(len(dictionary_agents)):
        for j in range(len(dictionary_agents)):
            try:
                nodes[i].update(dictionary_agents[j][nodes[i]['phone']])
            except Exception as e:
                warning(e)
                continue

    return nodes


# def test
def testting():
    node = {}
    for i in ['0355197948', '0378972958', '0383868657']:
        node.update(dict_data_output(str(i)))
    print(f'nodes :{node}')
    n = input('phone: ')
    x = input('promotion_code: ')
    new_nodes = input_refcode(n,x,node)
    print(f'new nodes :{new_nodes}')
    n = input('phone: ')
    x = input('promotion_code: ')
    new_nodes_1 = input_refcode(n,x,new_nodes)
    print(f'new nodes :{new_nodes_1}')

    return True


# testting()