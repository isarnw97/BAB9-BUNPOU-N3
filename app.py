import streamlit as st

st.set_page_config(page_title="Susun Kata Jepang - Bab 9", layout="centered")

# --- DATABASE SOAL LOKAL (BAB 9) ---
if "database_soal" not in st.session_state:
    st.session_state.database_soal = [
        # --- Pola 1: 〜という点から見ると / 〜という点から考えて ---
        {
            "id": 1, 
            "pola": "Pola 1: 〜点から見ると ・ 〜点から考えて (Dilihat dari sudut pandang... / Mempertimbangkan poin...)",
            "kanji": "経済的な点から見ると、この計画はあまり現実的ではないようだ。",
            "hiragana": "けいざいてきな てん から みると 、 この けいかく は あまり げんじつてき で は ない よう だ 。",
            "arti": "Dilihat dari sudut pandang ekonomi, rencana ini tampaknya tidak begitu realistis.",
            "kunci": ["経済的な", "点", "から", "見ると", "、", "この", "計画", "は", "あまり", "現実的", "では", "ない", "ようだ", "。"],
            "soal": ["経済的な", "点", "から", "見ると", "、", "この", "計画", "は", "あまり", "理想的", "では", "ない", "ようだ", "。"]
        },
        {
            "id": 2, 
            "pola": "Pola 1: 〜点から見ると ・ 〜点から考えて (Dilihat dari sudut pandang... / Mempertimbangkan poin...)",
            "kanji": "健康という点から考えても、毎日の十分な睡眠は不可欠です。",
            "hiragana": "けんこう という てん から かんがえて も 、 まいにち の じゅうぶんな すいみん は ふかけつ です 。",
            "arti": "Mempertimbangkan dari poin kesehatan pun, tidur yang cukup setiap hari adalah hal yang mutlak diperlukan.",
            "kunci": ["健康", "という", "点", "から", "考えて", "も", "、", "毎日", "の", "十分な", "睡眠", "は", "不可欠", "です", "。"],
            "soal": ["健康", "という", "点", "から", "考えて", "も", "、", "毎日", "の", "十分な", "睡眠", "は", "不必要", "です", "。"]
        },
        # --- Pola 2: 〜うえに ---
        {
            "id": 3, 
            "pola": "Pola 2: 〜うえに (Selain... juga... / Sudah... ditambah lagi...)",
            "kanji": "この町は、物価が安いうえに治安が良いのでとても住みやすい。",
            "hiragana": "この まち は 、 ぶっか が やすい うえ に ちあん が よい ので とても すみやすい 。",
            "arti": "Kota ini, selain harga barangnya murah, keamanan lingkungannya juga bagus sehingga sangat enak untuk ditinggali.",
            "kunci": ["この", "町", "は", "、", "物価", "が", "安い", "うえに", "治安", "が", "良い", "ので", "とても", "住みやすい", "。"],
            "soal": ["この", "町", "は", "、", "物価", "が", "高い", "うえに", "治安", "が", "良い", "ので", "とても", "住みやすい", "。"]
        },
        {
            "id": 4, 
            "pola": "Pola 2: 〜うえに (Selain... juga... / Sudah... ditambah lagi...)",
            "kanji": "昨日は道に迷ったうえに雨に降られて、本当に大変な一日だった。",
            "hiragana": "きのう は みち に まよった うえ に あめ に ふられて 、 ほんとう に たいへんな いちにち だった 。",
            "arti": "Hari kemarin sudah tersesat di jalan, ditambah lagi diguyur hujan, benar-benar hari yang melelahkan.",
            "kunci": ["昨日", "は", "道", "に", "迷った", "うえに", "雨", "に", "降られて", "、", "本当に", "大変な", "一日", "だった", "。"],
            "soal": ["昨日", "は", "道", "に", "迷った", "うえに", "晴れ", "に", "降られて", "、", "本当に", "大変な", "一日", "だった", "。"]
        },
        # --- Pola 3: 〜うちに / 〜ないうちに ---
        {
            "id": 5, 
            "pola": "Pola 3: 〜うちに ・ 〜ないうちに (Selagi... / Mumpung... / Sebelum...)",
            "kanji": "スープが温かいうちに早く召し上がってください。",
            "hiragana": "スープ が あたたかい うち に はやく めしあがってください 。",
            "arti": "Mumpung supnya masih hangat, silakan segera dinikmati.",
            "kunci": ["スープ", "が", "温かい", "うちに", "早く", "召し上がってください", "。"],
            "soal": ["スープ", "が", "冷たい", "うちに", "早く", "召し上がってください", "。"]
        },
        {
            "id": 6, 
            "pola": "Pola 3: 〜うちに ・ 〜ないうちに (Selagi... / Mumpung... / Sebelum...)",
            "kanji": "暗くならないうちに、山を下りて家へ帰ることにしよう。",
            "hiragana": "くらく ならない うち に 、 やま を おりて いえ へ かえる こと に しよう 。",
            "arti": "Sebelum hari menjadi gelap, mari kita turun gunung dan memutuskan pulang ke rumah.",
            "kunci": ["暗く", "ならない", "うちに", "、", "山", "を", "下りて", "家", "へ", "帰る", "ことにしよう", "。"],
            "soal": ["明るく", "ならない", "うちに", "、", "山", "を", "下りて", "家", "へ", "帰る", "ことにしよう", "。"]
        },
        # --- Pola 4: 〜にかわって / 〜にかわり ---
        {
            "id": 7, 
            "pola": "Pola 4: 〜にかわって (Sebagai pengganti... / Mewakili...)",
            "kanji": "病気の社長にかわって、副社長が会議の挨拶をすることになりました。",
            "hiragana": "びょうき の しゃちょう に かわって 、 ふくしゃちょう が かいぎ の あいさつ を する こと に なりました 。",
            "arti": "Mewakili direktur yang sedang sakit, wakil direktur diputuskan untuk menyampaikan salam di rapat.",
            "kunci": ["病気", "の", "社長", "に", "かわって", "、", "副社長", "が", "会議", "の", "挨拶", "を", "する", "ことに", "なりました", "。"],
            "soal": ["元気", "の", "社長", "に", "かわって", "、", "副社長", "が", "会議", "の", "挨拶", "を", "する", "ことに", "なりました", "。"]
        },
        # --- Pola 5: 〜通して / 〜通じて ---
        {
            "id": 8, 
            "pola": "Pola 5: 〜通して ・ 〜通じて (Melalui... / Sepanjang...)",
            "kanji": "私たちは共通の趣味を通して、多くの素晴らしい友人に出会った。",
            "hiragana": "わたしたち は きょうつう の しゅみ を とおして 、 おおく の すばらしい ゆうじん に であった 。",
            "arti": "Kami melalui hobi yang sama, telah bertemu dengan banyak teman yang luar biasa.",
            "kunci": ["私たち", "は", "共通", "の", "趣味", "を", "通して", "、", "多く", "の", "素晴らしい", "友人", "に", "出会った", "。"],
            "soal": ["私たち", "は", "共通", "の", "趣味", "を", "通して", "、", "少なく", "の", "素晴らしい", "友人", "に", "出会った", "。"]
        },
        {
            "id": 9, 
            "pola": "Pola 5: 〜通して ・ 〜通じて (Melalui... / Sepanjang...)",
            "kanji": "この地域は一年を通じて、比較的温暖な気候が続きます。",
            "hiragana": "この ちいき は いちねん を つうじて 、 ひかくてき おんだんな きこう が つづきます 。",
            "arti": "Wilayah ini sepanjang tahun, berlanjut dengan iklim yang relatif hangat.",
            "kunci": ["この", "地域", "は", "一年", "を", "通じて", "、", "比較的", "温暖な", "気候", "が", "続きます", "。"],
            "soal": ["この", "地域", "は", "一年", "を", "通じて", "、", "比較的", "寒冷な", "気候", "が", "続きます", "。"]
        }
    ]

