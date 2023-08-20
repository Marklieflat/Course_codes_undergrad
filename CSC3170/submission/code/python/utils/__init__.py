

__GROUPED_MODELS__ = {

    'chimera':[
        'chimera-chat-7b', 
        'chimera-inst-chat-7b',
        'chimera-chat-13b',
        'chimera-inst-chat-13b',
    ],

    'phoenix':[
        'phoenix-chat-7b',
        'phoenix-inst-chat-7b',
    ],

    'chinese_alpaca':[
        # chinese_alpaca with lora weights, by ymcui
        'chinese-alpaca-7b', 
        'chinese-alpaca-13b',
    ],

    'chatglm': [
        'chatglm-6b',
    ],

    'belle': [
        'belle-7b-2m',
    ],

    'vicuna': [
        'vicuna-7b-v1.1',
        'vicuna-13b-v1.1',
        'chinese-vicuna-13b',
        'vicuna-7b-v0',
        'vicuna-13b-v0',
    ]

}

__ALL_MODELS__ = []
for i in __GROUPED_MODELS__.values():
    __ALL_MODELS__.extend(list(i))

if __name__ == '__main__':
    print(__ALL_MODELS__)