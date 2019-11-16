from sayhello import app
import os

if __name__ == '__main__':
    print('dirname', os.path.dirname(app.root_path))
    app.run(port=8000)              # 默认5000， 端口号大于1024才有用