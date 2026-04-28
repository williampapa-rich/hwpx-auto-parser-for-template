"""
자동 추출된 스타일/레이아웃 상수
  생성 시점: 1개 파일 분석
  이 파일은 reverse_engineer 모듈이 자동 생성합니다.
  수정하지 마세요. 다시 추출하면 덮어써집니다.
"""

# ─── 페이지 레이아웃 (자동 추출) ─────────────────────────────────────────────
PAGE_WIDTH    = 59528
PAGE_HEIGHT   = 84188
MARGIN_L      = 8504
MARGIN_R      = 8504
MARGIN_T      = 5669
MARGIN_B      = 4252
HEADER_H      = 4252
FOOTER_H      = 2835

COL_COUNT     = 1
COL_GAP       = 0

HAS_HEADER    = False
HAS_FOOTER    = False
HEADER_HAS_PAGENUM = False
FOOTER_HAS_PAGENUM = False

# ─── 스타일 ID (자동 추출 — 다수결 + 역할 휴리스틱) ──────────────────────────
PARA_ID_BODY        = None
PARA_ID_CHOICE      = None
PARA_ID_GROUP_LABEL = None
BORDER_ID_PASSAGE_BOX = '4'

# 등록된 폰트
FONTS = {
    'HANGUL_0': '함초롬바탕',
    'HANGUL_1': '#태고딕',
    'HANGUL_2': '신명 견명조',
    'HANGUL_3': '신명 디나루',
    'HANGUL_4': '신명 신그래픽',
    'HANGUL_5': '신명 중고딕',
    'HANGUL_6': '신명 중명조',
    'HANGUL_7': '신명 태고딕',
    'HANGUL_8': '한양견고딕',
    'HANGUL_9': '한양견명조',
    'HANGUL_10': '한양신명조',
    'LATIN_0': 'Arial Black',
    'LATIN_1': 'Times New Roman',
    'LATIN_2': '#태고딕',
    'LATIN_3': '신명 견명조',
    'LATIN_4': '신명 디나루',
    'LATIN_5': '신명 신그래픽',
    'LATIN_6': '신명 중고딕',
    'LATIN_7': '신명 태고딕',
    'LATIN_8': '한양견고딕',
    'LATIN_9': '한양견명조',
    'LATIN_10': '한양신명조',
    'HANJA_0': '함초롬바탕',
    'HANJA_1': '#신디나루',
    'HANJA_2': '#태고딕',
    'HANJA_3': '신명 견고딕',
    'HANJA_4': '신명 견명조',
    'HANJA_5': '신명 중고딕',
    'HANJA_6': '신명 중명조',
    'HANJA_7': '신명 태고딕',
    'HANJA_8': '한양신명조',
    'JAPANESE_0': '함초롬바탕',
    'JAPANESE_1': '#태고딕',
    'JAPANESE_2': '신명 견명조',
    'JAPANESE_3': '신명 신명조',
    'JAPANESE_4': '신명 중고딕',
    'JAPANESE_5': '신명 태고딕',
    'JAPANESE_6': '한양신명조',
    'OTHER_0': '함초롬바탕',
    'OTHER_1': '한양신명조',
    'SYMBOL_0': '함초롬바탕',
    'SYMBOL_1': '#디나루',
    'SYMBOL_2': '#신그래픽',
    'SYMBOL_3': '#태고딕',
    'SYMBOL_4': '신명 견고딕',
    'SYMBOL_5': '신명 견명조',
    'SYMBOL_6': '신명 태그래픽',
    'SYMBOL_7': '한양신명조',
    'SYMBOL_8': '한양중고딕',
    'USER_0': '함초롬바탕',
    'USER_1': '명조',
}

# 모든 단락 속성 ID 목록
ALL_PARA_IDS  = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84']
ALL_CHAR_IDS  = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114']
ALL_BORDER_IDS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']

