APK parse3
=========

-  reference `androguard <https://github.com/androguard/androguard>`
-  reference `apk_parse <https://github.com/tdoly/apk_parse>`
-  REAL python3 support

## Example:

```

    apkf = APK("myfile.apk")
    apkf = APK(read("myfile.apk"), raw=True)
```

### app_name

Return the name of app or main activity


```

    >>> apkf.get_app_name()
    >>> apkf.get_app_name('zh')

```

### package

Return the name of the package

```

    >>> apkf.package
    com.android.vending

    >>> apkf.get_package()
    com.android.vending
```

### file_md5

Return the file md5 of the apk

```

    >>> apkf.file_md5
    40bdd920a3a3d2acf432e3c5b485eb11
```

### cert_md5

Return the cert md5 of the apk

```

    >>> apkf.get_cert_md5()
    ['5c7ea7e7479fc0bc10546b396d31b15d']
```

### cert_sha1

Return the cert sha1 of the apk

```

    >>> apkf.get_cert_sha1()
    ['61062655c4fcfc21d15d3917de515f88646c787f']
```

### file_size

Return the apk file size

```

    >>> apkf.file_size
    11194863
```

### androidversion

Return the apk version

```

    >>> apkf.androidversion
    {'Code': u'80341200', 'Name': u'5.4.12'}
```

### get_androidversion_code()

Return the android version code

```

    >>> apkf.get_androidversion_code()
    80341200
```

### get_androidversion_name()

Return the android version name

```

    >>> apkf.get_androidversion_name()
    5.4.12
```


### get_min_sdk_version()

Return the android:minSdkVersion attribute

```

    >>> apkf.get_min_sdk_version()
    9
```


### get_target_sdk_version()

Return the android:targetSdkVersion attribute

```

    >>> apkf.get_target_sdk_version()
    21
```

### get_libraries()

Return the android:name attributes for libraries

```

    >>> apkf.get_libraries()
    []
```

### get_files()

Return the files inside the APK

```

    >>> apkf.get_files()
    [u'AndroidManifest.xml', u'assets/keys/dcb-pin-encrypt-v1/1',...]
```

### get_files_types()

Return the files inside the APK with their associated types (by using python-magic)
Please `pip install python-magic`

```
    >>> apkf.get_files_types()
    {u'res/layout/play_card_bundle_item_small.xml': "Android's binary XML",...}
```


### get_main_activity()

Return the name of the main activity

```

    >>> apkf.get_main_activity()
    com.android.vending.AssetBrowserActivity
```

### get_activities()

Return the android:name attribute of all activities

```

    >>> apkf.get_activities()
    ['com.android.vending.AssetBrowserActivity', ...]
```

### get_services()

Return the android:name attribute of all services

```

    >>> apkf.get_services()
    ['com.android.vending.GCMIntentService', ...]
```

### get_receivers()

Return the android:name attribute of all receivers

```

    >>> apkf.get_receivers()
    ['com.google.android.gcm.GCMBroadcastReceiver', ...]
```


### get_providers()

Return the android:name attribute of all providers

```

    >>> apkf.get_providers()
    ['com.google.android.finsky.providers.RecentSuggestionsProvider', ...]
```

### get_permissions()

Return permissions

```

    >>> apkf.get_permissions()
    ['com.android.vending.permission.C2D_MESSAGE', ...]
```

### get_app_icon()

get ICON of the apk
Return the first non-greater density than max_dpi icon file name,
unless exact icon resolution is set in the manifest, in which case
return the exact file
```

    >>> apkf.get_app_icon()
    res/mipmap-xxhdpi-v4/ic_on.png
```

### show()

Return FILES, PERMISSIONS, MAIN ACTIVITY...
and certificates
```

    >>> apkf.show()
    FILES: ...
```
