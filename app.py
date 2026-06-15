import streamlit as st

st.set_page_config(page_title="Susun Kata Jepang - Bab 10", layout="centered")

# --- DATABASE SOAL LOKAL (BAB 10 - BERDASARKAN SOURCE PDF) ---
if "database_soal" not in st.session_state:
    st.session_state.database_soal = [
        # === POLA 1: 命令(しろ) / 禁止(~な) ===
        {
            "id": 1,
            "pola": "Bagian 1: 命令(しろ)・禁止(~な) (Perintah Kuat / Larangan Keras)",
            "kanji": "監督「走れ、走れ！」",
            "hiragana": "かんとく 「 はしれ 、 はしれ ！ 」",
            "arti": "(Di pertandingan) Pelatih: 'Lari, lari!'",
            "kunci": ["監督", "「", "走れ", "、", "走れ", "！」"],
            "soal": ["走れ", "監督", "、", "！」", "「", "走れ"]
        },
        {
            "id": 2,
            "pola": "Bagian 1: 命令(しろ)・禁止(~な) (Perintah Kuat / Larangan Keras)",
            "kanji": "犬に「降りろ。」と命令した。",
            "hiragana": "いぬ に 「 おりろ 。 」 と めいれい した 。",
            "arti": "Memerintah kepada anjing, 'Turun!'.",
            "kunci": ["犬に", "「", "降りろ", "。", "」と", "命令した", "。"],
            "soal": ["」と", "降りろ", "犬に", "命令した", "「", "。", "。"]
        },
        {
            "id": 3,
            "pola": "Bagian 1: 命令(しろ)・禁止(~な) (Perintah Kuat / Larangan Keras)",
            "kanji": "立て札に「スピードを出すな！」と書いてある。",
            "hiragana": "たてふだ に 「 すぴーど を だすな ！ 」 と かいて ある 。",
            "arti": "Di papan pengumuman tertulis, 'Jangan mengebut!'.",
            "kunci": ["立て札に", "「", "スピード", "を", "出すな", "！」と", "書いてある", "。"],
            "soal": ["を", "書いてある", "「", "スピード", "出すな", "立て札に", "！」と", "。"]
        },
        {
            "id": 4,
            "pola": "Bagian 1: 命令(しろ)・禁止(~な) (Perintah Kuat / Larangan Keras)",
            "kanji": "父は医者にお酒を飲むなと言われている。",
            "hiragana": "ちち は いしゃ に おさけ を のむ な と いわれている 。",
            "arti": "Ayah dilarang oleh dokter untuk minum minuman keras (alkohol).",
            "kunci": ["父は", "医者に", "お酒", "を", "飲むな", "と", "言われている", "。"],
            "soal": ["飲むな", "を", "医者に", "言われている", "お酒", "父は", "と", "。"]
        },
        # === POLA 2: ～こと ===
        {
            "id": 5,
            "pola": "Bagian 2: ～こと (Instruksi / Aturan Tertulis)",
            "kanji": "レポートは来週月曜日に必ず出すこと。遅れないこと。",
            "hiragana": "れぽーとおは らいしゅう げつようび に かならず だす こと 。 おくれない こと 。",
            "arti": "Laporan harus dikumpulkan hari Senin depan tanpa gagal. Jangan terlambat.",
            "kunci": ["レポートは", "来週月曜日に", "必ず", "出すこと", "。", "遅れないこと", "。"],
            "soal": ["必ず", "遅れないこと", "来週月曜日に", "出すこと", "レポートは", "。", "。"]
        },
        {
            "id": 6,
            "pola": "Bagian 2: ～こと (Instruksi / Aturan Tertulis)",
            "kanji": "申込書を書く前に注意書きをよく読むこと。",
            "hiragana": "もうしこみしょ を かく まえ に ちゅういがき を よく よむ こと 。",
            "arti": "Bacalah petunjuk catatan dengan saksama sebelum mengisi formulir pendaftaran.",
            "kunci": ["申込書を", "書く前に", "注意書き", "を", "よく読むこと", "。"],
            "soal": ["よく読むこと", "を", "書く前に", "注意書き", "申込書を", "。"]
        },
        {
            "id": 7,
            "pola": "Bagian 2: ～こと (Instruksi / Aturan Tertulis)",
            "kanji": "危ないからこの川で泳がないこと。",
            "hiragana": "あぶない から この かわ で およがない こと 。",
            "arti": "Karena berbahaya, dilarang berenang di sungai ini.",
            "kunci": ["危ないから", "この川で", "泳がないこと", "。"],
            "soal": ["泳がないこと", "この川で", "危ないから", "。"]
        },
        # === POLA 3: ～べきだ・～べきではない ===
        {
            "id": 8,
            "pola": "Bagian 3: ～べきだ・～べきではない (Sudah Seharusnya / Tidak Boleh)",
            "kanji": "これは大事なことですから、もう少し話し合ってから決めるべきだと思いますよ。",
            "hiragana": "これ は だいじ な こと です から 、 もうすこし はなしあって から きめる べき だ と おもいます よ 。",
            "arti": "Karena ini masalah penting, saya rasa kita seharusnya memutuskan setelah berdiskusi sedikit lagi.",
            "kunci": ["これは", "大事なことですから", "、", "もう少し", "話し合ってから", "決めるべきだ", "と", "思いますよ", "。"],
            "soal": ["話し合ってから", "決めるべきだ", "大事なことですから", "もう少し", "これは", "思いますよ", "と", "、", "。"]
        },
        {
            "id": 9,
            "pola": "Bagian 3: ～べきだ・～べきではない (Sudah Seharusnya / Tidak Boleh)",
            "kanji": "仕事はたくさんあるが、まず、今日中にやるべきことから始めよう。",
            "hiragana": "しごと は たくさん ある が 、 まず 、 きょうじゅう に やる べき こと から はじめよう 。",
            "arti": "Pekerjaan ada banyak, tapi mari kita mulai dari hal yang seharusnya dikerjakan hari ini.",
            "kunci": ["仕事は", "たくさんあるが", "、", "まず", "、", "今日中に", "やるべきこと", "から", "始めよう", "。"],
            "soal": ["今日中に", "まず", "たくさんあるが", "始めよう", "仕事は", "やるべきこと", "から", "、", "、", "。"]
        },
        {
            "id": 10,
            "pola": "Bagian 3: ～べきだ・～べきではない (Sudah Seharusnya / Tidak Boleh)",
            "kanji": "せっかく入った会社なのだから、簡単に辞めるべきではない。",
            "hiragana": "せっかく はいった かいしゃ な の だ から 、 かんたん に やめる べき ではない 。",
            "arti": "Karena sudah susah payah masuk ke perusahaan ini, tidak seharusanya mengundurkan diri begitu saja.",
            "kunci": ["せっかく", "入った会社なのだから", "、", "簡単に", "辞めるべきではない", "。"],
            "soal": ["簡単に", "入った会社なのだ加羅", "辞めるべきではない", "せっかく", "、", "。"]
        },
        {
            "id": 11,
            "pola": "Bagian 3: ～べきだ・～べきではない (Sudah Seharusnya / Tidak Boleh)",
            "kanji": "子どもは夜遅くまで外にいるべきではない。",
            "hiragana": "こども は よる おそく まで そと に いる べき ではない 。",
            "arti": "Anak-anak tidak seharusnya berada di luar rumah sampai larut malam.",
            "kunci": ["子どもは", "夜遅くまで", "外に", "いるべきではない", "。"],
            "soal": ["外に", "夜遅くまで", "いるべきではない", "子どもは", "。"]
        },
        {
            "id": 12,
            "pola": "Bagian 3: ～べきだ・～べきではない (Sudah Seharusnya / Tidak Boleh)",
            "kanji": "あしたまでのレポートがまだ書き終わらない。もっと早くから始めるべきだった。",
            "hiragana": "あした まで の れぽーと が まだ かきおわらない 。 もっと はやく から はじめる べき だった 。",
            "arti": "Laporan untuk besok belum selesai ditulis. Seharusnya saya memulainya lebih awal (penyesalan).",
            "kunci": ["あしたまでの", "レポートが", "まだ", "書き終わらない", "。", "もっと", "早くから", "始めるべきだった", "。"],
            "soal": ["もっと", "書き終わらない", "始めるべきだった", "レポートが", "あしたまでの", "早くから", "まだ", "。", "。"]
        },
        # === POLA 4: ～たらどうか ===
        {
            "id": 13,
            "pola": "Bagian 4: ～たらどうか (Bagaimana Kalau / Saran)",
            "kanji": "体のことが心配なら、一度健康診断を受けたらどうでしょうか。",
            "hiragana": "からだ の こと が しんぱい なら 、 いちど けんこうしんだん を うけたら どう でしょう か 。",
            "arti": "Jika kamu khawatir tentang kondisi tubuhmu, bagaimana kalau mencoba tes kesehatan sekali?",
            "kunci": ["体のことが", "心配なら", "、", "一度", "健康診断", "を", "受けたらどうでしょうか", "。"],
            "soal": ["一度", "受けたらどうでしょうか", "心配なら", "を", "健康診断", "体のことが", "、", "。"]
        },
        {
            "id": 14,
            "pola": "Bagian 4: ～たらどうか (Bagaimana Kalau / Saran)",
            "kanji": "疲れているみたいですね。少し休んだらどうですか。",
            "hiragana": "つかれている みたい です ね 。 すこし やすんだら どう です か 。",
            "arti": "Sepertinya kamu lelah ya. Bagaimana kalau beristirahat sebentar?",
            "kunci": ["疲れているみたいですね", "。", "少し", "休んだらどうですか", "。"],
            "soal": ["少し", "休んだらどうですか", "疲れているみたいですね", "。", "。"]
        },
        {
            "id": 15,
            "pola": "Bagian 4: ～たらどうか (Bagaimana Kalau / Saran)",
            "kanji": "迷惑メールが多いの？じゃ、アドレスを変えたらどう？",
            "hiragana": "めいわく めーる が おおい の ？ じゃ 、 あどれす を かえたら どう ？",
            "arti": "Banyak email spam ya? Kalau begitu, bagaimana kalau ganti alamat email saja?",
            "kunci": ["迷惑メールが", "多いの？", "じゃ、", "アドレス", "を", "変えたらどう？"],
            "soal": ["アドレス", "じゃ、", "変えたらどう？", "多いの？", "を", "迷惑メールが"]
        },
        {
            "id": 16,
            "pola": "Bagian 4: ～たらどうか (Bagaimana Kalau / Saran)",
            "kanji": "悪いのはそっちですよ。一言謝ったらどうですか。",
            "hiragana": "わるい の は そっち です よ 。 ひとこと あやまったら どう です か 。",
            "arti": "Yang salah itu pihakmu, lho. Bagaimana kalau kamu meminta maaf sepatah kata?",
            "kunci": ["悪いのは", "そっちですよ", "。", "一言", "謝ったらどうですか", "。"],
            "soal": ["一言", "そっちですよ", "謝ったらどうですか", "悪いのは", "。", "。"]
        }
    ]

