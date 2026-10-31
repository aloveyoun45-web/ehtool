[app]
title = EH Tool
package.name = ehtool
package.domain = com.ehtool.app
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True
android.build_tools_version = 34.0.0

[buildozer]
log_level = 2

[app:android]
archs = arm64-v8a, armeabi-v7a
