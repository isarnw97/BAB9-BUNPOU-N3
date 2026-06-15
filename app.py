import streamlit as st
import random

st.set_page_config(page_title="Susun Kata Jepang - Bab 10", layout="centered")

# --- DATABASE SOAL LOKAL LENGKAP (BAB 10) ---
if "database_soal" not in st.session_state:
    st.session_state.database_soal = [
        # === POLA 1: 命令(しろ) / 禁止(~な) ===
        {
            "id": 1,
            "pola": "Bagian 1: 命令(しろ)・禁止(~な) (Perintah/Larangan Tegas)",
            "kanji": "監督「走れ、走れ！」",
            "hiragana": "かんとく 「 はしれ 、 はしれ ！ 」",
            "arti": "(Di pertandingan) Pelatih: 'Lari, lari!'",
            "kunci": ["監督", "「", "走れ", "、", "走れ", "！」"]
        },
        {
            "id": 2,
            "pola": "Bagian 1: 命令(しろ)・禁止(~な) (Perintah/Larangan Tegas)",
            "kanji": "犬に「降りろ。」と命令した。",
            "hiragana": "いぬ に 「 おりろ 。 」 と めいれい した 。",
            "arti": "Memerintah kepada anjing, 'Turun!'.",
            "kunci": ["犬に", "「", "降りろ", "。", "」と", "命令した", "。"]
        },
        {
            "id": 3,
            "pola": "Bagian 1: 命令(しろ)・禁止(~な) (Perintah/Larangan Tegas)",
            "kanji": "赤信号は止まれという意味です。",
            "hiragana": "あかしんごう は とまれ と いう いみ です 。",
            "arti": "Lampu merah berarti 'Berhenti'.",
            "kunci": ["赤信号は", "止まれ", "という", "意味です", "。"]
        },
        {
            "id": 4,
            "pola": "Bagian 1: 命令(しろ)・禁止(~な) (Perintah/Larangan Tegas)",
            "kanji": "引っ越しを手伝ってくれと友だちに頼んでみよう。",
            "hiragana": "ひっこし を てつだって くれ と ともだち に たのんで みよう 。",
            "arti": "Mari coba meminta tolong kepada teman, 'Bantu aku pindahan'.",
            "kunci": ["引っ越しを", "手伝ってくれ", "と", "友だちに", "頼んでみよう", "。"]
        },
        {
            "id": 5,
            "pola": "Bagian 1: 命令(しろ)・禁止(~な) (Perintah/Larangan Tegas)",
            "kanji": "立て札に「スピードを出すな！」と書いてある。",
            "hiragana": "たてふだ に 「 すぴーど を だすな ！ 」 と かいて ある 。",
            "arti": "Di papan pengumuman tertulis, 'Jangan mengebut!'.",
            "kunci": ["立て札に", "「", "スピード", "を", "出すな", "！」と", "書いてある", "。"]
        },
        {
            "id": 6,
            "pola": "Bagian 1: 命令(しろ)・禁止(~な) (Perintah/Larangan Tegas)",
            "kanji": "父は医者にお酒を飲むなと言われている。",
            "hiragana": "ちち は いしゃ に おさけ を のむ な と いわれている 。",
            "arti": "Ayah dilarang oleh dokter untuk minum alkohol.",
            "kunci": ["父は", "医者に", "お酒", "を", "飲むな", "と", "言われている", "。"]
        },
        # === POLA 2: ～こと ===
        {
            "id": 7,
            "pola": "Bagian 2: ～こと (Instruksi / Aturan Tertulis)",
            "kanji": "レポートは来週月曜日に必ず出すこと。遅れないこと。",
            "hiragana": "れぽーと は らいしゅう げつようび に かかならず だす こと 。 おくれない こと 。",
            "arti": "Laporan harus dikumpulkan hari Senin depan tanpa gagal. Jangan terlambat.",
            "kunci": ["レポートは", "来週月曜日に", "必ず", "出すこと", "。", "遅れないこと", "。"]
        },
        {
            "id": 8,
            "pola": "Bagian 2: ～こと (Instruksi / Aturan Tertulis)",
            "kanji": "申込書を書く前に注意書きをよく読むこと。",
            "hiragana": "もうしこみしょ を かく まえ に ちゅういがき を よく よむ こと 。",
            "arti": "Bacalah petunjuk catatan dengan saksama sebelum mengisi formulir.",
            "kunci": ["申込書を", "書く前に", "注意書き", "を", "よく読むこと", "。"]
        },
        {
            "id": 9,
            "pola": "Bagian 2: ～こと (Instruksi / Aturan Tertulis)",
            "kanji": "危ないからこの川で泳がないこと。",
            "hiragana": "あぶない から この かわ で およがない こと 。",
            "arti": "Karena berbahaya, dilarang berenang di sungai ini.",
            "kunci": ["危ないから", "この川で", "泳がないこと", "。"]
        },
        # === POLA 3: ～べきだ・～べきではない ===
        {
            "id": 10,
            "pola": "Bagian 3: ～べきだ・～べきではない (Seharusnya / Tidak Boleh)",
            "kanji": "これは大事なことですから、もう少し話し合ってから決めるべきだと思いますよ。",
            "hiragana": "これ は だいじ な こと です から 、 もうすこし はなしあって から きめる べき だ と おもいます よ 。",
            "arti": "Karena ini masalah penting, saya rasa kita seharusnya memutuskan setelah berdiskusi lagi.",
            "kunci": ["これは", "大事なことですから", "、", "もう少し", "話し合ってから", "決めるべきだ", "と", "思いますよ", "。"]
        },
        {
            "id": 11,
            "pola": "Bagian 3: ～べきだ・～べきではない (Seharusnya / Tidak Boleh)",
            "kanji": "仕事はたくさんあるが、まず、今日中にやるべきことから始めよう。",
            "hiragana": "しごと は たくさん ある が 、 まず 、 きょうじゅう に やる べき こと から はじめよう 。",
            "arti": "Pekerjaan ada banyak, mari kita mulai dari hal yang seharusnya dikerjakan hari ini.",
            "kunci": ["仕事は", "たくさんあるが", "、", "まず", "、", "今日中に", "やるべきこと", "から", "始めよう", "。"]
        },
        {
            "id": 12,
            "pola": "Bagian 3: ～べきだ・～べきではない (Seharusnya / Tidak Boleh)",
            "kanji": "せっかく入った会社なのだから、簡単に辞めるべきではない。",
            "hiragana": "せっかく はいった かいしゃ な の だ から 、 かんたん に やめる べき ではない 。",
            "arti": "Karena sudah susah payah masuk kerja, tidak seharusnya mengundurkan diri begitu saja.",
            "kunci": ["せっかく", "入った会社なのだから", "、", "簡単に", "辞めるべきではない", "。"]
        },
        {
            "id": 13,
            "pola": "Bagian 3: ～べきだ・～べきではない (Seharusnya / Tidak Boleh)",
            "kanji": "あしたまでのレポートがまだ書き終わらない。もっと早くから始めるべきだった。",
            "hiragana": "あした まで の れぽーと が まだ かきおわらない 。 もっと はやく から はじめる べき だった 。",
            "arti": "Laporan besok belum selesai. Seharusnya saya memulainya lebih awal.",
            "kunci": ["あしたまでの", "レポートが", "まだ", "書き終わらない", "。", "もっと", "早くから", "始めるべきだった", "。"]
        },
        # === POLA 4: ～たらどうか ===
        {
            "id": 14,
            "pola": "Bagian 4: ～たらどうか (Bagaimana Kalau / Saran)",
            "kanji": "体のことが心配なら、一度健康診断を受けたらどうでしょうか。",
            "hiragana": "からだ の こと が しんぱい なら 、 いちど けんこうしんだん を うけたら どう でしょう か 。",
            "arti": "Jika khawatir tentang kondisi tubuh, bagaimana kalau mencoba tes kesehatan sekali?",
            "kunci": ["体のことが", "心配なら", "、", "一度", "健康診断", "を", "受けたらどうでしょうか", "。"]
        },
        {
            "id": 15,
            "pola": "Bagian 4: ～たらどうか (Bagaimana Kalau / Saran)",
            "kanji": "迷惑メールが多いの？じゃ、アドレスを変えたらどう？",
            "hiragana": "めいわく めーる が おおい の ？ じゃ 、 あどれす を かえたら どう ？",
            "arti": "Banyak email spam ya? Kalau begitu, bagaimana kalau ganti alamat email saja?",
            "kunci": ["迷惑メールが", "多いの？", "じゃ、", "アドレス", "を", "変えたらどう？"]
        },
        {
            "id": 16,
            "pola": "Bagian 4: ～たらどうか (Bagaimana Kalau / Saran)",
            "kanji": "悪いのはそっちですよ。一言謝ったらどうですか。",
            "hiragana": "わるい の は そっち です よ 。 ひとこと あやまったら どう です か 。",
            "arti": "Yang salah itu pihakmu, lho. Bagaimana kalau meminta maaf sepatah kata?",
            "kunci": ["悪いのは", "そっちですよ", "。", "一言", "謝ったらどうですか", "。"]
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

# --- PROSES KLIK DENGAN QUERY PARAMETERS ---
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

# --- CSS RADIKAL: PAKSA HORIZONTAL TOTAL (ANTI BREAK VERTIKAL) ---
st.markdown("""
<style>
    .info-box {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 12px;
        border-left: 5px solid #007bff;
        margin-bottom: 20px;
    }
    .text-bunpou { font-size: 1rem; font-weight: bold; color: #007bff; margin: 0; }
    .text-arti { font-size: 1.1rem; font-weight: bold; color: #1a1a1a; margin-top: 5px; }

    /* KONTEN UTAMA: Flexbox murni dipaksa inline ke samping */
    .flex-papan-jepang {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: wrap !important;
        justify-content: flex-start !important;
        align-items: center !important;
        gap: 8px !important;
        width: 100% !important;
        padding: 14px !important;
        background-color: #f8f9fa !important;
        border-radius: 14px !important;
        min-height: 60px !important;
        margin-bottom: 15px !important;
    }
    
    .papan-garis {
        border: 2px dashed #007bff !important;
        background-color: #ffffff !important;
    }

    /* DESAIN TOMBOL KAPSUL HTML MURNI (Anti Stack Kebawah) */
    .tombol-kata-inline {
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        background-color: #ffffff !important;
        color: #333333 !important;
        text-decoration: none !important;
        font-weight: bold !important;
        font-size: 1.05rem !important;
        padding: 8px 16px !important;
        border-radius: 50px !important;
        border: 1px solid #ced4da !important;
        box-shadow: 0px 2px 4px rgba(0,0,0,0.06) !important;
        white-space: nowrap !important;
        margin: 2px 0 !important;
    }
    
    .tombol-kata-inline:active {
        background-color: #e2e6ea !important;
        transform: scale(0.95);
    }
    
    .tombol-mati {
        background-color: #e9ecef !important;
        color: #ccc !important;
        border: 1px solid #dee2e6 !important;
        box-shadow: none !important;
        pointer-events: none !important;
    }

    /* Badge Analisis Posisi */
    .badge-pos-container { display: flex; flex-direction: row; flex-wrap: wrap; gap: 8px; margin-top: 10px; }
    .badge-pos-correct {
        background-color: #d4edda; color: #155724; padding: 8px 12px;
        border-radius: 10px; font-weight: bold; display: inline-flex;
        flex-direction: column; align-items: center; border: 2px solid #c3e6cb;
    }
    .badge-pos-wrong {
        background-color: #f8d7da; color: #721c24; padding: 8px 12px;
        border-radius: 10px; font-weight: bold; display: inline-flex;
        flex-direction: column; align-items: center; border: 2px solid #f5c6cb;
    }
    .sub-index { font-size: 0.7rem; color: #555555; margin-top: 3px; border-top: 1px dashed rgba(0,0,0,0.15); width: 100%; text-align:center;}
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

# --- PANEL 1: AREA KALIMAT SUSUNAN USER ---
st.write("### Kalimat Susunanmu:")

html_papan_user = "<div class='flex-papan-jepang papan-garis'>"
if not st.session_state.jawaban_user:
    html_papan_user += "<span style='color:#aaaaaa; font-style:italic;'>Klik pilihan kata di bawah...</span>"
else:
    for idx, kata in enumerate(st.session_state.jawaban_user):
        html_papan_user += f"<a href='?del={idx}' target='_self' class='tombol-kata-inline'>{kata}</a>"
html_papan_user += "</div>"

st.markdown(html_papan_user, unsafe_allow_html=True)

# --- PANEL 2: AREA PILIHAN KATA ASAL ---
st.write("### Pilihan Kata:")

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

    if user_joined == kunci_joined:
        st.success(f"🎉 **正解 (Benar)!** Susunan kalimatmu sudah tepat!\n\n"
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