# ─── 유형별 평균 지문 길이 (생성 프롬프트 가이드용) ─────────────────────────
TYPE_PROFILES = {
    '내용불일치(26)': {'samples': 1, 'avg_passage_len': 75, 'has_box_ratio': 1.00},
    '도표(25)': {'samples': 1, 'avg_passage_len': 151, 'has_box_ratio': 0.00},
    '듣기-그림(4)': {'samples': 1, 'avg_passage_len': 75, 'has_box_ratio': 0.00},
    '듣기-금액(6)': {'samples': 1, 'avg_passage_len': 0, 'has_box_ratio': 0.00},
    '듣기-내용일치(9)': {'samples': 1, 'avg_passage_len': 0, 'has_box_ratio': 0.00},
    '듣기-도표(10)': {'samples': 1, 'avg_passage_len': 0, 'has_box_ratio': 0.00},
    '듣기-목적(1)': {'samples': 1, 'avg_passage_len': 0, 'has_box_ratio': 0.00},
    '듣기-언급된대상(17)': {'samples': 1, 'avg_passage_len': 0, 'has_box_ratio': 0.00},
    '듣기-언급여부(8)': {'samples': 1, 'avg_passage_len': 0, 'has_box_ratio': 0.00},
    '듣기-요지(3)': {'samples': 1, 'avg_passage_len': 0, 'has_box_ratio': 0.00},
    '듣기-의견(2)': {'samples': 1, 'avg_passage_len': 0, 'has_box_ratio': 0.00},
    '듣기-이유(7)': {'samples': 1, 'avg_passage_len': 0, 'has_box_ratio': 0.00},
    '듣기-주제(16)': {'samples': 1, 'avg_passage_len': 0, 'has_box_ratio': 0.00},
    '듣기-짧은응답(11~14)': {'samples': 4, 'avg_passage_len': 2, 'has_box_ratio': 0.00},
    '듣기-할말(15)': {'samples': 1, 'avg_passage_len': 7, 'has_box_ratio': 0.00},
    '듣기-할일(5)': {'samples': 1, 'avg_passage_len': 0, 'has_box_ratio': 0.00},
    '목적(18)': {'samples': 1, 'avg_passage_len': 55, 'has_box_ratio': 1.00},
    '무관문장(35)': {'samples': 1, 'avg_passage_len': 0, 'has_box_ratio': 0.00},
    '문장삽입(38)': {'samples': 1, 'avg_passage_len': 335, 'has_box_ratio': 0.00},
    '문장삽입(39)': {'samples': 1, 'avg_passage_len': 167, 'has_box_ratio': 1.00},
    '밑줄함의(21)': {'samples': 1, 'avg_passage_len': 986, 'has_box_ratio': 0.00},
    '빈칸-단어(30)': {'samples': 5, 'avg_passage_len': 17, 'has_box_ratio': 0.00},
    '순서배열(36)': {'samples': 1, 'avg_passage_len': 1172, 'has_box_ratio': 0.00},
    '순서배열(37)': {'samples': 1, 'avg_passage_len': 1224, 'has_box_ratio': 0.00},
    '심경(19)': {'samples': 1, 'avg_passage_len': 697, 'has_box_ratio': 0.00},
    '안내문(27)': {'samples': 1, 'avg_passage_len': 1236, 'has_box_ratio': 0.00},
    '어법(28)': {'samples': 1, 'avg_passage_len': 1286, 'has_box_ratio': 0.00},
    '어휘(29)': {'samples': 1, 'avg_passage_len': 0, 'has_box_ratio': 0.00},
    '요약문(40)': {'samples': 1, 'avg_passage_len': 221, 'has_box_ratio': 1.00},
    '요지(22)': {'samples': 1, 'avg_passage_len': 931, 'has_box_ratio': 0.00},
    '장문독해(43-45)': {'samples': 3, 'avg_passage_len': 0, 'has_box_ratio': 0.00},
    '장문어법(41-42)': {'samples': 2, 'avg_passage_len': 0, 'has_box_ratio': 0.00},
    '제목(24)': {'samples': 1, 'avg_passage_len': 844, 'has_box_ratio': 0.00},
    '주장(20)': {'samples': 1, 'avg_passage_len': 782, 'has_box_ratio': 0.00},
    '주제(23)': {'samples': 1, 'avg_passage_len': 920, 'has_box_ratio': 0.00},
}
