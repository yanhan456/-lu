import wx



from workAttendanceSystem import RunWAT
class MyApp(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="登录", size=(532,420))
        # wx.App.__init__(self)
        # frame = wx.Frame(parent=None,title='Login',size=(532,420))
        #设置窗口的左上角的图标
        #其中参数type表示图片的类型，还有ico，jpgm等类型



        panel = wx.Panel(self)
        # 向panel中添加图片


        #添加静态标签
        label_user = wx.StaticText(panel,-1,"账号:", pos=(80,200))
        label_pass = wx.StaticText(panel,-1,"密码:", pos=(80,240))
        #添加文本输入框
        self.entry_user = wx.TextCtrl(panel,-1,size=(200,30), pos=(130,200))
        #style 为设置输入
        self.entry_pass = wx.TextCtrl(panel,-1, size=(200,30), pos=(130,240), style=wx.TE_PASSWORD)
        #添加按钮
        self.but_login = wx.Button(panel,-1,"登陆", size=(120,50), pos=(120,300))
        self.but_register = wx.Button(panel,-1,"取消", size=(120,50), pos=(260,300))
        #设置按钮的颜色
        self.but_login.SetBackgroundColour("#0a74f7")
        self.but_register.SetBackgroundColour("#0a74f7")
        #给按钮绑定事件
        self.Bind(wx.EVT_BUTTON, self.user, self.but_login)
        self.Bind(wx.EVT_BUTTON, self.Shut_down, self.but_register)
        # frame.Center()
        # frame.Show(True)
    def Shut_down(self,event):
        self.Close(True)
    def user(self,event):

        user_name = self.entry_user.GetValue()
        pass_word = self.entry_pass.GetValue()
        print(user_name,pass_word)

        from dome2 import www

        user = www()
        username = []
        password = []
        for User in user:
            username.append(User[0])
            password.append(User[1])
        print(username[0])
        print(password[0])
        if  user_name == str(username[0]):
            if pass_word == str(password[0]):
                RunWAT()
                self.Close(True)
            else:
                wx.MessageBox(message="密码错误", caption="提示")
                return
        # 密码判断b
        else:
            wx.MessageBox(message="账号错误", caption="提示")
            return

        # # 通过验证，关闭对话框并返回1

def login():
    frame = MyApp()
    frame.Show()



if __name__=='__main__':
    # app = MyApp()
    # app.MainLoop()   #
    app = wx.App()
    frame = MyApp()
    frame.Show()
    app.MainLoop()

