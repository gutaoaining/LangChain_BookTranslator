# 作者：顾涛
# 创建时间：2026/1/26
import random
import time

import gradio as gr


def do_it(message, history):
    responses = [
        "谢谢您的留言！",
        "非常有趣！",
        "我不确定该如何回答。",
        "请问还有其他问题吗？",
        "我会尽快回复您的。",
        "很高兴能与您交流！",
    ]
    # 生成一个答案，随机
    resp = random.choice(responses)
    # 流式输出
    res = ''
    for char in resp:
        res += char
        time.sleep(0.2)
        yield res


instance = gr.ChatInterface(  # 构建一个UI界面
    fn=do_it,
    title='模拟流式输出！'
)

# 启动服务
instance.launch(server_name='0.0.0.0', server_port=8008)