# --- STATE MANAGEMENT ---
if "index_soal" not in st.session_state:
    st.session_state.index_soal = 0
if "jawaban_user" not in st.session_state:
    st.session_state.jawaban_user = []
if "bank_kata" not in st.session_state:
    st.session_state.bank_kata = []
if "status_periksa" not in st.session_state:
    st.session_state.status_periksa = False

soal_sekarang = st.session_state.database_soal[st.session_state.index_soal]

if not st.session_state.bank_kata and not st.session_state.jawaban_user:
    st.session_state.bank_kata = [{"id": i, "teks": kata, "dipakai": False} for i, kata in enumerate(soal_sekarang["soal"])]

# --- INJEKSI CSS FLEXBOX MURNI (ANTI-VERTIKAL KEBANJIRAN) ---
st.markdown("""
<style>
    /* Menyembunyikan elemen judul radio / pil jika ada */
    div[data-testid="stStatusWidget"] + div div[data-testid="stWidgetLabel"] {
        display: none;
    }
    
    /* Box Info Atas */
    .info-box {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 12px;
        border-left: 5px solid #ff4b4b;
        margin-bottom: 20px;
    }
    .text-bunpou { font-size: 1.02rem; font-weight: bold; color: #ff4b4b; margin: 0 0 5px 0; }
    .text-arti { font-size: 1.15rem; font-weight: bold; color: #1a1a1a; margin: 0; }

    /* WADAH UTAMA KATA: Memaksa Berjejer ke Samping */
    .flex-container-jepang {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: wrap !important;
        align-items: center !important;
        justify-content: flex-start !important;
        gap: 8px !important;
        width: 100% !important;
        padding: 12px;
        background-color: #ffffff;
        border-radius: 12px;
        min-height: 60px;
    }
    
    /* Wadah khusus papan susunan kalimat */
    .papan-susunan {
        border: 2px dashed #cccccc;
        background-color: #fafafa;
        margin-bottom: 25px;
    }

    /* Penyetelan Tombol Kustom Streamlit di dalam wadah HTML */
    div.element-container div.stButton > button {
        border-radius: 14px !important;
        font-weight: bold !important;
        padding: 6px 12px !important;
        background-color: #ffffff !important;
        color: #333333 !important;
        border: 1px solid #dcdcdc !important;
        box-shadow: 0px 2px 4px rgba(0,0,0,0.05) !important;
        transition: all 0.2s ease;
    }
    
    div.element-container div.stButton > button:active {
        transform: scale(0.95);
    }
    
    /* Evaluasi Hasil Kotak Indeks Posisi */
    .badge-pos-container {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: wrap !important;
        gap: 8px !important;
        margin-top: 10px;
    }
    .badge-pos-correct {
        background-color: #d4edda;
        color: #155724;
        padding: 8px 12px;
        border-radius: 10px;
        font-weight: bold;
        display: inline-flex;
        flex-direction: column;
        align-items: center;
        border: 2px solid #c3e6cb;
        text-align: center;
    }
    .badge-pos-wrong {
        background-color: #f8d7da;
        color: #721c24;
        padding: 8px 12px;
        border-radius: 10px;
        font-weight: bold;
        display: inline-flex;
        flex-direction: column;
        align-items: center;
        border: 2px solid #f5c6cb;
        text-align: center;
    }
    .sub-index {
        font-size: 0.72rem;
        display: block;
        color: #555555;
        margin-top: 3px;
        border-top: 1px dashed rgba(0,0,0,0.15);
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

st.title("🦉 Bunpou Master - Bab 10")
st.caption(f"Soal {st.session_state.index_soal + 1} dari {len(st.session_state.database_soal)}")
st.markdown("---")

st.markdown(f"""
<div class="info-box">
    <p class="text-bunpou">📖 {soal_sekarang['pola']}</p>
    <p class="text-arti">🇮🇩 {soal_sekarang['arti']}</p>
</div>
""", unsafe_allow_html=True)

# --- PANEL INTERAKTIF BERJEJER KE SAMPING (CSS-GRID-FLEX INTERACTION) ---
st.write("### Kalimat Susunanmu:")

# Papan Susunan Jawaban (Horizontal Flex)
if not st.session_state.jawaban_user:
    st.markdown("<div style='color:#aaaaaa; font-style:italic; border:2px dashed #ddd; padding:15px; border-radius:12px; margin-bottom:20px;'>Klik kata-kata di bawah untuk mulai menyusun kalimat...</div>", unsafe_allow_html=True)
else:
    # Menggunakan kolom horizontal statis dinamis untuk memaksa jejeran tombol ke samping
    cols_jawaban = st.columns(max(len(st.session_state.jawaban_user), 2))
    for idx, item in enumerate(st.session_state.jawaban_user):
        with cols_jawaban[idx]:
            if st.button(item["teks"], key=f"papan_{idx}_{item['id']}", use_container_width=True):
                # Kembalikan ke Bank Kata
                kata_dicopot = st.session_state.jawaban_user.pop(idx)
                for kata_bank in st.session_state.bank_kata:
                    if kata_bank["id"] == kata_dicopot["id"]:
                        kata_bank["dipakai"] = False
                st.rerun()

st.write("### Pilihan Kata:")
# Papan Pilihan Kata Asal (Horizontal Grid 4 Kolom Maksimal di HP agar hemat ruang)
cols_pilihan = st.columns(4)
for idx, item in enumerate(st.session_state.bank_kata):
    posisi_kolom = idx % 4
    with cols_pilihan[posisi_kolom]:
        if item["dipakai"]:
            st.button(" ", key=f"blank_{item['id']}", disabled=True, use_container_width=True)
        else:
            if st.button(item["teks"], key=f"pilih_{item['id']}", use_container_width=True):
                item["dipakai"] = True
                st.session_state.jawaban_user.append(item)
                st.rerun()

st.markdown("<br><hr>", unsafe_allow_html=True)

# --- TOMBOL NAVIGASI UTAMA ---
col1, col2, col3 = st.columns([1, 1.2, 1])
with col1:
    if st.button("RESET 🔄", use_container_width=True):
        st.session_state.jawaban_user = []
        for kata in st.session_state.bank_kata:
            kata["dipakai"] = False
        st.session_state.status_periksa = False
        st.rerun()
with col2:
    if st.button("PERIKSA ✅", type="primary", use_container_width=True):
        st.session_state.status_periksa = True
with col3:
    if st.button("LANJUT ➡️", use_container_width=True):
        st.session_state.index_soal = (st.session_state.index_soal + 1) % len(st.session_state.database_soal)
        st.session_state.jawaban_user = []
        st.session_state.bank_kata = []
        st.session_state.status_periksa = False
        st.rerun()

# --- EVALUASI ANALISIS PRESISI POSISI INDEKS ---
if st.session_state.status_periksa:
    user_strings = [x["teks"] for x in st.session_state.jawaban_user]
    kunci_strings = soal_sekarang["kunci"]
    
    user_joined = "".join(user_strings).replace(" ", "").replace("、", "").replace("。", "").replace("「", "").replace("」", "").replace("！", "").replace("？", "")
    kunci_joined = "".join(kunci_strings).replace(" ", "").replace("、", "").replace("。", "").replace("「", "").replace("」", "").replace("！", "").replace("？", "")

    if user_joined == kunci_joined:
        st.success(f"🎉 **正解 (Benar)!** Susunan posisi kata kamu sudah sempurna!\n\n"
                   f"**Kanji:** {soal_sekarang['kanji']}\n\n"
                   f"**Hiragana:** {soal_sekarang['hiragana']}\n\n"
                   f"**Arti:** {soal_sekarang['arti']}")
    else:
        st.error("❌ **残念 (Kurang Tepat). Analisis Posisi Urutan Kata:**")
        
        html_koreksi = "<div class='badge-pos-container'>"
        max_len = max(len(user_strings), len(kunci_strings))
        
        for idx in range(max_len):
            if idx < len(user_strings):
                kata_user = user_strings[idx]
                
                # Cek presisi posisi indeks mutlak
                if idx < len(kunci_strings) and kata_user == kunci_strings[idx]:
                    html_koreksi += f"""
                    <div class='badge-pos-correct'>
                        {kata_user}
                        <span class='sub-index'>Posisi {idx+1}</span>
                    </div> """
                else:
                    html_koreksi += f"""
                    <div class='badge-pos-wrong'>
                        {kata_user}
                        <span class='sub-index'>Posisi {idx+1}</span>
                    </div> """
            else:
                html_koreksi += f"""
                <div class='badge-pos-wrong' style='border: 2px dashed #ff4b4b; background-color:#fff5f5; color:#ff4b4b;'>
                    (Kosong)
                    <span class='sub-index'>Posisi {idx+1}</span>
                </div> """
                
        html_koreksi += "</div>"
        
        st.markdown(html_koreksi, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown(f"**💡 Panduan Urutan yang Benar:**\n\n`{' ➔ '.join(soal_sekarang['kunci'])}`\n\n"
                    f"**Kanji:**\n{soal_sekarang['kanji']}\n\n"
                    f"**Hiragana:**\n{soal_sekarang['hiragana']}\n\n"
                    f"**Arti:**\n{soal_sekarang['arti']}")
