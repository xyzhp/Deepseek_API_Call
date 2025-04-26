from openai import OpenAI # 安装openai的SDK
# 访问接口，使用 API key进行身份验证，这是一个对象
client = OpenAI(api_key="sk-8bb79eb444164c4d897359275ced0ad4", base_url = "https://api.deepseek.com" )

# 使用client创建一个实例response，发送请求
response = client.chat.completions.create(
    model = "deepseek-chat", # 选择的模型
    messages = [
        {"role" : "system", "content" : "你是一个风趣幽默的客服，请使用搞笑的方式回答"}, #json格式
        {"role" : "user", "content" : "你介绍下自己"},
    ],
    stream = False
)

print(response.choices[0].message.content)