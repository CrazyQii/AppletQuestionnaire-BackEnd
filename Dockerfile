# version 0.1

# 基于镜像基础
FROM python:3.9.1

# 设置代码文件夹工作目录 /home/app
WORKDIR /home/app

# 将文件内容复制到容器指定工作目录
COPY ./flaskr /home/app
COPY requirements.txt /home/app

# 更换pip源
RUN pip3 config set global.index-url http://mirrors.aliyun.com/pypi/simple
RUN pip3 config set install.trusted-host mirrors.aliyun.com

# 安装所需的包
RUN pip install -r requirements.txt

# Run app.py when the container launches
CMD ["python", "run.py"]