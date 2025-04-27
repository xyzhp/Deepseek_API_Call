from openai import OpenAI # 安装openai的SDK
import time
import sys

key = "sk-8bb79eb444164c4d897359275ced0ad4"
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
def chat_func(say):
    response = client.chat.completions.create(
        model = "deepseek-chat", # 选择的模型
        messages = [
            {"role" : "system", "content" : "你是一个专业的科学家，请使用严谨的内容回答"}, #json格式
            {"role" : "user", "content" : say},
        ],
    stream = False
)
    print_slowly(response.choices[0].message.content,0.01)

while(1):
    user_input = input("请输入对话内容：")
    if user_input == "bye":
        break
    chat_func(user_input)
    print("\n-----------------------------------------------------------------------------------")
