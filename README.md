# Blrec-LLOneBot

## 部署要求

- NTQQ+LiteLoader+LLOneBot
- Blrec
  
**这些可以不部署在一台设备上面，保证能够通过网络互访即可**

## 部署流程

1. 安装Python  
2. 安装flask和request  
```
pip install requests flask
```
3. 安装NTQQ+LiteLoader+LLOneBot  
*不会安装的点[这里](https://llonebot.github.io/zh-CN/guide/getting-started)*

4. 配置文件  
设置正向HTTP地址与推送群号  
```
llonebot_url = " "  #此处填你的LLOneBot的正向HTTP地址，例如http://127.0.0.1:3000
group_id = " "  #此处填写计划推送消息的群号
```

5. 在blrec的 "设置>webhook" 中添加本程序的地址  

`http://your_ip_address:5000/webhook`

6. 运行本程序  
```
python blrec-llonebot.py
```

## 注意事项

- 部分消息暂未适配，请提ISSUE或者等待适配
- 打个广告，B站录播请[加群](https://qm.qq.com/q/TormYq7hMQ)
