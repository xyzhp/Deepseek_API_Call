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
    try:
        response = client.chat.completions.create(
            model = "deepseek-chat", # 选择的模型
            messages = message,
            stream = stream_judge # stream_judge用于控制是否采用流式输出
        )
    # 处理流式数据
        full_content = []
        if stream_judge:
            for chunk in response:
                if chunk.choices[0].delta.content: #chunk.choices[0].delta.content用于逐字获取并响应
                    content = chunk.choices[0].delta.content
                    print_slowly(content,0.01)
                    full_content.append(content)

            message.append({"role" : "assistant", "content" : "".join(full_content)})
        else:
            content = response.choices[0].message.content
            print(f"DeepSeek:{content}")
            message.append({"role": "assistant", "content": content})

    except Exception as e:
        print(f"\n发生错误：{str(e)}")
        message.pop()

# 代码执行区
stream_input = input("是否采用流式输出？(y/n): ").lower()
stream_judge = stream_input in ['y', 'yes', 'true']
message = [] # 用户输入放在循环外，若在循环内，无法保存上下文信息
while(True):
    try:
        user_input = input("\n用户：")
        if user_input.lower() in ['exit', 'bye']:
            break
        message.append({"role" : "user" , "content" : user_input})
        chat_func(message,stream_judge)
    except KeyboardInterrupt:
        print("\n对话已中断")
        break
    print("\n-----------------------------------------------------------------------------------")
