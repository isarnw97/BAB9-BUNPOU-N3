import streamlit as st
import random

st.set_page_config(page_title="Susun Kata Jepang - Bab 9", layout="centered")

# --- DATABASE SOAL LOKAL LENGKAP (BAB 9 - SOURCED FROM USER INPUT) ---
if "database_soal" not in st.session_state:
    st.session_state.database_soal = [
        # === POLA 1: ～てもらいたい・～ていただきたい・～てほしい ===
        {
            "id": 1,
            "pola": "Bagian 1: ～てもらいたい・～ていただきたい・～てほしい (Keinginan atas tindakan orang lain)",
            "kanji": "だれかに自分の悩みを聞いてもらいたいと思うことがあります。",
            "hiragana": "だれか に じぶん の なやみ を きいて もらいたい と おもう こと が あります 。",
            "arti": "Ada kalanya saya merasa ingin seseorang mendengarkan keluh kesah saya.",
            "kunci": ["だれかに", "自分の", "悩みを", "聞いて", "もらいたいと", "思うことが", "あります", "。"]
        },
        {
            "id": 2,
            "pola": "Bagian 1: ～てもらいたい・～ていただきたい・～てほしい (Keinginan atas tindakan orang lain)",
            "kanji": "この書類、ちょっと見ていただきたいんですが。",
            "hiragana": "この しょるい 、 ちょっと みて いただきたい ん です が 。",
            "arti": "Dokumen ini, saya ingin Anda bersedia meluangkan waktu sebentar untuk melihatnya.",
            "kunci": ["この書類", "、ちょっと", "見ていただきたい", "んですが", "。"]
        },
        {
            "id": 3,
            "pola": "Bagian 1: ～てもらいたい・～ていただきたい・～てほしい (Keinginan atas tindakan orang lain)",
            "kanji": "この仕事はだれにも手伝ってもらいたくない。自分一人でやりたい。",
            "hiragana": "この しごと は だれ に も てつだって もらいたくない 。 じぶん ひとり で やりたい 。",
            "arti": "Pekerjaan ini saya tidak ingin dibantu oleh siapa pun. Saya ingin melakukannya sendiri.",
            "kunci": ["この仕事は", "だれにも", "手伝ってもらいたくない", "。自分一人で", "やりたい", "。"]
        },
        {
            "id": 4,
            "pola": "Bagian 1: ～てもらいたい・～ていただきたい・～てほしい (Keinginan atas tindakan orang lain)",
            "kanji": "ぼくのそばにずっといてほしい。遠くへ行かないでほしい。",
            "hiragana": "ぼく の そば に ずっと いて ほしい 。 とおく へ いかないで ほしい 。",
            "arti": "Aku ingin kamu selalu berada di sisiku sepanjang waktu. Aku tidak ingin kamu pergi jauh.",
            "kunci": ["ぼくの", "そばに", "ずっと", "いてほしい", "。遠くへ", "行かないでほしい", "。"]
        },
        {
            "id": 5,
            "pola": "Bagian 1: ～てもらいたい・～ていただきたい・～てほしい (Keinginan atas tindakan orang lain)",
            "kanji": "この村の自然環境をこれ以上こわさないでほしい。",
            "hiragana": "この むら の しぜん かんきょう を これ いじょう こわさないで ほしい 。",
            "arti": "Saya berharap lingkungan alam di desa ini tidak dirusak lebih jauh lagi.",
            "kunci": ["この村の", "自然環境を", "これ以上", "こわさないでほしい", "。"]
        },
        {
            "id": 6,
            "pola": "Bagian 1: ～てもらいたい・～ていただきたい・～てほしい (Keinginan atas tindakan orang lain)",
            "kanji": "親ももう年を取った。無理はしてほしくない。",
            "hiragana": "おや も もう とし を とった 。 むり は して ほしくない 。",
            "arti": "Orang tua pun sudah berumur. Saya tidak ingin mereka memaksakan diri bekerja keras.",
            "kunci": ["親も", "もう", "年を取った", "。無理は", "してほしくない", "。"]
        },
        # === POLA 2: ～(さ)せてもらいたい・～(さ)せていただきたい・～(さ)せてほしい ===
        {
            "id": 7,
            "pola": "Bagian 2: ～(さ)せてもらいたい・～(さ)せてほしい (Memohon izin melakukan sesuatu)",
            "kanji": "「昼休みが短いよね」「もっとゆっくり昼ご飯を食べさせてもらいたいね」",
            "hiragana": "「 ひるやすみ が みじかい よね 」 「 もっと ゆっくり ひるごはん を たべさせ て もらいたい ね 」",
            "arti": "'Jam istirahat siang pendek ya.' 'Iya ya, rasanya ingin diizinkan makan siang dengan lebih santai.'",
            "kunci": ["「昼休み", "が短い", "よね」", "「もっと", "ゆっくり", "昼ご飯を", "食べさせてもらいたい", "ね」"]
        },
        {
            "id": 8,
            "pola": "Bagian 2: ～(さ)せてもらいたい・～(さ)せてほしい (Memohon izin melakukan sesuatu)",
            "kanji": "店長に言ってみよう。そうだね。",
            "hiragana": "てんちょう に いって みよう 。 そうだね 。",
            "arti": "Mari coba bicarakan dan katakan kepada manajer toko. Benar juga ya.",
            "kunci": ["店長に", "言ってみよう", "。", "そうだね", "。"]
        },
        {
            "id": 9,
            "pola": "Bagian 2: ～(さ)せてもらいたい・～(さ)せてほしい (Memohon izin melakukan sesuatu)",
            "kanji": "今日、入管へ行かなければならないので、早く帰らせていただきたいのですが。",
            "hiragana": "きょう 、 にゅうかん へ いかなければ ならない ので 、 はやく かえらせて いただきたい の です が 。",
            "arti": "Karena hari ini saya harus pergi ke biro imigrasi, jika diizinkan saya ingin pulang lebih awal.",
            "kunci": ["今日", "、入管へ", "行かなければならない", "ので、", "早く", "帰らせていただきたい", "のですが。"]
        },
        {
            "id": 10,
            "pola": "Bagian 2: ～(さ)せてもらいたい・～(さ)せてほしい (Memohon izin melakukan sesuatu)",
            "kanji": "さっき同じことを何度も説明したよ。それ以上は言わせないでもらいたいだよ。",
            "hiragana": "さっき おなじ こと を なんど も せつめい した よ 。 それ いじょう は いわせないで もらいたい だよ 。",
            "arti": "Tadi saya sudah menjelaskan hal yang sama berkali-kali. Tolong jangan buat saya mengatakannya lagi.",
            "kunci": ["さっき", "切に同じ", "ことを", "何度も", "説明したよ", "。それ", "以上は", "言わせないでもらいたい", "だよ。"]
        },
        {
            "id": 11,
            "pola": "Bagian 2: ～(さ)せてもらいたい・～(さ)せてほしい (Memohon izin melakukan sesuatu)",
            "kanji": "わたし、文化祭のポスターは作らせてほしいなあ。",
            "hiragana": "わたし 、 ぶんかさい の ぽすたー は つくらせて ほしい なあ 。",
            "arti": "Aku rasanya ingin diizinkan untuk membuat poster festival budaya nanti.",
            "kunci": ["わたし", "、文化祭の", "ポスターは", "作らせてほしい", "なあ。"]
        },
        {
            "id": 12,
            "pola": "Bagian 2: ～(さ)せてもらいたい・～(さ)せてほしい (Memohon izin melakukan sesuatu)",
            "kanji": "こんな暑い日には、運動場で４時間も練習をさせないでほしいです。",
            "hiragana": "こんな あつい ひ に は 、 うんどうじょう で よじかん も れんしゅう を させないで ほしい です 。",
            "arti": "Di hari yang panas seperti ini, saya berharap tidak dipaksa latihan sampai 4 jam di lapangan olahraga.",
            "kunci": ["こんな", "暑い日", "には", "、運動場で", "４時間も", "練習を", "させないでほしい", "です。"]
        },
        # === POLA 3: ～といい・～ばいい・～たらいい (Harapan / Saran) ===
        {
            "id": 13,
            "pola": "Bagian 3: ～といい・～ばいい・～たらいい (A: Harapan / Keinginan Situasi Baik)",
            "kanji": "今日でお別れですね。いつかまたみんなでこのクラスに会えるといいですね、先生もです。",
            "hiragana": "きょう で おわかれ です ね 。 いつか また みんな で この くらす に あえると いい です ね 、 せんせい も です 。",
            "arti": "Hari ini perpisahan kita ya. Semoga suatu saat nanti kita semua bisa bertemu lagi di kelas ini ya, Guru juga berharap demikian.",
            "kunci": ["今日でお別れ", "ですね。", "いつかまた", "みんなで", "このクラスに", "会えるといい", "ですね、", "先生もです", "。"]
        },
        {
            "id": 14,
            "pola": "Bagian 3: ～といい・～ばいい・～たらいい (A: Harapan / Keinginan Situasi Baik)",
            "kanji": "最近ずっと体の調子が悪い。悪い病気でなければいいが。",
            "hiragana": "さいきん ずっと からだ の ちょうし が わるい 。 わるい びょうき でなければ いい が 。",
            "arti": "Akhir-akhir ini kondisi tubuh saya terus memburuk. Semoga saja bukan penyakit yang parah.",
            "kunci": ["最近ずっと", "体の調子が", "悪い。", "悪い病気", "でなければいい", "が。"]
        },
        {
            "id": 15,
            "pola": "Bagian 3: ～といい・～ばいい・～たらいい (A: Harapan / Keinginan Situasi Baik)",
            "kanji": "あしたは入学試験だ。がんばろう。合格できたらいいなあ。",
            "hiragana": "あした は にゅうがくしけん だ 。 がんばろう 。 ごうかく できたら いい なあ 。",
            "arti": "Besok adalah ujian masuk sekolah. Mari berjuang. Semoga bisa lulus ya!",
            "kunci": ["あしたは", "入学試験だ", "。がんばろう", "。合格できたら", "いいなあ", "。"]
        },
        {
            "id": 16,
            "pola": "Bagian 3: ～といい・～ばいい・～たらいい (B: Saran / Rekomendasi Ringan)",
            "kanji": "あしたはゆっくり休むといいですよ。疲れているようですからね。",
            "hiragana": "あした は ゆっくり やすむ と いい です よ 。 つかれている よう です から ね 。",
            "arti": "Besok sebaiknya Anda beristirahat dengan santai saja. Karena Anda terlihat sangat lelah.",
            "kunci": ["あしたは", "ゆっくり", "休むといい", "ですよ。", "疲れている", "ようですからね", "。"]
        },
        {
            "id": 17,
            "pola": "Bagian 3: ～といい・～ばいい・～たらいい (B: Saran / Rekomendasi Ringan)",
            "kanji": "その仕事、気が進まないのなら引き受けなければいいんじゃないですか。",
            "hiragana": "その しごと 、 き が すすまない の なら ひきうけなければ いい ん じゃ ない です か 。",
            "arti": "Pekerjaan itu, kalau kamu merasa tidak bersemangat menjalankannya, bukankah sebaiknya tidak usah diambil saja?",
            "kunci": ["その仕事", "、気が進まない", "のなら", "引き受けなければいい", "んじゃないですか", "。"]
        },
        {
            "id": 18,
            "pola": "Bagian 3: ～といい・～ばいい・～たらいい (B: Saran / Rekomendasi Ringan)",
            "kanji": "申込書の書き方がわからなければ、事務の人に聞いてみたらいいですよ。",
            "hiragana": "もうしこみしょ の かきかた が わからなければ 、 じむ の ひと に きいて みたら いい です よ 。",
            "arti": "Jika tidak tahu cara mengisi formulir pendaftarannya, sebaiknya coba tanyakan saja kepada petugas administrasi.",
            "kunci": ["申込書の", "書き方が", "わakらなければ", "、事務の人", "に聞いてみたらいい", "ですよ", "。"]
        }
    ]

