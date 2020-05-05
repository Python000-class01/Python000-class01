# platform Linux
import ansible.runner

runner = ansible.runner.Runner(
   module_name='ping',
   module_args='',
   pattern='web*',
   forks=10
)
# datastructure = runner.run()
# 该方法将返回每个host主机是否可以被ping通.返回类型详情请参阅 模块相关.:

# {
#     "dark" : {
#        "web1.example.com" : "failure message"
#     },
#     "contacted" : {
#        "web2.example.com" : 1
#     }
# }