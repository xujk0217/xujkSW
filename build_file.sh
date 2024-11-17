pip3 install -r requirements.txt

# 运行数据库迁移
python3 manage.py migrate

# 收集静态文件
python3 manage.py collectstatic --no-input