# --- STATE MANAGEMENT ---
if "index_soal" not in st.session_state:
    st.session_state.index_soal = 0
if "jawaban_user" not in st.session_state:
    st.session_state.jawaban_user = []
if "status_periksa" not in st.session_state:
    st.session_state.status_periksa = False

soal_sekarang = st.session_state.database_soal[st.session_state.index_soal]

if "soal_acak" not in st.session_state or st.session_state.get("current_soal_id") != soal_sekarang["id"]:
    kata_list = list(soal_sekarang["kunci"])
    random.shuffle(kata_list)
    st.session_state.soal_acak = kata_list
    st.session_state.current_soal_id = soal_sekarang["id"]
    st.session_state.jawaban_user = []
    st.session_state.status_periksa = False

# --- PROSES INTERAKSI URL PARAMETERS ---
params = st.query_params
if "add" in params:
    kata_klik = params["add"]
    if st.session_state.jawaban_user.count(kata_klik) < st.session_state.soal_acak.count(kata_klik):
        st.session_state.jawaban_user.append(kata_klik)
    st.query_params.clear()
    st.rerun()

if "del" in params:
    idx_hapus = int(params["del"])
    if idx_hapus < len(st.session_state.jawaban_user):
        st.session_state.jawaban_user.pop(idx_hapus)
    st.query_params.clear()
    st.rerun()

