import streamlit as st

st.set_page_config(page_title="Susun Kata Jepang - Bab 9", layout="centered")

# --- DATABASE SOAL LOKAL (BAB 9 - 17 SOAL BARU) ---
if "database_soal" not in st.session_state:
    st.session_state.database_soal = [
        # === BAGIAN 1 ===
        {
            "id": 1,
            "pola": "Bagian 1: ～てもらいたい・～ていただきたい・～てほしい (Mengharap orang lain melakukan sesuatu)",
            "kanji": "だれかに自分の悩みを聞いてもらいたいと思うことがあります。",
            "hiragana": "だれか に じぶん の なやみ を きいて もらいたい と おもう こと が あります 。",
            "arti": "Kadang saya berpikir ingin seseorang mendengarkan keluh kesah saya.",
            "kunci": ["だれかに", "自分の", "悩み", "を", "聞いて", "もらいたい", "と", "思う", "ことが", "あります", "。"],
            "soal": ["おもう", "悩み", "と", "聞いて", "が", "だれか", "مらい", "あります", "じぶん", "に", "たい", "ほしい", "こと", "の"]
        },
        {
            "id": 2,
            "pola": "Bagian 1: ～てもらいたい・～ていただきたい・～てほしい (Mengharap orang lain melakukan sesuatu)",
            "kanji": "この書類、ちょっと見ていただきたいんですが。",
            "hiragana": "この しょるい 、 ちょっと みて いただきたい ん です が 。",
            "arti": "Dokumen ini, saya ingin Anda tolong lihat sebentar...",
            "kunci": ["この", "書類", "、", "ちょっと", "見て", "いただきたい", "ん", "ですが", "。"],
            "soal": ["ちょっと", "が", "見て", "書類", "この", "です", "いただき", "たい", "ん"]
        },
        {
            "id": 3,
            "pola": "Bagian 1: ～てもらいたい・～ていただきたい・～てほしい (Mengharap orang lain melakukan sesuatu)",
            "kanji": "この仕事はだれにも手伝ってもらいたくない。自分一人でやりたい。",
            "hiragana": "この しごと は だれ に も てつだって もらいたく ない 。 じぶん ひとり で やりたい 。",
            "arti": "Pekerjaan ini saya tidak ingin dibantu siapapun. Saya ingin melakukannya sendiri.",
            "kunci": ["この", "仕事", "は", "だれに", "も", "手伝って", "もらいたくない", "。", "自分", "一人", "で", "やりたい", "。"],
            "soal": ["やり", "だれ", "もらい", "は", "手伝っ", "じぶん", "に", "仕事", "たく", "で", "この", "ない", "たい", "も", "一人"]
        },
        {
            "id": 4,
            "pola": "Bagian 1: ～てもらいたい・～ていただきたい・～てほしい (Mengharap orang lain melakukan sesuatu)",
            "kanji": "ずっとぼくのそばにいてほしい。遠くへ行かないでほしい。",
            "hiragana": "ずっと ぼく の そば に いて ほしい 。 とおく へ いかないで ほしい 。",
            "arti": "Aku ingin kamu selalu berada di sisiku. Aku tidak ingin kamu pergi jauh.",
            "kunci": ["ずっと", "ぼくの", "そば", "に", "いてほしい", "。", "遠く", "へ", "行かないで", "ほしい", "。"],
            "soal": ["遠く", "に", "ずっと", "行か", "そば", "ない", "へ", "ほしい", "ぼく", "で", "の", "いて", "ほしい"]
        },
        {
            "id": 5,
            "pola": "Bagian 1: ～てもらいたい・～ていただきたい・～てほしい (Mengharap orang lain melakukan sesuatu)",
            "kanji": "これ以上この村の自然環境をこわさないでほしい。",
            "hiragana": "これ いじょう この むら の しぜんかんきょう を こわさないで ほしい 。",
            "arti": "Jangan merusak lingkungan alam desa ini lebih dari ini.",
            "kunci": ["これ", "以上", "この", "村", "の", "自然環境", "を", "こわさないで", "ほしい", "。"],
            "soal": ["自然環境", "を", "これ", "ほしい", "ない", "こわさ", "村", "の", "以上", "この", "で"]
        },
        {
            "id": 6,
            "pola": "Bagian 1: ～てもらいたい・～ていただきたい・～てほしい (Mengharap orang lain melakukan sesuatu)",
            "kanji": "年を取った親にはもう無理をしてほしくない。",
            "hiragana": "とし を とった おや に は もう むり を して ほしく ない 。",
            "arti": "Saya tidak ingin orang tua yang sudah berumur memaksakan diri lagi.",
            "kunci": ["年", "を", "取った", "親", "in", "は", "もう", "無理", "を", "して", "ほしくない", "。"],
            "soal": ["を", "取っ", "親", "に", "年", "もう", "して", "は", "無理", "ほしく", "ない", "た"]
        },
        # === BAGIAN 2 ===
        {
            "id": 7,
            "pola": "Bagian 2: ～(さ)せてもらいたい・～(さ)せていただきたい・～(さ)せてほしい (Mengharap diizinkan melakukan sesuatu)",
            "kanji": "昼休みが短いよね。昼ご飯をもっとゆっくり食べさせてもらいたいね。",
            "hiragana": "ひるやすみ が みじかい よね 。 ひるごはん を もっと ゆっくり たべさせ もらいたい ね 。",
            "arti": "Istirahat makan siang pendek ya. Aku ingin diizinkan makan siang dengan lebih santai.",
            "kunci": ["昼休み", "が", "短い", "よね", "。", "昼ご飯", "を", "もっと", "ゆっくり", "食べさせ", "もらいたい", "ね", "。"],
            "soal": ["食べ", "もっと", "もらい", "が", "昼休み", "昼ご飯", "短い", "させ", "て", "たい", "ね", "よね", "ゆっくり", "ね", "を"]
        },
        {
            "id": 8,
            "pola": "Bagian 2: ～(さ)せてもらいたい・～(さ)せていただきたい・～(さ)せてほしい (Mengharap diizinkan melakukan sesuatu)",
            "kanji": "今日は入管へ行かなければならないので、早く帰らせていただきたいのですが……。",
            "hiragana": "きょう は にゅうかん へ いかなければ ならない ので 、 はやく かえらせて いただきたい の です が …… 。",
            "arti": "Karena hari ini saya harus pergi ke imigrasi, saya ingin meminta izin untuk pulang cepat...",
            "kunci": ["今日", "は", "入管", "へ", "行かなければ", "ならない", "ので", "、", "早く", "帰らせて", "いただきたい", "の", "ですが", "……", "。"],
            "soal": ["帰ら", "なければ", "いただき", "今日", "は", "入管", "へ", "行か", "なら", "ない", "ので", "早く", "せて", "たい", "の", "ですが", "……"]
        },
        {
            "id": 9,
            "pola": "Bagian 2: ～(さ)せてもらいたい・～(さ)せていただきたい・～(さ)せてほしい (Mengharap diizinkan melakukan sesuatu)",
            "kanji": "それはさっきも説明したことだよ。何度も同じことを言わさせないでもらいたいよ。",
            "hiragana": "それ は さっき も せつめい した こと だ よ 。 なんど も おなじ こと を いわさせないで もらいたい よ 。",
            "arti": "Itu kan hal yang sudah saya jelaskan tadi. Tolong jangan buat saya mengatakan hal yang sama berulang kali.",
            "kunci": ["それ", "は", "さっき", "も", "説明", "した", "こと", "だよ", "。", "何度も", "同じ", "こと", "を", "言わさせないで", "もらいたい", "よ", "。"],
            "soal": ["説明", "同じ", "もらい", "言わ", "さっき", "し", "と", "こと", "も", "何度", "それ", "だよ", "は", "も", "た", "ない", "で", "たい", "よ", "を"]
        },
        {
            "id": 10,
            "pola": "Bagian 2: ～(さ)せてもらいたい・～(さ)せていただきたい・～(さ)せてほしい (Mengharap diizinkan melakukan sesuatu)",
            "kanji": "文化祭のポスターはわたしに作らせてほしいなあ。",
            "hiragana": "ぶんかさい の ぽすたー は わたし に つくらせて ほしい なあ 。",
            "arti": "Poster festival budaya, biarkan aku saja yang membuatnya.",
            "kunci": ["文化祭", "の", "ポスター", "は", "わたし", "に", "作らせて", "ほしい", "なあ", "。"],
            "soal": ["ポスター", "は", "作ら", "文化祭", "わたし", "に", "せて", "ほしい", "なあ", "の"]
        },
        {
            "id": 11,
            "pola": "Bagian 2: ～(さ)せてもらいたい・～(さ)せていただきたい・～(さ)せてほしい (Mengharap diizinkan melakukan sesuatu)",
            "kanji": "こんな暑い日に運動場で4時間も練習をさせないでほしいです。",
            "hiragana": "こんな あつい ひ に うんどうじょう で よじかん も れんしゅう を させないで ほしい です 。",
            "arti": "Di hari sepanas ini, saya harap tidak disuruh latihan sampai 4 jam di lapangan olahraga.",
            "kunci": ["こんな", "暑い", "日", "に", "運動場", "で", "4時間", "も", "練習", "を", "させないで", "ほしい", "です", "。"],
            "soal": ["暑い", "練習", "運動場", "4時間", "も", "ない", "ほしい", "です", "こんな", "日", "に", "で", "を", "させ", "で"]
        },
        # === BAGIAN 3 ===
        {
            "id": 12,
            "pola": "Bagian 3: ～といい・～ばいい・～たらいい (Harapan / Saran)",
            "kanji": "このクラスも今日でお別れです。いつかまたみんなで会えるといいですね。",
            "hiragana": "この くらす も きょう で おわかれ です 。 いつか また みんな で あえる と いい です ね 。",
            "arti": "Kelas ini juga akan berpisah hari ini. Semoga suatu saat kita semua bisa bertemu lagi ya.",
            "kunci": ["この", "クラス", "も", "今日", "で", "お別れ", "です", "。", "いつか", "また", "みんな", "で", "会えると", "いいですね", "。"],
            "soal": ["今日", "クラス", "別れ", "会える", "いい", "お", "です", "いつか", "また", "みんな", "で", "と", "です", "ね", "この", "も", "で"]
        },
        {
            "id": 13,
            "pola": "Bagian 3: ～といい・～ばいい・～たらいい (Harapan / Saran)",
            "kanji": "最近ずっと体の調子が悪い。悪い病気でなければいいが･･････。",
            "hiragana": "さいきん ずっと からだ の ちょうし が わるい 。 わるい びょうき で なければ いい が ･･････ 。",
            "arti": "Belakangan ini kondisi tubuh saya terus memburuk. Semoga bukan penyakit yang parah...",
            "kunci": ["最近", "ずっと", "体", "の", "調子", "が", "悪い", "。", "悪い", "病気", "で", "なければ", "いいが", "･･････", "。"],
            "soal": ["体", "が", "病気", "なけれ", "いい", "調子", "最近", "ずっと", "の", "悪い", "悪い", "ば", "が", "……", "で"]
        },
        {
            "id": 14,
            "pola": "Bagian 3: ～といい・～ばいい・～たらいい (Harapan / Saran)",
            "kanji": "あしたは入学試験だ。がんばろう。合格できたらいいなあ。",
            "hiragana": "あした は にゅうがくしけん だ 。 がんばろう 。 ごうかく できたら いい なあ 。",
            "arti": "Besok adalah ujian masuk. Ayo berjuang. Semoga bisa lulus ya.",
            "kunci": ["あした", "は", "入学", "試験", "だ", "。", "がんばろう", "。", "合格", "できたら", "いいなあ", "。"],
            "soal": ["試験", "合格", "あした", "入学", "だ", "がんばろう", "でき", "たら", "いい", "なあ", "は"]
        },
        {
            "id": 15,
            "pola": "Bagian 3: ～といい・～ばいい・～たらいい (Harapan / Saran)",
            "kanji": "疲れているようですね。あしたはゆっくり休むといいですよ。",
            "hiragana": "つかれている よう です ね 。 あした は ゆっくり やすむ と いい です よ 。",
            "arti": "Sepertinya Anda lelah. Besok sebaiknya Anda beristirahat dengan santai.",
            "kunci": ["疲れている", "ようですね", "。", "あした", "は", "ゆっくり", "休むと", "いいですよ", "。"],
            "soal": ["休む", "疲れ", "よう", "あした", "ゆっくり", "と", "いい", "です", "よ", "て", "いる", "ね"]
        },
        {
            "id": 16,
            "pola": "Bagian 3: ～といい・～ばいい・～たらいい (Harapan / Saran)",
            "kanji": "その仕事、気が進まないのなら引き受けなければいいんじゃないですか。",
            "hiragana": "その しごと 、 き が すすまない の なら ひきうけなければ いい ん じゃ ない です か 。",
            "arti": "Pekerjaan itu, kalau kamu tidak berminat, bukankah sebaiknya tidak usah diambil saja?",
            "kunci": ["その", "仕事", "、", "気が進まない", "のなら", "引き受けなければ", "いいんじゃないですか", "。"],
            "soal": ["引き受け", "気が進ま", "ない", "の", "なら", "その", "仕事", "なけれ", "ば", "いい", "ん", "じゃ", "ない", "です", "か"]
        },
        {
            "id": 17,
            "pola": "Bagian 3: ～といい・～ばいい・～たらいい (Harapan / Saran)",
            "kanji": "申込書の書き方がわからなければ、事務の人に聞いてみたらいいですよ。",
            "hiragana": "もうしこみしょ の かきかた が わからなければ 、 じむ の ひと に きいて みたら いい です よ 。",
            "arti": "Jika tidak tahu cara mengisi formulir pendaftaran, sebaiknya coba tanyakan pada orang tata usaha.",
            "kunci": ["申込書", "の", "書き方", "が", "わからなければ", "、", "事務", "の", "人", "に", "聞いて", "みたら", "いいですよ", "。"],
            "soal": ["人", "申込書", "書き方", "わから", "なけれ", "ば", "事務", "の", "に", "聞いて", "み", "たら", "いい", "です", "よ"]
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
    
    # Pembersihan string agar tanda baca dan spasi tidak bikin error saat pencocokan otomatis
    user_joined = "".join(user_strings).replace(" ", "").replace("、", "").replace("。", "").replace("?", "").replace("？", "").replace("……", "").replace("…", "").replace("･･････", "")
    kunci_joined = "".join(soal_sekarang["kunci"]).replace(" ", "").replace("、", "").replace("。", "").replace("?", "").replace("？", "").replace("……", "").replace("…", "").replace("･･････", "")

    # Normalisasi typo kecil atau perbedaan input tertentu agar fleksibel
    user_joined = user_joined.replace("帰らせetいただき", "帰らせていただき").replace("帰らせていただき", "帰らせていただき")
    kunci_joined = kunci_joined.replace("帰らせetいただき", "帰らせていただき").replace("帰らせていただき", "帰らせていただき")

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
