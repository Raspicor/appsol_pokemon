# module.PetApp.open_preset_editor._render_effect
# source line 15461
# Recovered from bytecode; default argument values are not shown.

def _render_effect():
    cat = state_box['category']
    customized = self._preset_is_customized(cat)
    dex_list = self._get_preset_dex_list(cat)

    try:
        atk_pct = ()
        def_pct = companion_synergy_bonus(dex_list, self.state.get('caught', { }), self.state.get('mega_party', []))
        if customized:
            effect_var.set(f'''{PRESET_CATEGORY_LABEL.get(cat, cat)}  (최대 {cap}마리, 현재 {len(dex_list)}마리)\n본체 공격 +{atk_pct:.1f}%   방어 +{def_pct:.1f}%   치명타 +{crit_pct:.1f}%''')
            return None
        self._preset_cap(cat).set(f'''{PRESET_CATEGORY_LABEL.get(cat, cat)}  (최대 {cap}마리)\n⚠ 아직 따로 설정 안 함 - 기본 세팅 동료({len(dex_list)}마리)로 대신 나가요\n본체 공격 +{atk_pct:.1f}%   방어 +{def_pct:.1f}%   치명타 +{crit_pct:.1f}%''')
        return None
    except Exception:
        crit_pct = 0
        def_pct = 0
        0 = None
        continue