# --- CSS PREMIUM DESIGN (DUOLINGO STYLE) ---
st.markdown("""
<style>
    /* Info Box */
    .info-box {
        background-color: #f0f7ff;
        padding: 16px;
        border-radius: 16px;
        border: 2px solid #b8daff;
        margin-bottom: 25px;
        box-shadow: 0px 4px 0px #b8daff;
    }
    .text-bunpou { font-size: 0.95rem; font-weight: 800; color: #007bff; text-transform: uppercase; letter-spacing: 0.5px; margin: 0; }
    .text-arti { font-size: 1.2rem; font-weight: 700; color: #212529; margin-top: 6px; }

    /* Label Section */
    .label-section {
        font-size: 1rem;
        font-weight: 700;
        color: #495057;
        margin-bottom: 8px;
    }

    /* KONTEN UTAMA: Flexbox horizontal lock anti meluber kebawah */
    .flex-papan-jepang {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: wrap !important;
        justify-content: flex-start !important;
        align-items: center !important;
        gap: 10px !important;
        width: 100% !important;
        padding: 16px !important;
        background-color: #f8f9fa !important;
        border-radius: 18px !important;
        min-height: 70px !important;
        margin-bottom: 25px !important;
    }
    
    .papan-garis {
        border: 2px dashed #ccc !important;
        background-color: #ffffff !important;
    }

    /* PREMIUM 3D BUTTON KAPSUL (GARANSI TETAP HORIZONTAL) */
    .tombol-kata-inline {
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        background-color: #ffffff !important;
        color: #3c3c3c !important;
        text-decoration: none !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        padding: 10px 18px !important;
        border-radius: 14px !important;
        border: 2px solid #e5e5e5 !important;
        box-shadow: 0px 4px 0px #e5e5e5 !important;
        white-space: nowrap !important;
        transition: all 0.1s ease;
        margin: 2px 0 !important;
    }
    
    .tombol-kata-inline:active {
        transform: translateY(4px) !important;
        box-shadow: 0px 0px 0px #e5e5e5 !important;
    }
    
    /* Tombol Mati (Sudah Dipilih) */
    .tombol-mati {
        background-color: #e5e5e5 !important;
        color: #e5e5e5 !important;
        border: 2px solid #e5e5e5 !important;
        box-shadow: 0px 0px 0px !important;
        pointer-events: none !important;
        user-select: none !important;
    }

    /* Badge Analisis Urutan Posisi */
    .badge-pos-container { display: flex; flex-direction: row; flex-wrap: wrap; gap: 8px; margin-top: 15px; }
    .badge-pos-correct {
        background-color: #d4edda; color: #155724; padding: 10px 14px;
        border-radius: 12px; font-weight: 700; display: inline-flex;
        flex-direction: column; align-items: center; border: 2px solid #c3e6cb;
    }
    .badge-pos-wrong {
        background-color: #f8d7da; color: #721c24; padding: 10px 14px;
        border-radius: 12px; font-weight: 700; display: inline-flex;
        flex-direction: column; align-items: center; border: 2px solid #f5c6cb;
    }
    .sub-index { font-size: 0.75rem; color: #6c757d; margin-top: 4px; border-top: 1px dashed rgba(0,0,0,0.1); width: 100%; text-align:center;}
</style>
""", unsafe_allow_html=True)

