# realcat
APK静态分析工具
## 安装依赖
androguard
```
pip install -U androguard[magic,GUI]
```
## 使用方法
```
python3 realcat.py apkfile
```
## 功能及使用示例
1.搜索APK的androidmanifest.xml中可deeplink拉起的activity  
2.检查DEX是否加壳，如果未加壳找出webview注册的Javascript接口方法  
示例如下：  
```
python3 realcat.py "d:\apk\crowdtest\base.apk"
```
输出:  
```
++++++ Browsable activities:
package: com.huawei.deveco.crowdtest
name: com.huawei.activity.PrivacyNoticeActivity
deeplink: crowdtest://com.huawei.deveco.crowdtest/launch
----------------------------------
package: com.huawei.deveco.crowdtest
name: com.huawei.activity.NotificationClickActivity
deeplink: crowdtest://com.huawei.deveco.crowdtest/notification
----------------------------------
++++++ End
Working...

++++++ JavascriptInterface:
Lcom/huawei/hwid/api/common/CloudAccountCenterActivity$JavaScriptLocalObj;

    public void intoApp(String p2)
    {
        com.huawei.hwid.core.d.b.e.b("CloudActivity", "enter intoApp");
        new android.os.Handler(this.a.getMainLooper()).post(new com.huawei.hwid.api.common.CloudAccountCenterActivity$JavaScriptLocalObj$1(this));
        return;
    }

----------------------------------
++++++ End
```