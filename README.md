# realcat
APK静态分析工具
## 依赖
python3.7
```python
https://www.python.org/downloads/
```
androguard
```
pip install -U androguard[magic,GUI]
```
wget
```python
pip install wget
```
Ghidra
```
https://github.com/NationalSecurityAgency/ghidra
```
JDK11  
```
自行安装
```
## 安装
执行install.py，会自动下载解压GHIDRA工程
```python
python3 install.py
```
## 使用方法
```
RealCat [OPTION] -i <apkfile> -o [projectdir]
OPTION:
         -j: use GHIDRA to recompile so.
```
## 功能及使用示例
1.搜索APK的androidmanifest.xml中导出的组件  
2.检查DEX是否加壳，尝试找出webview注册的Javascript接口方法  
3.找出JNI方法，并使用Ghidra反编译成C

示例如下：  
```
python3 realcat.py -i "d:\apk\crowdtest\base.apk"
```
输出:  
```
++++++ Exported Components:
package: com.huawei.deveco.crowdtest
type: Component.Service
name: com.huawei.rfloat.top.TopMonitorService
----------------------------------
package: com.huawei.deveco.crowdtest
type: Component.Service
name: com.huawei.rfloat.top.TopAccessibilityService
permission: android.permission.BIND_ACCESSIBILITY_SERVICE
----------------------------------
package: com.huawei.deveco.crowdtest
type: Component.Activity
name: com.huawei.activity.PrivacyStatementActivity
permission: com.huawei.dataprivacycenter.permission.LAUNCH_APP_PRIVACY_STATEMENT
browsable: False
----------------------------------
package: com.huawei.deveco.crowdtest
type: Component.Activity
name: com.huawei.activity.PrivacyNoticeActivity
browsable: True
deeplink: crowdtest://com.huawei.deveco.crowdtest/launch
----------------------------------
package: com.huawei.deveco.crowdtest
type: Component.BroadcastReceiver
name: com.huawei.receiver.SDKCallLoginReceiver
----------------------------------
package: com.huawei.deveco.crowdtest
type: Component.Activity
name: com.huawei.activity.NotificationClickActivity
browsable: True
deeplink: crowdtest://com.huawei.deveco.crowdtest/notification
----------------------------------
package: com.huawei.deveco.crowdtest
type: Component.Service
name: com.baidu.location.f
----------------------------------
package: com.huawei.deveco.crowdtest
type: Component.Activity
name: com.huawei.activity.FloatMenuActivity
browsable: False
----------------------------------
package: com.huawei.deveco.crowdtest
type: Component.Activity
name: com.huawei.fastengine.fastview.download.download.DownloadActivity
browsable: False
----------------------------------
package: com.huawei.deveco.crowdtest
type: Component.Activity
name: com.huawei.fastengine.fastview.download.download.HiappDownloadActivity
browsable: False
----------------------------------
package: com.huawei.deveco.crowdtest
type: Component.Activity
name: com.zhihu.matisse.ui.MatisseActivity
browsable: False
----------------------------------
package: com.huawei.deveco.crowdtest
type: Component.Activity
name: com.zhihu.matisse.ui.MatisseForSmarttestActivity
browsable: False
----------------------------------
package: com.huawei.deveco.crowdtest
type: Component.Activity
name: com.zhihu.matisse.internal.ui.AlbumPreviewActivity
browsable: False
----------------------------------
package: com.huawei.deveco.crowdtest
type: Component.Activity
name: com.zhihu.matisse.internal.ui.SelectedPreviewActivity
browsable: False
----------------------------------
package: com.huawei.deveco.crowdtest
type: Component.Service
name: com.liulishuo.filedownloader.services.FileDownloadService$SharedMainProcessService
----------------------------------
package: com.huawei.deveco.crowdtest
type: Component.Service
name: com.liulishuo.filedownloader.services.FileDownloadService$SeparateProcessService
----------------------------------
package: com.huawei.deveco.crowdtest
type: Component.BroadcastReceiver
name: com.huawei.hms.support.api.push.PushMsgReceiver
permission: com.huawei.deveco.crowdtest.permission.PROCESS_PUSH_MSG
----------------------------------
package: com.huawei.deveco.crowdtest
type: Component.BroadcastReceiver
name: com.huawei.hms.support.api.push.PushReceiver
permission: com.huawei.deveco.crowdtest.permission.PROCESS_PUSH_MSG
----------------------------------
package: com.huawei.deveco.crowdtest
type: Component.Service
name: com.huawei.hms.support.api.push.service.HmsMsgService
----------------------------------
package: com.huawei.deveco.crowdtest
type: Component.ContentProvider
name: com.huawei.hms.support.api.push.PushProvider
permission: com.huawei.deveco.crowdtest.permission.PUSH_PROVIDER
----------------------------------
package: com.huawei.deveco.crowdtest
type: Component.Activity
name: com.huawei.hms.activity.EnableServiceActivity
browsable: False
----------------------------------
++++++ End
Working...

++++++ Native Methods:
Lcom/baidu/location/Jni; -> encrypt([B)[B
Lcom/baidu/location/Jni; -> b(D D I I)Ljava/lang/String;
Lcom/baidu/location/Jni; -> ib([B [B)Ljava/lang/String;
Lcom/baidu/location/Jni; -> a([B I)Ljava/lang/String;
Lcom/baidu/location/Jni; -> c([B I)Ljava/lang/String;
Lcom/baidu/location/Jni; -> murmur(Ljava/lang/String;)J
Lcom/baidu/location/Jni; -> encodeNotLimit(Ljava/lang/String; I)Ljava/lang/String;
Lcom/baidu/location/Jni; -> ee(Ljava/lang/String; I)Ljava/lang/String;
Lcom/baidu/location/Jni; -> sky()Ljava/lang/String;
Lcom/baidu/location/Jni; -> g([B)Ljava/lang/String;
Lcom/baidu/location/Jni; -> f([B [B)V
Lcom/baidu/platform/comapi/map/MapRenderer; -> nativeResize(J I I)V
Lcom/baidu/platform/comapi/map/MapRenderer; -> nativeRender(J)I
Lcom/baidu/platform/comapi/map/MapRenderer; -> nativeInit(J)V
Lcom/baidu/platform/comjni/engine/JNIEngine; -> initClass(Ljava/lang/Object; I)I
Lcom/baidu/platform/comjni/engine/JNIEngine; -> InitEngine(Landroid/content/Context; Landroid/os/Bundle;)Z
Lcom/baidu/platform/comjni/engine/JNIEngine; -> SetProxyInfo(Ljava/lang/String; I)V
Lcom/baidu/platform/comjni/engine/JNIEngine; -> StartSocketProc()Z
Lcom/baidu/platform/comjni/engine/JNIEngine; -> UnInitEngine()Z
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> MapProc(J I I I)I
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> SetMapCustomEnable(J Z)V
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> SetMapControlMode(J I)I
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> AddLayer(J I I Ljava/lang/String;)J
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> ScrPtToGeoPoint(J I I)Ljava/lang/String;
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> GetNearlyObjID(J J I I I)Ljava/lang/String;
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> OnSchcityGet(J Ljava/lang/String;)Ljava/lang/String;
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> ShowLayers(J J Z)V
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> SetMapStatus(J Landroid/os/Bundle;)V
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> SaveScreenToLocal(J Ljava/lang/String; Landroid/os/Bundle;)V
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> ShowSatelliteMap(J Z)V
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> addOverlayItems(J [Landroid/os/Bundle; I)V
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> Create()J
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> CreateDuplicate(J)J
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> SetCallback(J Lcom/baidu/platform/comjni/map/basemap/BaseMapCallback;)I
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> OnRecordReload(J I Z)Z
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> OnRecordStart(J I Z I)Z
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> LayersIsShow(J J)Z
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> SwitchBaseIndoorMapFloor(J Ljava/lang/String; Ljava/lang/String;)Z
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> Init(J Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; I I I I I I I)Z
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> OnRecordImport(J Z Z)Z
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> GetScreenBuf(J [I I I)[I
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> GeoPtToScrPoint(J I I)Ljava/lang/String;
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> UpdateLayers(J J)V
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> setMapStatusLimits(J Landroid/os/Bundle;)V
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> ShowHotMap(J Z)V
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> Release(J)I
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> OnRecordAdd(J I)Z
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> OnRecordRemove(J I Z)Z
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> OnRecordSuspend(J I Z I)Z
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> GetZoomToBound(J Landroid/os/Bundle;)F
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> OnRecordGetAt(J I)Ljava/lang/String;
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> ShowTrafficMap(J Z)V
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> cleanSDKTileDataCache(J J)Z
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> ClearLayer(J J)V
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> enableDrawHouseHeight(J Z)V
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> updateSDKTile(J Landroid/os/Bundle;)Z
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> getCompassPosition(J J)Ljava/lang/String;
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> OnPause(J)V
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> ShowBaseIndoorMap(J Z)V
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> addtileOverlay(J Landroid/os/Bundle;)Z
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> OnResume(J)V
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> addOneOverlayItem(J Landroid/os/Bundle;)V
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> OnBackground(J)V
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> updateOneOverlayItem(J Landroid/os/Bundle;)V
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> OnForeground(J)V
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> removeOneOverlayItem(J Landroid/os/Bundle;)V
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> ResetImageRes(J)V
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> GetMapStatus(J)Landroid/os/Bundle;
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> getMapStatusLimits(J)Landroid/os/Bundle;
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> getDrawingMapStatus(J)Landroid/os/Bundle;
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> GetBaiduHotMapCityInfo(J)Z
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> OnRecordGetAll(J)Ljava/lang/String;
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> OnHotcityGet(J)Ljava/lang/String;
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> PostStatInfo(J)V
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> isDrawHouseHeightEnable(J)Z
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> clearHeatMapLayerCache(J)V
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> getfocusedBaseIndoorMapInfo(J)Ljava/lang/String;
Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap; -> IsBaseIndoorMapMode(J)Z
Lcom/baidu/platform/comjni/map/commonmemcache/JNICommonMemCache; -> Create()J
Lcom/baidu/platform/comjni/map/commonmemcache/JNICommonMemCache; -> Init(J Landroid/os/Bundle;)V
Lcom/baidu/platform/comjni/map/commonmemcache/JNICommonMemCache; -> GetPhoneInfoUrl(J)Ljava/lang/String;
Lcom/baidu/platform/comjni/tools/JNITools; -> TransGeoStr2Pt(Ljava/lang/Object;)Z
Lcom/baidu/platform/comjni/tools/JNITools; -> CoordinateEncryptEx(F F Ljava/lang/String; Ljava/lang/Object;)Z
Lcom/baidu/platform/comjni/tools/JNITools; -> TransNodeStr2Pt(Ljava/lang/Object;)V
Lcom/baidu/platform/comjni/tools/JNITools; -> GetDistanceByMC(Ljava/lang/Object;)V
Lcom/baidu/platform/comjni/tools/JNITools; -> TransGeoStr2ComplexPt(Ljava/lang/Object;)Z
Lcom/baidu/platform/comjni/tools/JNITools; -> GetToken()Ljava/lang/String;
Lcom/baidu/platform/comjni/tools/JNITools; -> openLogEnable(Z I)V
Lcom/baidu/platform/comjni/util/JNIMD5; -> encodeUrlParamsValue(Ljava/lang/String;)Ljava/lang/String;
Lcom/baidu/platform/comjni/util/JNIMD5; -> getSignMD5String(Ljava/lang/String;)Ljava/lang/String;
Lcom/baidu/vi/VDeviceAPI; -> onNetworkStateChanged()V
Lcom/baidu/vi/VMsg; -> OnUserCommand1(I I I J)V
Lcom/facebook/jni/Countable; -> dispose()V
Lcom/facebook/jni/HybridData; -> resetNative()V
Lcom/facebook/jni/ThreadScopeSupport; -> runStdFunctionImpl(J)V
++++++ End

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
Report ./base.apk_9zVhQkxs.json generated.
```
同时生成一份json格式的报告base.apk_9zVhQkxs.json:
```json
{
    "BroadcastReceiver": [
        {
            "name": "com.huawei.receiver.SDKCallLoginReceiver"
        },
        {
            "name": "com.huawei.hms.support.api.push.PushMsgReceiver",
            "permission": "com.huawei.deveco.crowdtest.permission.PROCESS_PUSH_MSG"
        },
        {
            "name": "com.huawei.hms.support.api.push.PushReceiver",
            "permission": "com.huawei.deveco.crowdtest.permission.PROCESS_PUSH_MSG"
        }
    ],
    "ContentProvider": [
        {
            "name": "com.huawei.hms.support.api.push.PushProvider",
            "permission": "com.huawei.deveco.crowdtest.permission.PUSH_PROVIDER"
        }
    ],
    "JavascriptInterface": [
        {
            "class": "Lcom/huawei/hwid/api/common/CloudAccountCenterActivity$JavaScriptLocalObj;",
            "method": "intoApp(Ljava/lang/String;)V",
            "src_code": "\n    public void intoApp(String p2)\n    {\n        com.huawei.hwid.core.d.b.e.b(\"CloudActivity\", \"enter intoApp\");\n        new android.os.Handler(this.a.getMainLooper()).post(new com.huawei.hwid.api.common.CloudAccountCenterActivity$JavaScriptLocalObj$1(this));\n        return;\n    }\n"
        }
    ],
    "activity": [
        {
            "browsable": false,
            "name": "com.huawei.activity.PrivacyStatementActivity",
            "permission": "com.huawei.dataprivacycenter.permission.LAUNCH_APP_PRIVACY_STATEMENT"
        },
        {
            "browsable": true,
            "deeplinks": [
                [
                    "crowdtest://com.huawei.deveco.crowdtest/launch"
                ]
            ],
            "name": "com.huawei.activity.PrivacyNoticeActivity"
        },
        {
            "browsable": true,
            "deeplinks": [
                [
                    "crowdtest://com.huawei.deveco.crowdtest/notification"
                ]
            ],
            "name": "com.huawei.activity.NotificationClickActivity"
        },
        {
            "browsable": false,
            "name": "com.huawei.activity.FloatMenuActivity"
        },
        {
            "browsable": false,
            "name": "com.huawei.fastengine.fastview.download.download.DownloadActivity"
        },
        {
            "browsable": false,
            "name": "com.huawei.fastengine.fastview.download.download.HiappDownloadActivity"
        },
        {
            "browsable": false,
            "name": "com.zhihu.matisse.ui.MatisseActivity"
        },
        {
            "browsable": false,
            "name": "com.zhihu.matisse.ui.MatisseForSmarttestActivity"
        },
        {
            "browsable": false,
            "name": "com.zhihu.matisse.internal.ui.AlbumPreviewActivity"
        },
        {
            "browsable": false,
            "name": "com.zhihu.matisse.internal.ui.SelectedPreviewActivity"
        },
        {
            "browsable": false,
            "name": "com.huawei.hms.activity.EnableServiceActivity"
        }
    ],
    "jni_method": [
        {
            "address": "00104f40",
            "class": "Lcom/baidu/location/Jni;",
            "jni_lib": "liblocSDK6a.so",
            "method": "encrypt([B)[B",
            "src_code": "undefined8 Java_com_baidu_location_Jni_encrypt(long *param_1,undefined8 param_2,undefined8 param_3)\n\n{\n  int __edflag;\n  char *__block;\n  size_t sVar1;\n  undefined8 uVar2;\n  \n  __edflag = (**(code **)(*param_1 + 0x558))(param_1,param_3);\n  __block = (char *)(**(code **)(*param_1 + 0x5c0))(param_1,param_3,0);\n  encrypt(__block,__edflag);\n  sVar1 = strlen(__block);\n  uVar2 = (**(code **)(*param_1 + 0x580))(param_1,sVar1 & 0xffffffff);\n  (**(code **)(*param_1 + 0x680))(param_1,uVar2,0,sVar1 & 0xffffffff,__block);\n  (**(code **)(*param_1 + 0x600))(param_1,param_3,__block,0);\n  return uVar2;\n}\n\n"
        },
        {
            "address": "001048a0",
            "class": "Lcom/baidu/location/Jni;",
            "jni_lib": "liblocSDK6a.so",
            "method": "b(D D I I)Ljava/lang/String;",
            "src_code": "void Java_com_baidu_location_Jni_b\n               (double param_1,double param_2,long *param_3,undefined8 param_4,int param_5,\n               int param_6)\n\n{\n  long lVar1;\n  undefined8 *puVar2;\n  byte bVar3;\n  char *local_b8;\n  char *local_b0;\n  undefined8 local_a8 [17];\n  long local_20;\n  \n  bVar3 = 0;\n  local_b8 = (char *)0x0;\n  local_b0 = (char *)0x0;\n  local_20 = __stack_chk_guard;\n  if (param_5 == 0) {\n    C02209(param_1,param_2,(double *)&local_b8,(double *)&local_b0,param_6);\n  }\n  else {\n    if (param_5 == 1) {\n      C0220911(param_1,param_2,(double *)&local_b8,(double *)&local_b0,param_6);\n    }\n    else {\n      if (param_5 == 0xb) {\n        C84202(param_1,param_2,(double *)&local_b8,(double *)&local_b0,param_6);\n      }\n      else {\n        if (param_5 == 0xc) {\n          C09202(param_1,param_2,(double *)&local_b8,(double *)&local_b0,param_6);\n        }\n        else {\n          if (param_5 == 0xd) {\n            C0911202(param_1,param_2,(double *)&local_b8,(double *)&local_b0,param_6);\n          }\n          else {\n            if (param_5 == 0xf) {\n              C02209mc(param_1,param_2,(double *)&local_b8,(double *)&local_b0,param_6);\n            }\n            else {\n              if (param_5 == 0x10) {\n                C84203(param_1,param_2,(double *)&local_b8,(double *)&local_b0,param_6);\n              }\n            }\n          }\n        }\n      }\n    }\n  }\n  lVar1 = 0x10;\n  puVar2 = local_a8;\n  while (lVar1 != 0) {\n    lVar1 = lVar1 + -1;\n    *puVar2 = 0;\n    puVar2 = puVar2 + (ulong)bVar3 * 0x1ffffffffffffffe + 1;\n  }\n  sprintf(local_b8,local_b0,local_a8,\"%lf:%lf\");\n  (**(code **)(*param_3 + 0x538))(param_3,local_a8);\n  if (local_20 == __stack_chk_guard) {\n    return;\n  }\n                    // WARNING: Subroutine does not return\n  __stack_chk_fail();\n}\n\n"
        },
        {
            "address": "00104fe0",
            "class": "Lcom/baidu/location/Jni;",
            "jni_lib": "liblocSDK6a.so",
            "method": "ib([B [B)Ljava/lang/String;",
            "src_code": "undefined8 Java_com_baidu_location_Jni_ib(long *param_1,undefined8 param_2,long param_3)\n\n{\n  int iVar1;\n  long lVar2;\n  size_t __n;\n  undefined8 *puVar3;\n  void *__src;\n  undefined8 local_438 [129];\n  long local_30;\n  \n  lVar2 = 0x80;\n  local_30 = __stack_chk_guard;\n  puVar3 = local_438;\n  while (lVar2 != 0) {\n    lVar2 = lVar2 + -1;\n    *puVar3 = 0;\n    puVar3 = puVar3 + 1;\n  }\n  if (param_3 == 0) {\n    __n = 0;\n    __src = (void *)0x0;\n  }\n  else {\n    __src = (void *)(**(code **)(*param_1 + 0x5c0))(param_1,param_3,0);\n    iVar1 = (**(code **)(*param_1 + 0x558))(param_1,param_3);\n    __n = SEXT48(iVar1);\n  }\n  memcpy(local_438,__src,__n);\n  (**(code **)(*param_1 + 0x600))(param_1,param_3,__src,0);\n  if (local_30 == __stack_chk_guard) {\n    return 0;\n  }\n                    // WARNING: Subroutine does not return\n  __stack_chk_fail();\n}\n\n"
        },
        {
            "address": "00104790",
            "class": "Lcom/baidu/location/Jni;",
            "jni_lib": "liblocSDK6a.so",
            "method": "a([B I)Ljava/lang/String;",
            "src_code": "void Java_com_baidu_location_Jni_a(long *param_1,undefined8 param_2,long param_3,int param_4)\n\n{\n  int iVar1;\n  long lVar2;\n  size_t __n;\n  undefined8 *puVar3;\n  void *__src;\n  undefined8 local_848 [128];\n  undefined8 local_448 [129];\n  long local_40;\n  \n  lVar2 = 0x80;\n  local_40 = __stack_chk_guard;\n  puVar3 = local_848;\n  while (lVar2 != 0) {\n    lVar2 = lVar2 + -1;\n    *puVar3 = 0;\n    puVar3 = puVar3 + 1;\n  }\n  lVar2 = 0x80;\n  puVar3 = local_448;\n  while (lVar2 != 0) {\n    lVar2 = lVar2 + -1;\n    *puVar3 = 0;\n    puVar3 = puVar3 + 1;\n  }\n  if (param_3 == 0) {\n    __n = 0;\n    __src = (void *)0x0;\n  }\n  else {\n    __src = (void *)(**(code **)(*param_1 + 0x5c0))(param_1,param_3,0);\n    iVar1 = (**(code **)(*param_1 + 0x558))(param_1,param_3);\n    __n = SEXT48(iVar1);\n  }\n  memcpy(local_848,__src,__n);\n  encode((char *)local_448,(char *)local_848,param_4);\n  (**(code **)(*param_1 + 0x600))(param_1,param_3,__src,0);\n  (**(code **)(*param_1 + 0x538))(param_1,local_448);\n  if (local_40 == __stack_chk_guard) {\n    return;\n  }\n                    // WARNING: Subroutine does not return\n  __stack_chk_fail();\n}\n\n"
        },
        {
            "address": "00104a70",
            "class": "Lcom/baidu/location/Jni;",
            "jni_lib": "liblocSDK6a.so",
            "method": "c([B I)Ljava/lang/String;",
            "src_code": "void Java_com_baidu_location_Jni_c(long *param_1,undefined8 param_2,long param_3,int param_4)\n\n{\n  int iVar1;\n  long lVar2;\n  size_t __n;\n  undefined8 *puVar3;\n  void *__src;\n  undefined8 local_248 [32];\n  undefined8 local_148 [33];\n  long local_40;\n  \n  lVar2 = 0x20;\n  local_40 = __stack_chk_guard;\n  puVar3 = local_248;\n  while (lVar2 != 0) {\n    lVar2 = lVar2 + -1;\n    *puVar3 = 0;\n    puVar3 = puVar3 + 1;\n  }\n  lVar2 = 0x20;\n  puVar3 = local_148;\n  while (lVar2 != 0) {\n    lVar2 = lVar2 + -1;\n    *puVar3 = 0;\n    puVar3 = puVar3 + 1;\n  }\n  if (param_3 == 0) {\n    __n = 0;\n    __src = (void *)0x0;\n  }\n  else {\n    __src = (void *)(**(code **)(*param_1 + 0x5c0))(param_1,param_3,0);\n    iVar1 = (**(code **)(*param_1 + 0x558))(param_1,param_3);\n    __n = SEXT48(iVar1);\n  }\n  memcpy(local_248,__src,__n);\n  encode2((char *)local_148,(uchar *)local_248,param_4);\n  (**(code **)(*param_1 + 0x600))(param_1,param_3,__src,0);\n  (**(code **)(*param_1 + 0x538))(param_1,local_148);\n  if (local_40 == __stack_chk_guard) {\n    return;\n  }\n                    // WARNING: Subroutine does not return\n  __stack_chk_fail();\n}\n\n"
        },
        {
            "address": "00104580",
            "class": "Lcom/baidu/location/Jni;",
            "jni_lib": "liblocSDK6a.so",
            "method": "murmur(Ljava/lang/String;)J",
            "src_code": "undefined8 Java_com_baidu_location_Jni_murmur(long *param_1,undefined8 param_2,undefined8 param_3)\n\n{\n  char *__s;\n  size_t sVar1;\n  undefined8 local_30 [2];\n  \n  __s = (char *)(**(code **)(*param_1 + 0x548))(param_1,param_3,0);\n  sVar1 = strlen(__s);\n  uln_sign_murmur2_64(__s,sVar1,(long_long *)local_30);\n  (**(code **)(*param_1 + 0x550))(param_1,param_3,__s);\n  return local_30[0];\n}\n\n"
        },
        {
            "address": "001045f0",
            "class": "Lcom/baidu/location/Jni;",
            "jni_lib": "liblocSDK6a.so",
            "method": "encodeNotLimit(Ljava/lang/String; I)Ljava/lang/String;",
            "src_code": "undefined8\nJava_com_baidu_location_Jni_encodeNotLimit\n          (long *param_1,undefined8 param_2,undefined8 param_3,int param_4)\n\n{\n  char *__s;\n  size_t sVar1;\n  ulong uVar2;\n  char *__ptr;\n  undefined8 uVar3;\n  double dVar4;\n  \n  __s = (char *)(**(code **)(*param_1 + 0x548))(param_1,param_3,0);\n  sVar1 = strlen(__s);\n  uVar2 = sVar1 + 5;\n  if ((long)uVar2 < 0) {\n    dVar4 = (double)(uVar2 >> 1 | (ulong)((uint)uVar2 & 1));\n    dVar4 = dVar4 + dVar4;\n  }\n  else {\n    dVar4 = (double)uVar2;\n  }\n  __ptr = (char *)malloc((long)((int)(dVar4 * 1.40000000) + 1));\n  uVar3 = encode(__ptr,__s,param_4);\n  uVar3 = (**(code **)(*param_1 + 0x538))(param_1,uVar3);\n  (**(code **)(*param_1 + 0x550))(param_1,param_3,__s);\n  free(__ptr);\n  return uVar3;\n}\n\n"
        },
        {
            "address": "001046c0",
            "class": "Lcom/baidu/location/Jni;",
            "jni_lib": "liblocSDK6a.so",
            "method": "ee(Ljava/lang/String; I)Ljava/lang/String;",
            "src_code": "undefined8\nJava_com_baidu_location_Jni_ee(long *param_1,undefined8 param_2,undefined8 param_3,int param_4)\n\n{\n  char *__s;\n  size_t sVar1;\n  ulong uVar2;\n  char *__ptr;\n  undefined8 uVar3;\n  double dVar4;\n  \n  __s = (char *)(**(code **)(*param_1 + 0x548))(param_1,param_3,0);\n  sVar1 = strlen(__s);\n  uVar2 = sVar1 + 5;\n  if ((long)uVar2 < 0) {\n    dVar4 = (double)(uVar2 >> 1 | (ulong)((uint)uVar2 & 1));\n    dVar4 = dVar4 + dVar4;\n  }\n  else {\n    dVar4 = (double)uVar2;\n  }\n  __ptr = (char *)malloc((long)((int)(dVar4 * 1.40000000) + 1));\n  uVar3 = encode4(__ptr,__s,param_4);\n  uVar3 = (**(code **)(*param_1 + 0x538))(param_1,uVar3);\n  (**(code **)(*param_1 + 0x550))(param_1,param_3,__s);\n  free(__ptr);\n  return uVar3;\n}\n\n"
        },
        {
            "address": "00104480",
            "class": "Lcom/baidu/location/Jni;",
            "jni_lib": "liblocSDK6a.so",
            "method": "sky()Ljava/lang/String;",
            "src_code": "void Java_com_baidu_location_Jni_sky(long *param_1)\n\n{\n  long lVar1;\n  undefined8 *puVar2;\n  undefined8 local_98;\n  undefined8 local_90;\n  undefined8 local_88;\n  undefined8 local_80;\n  undefined8 local_78;\n  undefined8 local_70;\n  undefined8 local_68;\n  undefined8 local_60;\n  undefined8 local_58;\n  undefined8 local_50;\n  undefined8 local_48 [7];\n  long local_10;\n  \n  lVar1 = 6;\n  local_50 = 0x674e;\n  local_10 = __stack_chk_guard;\n  local_98 = 0x4f73557756774a65;\n  local_90 = 0x314363424d414241;\n  local_88 = 0x74666f3652547a77;\n  local_80 = 0x6d3569376c387951;\n  local_78 = 0x4b50457839444875;\n  local_70 = 0x685161786a525453;\n  local_68 = 0x6b4a6759336a304d;\n  local_60 = 0x36556a376d2d6355;\n  local_58 = 0x4c38794544347530;\n  puVar2 = local_48;\n  while (lVar1 != 0) {\n    lVar1 = lVar1 + -1;\n    *puVar2 = 0;\n    puVar2 = puVar2 + 1;\n  }\n  (**(code **)(*param_1 + 0x538))(param_1,&local_98);\n  if (local_10 == __stack_chk_guard) {\n    return;\n  }\n                    // WARNING: Subroutine does not return\n  __stack_chk_fail();\n}\n\n"
        },
        {
            "address": "00104b80",
            "class": "Lcom/baidu/location/Jni;",
            "jni_lib": "liblocSDK6a.so",
            "method": "g([B)Ljava/lang/String;",
            "src_code": "void Java_com_baidu_location_Jni_g(long *param_1,undefined8 param_2,long param_3)\n\n{\n  byte bVar1;\n  char cVar2;\n  int iVar3;\n  undefined8 *puVar4;\n  undefined8 *puVar5;\n  uint uVar6;\n  uint uVar7;\n  long lVar8;\n  size_t __n;\n  void *__src;\n  bool bVar9;\n  undefined8 local_598 [32];\n  undefined8 local_498 [139];\n  long local_40;\n  \n  lVar8 = 0x89;\n  local_40 = __stack_chk_guard;\n  puVar5 = local_498;\n  while (lVar8 != 0) {\n    lVar8 = lVar8 + -1;\n    *puVar5 = 0;\n    puVar5 = puVar5 + 1;\n  }\n  *(undefined4 *)puVar5 = 0;\n  lVar8 = 0x20;\n  puVar5 = local_598;\n  while (lVar8 != 0) {\n    lVar8 = lVar8 + -1;\n    *puVar5 = 0;\n    puVar5 = puVar5 + 1;\n  }\n  if (param_3 == 0) {\n    __n = 0;\n    __src = (void *)0x0;\n  }\n  else {\n    __src = (void *)(**(code **)(*param_1 + 0x5c0))(param_1,param_3,0);\n    iVar3 = (**(code **)(*param_1 + 0x558))(param_1,param_3);\n    __n = SEXT48(iVar3);\n  }\n  memcpy(local_598,__src,__n);\n  puVar5 = local_598;\n  do {\n    puVar4 = puVar5;\n    uVar6 = *(uint *)puVar4 + 0xfefefeff & ~*(uint *)puVar4;\n    uVar7 = uVar6 & 0x80808080;\n    puVar5 = (undefined8 *)((long)puVar4 + 4);\n  } while (uVar7 == 0);\n  bVar9 = (uVar6 & 0x8080) == 0;\n  bVar1 = (byte)uVar7;\n  if (bVar9) {\n    bVar1 = (byte)(uVar7 >> 0x10);\n  }\n  if (bVar9) {\n    puVar5 = (undefined8 *)((long)puVar4 + 6);\n  }\n  puVar5 = (undefined8 *)((long)puVar5 + (-3 - (ulong)CARRY1(bVar1,bVar1)));\n  *puVar5 = 0x742f75646961622f;\n  puVar5[1] = 0x2f61746164706d65;\n  *(undefined4 *)(puVar5 + 2) = 0x2e646c67;\n  *(undefined2 *)((long)puVar5 + 0x14) = 0x6164;\n  *(undefined *)((long)puVar5 + 0x16) = 0x74;\n  (**(code **)(*param_1 + 0x600))(param_1,param_3,__src,0);\n  cVar2 = gtr2((char *)local_598,(char *)local_498);\n  if (cVar2 == '\\0') {\n    (**(code **)(*param_1 + 0x538))(param_1,&DAT_0010a2c8);\n  }\n  else {\n    (**(code **)(*param_1 + 0x538))(param_1,local_498);\n  }\n  if (local_40 == __stack_chk_guard) {\n    return;\n  }\n                    // WARNING: Subroutine does not return\n  __stack_chk_fail();\n}\n\n"
        },
        {
            "address": "00104d30",
            "class": "Lcom/baidu/location/Jni;",
            "jni_lib": "liblocSDK6a.so",
            "method": "f([B [B)V",
            "src_code": "void Java_com_baidu_location_Jni_f(long *param_1,undefined8 param_2,long param_3,long param_4)\n\n{\n  byte bVar1;\n  int iVar2;\n  uint uVar3;\n  long lVar4;\n  size_t __n;\n  undefined8 *puVar5;\n  undefined8 *puVar6;\n  void *__src;\n  bool bVar7;\n  void *local_880;\n  size_t local_870;\n  undefined8 local_848 [128];\n  undefined8 local_448 [129];\n  long local_40;\n  \n  lVar4 = 0x80;\n  local_40 = __stack_chk_guard;\n  puVar6 = local_848;\n  while (lVar4 != 0) {\n    lVar4 = lVar4 + -1;\n    *puVar6 = 0;\n    puVar6 = puVar6 + 1;\n  }\n  lVar4 = 0x80;\n  puVar6 = local_448;\n  while (lVar4 != 0) {\n    lVar4 = lVar4 + -1;\n    *puVar6 = 0;\n    puVar6 = puVar6 + 1;\n  }\n  if (param_3 == 0) {\n    __n = 0;\n    __src = (void *)0x0;\n  }\n  else {\n    __src = (void *)(**(code **)(*param_1 + 0x5c0))(param_1,param_3,0);\n    iVar2 = (**(code **)(*param_1 + 0x558))(param_1,param_3);\n    __n = SEXT48(iVar2);\n  }\n  if (param_4 == 0) {\n    local_870 = 0;\n    local_880 = (void *)0x0;\n  }\n  else {\n    local_880 = (void *)(**(code **)(*param_1 + 0x5c0))(param_1,param_4,0);\n    iVar2 = (**(code **)(*param_1 + 0x558))(param_1,param_4);\n    local_870 = SEXT48(iVar2);\n  }\n  memcpy(local_848,__src,__n);\n  puVar6 = local_848;\n  do {\n    puVar5 = puVar6;\n    uVar3 = *(uint *)puVar5 + 0xfefefeff & ~*(uint *)puVar5;\n    _bVar1 = uVar3 & 0x80808080;\n    bVar1 = (byte)_bVar1;\n    puVar6 = (undefined8 *)((long)puVar5 + 4);\n  } while (_bVar1 == 0);\n  bVar7 = (uVar3 & 0x8080) == 0;\n  if (bVar7) {\n    bVar1 = (byte)(_bVar1 >> 0x10);\n  }\n  if (bVar7) {\n    puVar6 = (undefined8 *)((long)puVar5 + 6);\n  }\n  puVar6 = (undefined8 *)((long)puVar6 + (-3 - (ulong)CARRY1(bVar1,bVar1)));\n  *puVar6 = 0x742f75646961622f;\n  puVar6[1] = 0x2f61746164706d65;\n  *(undefined4 *)(puVar6 + 2) = 0x2e646c67;\n  *(undefined2 *)((long)puVar6 + 0x14) = 0x6164;\n  *(undefined *)((long)puVar6 + 0x16) = 0x74;\n  memcpy(local_448,local_880,local_870);\n  tr2((uchar *)local_848,(uchar *)local_448);\n  (**(code **)(*param_1 + 0x600))(param_1,param_3,__src,0);\n  (**(code **)(*param_1 + 0x600))(param_1,param_4,local_880,0);\n  if (local_40 != __stack_chk_guard) {\n                    // WARNING: Subroutine does not return\n    __stack_chk_fail();\n  }\n  return;\n}\n\n"
        },
        {
            "class": "Lcom/baidu/platform/comapi/map/MapRenderer;",
            "method": "nativeResize(J I I)V"
        },
        {
            "class": "Lcom/baidu/platform/comapi/map/MapRenderer;",
            "method": "nativeRender(J)I"
        },
        {
            "class": "Lcom/baidu/platform/comapi/map/MapRenderer;",
            "method": "nativeInit(J)V"
        },
        {
            "class": "Lcom/baidu/platform/comjni/engine/JNIEngine;",
            "method": "initClass(Ljava/lang/Object; I)I"
        },
        {
            "class": "Lcom/baidu/platform/comjni/engine/JNIEngine;",
            "method": "InitEngine(Landroid/content/Context; Landroid/os/Bundle;)Z"
        },
        {
            "class": "Lcom/baidu/platform/comjni/engine/JNIEngine;",
            "method": "SetProxyInfo(Ljava/lang/String; I)V"
        },
        {
            "class": "Lcom/baidu/platform/comjni/engine/JNIEngine;",
            "method": "StartSocketProc()Z"
        },
        {
            "class": "Lcom/baidu/platform/comjni/engine/JNIEngine;",
            "method": "UnInitEngine()Z"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "MapProc(J I I I)I"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "SetMapCustomEnable(J Z)V"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "SetMapControlMode(J I)I"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "AddLayer(J I I Ljava/lang/String;)J"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "ScrPtToGeoPoint(J I I)Ljava/lang/String;"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "GetNearlyObjID(J J I I I)Ljava/lang/String;"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "OnSchcityGet(J Ljava/lang/String;)Ljava/lang/String;"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "ShowLayers(J J Z)V"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "SetMapStatus(J Landroid/os/Bundle;)V"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "SaveScreenToLocal(J Ljava/lang/String; Landroid/os/Bundle;)V"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "ShowSatelliteMap(J Z)V"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "addOverlayItems(J [Landroid/os/Bundle; I)V"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "Create()J"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "CreateDuplicate(J)J"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "SetCallback(J Lcom/baidu/platform/comjni/map/basemap/BaseMapCallback;)I"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "OnRecordReload(J I Z)Z"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "OnRecordStart(J I Z I)Z"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "LayersIsShow(J J)Z"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "SwitchBaseIndoorMapFloor(J Ljava/lang/String; Ljava/lang/String;)Z"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "Init(J Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; I I I I I I I)Z"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "OnRecordImport(J Z Z)Z"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "GetScreenBuf(J [I I I)[I"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "GeoPtToScrPoint(J I I)Ljava/lang/String;"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "UpdateLayers(J J)V"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "setMapStatusLimits(J Landroid/os/Bundle;)V"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "ShowHotMap(J Z)V"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "Release(J)I"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "OnRecordAdd(J I)Z"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "OnRecordRemove(J I Z)Z"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "OnRecordSuspend(J I Z I)Z"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "GetZoomToBound(J Landroid/os/Bundle;)F"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "OnRecordGetAt(J I)Ljava/lang/String;"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "ShowTrafficMap(J Z)V"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "cleanSDKTileDataCache(J J)Z"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "ClearLayer(J J)V"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "enableDrawHouseHeight(J Z)V"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "updateSDKTile(J Landroid/os/Bundle;)Z"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "getCompassPosition(J J)Ljava/lang/String;"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "OnPause(J)V"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "ShowBaseIndoorMap(J Z)V"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "addtileOverlay(J Landroid/os/Bundle;)Z"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "OnResume(J)V"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "addOneOverlayItem(J Landroid/os/Bundle;)V"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "OnBackground(J)V"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "updateOneOverlayItem(J Landroid/os/Bundle;)V"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "OnForeground(J)V"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "removeOneOverlayItem(J Landroid/os/Bundle;)V"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "ResetImageRes(J)V"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "GetMapStatus(J)Landroid/os/Bundle;"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "getMapStatusLimits(J)Landroid/os/Bundle;"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "getDrawingMapStatus(J)Landroid/os/Bundle;"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "GetBaiduHotMapCityInfo(J)Z"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "OnRecordGetAll(J)Ljava/lang/String;"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "OnHotcityGet(J)Ljava/lang/String;"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "PostStatInfo(J)V"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "isDrawHouseHeightEnable(J)Z"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "clearHeatMapLayerCache(J)V"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "getfocusedBaseIndoorMapInfo(J)Ljava/lang/String;"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/basemap/JNIBaseMap;",
            "method": "IsBaseIndoorMapMode(J)Z"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/commonmemcache/JNICommonMemCache;",
            "method": "Create()J"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/commonmemcache/JNICommonMemCache;",
            "method": "Init(J Landroid/os/Bundle;)V"
        },
        {
            "class": "Lcom/baidu/platform/comjni/map/commonmemcache/JNICommonMemCache;",
            "method": "GetPhoneInfoUrl(J)Ljava/lang/String;"
        },
        {
            "class": "Lcom/baidu/platform/comjni/tools/JNITools;",
            "method": "TransGeoStr2Pt(Ljava/lang/Object;)Z"
        },
        {
            "class": "Lcom/baidu/platform/comjni/tools/JNITools;",
            "method": "CoordinateEncryptEx(F F Ljava/lang/String; Ljava/lang/Object;)Z"
        },
        {
            "class": "Lcom/baidu/platform/comjni/tools/JNITools;",
            "method": "TransNodeStr2Pt(Ljava/lang/Object;)V"
        },
        {
            "class": "Lcom/baidu/platform/comjni/tools/JNITools;",
            "method": "GetDistanceByMC(Ljava/lang/Object;)V"
        },
        {
            "class": "Lcom/baidu/platform/comjni/tools/JNITools;",
            "method": "TransGeoStr2ComplexPt(Ljava/lang/Object;)Z"
        },
        {
            "class": "Lcom/baidu/platform/comjni/tools/JNITools;",
            "method": "GetToken()Ljava/lang/String;"
        },
        {
            "class": "Lcom/baidu/platform/comjni/tools/JNITools;",
            "method": "openLogEnable(Z I)V"
        },
        {
            "class": "Lcom/baidu/platform/comjni/util/JNIMD5;",
            "method": "encodeUrlParamsValue(Ljava/lang/String;)Ljava/lang/String;"
        },
        {
            "class": "Lcom/baidu/platform/comjni/util/JNIMD5;",
            "method": "getSignMD5String(Ljava/lang/String;)Ljava/lang/String;"
        },
        {
            "class": "Lcom/baidu/vi/VDeviceAPI;",
            "method": "onNetworkStateChanged()V"
        },
        {
            "class": "Lcom/baidu/vi/VMsg;",
            "method": "OnUserCommand1(I I I J)V"
        },
        {
            "class": "Lcom/facebook/jni/Countable;",
            "method": "dispose()V"
        },
        {
            "class": "Lcom/facebook/jni/HybridData;",
            "method": "resetNative()V"
        },
        {
            "class": "Lcom/facebook/jni/ThreadScopeSupport;",
            "method": "runStdFunctionImpl(J)V"
        }
    ],
    "package_name": "com.huawei.deveco.crowdtest",
    "service": [
        {
            "name": "com.huawei.rfloat.top.TopMonitorService"
        },
        {
            "name": "com.huawei.rfloat.top.TopAccessibilityService",
            "permission": "android.permission.BIND_ACCESSIBILITY_SERVICE"
        },
        {
            "name": "com.baidu.location.f"
        },
        {
            "name": "com.liulishuo.filedownloader.services.FileDownloadService$SharedMainProcessService"
        },
        {
            "name": "com.liulishuo.filedownloader.services.FileDownloadService$SeparateProcessService"
        },
        {
            "name": "com.huawei.hms.support.api.push.service.HmsMsgService"
        }
    ]
}
```
