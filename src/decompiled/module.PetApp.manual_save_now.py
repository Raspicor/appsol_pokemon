# module.PetApp.manual_save_now
# source line 4890
# Recovered from bytecode; default argument values are not shown.

def manual_save_now(self):
    ok = save_state_to_disk(self.state)
    if ok:
        None('저장 완료', f'''✅ 지금 상태가 확실하게 저장됐어요!\n컴퓨터를 끄거나 프로그램을 종료한 뒤 다시 켜도 이 상태 그대로 이어져요.\n\n저장 위치: {STATE_PATH}''')
        return None
    None('저장 실패 - 확인해주세요', f'''⚠ 저장이 안 됐어요! 아래를 확인해주세요.\n\n예상되는 원인:\n· 윈도우 보안 > 바이러스 및 위협 방지 > \'랜섬웨어 방지\'의\n   \'제어된 폴더 접근\'이 이 프로그램의 파일 쓰기를 막고 있을 수 있어요\n   (꺼주시거나, 이 프로그램을 허용 앱 목록에 추가해주세요)\n· 백신 프로그램이 저장을 차단하고 있을 수 있어요\n\n저장 위치: {STATE_PATH}\n이 폴더에 이 프로그램이 파일을 쓸 수 있는지 확인해주세요.''')
