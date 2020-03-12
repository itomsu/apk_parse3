#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys

sys.path.append(os.path.abspath(os.path.join('..')))

from apk_parse3.apk import APK


def test():
    apk_path = "/home/tomsu/BarcodeAdmin-v1.9.6-release2.apk"
    apkf = APK(apk_path)
    print('filename', apkf.get_filename())
    print('filesize', apkf.file_size)
    print('file md5', apkf.file_md5)
    print('cert md5', apkf.get_cert_md5())
    print('cert sha1', apkf.get_cert_sha1())
    print('cert sha256', apkf.get_cert_sha256())
    print('cert sha512', apkf.get_cert_sha512())
    print('android version', apkf.androidversion)
    print('package', apkf.package)
    print('app name', apkf.get_app_name())
    print('app name', apkf.get_app_name('zh'))
    print('is valid', apkf.is_valid_APK())
    print('package', apkf.get_package())
    print('version code', apkf.get_androidversion_code())
    print('version name', apkf.get_androidversion_name())
    print('max sdk', apkf.get_max_sdk_version())
    print('min sdk', apkf.get_min_sdk_version())
    print('target sdk', apkf.get_target_sdk_version())
    print('main activity', apkf.get_main_activity())
    print('signature name', apkf.get_signature_name())
    print('signature names', apkf.get_signature_names())
    print('-----------------------')
    #apkf.show()

    open('/tmp/'+apkf.package+'.icon', 'wb').write(apkf.get_file(apkf.get_app_icon()))

if __name__ == "__main__":
    test()