# --- HEADER APP ---
st.markdown("<h2 style='text-align: center; color: #212529; font-weight: 800; margin-bottom: 2px;'>🦉 Bunpou Master</h2>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #6c757d; font-weight: 600; margin-top: 0;'>Bab 9 — Soal {st.session_state.index_soal + 1} dari {len(st.session_state.database_soal)}</p>", unsafe_allow_html=True)
st.markdown("<hr style='margin-top: 10px; margin-bottom: 20px;'>", unsafe_allow_html=True)

# Info Box Pola Bunpou & Arti
st.markdown(f"""
<div class="info-box">
    <p class="text-bunpou">📖 {soal_sekarang['pola']}</p>
    <p class="text-arti">{soal_sekarang['arti']}</p>
</div>
""", unsafe_allow_html=True)

# --- PANEL 1: AREA KALIMAT SUSUNAN USER ---
st.markdown("<div class='label-section'>Kalimat Susunanmu:</div>", unsafe_allow_html=True)

html_papan_user = "<div class='flex-papan-jepang papan-garis'>"
if not st.session_state.jawaban_user:
    html_papan_user += "<span style='color:#adb5bd; font-style:italic; font-weight:600;'>Ketuk kata di bawah untuk mulai menyusun...</span>"
else:
    for idx, kata in enumerate(st.session_state.jawaban_user):
        html_papan_user += f"<a href='?del={idx}' target='_self' class='tombol-kata-inline'>{kata}</a>"
