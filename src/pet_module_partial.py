# Source Generated with Decompyle++
# File: pet_hdr.pyc (Python 3.14)

'''
PikaPet - 데스크탑 포켓몬 펫 (도감/포획/전투/동료 시너지 확장판 v2)
'''
import os
import sys
import json
import math
import colorsys
import base64
import random
import shutil
import time
import threading
import queue
import asyncio
import subprocess
import webbrowser
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont
import spriteanim
import winlayer
if None(sys, 'frozen', False):
    RUNTIME_DIR = os.path.dirname(os.path.abspath(sys.executable))
    RESOURCE_DIR = None(sys, '_MEIPASS', RUNTIME_DIR)
    if not os.environ.get('APPDATA'):
        os.environ.get('APPDATA')
    _appdata = RUNTIME_DIR
    SAVE_DIR = os.path.join(_appdata, 'PikaPet')
    
    try:
        None(SAVE_DIR, exist_ok = True)
    RUNTIME_DIR = os.path.dirname(os.path.abspath(__file__))
    RESOURCE_DIR = RUNTIME_DIR
    SAVE_DIR = RUNTIME_DIR
    BASE_DIR = RUNTIME_DIR
    SPRITE_DIR = os.path.join(RESOURCE_DIR, 'assets', 'sprites')
    STATE_PATH = os.path.join(SAVE_DIR, 'pet_state.json')
    POKEDEX_PATH = os.path.join(RESOURCE_DIR, 'assets', 'pokedex_data_v2.json')
    if not os.environ.get('LOCALAPPDATA'):
        os.environ.get('LOCALAPPDATA')

_local_appdata = RUNTIME_DIR
SECONDARY_SAVE_DIR = os.path.join(_local_appdata, 'PikaPet')

