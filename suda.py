

# l= ["小九","苏打","朴宝剑","王一博"]
# if ("小九" in l ):
#     print("女朋友")
# else:
#     print("前女友")





# flag =True
# z=99
# while flag :
#     b = int (input("请输入数字"))
#     if b > z:
#         print("数字过大请重输")
#     elif b < z:
#          print("数字过小请重输")
#     else:
#          print("恭喜你答对了")
#          flag = False



#用for循环计算1 + 2 + 3 +...+ 100的结果
# s = 0
# for i in range (1,100):
#     s=s+i
# print(s)





# 求出10*9*8....*1 的结果 10的阶乘   10

# s=1
# for i in range (1,10,1):
#     s*=i
# print(s)





#成绩评定： 0-59分 不及格 60-70 及格 71-80 良好 81-100 优秀编写程序实现下列需求，给定任意成绩，程序运行之后输出该成绩的级别例如：59分，程序打印出"不及格"
# score=61
# if(score > 0 and score <60):
#     print("不及格")
# if(score >= 60 and score <=70):
#     print("及格")
# if(score >= 71 and score <=80):
#     print("良好")
# if(score >= 81 and score <=100):
#     print("优秀")
# else:
#     print("请输入正确成绩")



# l = 77
# if l in range (0,59):
#      print("不及格")
# if l in range(60,70):
#      print("及格")
# if l in range(71, 80):
#      print("良好")
# if l in range(81, 100):
#      print("优秀")




# 找出100以内能被3整除的整数
# for i in range(1,100):
#     if( i % 3 != 0 ):
#         continue
#     print(i)




# 定义一个求两个数商和余数的方法   (方法定义）
# def number(a,b):
#     print("商:", a // b, "余数:", a % b)
#
# number(20,4)  方法调用




# def number(a,b):
#      if(b == 0):
#          return  None
#      else:
#          return (a // b , a % b )

# res = number(b = 2, a = 20)
# if res is None:
#      print(res)
#      print("参数错误")
# else:
#      print(res)
#      print("商:", res[0], "余数:",res[1])



# def sm(a,b=2):
#     return a+b
#
# print(sm(2))



# c =1,2,3,4,
# a,*b =(1,2,3,4,5,6,7,8,9)
# print(b)





# def number(a,b,*args):
#     s = 0
#     for i in args:
#         s=s+i
#     return s
# print(number(1,2,3,4,5,6,7,8,9,10,11))



# class calc():
#     a=None
#     b=None
#     res=None
#     def input(self,a,b):
#         self.a=a
#         self.b=b
#     def sum(self):
#         self.res = self.a +self.b
#     def div(self):
#         self.res = self.a / self.b
#     def get_result(self):
#         print(self.res)
#
# c=calc()
#
# c.input(10,20)
# c.sum()
# c.get_result()
# c.div()
# c.get_result()



# class calc():
#     res =None
#
#     def __init__(self,a,b):#魔法函数  构造方法
#         self.a=a
#         self.b=b
#
#     def sum(self):
#         self.res=self.a + self.b
#     def div(self):
#         self.res = self.a / self.b
#     def get_result(self):
#         print(self.res)
#
# c=calc(20,30)
# c.sum()
# c.get_result()
# c.div()
# c.get_result()



#  # 九九乘法表
# for i  in range(1,10):
#     for j in range(1,i+1):
#         print(j,"x",i,"=",i*j,end="\t")
#     print( )
#



# for a in range(1,10):
#         for b in range(1,a+1):
#             print(b,"x",a,"=",a*b,end="\t")
#         print()


# for a in range(1,10):
#         for b in range(1,a+1):
#           print(b,"x",a,"=",a*b,end="\t")
#         print()


# l = [1,9,6,2,8,7,5,4,20,50,21,66,30]
# a = len(l)
# print(a)
# for n in range(a-1,0,-1):
#     for m in range(n):
#         if(l[m]>l[m+1]):
#             l[m],l[m+1] =l[m+1],l[m]
# print(l)




# l = [2,3,10,5,6,7,83,2,1,6,8]
# # 升序
# l.sort()
# print(l)
# # 降序
# l.sort(reverse=True)
# print(l)



# 继承
# class parent():
#
#     money = 100000000
#     house = 100
#     __yi_wu = "裙子"
#
#     def shou_yi(self):
#         print("传统手艺")
#
#
# class child(parent):
#     ai_hao = "花钱"
#     def __init__(self,*args,**kwargs):
#         super().__init__()
#
#
#      def shou_yi(self):  #方法重写
#         # super().shou_yi()
#         print("水遁大水龙之术")
#
# c =child()
# print(c.ai_hao)
# print(c.house)
# print(c.money)
# c.shou_yi()



# f = open("pbj.txt","w")#open打开文件
# f.write("Park Baojian's Chinese girlfriend")
# #write写入内容至打开的文件
# f.close()#关闭文件



# l = [1,2,3,4,5,6,7,8,9]
#
# l[0] = 20
# print(l)
# l[1:3] = 20,30
# print(l)



# print(l.pop())
# print(l)
#
# print(l.pop(1))
# print(l)
#
# l.remove(3)
# print(l)

l = [2,3,4,5,6,7,8,9]
l.remove(2)
print(l)

l = [True,1,2,3,4,5,6,7,8,9]
l.remove(1)
print(1)

l.clear()
print(l)


d = {"name":"小明","age":18,"sex":"男"}

d.update({"addr":"上海闵行","学历":"本科"})
print(d)


try:
    f = open("bbbb.txt","r")
    print(f.read())
    f.close()
except:
    print("文件不存在")

print("操作完文件")


def div(a,b):
    try:
        return
    except:
        return

print(div(10,0  ))



class customexception(Exception):
    def __init__(self,Value="值不能为0"):
    self.