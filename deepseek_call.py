from openai import OpenAI # 安装openai的SDK
import time
import sys

key = ""
# 访问接口，使用 API key进行身份验证，这是一个对象
client = OpenAI(api_key=key, base_url = "https://api.deepseek.com" )
def print_slowly(text, delay): # 逐字输出，贴合deepseek等语言模型输出样式
    index = 0
    while index < len(text):
        sys.stdout.write(text[index])
        sys.stdout.flush()
        time.sleep(delay)
        index+=1
# 使用client创建一个实例response，发送请求
def chat_func(message,stream_judge):
    response = client.chat.completions.create(
        model = "deepseek-chat", # 选择的模型
        messages = message,
    stream = stream_judge # stream_judge用于控制是否采用流式输出
)
    # 处理流式数据
    if stream_judge:
        for chunk in response:
            if chunk.choices[0].delta.content: #chunk.choices[0].delta.content用于逐字获取并响应
                content = chunk.choices[0].delta.content
                print_slowly(content,0.01)

        message.append({"role" : "assistant", "content" : content})
    else:
        content = response.choices[0].message.content
        print(f"DeepSeek:{content}")
# 代码执行区
stream_judge = input("是否采用流式输出,若使用请填True,否则为False: ")
stream_judge = bool(stream_judge)
message = [] # 用户输入放在循环外，若在循环内，无法保存上下文信息
while(1):
    user_input = input("请输入对话内容：")
    message.append({"role" : "user" , "content" : user_input})
    if user_input == "bye":
        break
    chat_func(message,stream_judge)

    print("\n-----------------------------------------------------------------------------------")