try:
    None(SECONDARY_SAVE_DIR, exist_ok = True)
    SECONDARY_STATE_PATH = os.path.join(SECONDARY_SAVE_DIR, 'pet_state.json')
    if SAVE_DIR != RUNTIME_DIR:
        
        try:
            if not os.path.exists(STATE_PATH):
                
                try:
                    _legacy_candidates = [
                        os.path.join(RUNTIME_DIR, 'pet_state.json'),
                        os.path.join(os.path.dirname(RUNTIME_DIR), 'pet_state.json')]
                    for None in :
                        if not os.path.exists(p):
                            continue
                    
                    try:
                        p, _found = , [], 
                        if _found:
                            
                            try:
                                _best = None(_found, key = (lambda p: os.path.getmtime(p)))
                                None(_best, STATE_PATH)
                                SPRITE_SEARCH_DIRS = [
                                    SPRITE_DIR,
                                    os.path.join(RESOURCE_DIR, 'assets_v3', 'assets', 'sprites'),
                                    os.path.join(RESOURCE_DIR, 'assets_v3', 'assets_mega', 'sprites'),
                                    os.path.join(RESOURCE_DIR, 'assets_v3', 'sprites'),
                                    os.path.join(RESOURCE_DIR, 'assets_v4', 'assets', 'sprites')]
                                
                                def sprite_folder_path(name):
                                    '''스프라이트 폴더의 실제 전체 경로를 찾아서 돌려준다. SPRITE_SEARCH_DIRS를 순서대로
뒤져서 그 이름의 폴더가 실제로 있는 첫 번째 위치를 쓰고, 어디에도 없으면(아직 그림이
없는 경우) 기본 assets/sprites 경로를 그대로 돌려준다(호출부에서 실패 처리하게 됨).'''
                                    for base in SPRITE_SEARCH_DIRS:
                                        p = os.path.join(base, name)
                                        if not os.path.isdir(p):
                                            continue
                                        
                                        return SPRITE_SEARCH_DIRS, p
                                    return os.path.join(SPRITE_DIR, name)

                                MAGIC = '#ff00ff'
                                TICK_MS = 50
                                ANIM_TICK_MS = 40
                                GROUND_MARGIN = 46
                                WALK_SPEED = 55
                                DRAG_THRESHOLD_PX = 6
                                FALL_GRAVITY = 1500
                                FALL_MAX_SPEED = 1900
                                KB_JUMP_VELOCITY_SINGLE = -505
                                KB_JUMP_VELOCITY_DOUBLE = -720
                                KB_MAX_AIR_JUMPS = 2
                                KB_AIR_MOVE_MULT = 2.1
                                KB_CLIMB_SPEED = 65
                                DAILY_QUOTA = 10
                                BASE_PASSIVE_DAYS = 7
                                BASE_QUOTA_DAYS = 4
                                COMPANION_EVOLVE_DAYS_BY_TIER = {
                                    2: 15,
                                    1: 7 }
                                COMPANION_EVOLVE_SLOWDOWN = 1
                                COMPANION_EVOLVE_EXCLUDE = {
                                    265,
                                    290,
                                    236}
                                EEVEE_BASE_DEX = 133
                                COMPANION_EVOLVE_OVERRIDE = { }[198][200][438][439][440][446][458][173][174][238][239][240][298][360][215][433]
                                for None in :
                                    k = ()
                                    v = None
                                
                                v, k, REVERSE_COMPANION_EVOLVE_OVERRIDE = { }[198][200][438][439][440][446][458][173][174][238][239][240][298][360][215], COMPANION_EVOLVE_OVERRIDE.items(), k, v, , { }
                                COMPANION_LEVEL_UP_BASE_DAYS = 3
                                COMPANION_LEVEL_UP_STAGE_MULT = 1.6
                                EEVEE_DEX_SET = {
                                    133,
                                    134,
                                    135,
                                    136,
                                    196,
                                    197}
                                EEVEE_BRANCH_BY_DEX = {
                                    197: 'dark',
                                    196: 'psychic',
                                    136: 'fire',
                                    135: 'electric',
                                    134: 'water' }
                                
                                def evolution_chain_for_dex(d):
                                    '''(이브이 계열 제외) 이 도감번호가 속한 진화 라인 전체를 [1단계, 2단계, ...] 순서의
도감번호 리스트로 재구성한다. 역추적/순추적 도중 어긋나면 안전하게 자기 자신만 담아 돌려준다.'''
                                    entry = POKEDEX.get(d)
                                    if not entry:
                                        return [
                                            d]
                                    chain_len = None.get('chain_len', 1)
                                    stage = entry.get('stage', 0)
                                    cur = d
                                    cur_stage = stage
                                    guard = 0
                                    if cur_stage > 0 and guard < 10:
                                        guard += 1
                                        prev = REVERSE_COMPANION_EVOLVE_OVERRIDE.get(cur, cur - 1)
                                        prev_entry = POKEDEX.get(prev)
                                        if prev_entry and prev_entry.get('chain_len', 1) != chain_len or prev_entry.get('stage', -1) != cur_stage - 1:
                                            return [
                                                d]
                                        cur = None
                                        cur_stage -= 1
                                        continue
                                    chain = [
                                        cur]
                                    nd = cur
                                    for i in range(1, chain_len):
                                        nxt = COMPANION_EVOLVE_OVERRIDE.get(nd, nd + 1)
                                        nxt_entry = POKEDEX.get(nxt)
                                        if nxt_entry and nxt_entry.get('chain_len', 1) != chain_len or nxt_entry.get('stage', -1) != i:
                                            range(1, chain_len)
                                            return chain
                                        range(1, chain_len).append(nxt)
                                        nd = nxt
                                    return chain

                                ENCOUNTER_CHANCE_PER_SEC = 0.006
                                KEYBOARD_CONTROL_ENCOUNTER_MULT = 1.25
                                ENCOUNTER_COOLDOWN = 25
                                IDLE_ENCOUNTER_CHANCE_MULT = 0.6
                                ENCOUNTER_IGNORE_TIMEOUT_MS = 90000
                                SHINY_CHANCE = 0.01
                                SHINY_STAT_MULT = 2
                                HAPPY_ACTION_CANDIDATES = [
                                    'Sit',
                                    'Laying',
                                    'LookUp',
                                    'Pose',
                                    'Nod']
                                HUNGRY_ACTION_CANDIDATES = [
                                    'Cringe',
                                    'Pain',
                                    'LostBalance',
                                    'Trip',
                                    'Sink',
                                    'Hurt']
                                AFFECTION_HAPPY_THRESHOLD = 80
                                HUNGRY_REACT_THRESHOLD = 25
                                TRAIN_SESSION_SECONDS = 3600
                                TRAIN_MAX_PER_DAY = 5
                                TRAIN_ATK_BONUS_PER_SESSION = 1
                                MINIGAME_TIER_ATK_PCT = {
                                    'fail': 0,
                                    'bronze': 0.15,
                                    'silver': 0.3,
                                    'gold': 0.5 }
                                MINIGAME_ALL_CLEAR_BONUS_PCT = 0.5
                                MINIGAME_KEYS = ('feed', 'card', 'quiz', 'throw')
                                GOLD_PER_CATCH = 10
                                SHOP_GACHA_COST = 100
                                SHOP_LEGEND_TOKEN_COST = 500
                                SHOP_LEGEND_TOKEN_COUNT = 3
                                SHOP_GEN_PRICE_MULT = {
                                    4: 2.5,
                                    3: 2,
                                    2: 1.5,
                                    1: 1 }
                                SHOP_LEGEND_TOKEN_COST_MULT = SHOP_GEN_PRICE_MULT
                                LEGEND_TOKEN_MIN_LEVEL = {
                                    4: 10,
                                    3: 10,
                                    2: 10,
                                    1: 5 }
                                POKEMON_FOOD_COST = 300
                                POKEMON_FOOD_DURATION_SEC = 1800
                                POKEMON_FOOD_MULT = 2
                                POKEMON_FOOD_DAILY_LIMIT = 3
                                SHOP_MYTH_TOKEN_COST = 2500
                                MINE_MAX_PER_DAY = 5
                                MINE_TRIP_SECONDS = 10
                                MINE_SECRET_SPEED_MULT = 2
                                MINE_TAP_STEP = 0.01
                                MINE_REWARD_TABLE = [
                                    (10, 40),
                                    (20, 30),
                                    (50, 15),
                                    (100, 10),
                                    (200, 5)]
                                GACHA_MAX_PER_DAY = 3
                                GACHA_PULL_COST = 100
                                GACHA_GRID_N = 10
                                GACHA_POOL_COMPOSITION = [
                                    (50, 40),
                                    (100, 30),
                                    (150, 15),
                                    (200, 10),
                                    (500, 4),
                                    (1000, 1)]
                                MEGA_STAT_MULT = 2
                                MEGA_SACRIFICE_N = 5
                                MEGA_NAME_KR = {
                                    150: {
                                        'y': '메가뮤츠Y',
                                        'x': '메가뮤츠X' },
                                    9: '메가거북왕',
                                    6: {
                                        'y': '메가리자몽Y',
                                        'x': '메가리자몽X' },
                                    3: '메가이상해꽃' }
                                MEGA_XY_STAT_MULT = {
                                    150: {
                                        'y': {
                                            'def': 1.55,
                                            'atk': 2.55 },
                                        'x': {
                                            'def': 2.25,
                                            'atk': 2.05 } },
                                    6: {
                                        'y': {
                                            'def': 1.65,
                                            'atk': 2.3 },
                                        'x': {
                                            'def': 2.15,
                                            'atk': 1.9 } } }
                                
                                def mega_form_stat_mult(dex, form, key, default):
                                    '''dex/form(x·y)에 등록된 전용 공격력/방어력 배율이 있으면 그걸, 없으면(X/Y 구분이
없는 일반 메가진화 종) default(보통 MEGA_STAT_MULT 그대로)를 돌려준다.'''
                                    
                                    try:
                                        d = MEGA_XY_STAT_MULT.get(int(dex))
                                        if not d:
                                            return default
                                        f = None.get(form)
                                        if not f:
                                            return default
                                        return None.get(key, default)
                                    except Exception:
                                        d = None
                                        continue


                                MEGA_AURA_PRESETS = {
                                    'vivid': 1,
                                    'soft': 0.55,
                                    'off': 0 }
                                MEGA_COMPANION_ELIGIBLE_DEX = {
                                    6,
                                    282,
                                    302,
                                    303,
                                    308,
                                    310,
                                    65,
                                    323,
                                    334,
                                    94,
                                    354,
                                    359,
                                    362,
                                    115,
                                    380,
                                    381,
                                    384,
                                    142,
                                    150,
                                    208,
                                    229,
                                    248}
                                MEGA_COMPANION_LEVEL_REQUIRE = 15
                                MEGA_COMPANION_STAT_MULT = 1.6
                                COMPANION_GEN_SYNERGY_MULT = {
                                    4: 2.35,
                                    3: 1.96,
                                    2: 1.68,
                                    1: 1 }
                                COMPANION_LEGENDARY_SYNERGY_MULT = 1.55
                                ARCEUS_DEX = 493
                                ARCEUS_EQUIP_ATK_PCT_AT_LV15 = 100
                                LEGENDARY_LEVEL_GROWTH_BONUS = 0.06
                                LEGENDARY_GEN_STAT_MULT = {
                                    5: 1.32,
                                    4: 1.24,
                                    3: 1.16,
                                    2: 1.08,
                                    1: 1 }
                                LEGENDARY_SIGNATURE_TIER_MULT = {
                                    493: 3.6,
                                    484: 3,
                                    483: 3 }
                                SINNOH_TRIO_DEX = None(LEGENDARY_SIGNATURE_TIER_MULT.keys())
                                WILD_TOUGH_LEGEND_DEX = {
                                    483,
                                    484,
                                    493}
                                WILD_TOUGH_LEGEND_HP_MULT = 1.8
                                WILD_TOUGH_LEGEND_DEF_MULT = 1.6
                                WILD_LEGEND_CATCH_TIER_MULT = {
                                    493: 2.3,
                                    484: 1.7,
                                    483: 1.7 }
                                BATTLE_SPRITE_MEGA_SCALE = 1.2
                                BATTLE_SPRITE_BIG_LEGEND_SCALE = 1.45
                                BATTLE_SPRITE_BIG_LEGEND_DEX = {
                                    484,
                                    493,
                                    249}
                                SPRITE_SCALE_FIX_DEX = {
                                    149: 1.3 }
                                MEGA_BODY2_STAT_MULT = 1.7
                                
                                def sprite_extra_scale(dex):
                                    '''화면에 그릴 때 곱해줄 종족번호별 추가 배율. 초전설급 3종은 기존 그대로 크게,
SPRITE_SCALE_FIX_DEX에 등록된 종은 그 배율만큼, 나머지는 1.0(보정 없음).'''
                                    
                                    try:
                                        dex = int(dex)
                                        if dex in BATTLE_SPRITE_BIG_LEGEND_DEX:
                                            return BATTLE_SPRITE_BIG_LEGEND_SCALE
                                        return None.get(dex, 1)
                                    except Exception:
                                        return 1


                                RAISED_STAT_BONUS_MULT = 1.1
                                
                                def mega_companion_eligible_species(dex):
                                    '''이 도감번호가 동료/2번본체 메가진화 대상(실제 스프라이트가 있는 22종)인지.'''
                                    
                                    try:
                                        return int(dex) in MEGA_COMPANION_ELIGIBLE_DEX
                                    except Exception:
                                        return False


                                
                                def mega_companion_ready(dex, caught):
                                    '''이 도감번호가 지금 당장 메가진화 스위치를 켤 수 있는 상태인지
(대상 종이면서, 최고 레벨(15)로 잡아둔 개체 기록이 있어야 함).'''
                                    if not mega_companion_eligible_species(dex):
                                        return False
                                    if not None:
                                        pass
                                    caught = { }
                                    info = caught.get(str(int(dex)))
                                    lv = info.get('level', 0) if isinstance(info, dict) else 0
                                    
                                    try:
                                        return int(lv) >= MEGA_COMPANION_LEVEL_REQUIRE
                                    except Exception:
                                        return False


                                
                                def mega_companion_display_kr(dex, entry):
                                    """동료/2번본체 메가진화 표시 이름. 리자몽처럼 본체 전용 정식명칭이 등록돼 있으면 그걸
재사용하고(X형태), 나머지는 '메가'+기존 한글명 형태(실제 한국어 공식 명명 방식과 동일)로 만든다."""
                                    names = MEGA_NAME_KR.get(int(dex)) if dex is not None else None
                                    if isinstance(names, dict):
                                        if not names.get('x'):
                                            names.get('x')
                                            if not names.get('y'):
                                                names.get('y')
                                                if not entry:
                                                    entry
                                        return f'''메가{{ }.get('kr', '?')}'''
                                    if None(names, str):
                                        return names
                                    if not entry:
                                        entry
                                    return f'''{{ }.get('kr', '?')}'''

                                
                                def companion_mega_sprite_folder(entry):
                                    '''동료/2번본체가 메가진화했을 때 쓸 실제 스프라이트 폴더 이름을 찾는다.
(assets_v3/assets_mega 안의 하이픈 명명규칙: <en>-mega / <en>-mega-x / <en>-mega-y)
실제로 폴더가 있는 것만 돌려주고, 없으면 None(그러면 원래 폼 그림을 그대로 쓴다).'''
                                    if not entry:
                                        return None
                                    base = None.get('en')
                                    if not base:
                                        return None
                                    for suffix in None:
                                        candidate = base + suffix
                                        for search_base in SPRITE_SEARCH_DIRS:
                                            if os.path.isdir(os.path.join(search_base, candidate)):
                                                
                                                
                                                return None, SPRITE_SEARCH_DIRS, candidate
                                    return None
                                    except Exception:
                                        continue

                                TYPE_COLORS = { }['normal']['fighting']['flying']['poison']['ground']['rock']['bug']['ghost']['steel']['fire']['water']['grass']['electric']['psychic']['ice']['dragon']['dark']
                                TYPE_SKILL_LABEL = { }['normal']['fighting']['flying']['poison']['ground']['rock']['bug']['ghost']['steel']['fire']['water']['grass']['electric']['psychic']['ice']['dragon']['dark']
                                SKILL_LABEL = TYPE_SKILL_LABEL
                                ELEMENT_COLORS = TYPE_COLORS
                                TYPE_KR = { }['normal']['fighting']['flying']['poison']['ground']['rock']['bug']['ghost']['steel']['fire']['water']['grass']['electric']['psychic']['ice']['dragon']['dark']
                                OFFENSIVE_TYPES = {
                                    'dark',
                                    'fire',
                                    'rock',
                                    'dragon',
                                    'ground',
                                    'fighting'}
                                DEFENSIVE_TYPES = {
                                    'ice',
                                    'rock',
                                    'steel',
                                    'water',
                                    'normal'}
                                FAST_TYPES = {
                                    'bug',
                                    'flying',
                                    'psychic',
                                    'electric'}
                                LEVEL_GLOW_COLORS = {
                                    10: (255, 215, 0),
                                    9: (200, 40, 220),
                                    8: (255, 60, 140),
                                    7: (255, 90, 90),
                                    6: (255, 140, 60),
                                    5: (255, 175, 30),
                                    4: (200, 110, 250),
                                    3: (90, 150, 255),
                                    2: (110, 210, 120),
                                    1: (190, 190, 190) }
                                SIZE_OPTIONS = [
                                    ('최소 크기', 0.3),
                                    ('매우 작게', 0.45),
                                    ('아주 작게', 0.6),
                                    ('작게', 0.8),
                                    ('보통', 1),
                                    ('조금 크게', 1.25),
                                    ('크게', 1.5),
                                    ('아주 크게', 1.8),
                                    ('거대', 2.3),
                                    ('초거대', 3)]
                                SPECIES = {
                                    'eevee': {
                                        'branches': {
                                            'dark': {
                                                'wake': 'Wake',
                                                'land': 'HitGround',
                                                'hide': 'Sink',
                                                'react': 'Nod',
                                                'trick': 'Pose',
                                                'skill': 'Shoot',
                                                'eat': 'Eat',
                                                'element': 'dark',
                                                'scale': 1.7,
                                                'dex': 197,
                                                'kr': '블래키',
                                                'id': 'umbreon' },
                                            'psychic': {
                                                'wake': None,
                                                'land': 'Hurt',
                                                'hide': None,
                                                'react': 'Hurt',
                                                'trick': 'Rotate',
                                                'skill': 'Shoot',
                                                'eat': 'Charge',
                                                'element': 'psychic',
                                                'scale': 1.7,
                                                'dex': 196,
                                                'kr': '에브이',
                                                'id': 'espeon' },
                                            'electric': {
                                                'wake': 'Wake',
                                                'land': 'HitGround',
                                                'hide': 'Sink',
                                                'react': 'Nod',
                                                'trick': 'Pose',
                                                'skill': 'Shock',
                                                'eat': 'Eat',
                                                'element': 'electric',
                                                'scale': 1.7,
                                                'dex': 135,
                                                'kr': '쥬피썬더',
                                                'id': 'jolteon' },
                                            'water': {
                                                'wake': None,
                                                'land': 'Hurt',
                                                'hide': None,
                                                'react': 'Hurt',
                                                'trick': 'Rotate',
                                                'skill': 'Shoot',
                                                'eat': 'Charge',
                                                'element': 'water',
                                                'scale': 1.7,
                                                'dex': 134,
                                                'kr': '샤미드',
                                                'id': 'vaporeon' },
                                            'fire': {
                                                'wake': 'Wake',
                                                'land': 'HitGround',
                                                'hide': 'Sink',
                                                'react': 'Nod',
                                                'trick': 'Pose',
                                                'skill': 'DeepBreath',
                                                'eat': 'Eat',
                                                'element': 'fire',
                                                'scale': 1.7,
                                                'dex': 136,
                                                'kr': '부스터',
                                                'id': 'flareon' } },
                                        'stages': [
                                            {
                                                'wake': 'Wake',
                                                'land': 'HitGround',
                                                'hide': 'Sink',
                                                'react': 'Nod',
                                                'trick': 'Pose',
                                                'skill': 'Attack',
                                                'eat': 'Eat',
                                                'scale': 1.05,
                                                'dex': 133,
                                                'kr': '이브이',
                                                'id': 'eevee' }],
                                        'branching': True,
                                        'evolve_tiers': [
                                            1],
                                        'element': 'normal',
                                        'kr': '이브이' },
                                    'squirtle': {
                                        'stages': [
                                            {
                                                'wake': 'Wake',
                                                'land': 'HitGround',
                                                'hide': 'Withdraw',
                                                'react': 'Nod',
                                                'trick': 'Pose',
                                                'skill': 'Shoot',
                                                'eat': 'Eat',
                                                'scale': 1,
                                                'dex': 7,
                                                'kr': '꼬부기',
                                                'id': 'squirtle' },
                                            {
                                                'wake': None,
                                                'land': 'Hurt',
                                                'hide': 'Withdraw',
                                                'react': 'Hurt',
                                                'trick': 'Rotate',
                                                'skill': 'Shoot',
                                                'eat': 'Charge',
                                                'scale': 1.4,
                                                'dex': 8,
                                                'kr': '어니부기',
                                                'id': 'wartortle' },
                                            {
                                                'wake': None,
                                                'land': 'Hurt',
                                                'hide': 'Withdraw',
                                                'react': 'Hurt',
                                                'trick': 'Rotate',
                                                'skill': 'Shoot',
                                                'eat': 'Charge',
                                                'scale': 1.85,
                                                'dex': 9,
                                                'kr': '거북왕',
                                                'id': 'blastoise' }],
                                        'evolve_tiers': [
                                            1,
                                            2],
                                        'element': 'water',
                                        'kr': '꼬부기' },
                                    'bulbasaur': {
                                        'stages': [
                                            {
                                                'wake': 'Wake',
                                                'land': 'HitGround',
                                                'hide': 'Sink',
                                                'react': 'Nod',
                                                'trick': 'Pose',
                                                'skill': 'Swing',
                                                'eat': 'Eat',
                                                'scale': 1,
                                                'dex': 1,
                                                'kr': '이상해씨',
                                                'id': 'bulbasaur' },
                                            {
                                                'wake': None,
                                                'land': 'Hurt',
                                                'hide': None,
                                                'react': 'Shake',
                                                'trick': 'Rotate',
                                                'skill': 'Swing',
                                                'eat': 'Charge',
                                                'scale': 1.4,
                                                'dex': 2,
                                                'kr': '이상해풀',
                                                'id': 'ivysaur' },
                                            {
                                                'wake': None,
                                                'land': 'Hurt',
                                                'hide': None,
                                                'react': 'Shake',
                                                'trick': 'Rotate',
                                                'skill': 'Swing',
                                                'eat': 'Charge',
                                                'scale': 1.75,
                                                'dex': 3,
                                                'kr': '이상해꽃',
                                                'id': 'venusaur' }],
                                        'evolve_tiers': [
                                            1,
                                            2],
                                        'element': 'grass',
                                        'kr': '이상해씨' },
                                    'charmander': {
                                        'stages': [
                                            {
                                                'wake': 'Wake',
                                                'land': 'HitGround',
                                                'hide': 'Sink',
                                                'react': 'Nod',
                                                'trick': 'Pose',
                                                'skill': 'DeepBreath',
                                                'eat': 'Eat',
                                                'scale': 1,
                                                'dex': 4,
                                                'kr': '파이리',
                                                'id': 'charmander' },
                                            {
                                                'wake': 'Wake',
                                                'land': 'HitGround',
                                                'hide': 'Sink',
                                                'react': 'Nod',
                                                'trick': 'Pose',
                                                'skill': 'DeepBreath',
                                                'eat': 'Eat',
                                                'scale': 1.4,
                                                'dex': 5,
                                                'kr': '리자드',
                                                'id': 'charmeleon' },
                                            {
                                                'wake': None,
                                                'land': 'Hurt',
                                                'hide': None,
                                                'react': 'Hurt',
                                                'trick': 'Rotate',
                                                'skill': 'Shoot',
                                                'eat': 'Charge',
                                                'scale': 1.85,
                                                'dex': 6,
                                                'kr': '리자몽',
                                                'id': 'charizard' }],
                                        'evolve_tiers': [
                                            1,
                                            2],
                                        'element': 'fire',
                                        'kr': '파이리' },
                                    'pikachu': {
                                        'stages': [
                                            {
                                                'wake': 'Wake',
                                                'land': 'HitGround',
                                                'hide': 'Sink',
                                                'react': 'Nod',
                                                'trick': 'Pose',
                                                'skill': 'Shock',
                                                'eat': 'Eat',
                                                'scale': 1.1,
                                                'dex': 25,
                                                'kr': '피카츄',
                                                'id': 'pikachu' },
                                            {
                                                'wake': 'Wake',
                                                'land': 'HitGround',
                                                'hide': 'Sink',
                                                'react': 'Nod',
                                                'trick': 'Pose',
                                                'skill': 'Shock',
                                                'eat': 'Eat',
                                                'scale': 1.7,
                                                'dex': 26,
                                                'kr': '라이츄',
                                                'id': 'raichu' }],
                                        'evolve_tiers': [
                                            1],
                                        'element': 'electric',
                                        'kr': '피카츄' } }
                                STARTER_ORDER = [
                                    'pikachu',
                                    'charmander',
                                    'bulbasaur',
                                    'squirtle',
                                    'eevee']
                                
                                def _build_body_chain_lookup():
                                    '''stages'''
                                    lookup = { }
                                    for None in SPECIES.items():
                                        sp_key = ()
                                        sp = None
                                        for None in enumerate(sp['stages']):
                                            i = ()
                                            st = None
                                        if not sp.get('branching'):
                                            continue
                                        for None in sp.get('branches', { }).items():
                                            br_key = ()
                                            br = None
                                        sp.get('branches', { }).items()
                                    return lookup

                                BODY_CHAIN_LOOKUP = None()
                                DEFAULT_STATE = { }['gym_badges']['single_monitor_mode']['secondary_monitor_mode']['shiny_caught']['mine_sessions']['mine_lifetime_plays']['gacha_sessions']['food_sessions']['coin_gacha_pool']['coin_wallet']['rocket_defeat_count']['login_days_count']['last_login_day_recorded']['daily_quest_lifetime_days']['rocket_last_encounter_at']['rocket_party']
                                
                                def get_all_stage_ids(species_key):
                                    '''stages'''
                                    sp = SPECIES[species_key]
                                    for None in :
                                        s = None
                                    
                                    , [], ids, s = sp['stages'], s
                                    if sp.get('branching'):
                                        for None in :
                                            b = None
                                        
                                        sp['branches'].values(), b, , [] += b, = ids
                                    return ids
                                    
                                    

                                
                                def stage_conf_for(state):
                                    '''starter'''
                                    sp = SPECIES[state['starter']]
                                    stage = state.get('stage', 0)
                                    if sp.get('branching'):
                                        if stage <= 0:
                                            return sp['stages'][0]
                                        if not None.get('eevee_branch'):
                                            None.get('eevee_branch')
                                        branch = 'water'
                                        return sp['branches'][branch]
                                    idx = None(0, min(stage, len(sp['stages']) - 1))
                                    return sp['stages'][idx]

                                
                                def pokedex_entry_as_stage_conf(entry):
                                    '''POKEDEX 항목 하나를 SPECIES의 "단계(stage)" 딕셔너리와 같은 모양으로 바꿔준다.
본체를 "잡은 아무 포켓몬"으로 교체했을 때, 기존 렌더링/애니메이션 코드가 그대로
돌아가도록 맞춰주는 어댑터. POKEDEX 항목엔 이미 eat/skill/trick/react/hide/land/wake
같은 애니메이션 필드가 SPECIES 단계와 똑같은 이름으로 들어있어서 거의 그대로 쓸 수 있다.'''
                                    dex = entry.get('dex')
                                    stage_n = entry.get('stage', 0)
                                    return {
                                        'idle': entry.get('idle', 'Idle'),
                                        'wake': entry.get('wake'),
                                        'land': entry.get('land'),
                                        'hide': entry.get('hide'),
                                        'react': entry.get('react'),
                                        'trick': entry.get('trick'),
                                        'skill': entry.get('skill'),
                                        'eat': entry.get('eat'),
                                        'scale': 1 + 0.35 * stage_n,
                                        'element': entry.get('element', entry.get('types', [
                                            'normal'])[0] if entry.get('types') else 'normal'),
                                        'dex': dex,
                                        'kr': entry.get('kr', '?'),
                                        'id': f'''pdx_{dex}''' }

                                
                                def display_stage_conf_for(state):
