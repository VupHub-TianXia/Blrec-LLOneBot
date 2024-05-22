# 需要NTQQ+LiteLoader+LLOneBot
# 需要安装flask
# pip install requests flask


from flask import Flask, request
import requests
import json

app = Flask(__name__)

# LLOneBot 服务器配置
llonebot_url = " "  #此处填你的LLOneBot的正向HTTP地址，例如http://127.0.0.1:3000
group_id = " "  #此处填写计划推送消息的群号

@app.route('/webhook', methods=['POST'])
def webhook():

    # 此处是调试用的
    data = request.json
    print(f"Received webhook data: {json.dumps(data, indent=2)}")  # 打印收到的 webhook 数据
    # 此处是调试用的
    
    event_type = data.get('type')
    room_id = None
    title = None

    if event_type in ["RecordingStartedEvent", "RecordingStoppedEvent", "RecordingCancelledEvent", "RecordingErrorEvent"]:
        room_info = data.get('data', {}).get('room_info', {})
        room_id = room_info.get('room_id')
        title = room_info.get('title')
    elif event_type == "VideoPostprocessingCompletedEvent":
        room_id = data.get('data', {}).get('room_id')
        # VideoPostprocessingCompletedEvent不以相同的方式包含标题，因此未设置标题

    message = ""

    if event_type == "RecordingStartedEvent":
        message = f"录播已【开始】，直播间 ID: {room_id}, 标题: {title}，直播间链接: https://live.bilibili.com/{room_id}"

    elif event_type == "RecordingCancelledEvent":
        message = f"录播已【取消】，直播间 ID: {room_id}, 标题: {title}"

    elif event_type == "RecordingStoppedEvent":
        message = f"录播已【停止】，直播间 ID: {room_id}, 标题: {title}"    #这个可能不能用，，，后续会修

    elif event_type == "RecordingErrorEvent":
        error_info = data.get('data', {}).get('error')
        message = f"录播出错，直播间 ID: {room_id}, 错误信息: {error_info}"    #这个可能不能用，，，后续会修

    elif event_type == "VideoPostprocessingCompletedEvent":
        message = f"视频后处理完成，直播间 ID: {room_id}"

    elif event_type == "DiskSpaceLowEvent":
        message = f"硬盘空间不足"    #这个可能不能用，，，后续会修


    if message:
        send_qq_message(message)

    return "", 200

def send_qq_message(message):
    headers = {"Content-Type": "application/json"}
    payload = {
        "group_id": group_id,
        "message": message
    }
    response = requests.post(f"{llonebot_url}/send_group_msg", headers=headers, data=json.dumps(payload))
    
    # 打印响应状态码和正文以便调试
    print(f"Response status: {response.status_code}")
    print(f"Response body: {response.text}")

    if response.status_code != 200:
        print("Failed to send message:", response.text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
