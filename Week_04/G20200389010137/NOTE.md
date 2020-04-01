# 学习笔记

## 作业 1

使用 Ansible API2.0 版本。
以 Ad-Hoc 方式，ssh 密码登录批量到远程主机执行 shell 命令启动停止 nginx。

```python
cmd = 'nginx'               # 启动
cmd = 'nginx -s stop'       # 停止
cmd = 'nginx -s reload'     # 重载配置文件
# Ad-Hoc 执行
ansible2.run(hosts='nginx', module="shell", args={'chdir': '/usr/local/nginx/sbin', 'cmd': cmd})
```

不可达：

```python
Sunday 29 March 2020  16:56:21 +0800 (0:00:00.167)       0:00:00.167 **********
[WARNING]: Unhandled error in Python interpreter discovery for host
192.168.189.230: Failed to connect to the host via ssh: ssh: connect to host
192.168.189.230 port 22: Operation timed out
{
    "success": {},
    "failed": {},
    "unreachable": {
        "192.168.189.231": {
            "unreachable": true,
            "msg": "Data could not be sent to remote host \"192.168.189.231\". Make sure this host can be reached over ssh: ssh: connect to host 192.168.189.231 port 22: Operation timed out\r\n",
            "changed": false
        },
        "192.168.189.230": {
            "unreachable": true,
            "msg": "Data could not be sent to remote host \"192.168.189.230\". Make sure this host can be reached over ssh: ssh: connect to host 192.168.189.230 port 22: Operation timed out\r\n",
            "changed": false
        }
    }
}
```

## 作业 2

```python
# select * from data
order_df

# select * from data limit(10)
order_df.head(10)
order_df[0:10]

# select id from data  //id 是 data 表的特定一列
order_df['id']

# select count(id) from data
order_df['id'].count()

# select * from data where id <1000 and  age >30
# user_df[(order_df['id'].astype('int')<1000) & (order_df['age']>30)]
user_df[(user_df['id'].astype('int')<1000) & (user_df['age']>30)]

# select id, count(distinct orderid) from data group by id;
order_df.groupby('id')['orderid'].nunique()

# select * from table1 t1 inner_join table2 t2 on t1.id = t2.id
pd.merge(order_df, user_df, on='id', how='inner')

# select * from t1 union select * from t2
# pd.concat([order_df, order2_df])
pd.concat([order_df, order2_df]).drop_duplicates()

# delete from t1 where id=10
order_df[order_df['id'] != 10]

# alter table t1 drop column name
order_df.drop(['amount'], axis=1)
```
