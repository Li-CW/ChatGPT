## 说明

该项目是 OpenAI 的 ChatGPT 本地化项目。

原理很简单：前端页面向 django 后端发送对话，django后端负责调用 ChatGPT 给的接口，得到回复，然后发送到前端，前端渲染展示。

自己玩的，没有做其他模块。

## 使用方式

1. 下载项目：`git@github.com:Li-CW/ChatGPT.git`
2. 修改`backend\Hasity\Hasity\settings.py`中的`OPEN_AI_KEY ="your key"`，填入ChatGPT的秘钥。
3. 打开cmd，切换到 `backend\Hasity`目录，运行`pip install -r requirements.txt` 安装python环境。（最好替换国内源）
4. 打开cmd，切换到`web\canwin`目录，运行`npm install`，安装 vue 依赖。
5. 打开cmd，切换到`backend\Hasity`目录，运行`python manage.py runserver`命令，启动后端。
6. 打开cmd，运行`vue ui`命令，启动前端。

在线体验：[https://app2098.acapp.acwing.com.cn/](https://app2098.acapp.acwing.com.cn/)



## 后续计划

**`OpenAI`除了对话人工智能：`GPT-3`模型，还有的自动生成代码人工智能：`Codex`模型，文字描述生成图片：`Image`模型等等，后续会陆续上线**。

进度安排：

1. Codex自动编写代码。
2. Image 描述生成图片。
3. .....

**欢迎stra,fock**



