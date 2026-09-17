# module.PetApp.open_pvp_lobby._install_websockets
# source line 17726
# Recovered from bytecode; default argument values are not shown.

def _install_websockets():
    try:
        cmd = 'start "PikaPet 온라인대결 설치" cmd /k "pip install websockets"'
        None(cmd, shell = True)
        return None
    except Exception:
        e = None
        None('PikaPet', f'''설치 창을 여는 데 실패했어요: {e}\n직접 cmd를 열고 아래를 입력해주세요:\npip install websockets''')
        e = None
        del e
        return None
        e = None
        del e