# --- INISIALISASI STATE ---
if "index_soal" not in st.session_state:
    st.session_state.index_soal = 0
if "jawaban_user" not in st.session_state:
    st.session_state.jawaban_user = []
if "bank_kata" not in st.session_state:
    st.session_state.bank_kata = []
if "status_periksa" not in st.session_state:
    st.session_state.status_periksa = False
if "idx_kata_dipilih" not in st.session_state:
    st.session_state.idx_kata_dipilih = None
if "mode_tukar" not in st.session_state:
    st.session_state.mode_tukar = False

soal_sekarang = st.session_state.database_soal[st.session_state.index_soal]

if not st.session_state.bank_kata and not st.session_state.jawaban_user:
    st.session_state.bank_kata = [{"id": i, "teks": kata, "dipakai": False} for i, kata in enumerate(soal_sekarang["soal"])]

# --- STYLING CSS ---
st.markdown("""
<style>
    div[data-testid="stStatusWidget"] + div div[data-testid="stWidgetLabel"] {
        display: none;
    }
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: wrap !important;
        gap: 6px !important;
    }
    [data-testid="stHorizontalBlock"] > div {
        flex: 1 1 22% !important; 
        min-width: 70px !important; 
    }
    .info-box {
        background-color: #e8f4fd;
        padding: 15px;
        border-radius: 12px;
        border-left: 5px solid #1fa2ff;
        margin-bottom: 20px;
    }
    .text-bunpou { font-size: 1.05rem; font-weight: bold; color: #1fa2ff; margin: 0 0 6px 0; }
    .text-arti { font-size: 1.2rem; font-weight: bold; color: #1a1a1a; margin: 0; }
    
    div.stButton > button {
        border-radius: 12px !important;
        font-weight: bold !important;
        padding: 6px 10px !important;
    }
    .swap-indicator {
        background-color: #e6fffa;
        border: 1px dashed #319795;
        padding: 10px;
        border-radius: 8px;
        color: #234e52;
        font-weight: bold;
        margin-bottom: 10px;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

st.title("🦉 Bunpou Master - Bab 9")
st.caption(f"Soal {st.session_state.index_soal + 1} dari {len(st.session_state.database_soal)}")
st.markdown("---")

st.markdown(f"""
<div class="info-box">
    <p class="text-bunpou">📖 {soal_sekarang['pola']}</p>
    <p class="text-arti">🇮🇩 {soal_sekarang['arti']}</p>
</div>
""", unsafe_allow_html=True)

# --- MENU UTAMA INTERAKTIF (FRAGMENT) ---
@st.fragment
def render_kuis_lengkap():
    st.write("### Kalimat Susunanmu:")
    
    mode = st.radio(
        "Aksi Sentuhan Papan:",
        ["Copot Kata (Normal)", "Tukar Posisi 2 Kata 🔄"],
        horizontal=True,
        label_visibility="collapsed"
    )
    
    if mode == "Tukar Posisi 2 Kata 🔄":
        st.session_state.mode_tukar = True
        if st.session_state.idx_kata_dipilih is not None:
            kata_terpilih = st.session_state.jawaban_user[st.session_state.idx_kata_dipilih]["teks"]
            st.markdown(f'<div class="swap-indicator">📍 Kata [{kata_terpilih}] terpilih. Sekarang klik kata tujuan untuk bertukar posisi!</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="swap-indicator">💡 Klik kata pertama yang ingin ditukar posisinya...</div>', unsafe_allow_html=True)
    else:
        st.session_state.mode_tukar = False
        st.session_state.idx_kata_dipilih = None

    if not st.session_state.jawaban_user:
        st.markdown("<div style='border-bottom: 2px solid #e5e5e5; padding-bottom: 15px; margin-bottom: 20px; color:#aaaaaa; font-style:italic;'>Klik kata di bawah untuk mulai menyusun...</div>", unsafe_allow_html=True)
    else:
        opsi_papan = [f"{idx}. {item['teks']}" for idx, item in enumerate(st.session_state.jawaban_user)]
        format_papan = {opt: opt.split(". ", 1)[1] for opt in opsi_papan}
        
        klik_papan = st.pills(
            label="Papan Jawaban",
            options=opsi_papan,
            format_func=lambda x: format_papan[x],
            selection_mode="single",
            label_visibility="collapsed"
        )
        st.markdown("<div style='border-bottom: 2px solid #e5e5e5; margin-top: -10px; margin-bottom: 25px;'></div>", unsafe_allow_html=True)
        
        if klik_papan:
            idx_klik = int(klik_papan.split(". ")[0])
            
            if st.session_state.mode_tukar:
                if st.session_state.idx_kata_dipilih is None:
                    st.session_state.idx_kata_dipilih = idx_klik
                    st.rerun()
                else:
                    idx1 = st.session_state.idx_kata_dipilih
                    idx2 = idx_klik
                    if idx1 != idx2:
                        st.session_state.jawaban_user[idx1], st.session_state.jawaban_user[idx2] = st.session_state.jawaban_user[idx2], st.session_state.jawaban_user[idx1]
                    st.session_state.idx_kata_dipilih = None
                    st.rerun()
            else:
                kata_dicopot = st.session_state.jawaban_user.pop(idx_klik)
                for kata_bank in st.session_state.bank_kata:
                    if kata_bank["id"] == kata_dicopot["id"]:
                        kata_bank["dipakai"] = False
                st.rerun()

    st.write("### Pilihan Kata:")
    cols_pilihan = st.columns(4)
    for idx, item in enumerate(st.session_state.bank_kata):
        posisi_kolom = idx % 4
        with cols_pilihan[posisi_kolom]:
            if item["dipakai"]:
                st.button(" ", key=f"disabled_{item['id']}", disabled=True, use_container_width=True)
            else:
                if st.button(item["teks"], key=f"pilih_{item['id']}", use_container_width=True):
                    item["dipakai"] = True
                    st.session_state.jawaban_user.append(item)
                    st.rerun()

render_kuis_lengkap()

st.markdown("<br><hr>", unsafe_allow_html=True)

# --- TOMBOL NAVIGASI UTAMA ---
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Reset 🔄", use_container_width=True):
        st.session_state.jawaban_user = []
        for kata in st.session_state.bank_kata:
            kata["dipakai"] = False
        st.session_state.idx_kata_dipilih = None
        st.session_state.status_periksa = False
        st.rerun()
with col2:
    if st.button("PERIKSA ✅", type="primary", use_container_width=True):
        st.session_state.status_periksa = True
with col3:
    if st.button("Lanjut ➡️", use_container_width=True):
        st.session_state.index_soal = (st.session_state.index_soal + 1) % len(st.session_state.database_soal)
        st.session_state.jawaban_user = []
        st.session_state.bank_kata = []
        st.session_state.idx_kata_dipilih = None
        st.session_state.status_periksa = False
        st.rerun()

# --- VALIDASI JAWABAN ---
if st.session_state.status_periksa:
    user_strings = [x["teks"] for x in st.session_state.jawaban_user]
    
    user_joined = "".join(user_strings).replace(" ", "").replace("、", "").replace("。", "")
    kunci_joined = "".join(soal_sekarang["kunci"]).replace(" ", "").replace("、", "").replace("。", "")

    # Normalisasi otomatis untuk variasi pengecoh kosakata di Bab 9
    user_joined = user_joined.replace("理想的", "現実的").replace("不必要", "不可欠").replace("高い", "安い").replace("晴れ", "雨").replace("冷たい", "温かい").replace("明るく", "暗く").replace("元気", "病気").replace("少なく", "多く").replace("寒冷な", "温暖な")
    kunci_joined = kunci_joined.replace("理想的", "現実的").replace("不必要", "不可欠").replace("高い", "安い").replace("晴れ", "雨").replace("冷たい", "温かい").replace("明るく", "暗く").replace("元気", "病気").replace("少なく", "多く").replace("寒冷な", "温暖な")

    if user_joined == kunci_joined:
        st.success(f"🎉 **正解 (Benar)!** Susunan bunpou kamu sudah sempurna!\n\n"
                   f"**Kanji:**\n{soal_sekarang['kanji']}\n\n"
                   f"**Hiragana:**\n{soal_sekarang['hiragana']}\n\n"
                   f"**Arti:**\n{soal_sekarang['arti']}")
    else:
        st.error(f"❌ **残念 (Kurang Tepat).**\n\n"
                 f"**Susunan yang benar:**\n\n`{' '.join(soal_sekarang['kunci'])}`\n\n"
                 f"**Kanji:**\n{soal_sekarang['kanji']}\n\n"
                 f"**Hiragana:**\n{soal_sekarang['hiragana']}\n\n"
                 f"**Arti:**\n{soal_sekarang['arti']}")