html_papan_user += "</div>"

st.markdown(html_papan_user, unsafe_allow_html=True)

# --- PANEL 2: AREA PILIHAN KATA ASAL ---
st.markdown("<div class='label-section'>Pilihan Kata:</div>", unsafe_allow_html=True)

temp_jawaban = list(st.session_state.jawaban_user)
html_papan_asal = "<div class='flex-papan-jepang'>"
for kata in st.session_state.soal_acak:
    if kata in temp_jawaban:
        html_papan_asal += f"<span class='tombol-kata-inline tombol-mati'>{kata}</span>"
        temp_jawaban.remove(kata)
    else:
        html_papan_asal += f"<a href='?add={kata}' target='_self' class='tombol-kata-inline'>{kata}</a>"
html_papan_asal += "</div>"

st.markdown(html_papan_asal, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- PANEL NAVIGASI UTAMA ---
col1, col2, col3 = st.columns([1, 1.2, 1])
with col1:
    if st.button("RESET 🔄", use_container_width=True):
        st.session_state.jawaban_user = []
        st.session_state.status_periksa = False
        st.rerun()
with col2:
    if st.button("PERIKSA ✅", type="primary", use_container_width=True):
        st.session_state.status_periksa = True
with col3:
    if st.button("LANJUT ➡️", use_container_width=True):
        st.session_state.index_soal = (st.session_state.index_soal + 1) % len(st.session_state.database_soal)
        if "soal_acak" in st.session_state: 
            del st.session_state.soal_acak
        st.rerun()

# --- VALIDASI HASIL KOREKSI ---
if st.session_state.status_periksa:
    user_strings = st.session_state.jawaban_user
    kunci_strings = soal_sekarang["kunci"]
    
    user_joined = "".join(user_strings).replace(" ", "").replace("、", "").replace("。", "").replace("「", "").replace("」", "").replace("！", "").replace("？", "")
    kunci_joined = "".join(kunci_strings).replace(" ", "").replace("、", "").replace("。", "").replace("「", "").replace("」", "").replace("！", "").replace("？", "")

    st.markdown("<br><hr>", unsafe_allow_html=True)
    if user_joined == kunci_joined:
        st.success(f"🎉 **正解 (Benar)!** Susunan kalimatmu sudah luar biasa tepat!\n\n"
                   f"**Kanji:**\n{soal_sekarang['kanji']}\n\n"
                   f"**Hiragana:**\n{soal_sekarang['hiragana']}\n\n"
                   f"**Arti:**\n{soal_sekarang['arti']}")
    else:
        st.error("❌ **残念 (Kurang Tepat). Analisis Posisi Urutan Kata:**")
        
        html_koreksi = "<div class='badge-pos-container'>"
        max_len = max(len(user_strings), len(kunci_strings))
        
        for idx in range(max_len):
            if idx < len(user_strings):
                kata_user = user_strings[idx]
                
                if idx < len(kunci_strings) and kata_user == kunci_strings[idx]:
                    html_koreksi += f"""<div class='badge-pos-correct'>{kata_user}<span class='sub-index'>Posisi {idx+1}</span></div>"""
                else:
                    html_koreksi += f"""<div class='badge-pos-wrong'>{kata_user}<span class='sub-index'>Posisi {idx+1}</span></div>"""
            else:
                html_koreksi += f"""<div class='badge-pos-wrong' style='border: 2px dashed #ff4b4b; background-color:#fff5f5; color:#ff4b4b;'>(Kosong)<span class='sub-index'>Posisi {idx+1}</span></div>"""
                
        html_koreksi += "</div>"
        st.markdown(html_koreksi, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown(f"**💡 Panduan Urutan yang Benar:**\n\n`{' ➔ '.join(soal_sekarang['kunci'])}`\n\n"
                    f"**Kanji:**\n{soal_sekarang['kanji']}\n\n"
                    f"**Hiragana:**\n{soal_sekarang['hiragana']}\n\n"
                    f"**Arti:**\n{soal_sekarang['arti']}")
