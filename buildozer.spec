[app]
title = Sons de Animais
package.name = sonsdeanimais
package.domain = org.sonsdeanimais_ByAdriano
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
orientation = portrait

# Requisitos para a compilação (simples e estável)
requirements = python3,kivy==2.2.1,sdl2,openssl,kivy_sdl2,sdl2_mixer,pyjnius,requests,certifi

# Configurações do Android
fullscreen = 0
android.api = 27
android.minapi = 21
android.ndk = 23b
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
# android.accept_sdk_license = True  # Pode ser útil se houver problema de licença

# Configurações do P4A
p4a.extra_args = --branch master

[buildozer]
log_level = 2
warn_on_root = 0
