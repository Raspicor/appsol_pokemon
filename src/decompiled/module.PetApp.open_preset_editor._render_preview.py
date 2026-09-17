# module.PetApp.open_preset_editor._render_preview
# source line 15312
# Recovered from bytecode; default argument values are not shown.

def _render_preview():
    dex = state_box['pending_dex']
    if dex is None:
        preview_img_label.configure(image = '')
        preview_photo_cache.clear()
        preview_name_var.set('포켓몬을 누르면 여기에 미리보기가 나와요.')
        return None
    e = None.get(dex, { })
    lv = self.state.get('caught', { }).get(str(dex), { }).get('level', 1)
    img = None(dex, 48)
    photo = None(img)
    preview_photo_cache.clear()
    preview_photo_cache.append(photo)
    preview_img_label.configure(image = photo)
    preview_name_var.set(f'''👉 \'{e.get('kr', '?')}\' Lv.{lv} 선택됨 - 오른쪽 슬롯 칸을 클릭하면 그 자리에 장착돼요. (다시 누르면 선택 취소)''')
