from flask_script import Manager, Server
from flask_migrate import MigrateCommand

from apps import create_app

app = create_app()
manager = Manager(app=app)

manager.add_command('start', Server(host='192.168.50.17', port=9000))
# 添加数据库迁移的脚本命令
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
