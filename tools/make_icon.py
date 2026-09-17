#!/usr/bin/env python3
"""`tools/icon.png`(몬스터볼)로 앱 아이콘을 만든다.

    tools/make_icon.py --preview /tmp/ball.png          # 한 장만 크게
    tools/make_icon.py --iconset build/PikaPet.iconset  # icns 재료 전부

원본에 두 가지 손질이 필요하다.

**배경 빼기.** 원본은 알파가 없는 RGB라 공 바깥이 흰색으로 차 있다. 그대로
쓰면 Dock에 흰 사각형이 붙는다. 다행히 공이 캔버스에 정확히 내접해 있어서
(가로·세로 중앙선 둘 다 0번 픽셀부터 마지막 픽셀까지가 공이다) 원형 마스크로
정확히 잘린다. 흰색을 지우는 방식은 못 쓴다 — 공 아래쪽 절반과 하이라이트도
흰색이라 같이 지워진다.

**크기별로 줄이기.** 아이콘은 16px부터 1024px까지 필요하고, 매번 원본에서
LANCZOS로 줄인다.
"""

import argparse
import os
import sys

from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "icon.png")

# 아이콘 격자 안에서 공이 차지할 비율. 1.0이면 캔버스에 꽉 차서 Dock의 다른
# 아이콘들보다 커 보인다.
FILL = 0.92

SS = 4          # 마스크 슈퍼샘플링 배율. PIL의 원에는 안티에일리어싱이 없다.

_cache = None


def load_ball():
    """원본을 읽어 공 바깥을 투명하게 만든 RGBA 이미지."""
    global _cache
    if _cache is not None:
        return _cache
    if not os.path.exists(SOURCE):
        raise SystemExit(f"아이콘 원본이 없습니다: {SOURCE}")
    img = Image.open(SOURCE).convert("RGBA")
    n = min(img.size)
    img = img.crop(((img.width - n) // 2, (img.height - n) // 2,
                    (img.width + n) // 2, (img.height + n) // 2))

    mask = Image.new("L", (n * SS, n * SS), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, n * SS - 1, n * SS - 1), fill=255)
    img.putalpha(mask.resize((n, n), Image.LANCZOS))
    _cache = img
    return img


def render(size):
    """한 변이 `size`인 RGBA 아이콘. 배경은 투명."""
    ball = load_ball()
    inner = max(1, int(round(size * FILL)))
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    scaled = ball.resize((inner, inner), Image.LANCZOS)
    offset = (size - inner) // 2
    canvas.paste(scaled, (offset, offset), scaled)
    return canvas


def write_iconset(path):
    """iconutil이 먹는 .iconset 디렉터리를 채운다."""
    os.makedirs(path, exist_ok=True)
    for size in (16, 32, 64, 128, 256, 512, 1024):
        for scale, suffix in ((1, ""), (2, "@2x")):
            px = size * scale
            if px > 1024:
                continue
            render(px).save(os.path.join(path, f"icon_{size}x{size}{suffix}.png"))
    return path


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--preview", metavar="PNG", help="한 장만 그려서 저장")
    ap.add_argument("--size", type=int, default=512, help="--preview 의 크기")
    ap.add_argument("--iconset", metavar="DIR", help=".iconset 디렉터리를 채운다")
    args = ap.parse_args()

    if not args.preview and not args.iconset:
        ap.error("--preview 나 --iconset 중 하나는 필요합니다")
    if args.preview:
        render(args.size).save(args.preview)
        print(f"  {args.preview} ({args.size}x{args.size})")
    if args.iconset:
        write_iconset(args.iconset)
        print(f"  {args.iconset} 채움")
    return 0


if __name__ == "__main__":
    sys.exit(main())
