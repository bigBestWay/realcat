# realcat
APK静态分析工具
## 安装依赖
androguard
```
pip install -U androguard[magic,GUI]
```
## 使用方法
```
python3 realcat.py <apkfile> [project dir]
```
## 功能及使用示例
1.搜索APK的androidmanifest.xml中导出的组件  
2.检查DEX是否加壳，尝试找出webview注册的Javascript接口方法  
3.找出JNI方法

示例如下：  
```
python3 realcat.py "d:\apk\crowdtest\base.apk"
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
