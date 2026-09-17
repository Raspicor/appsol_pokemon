# Source Generated with Decompyle++
# File: spriteanim.pyc (Python 3.14)

'''
spriteanim.py
PMD(포켓몬 불가사의 던전) 스타일 스프라이트시트에서 방향/프레임별 이미지를 잘라내는 엔진.

폴더 구조 (포켓몬 한 종당 하나):
    assets/sprites/<species>/AnimData.xml
    assets/sprites/<species>/<ActionName>-Anim.png

AnimData.xml 안의 각 <Anim>은 FrameWidth/FrameHeight/Durations 를 갖고,
이미지 파일은 가로= 프레임 수, 세로 = 방향 수(보통 8, 없으면 1)로 배치된 그리드.
방향 순서(8방향 기준): 아래,아래오른쪽,오른쪽,위오른쪽,위,위왼쪽,왼쪽,아래왼쪽
'''
import os

ElementTree
from PIL import Image
import xml.etree.ElementTree, etree
DIR_DOWN = 0
DIR_DOWN_RIGHT = 1
DIR_RIGHT = 2
DIR_UP_RIGHT = 3
DIR_UP = 4
DIR_UP_LEFT = 5
DIR_LEFT = 6
DIR_DOWN_LEFT = 7
_DIR_COUNT = 8

def AnimInfo():
    '''AnimInfo'''
    __firstlineno__ = 33
    __classdict__ = <NODE:36>
    __slots__ = ('name', 'frame_w', 'frame_h', 'durations', 'n_dirs')
    
    def __init__(self, name, frame_w, frame_h, durations, n_dirs):
        self.name = name
        self.frame_w = frame_w
        self.frame_h = frame_h
        self.durations = durations
        self.n_dirs = n_dirs

    n_frames = (lambda self: len(self.durations))()
    __static_attributes__ = ('durations', 'frame_h', 'frame_w', 'n_dirs', 'name')
    __classdictcell__ = __classdict__

AnimInfo = None(AnimInfo, 'AnimInfo')

def AnimSet():
    '''AnimSet'''
    __firstlineno__ = 48
    __classdict__ = <NODE:36>
    __doc__ = '포켓몬 한 종 폴더 전체를 로드해서 프레임 이미지를 제공.'
    
    def __init__(self, folder):
        '''AnimData.xml'''
        self.folder = folder
        self.anims = { }
        self.sheets = { }
        self._frame_cache = { }
        xml_path = os.path.join(folder, 'AnimData.xml')
        tree = None(xml_path)
        root = tree.getroot()
        anims_node = root.find('Anims')
        if anims_node is None:
            anims_node = root
        raw = { }
        order = []
        for anim_node in anims_node.findall('Anim'):
            name_node = anim_node.find('Name')
            if not name_node is not None or name_node.text:
                continue
            name = name_node.text.strip()
            copy_node = anim_node.find('CopyOf')
            copy_of = copy_node.text.strip() if copy_node is not None and copy_node.text else None
            fw_node = anim_node.find('FrameWidth')
            fh_node = anim_node.find('FrameHeight')
            frame_w = int(fw_node.text) if fw_node is not None and fw_node.text else None
            frame_h = int(fh_node.text) if fh_node is not None and fh_node.text else None
            durations = []
            dur_parent = anim_node.find('Durations')
            if dur_parent is not None:
                for d in dur_parent.findall('Duration'):
                    durations.append(max(1, int(d.text)))
                anims_node.findall('Anim')
            raw[name] = {
                'durations': durations,
                'frame_h': frame_h,
                'frame_w': frame_w,
                'copy_of': copy_of }
            order.append(name)
        
        def _resolve_source(name, _seen = None):
            '''CopyOf 체인을 따라가서 실제 PNG 파일을 갖고 있는 원본 동작 이름을 찾는다.
(자기 파일이 있으면 자기 자신, 없고 CopyOf가 있으면 그 대상을 재귀적으로 확인)'''
            _seen = _seen if _seen is not None else set()
            if name in _seen or name not in raw:
                return None
            None.add(name)
            if os.path.isfile(os.path.join(folder, f'''{name}-Anim.png''')):
                return name
            copy_of = None[name].get('copy_of')
            if copy_of:
                return None(copy_of, _seen)

        for name in order:
            info = raw[name]
            src_name = None(name)
            if src_name is None:
                continue
            src_info = raw.get(src_name, info)
            if not info['frame_w']:
                info['frame_w']
            frame_w = src_info.get('frame_w')
            if not info['frame_h']:
                info['frame_h']
            frame_h = src_info.get('frame_h')
            if not info['durations']:
                info['durations']
                if not src_info.get('durations'):
                    src_info.get('durations')
            durations = [
                4]
            if frame_w and frame_h and frame_w <= 0 or frame_h <= 0:
                continue
            (sheet_w, sheet_h) = img.size
            n_dirs = max(1, sheet_h // frame_h)
            if n_dirs > _DIR_COUNT:
                n_dirs = _DIR_COUNT
            self.anims[name] = AnimInfo(name, frame_w, frame_h, durations, n_dirs)
            self.sheets[name] = img
        order
        return None
        except (TypeError, ValueError):
            durations.append(4)
            continue
        except Exception:
            continue

    
    def has(self, name):
        return name in self.anims

    
    def info(self, name):
        return self.anims.get(name)

    
    def frame(self, name, frame_idx, dir_idx = DIR_DOWN):
        '''지정한 액션/프레임/방향의 PIL 이미지를 반환 (없으면 None).'''
        key = (name, frame_idx, dir_idx)
        cached = self._frame_cache.get(key)
        if cached is not None:
            return cached
        info = None.anims.get(name)
        if info is None:
            return None
        n_frames = None.n_frames
        if n_frames <= 0:
            return None
        frame_idx = None % None
        n_dirs = info.n_dirs
        use_dir = dir_idx if dir_idx < n_dirs else dir_idx % n_dirs
        sheet = self.sheets[name]
        x0 = frame_idx * info.frame_w
        y0 = use_dir * info.frame_h
        x1 = x0 + info.frame_w
        y1 = y0 + info.frame_h
        (sw, sh) = sheet.size
        if x1 > sw or y1 > sh:
            return None
        cropped = None.crop((x0, y0, x1, y1))
        self._frame_cache[key] = cropped
        return cropped

    
    def duration_of(self, name, frame_idx):
        info = self.anims.get(name)
        if info is None:
            return 4
        n = None.n_frames
        if n <= 0:
            return 4
        return None.durations[frame_idx % n]

    
    def n_frames(self, name):
        info = self.anims.get(name)
        if info:
            return info.n_frames

    __static_attributes__ = ('_frame_cache', 'anims', 'folder', 'sheets')
    __classdictcell__ = __classdict__

AnimSet = None(AnimSet, 'AnimSet')
