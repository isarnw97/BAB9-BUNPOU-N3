import streamlit as st

st.set_page_config(page_title="Susun Kata Jepang - Bab 9", layout="centered")

# --- DATABASE SOAL LOKAL (BALIK KE BAB 9 - 17 SOAL UTUH) ---
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
            "soal": ["思う", "悩み", "と", "聞いて", "ことが", "だれかに", "もらいたい", "あります", "自分の", "を", "。"]
        },
        {
            "id": 2,
            "pola": "Bagian 1: ～てもらいたい・～ていただきたい・～てほしい (Mengharap orang lain melakukan sesuatu)",
            "kanji": "この書類、ちょっと見ていただきたいんですが。",
            "hiragana": "この しょるい 、 ちょっと みて いただきたい ん です が 。",
            "arti": "Dokumen ini, saya ingin Anda tolong lihat sebentar...",
            "kunci": ["この", "書類", "、", "ちょっと", "見て", "いただきたい", "ん", "ですが", "。"],
            "soal": ["ちょっと", "maxsですが", "見て", "書類", "この", "いただき", "たい", "ん", "、", "。"]
        },
        {
            "id": 3,
            "pola": "Bagian 1: ～てもらいたい・～ていただきたい・～てほしい (Mengharap orang lain melakukan sesuatu)",
            "kanji": "この仕事はだれにも手伝ってもらいたくない。自分一人でやりたい。",
            "hiragana": "この しごと は だれ に も てつだって もらいたく ない 。 じぶん ひとり で やりたい 。",
            "arti": "Pekerjaan ini saya tidak ingin dibantu siapapun. Saya ingin melakukannya sendiri.",
            "kunci": ["この", "仕事", "は", "だれに", "も", "手伝って", "もらいたくない", "。", "自分", "一人", "で", "やりたい", "。"],
            "soal": ["やりたい", "だれに", "もらいたくない", "は", "手伝って", "自分", "仕事", "で", "この", "も", "一人", "。", "。"]
        },
        {
            "id": 4,
            "pola": "Bagian 1: ～てもらいたい・～ていただきたい・～てほしい (Mengharap orang lain melakukan sesuatu)",
            "kanji": "ずっとぼくのそばにいてほしい。遠くへ行かないでほしい。",
            "hiragana": "ずっと ぼく の そば に いて ほしい 。 とおく へ いかないで ほしい 。",
            "arti": "Aku ingin kamu selalu berada di sisiku. Aku tidak ingin kamu pergi jauh.",
            "kunci": ["ずっと", "ぼくの", "そば", "に", "いてほしい", "。", "遠く", "へ", "行かないで", "ほしい", "。"],
            "soal": ["遠く", "に", "ずっと", "行かないで", "そば", "へ", "ほしい", "ぼくの", "いてほしい", "。", "。"]
        },
        {
            "id": 5,
            "pola": "Bagian 1: ～てもらいたい・～ていただきたい・～てほしい (Mengharap orang lain melakukan sesuatu)",
            "kanji": "これ以上この村の自然環境をこわさないでほしい。",
            "hiragana": "これ いじょう この むら の しぜんかんきょう を こわさないで ほしい 。",
            "arti": "Jangan merusak lingkungan alam desa ini lebih dari ini.",
            "kunci": ["これ", "以上", "この", "村", "の", "自然環境", "を", "こわさないで", "ほしい", "。"],
            "soal": ["自然環境", "を", "これ", "ほしい", "こわさないで", "村", "の", "以上", "この", "。"]
        },
        {
            "id": 6,
            "pola": "Bagian 1: ～てもらいたい・～ていただきたい・～てほしい (Mengharap orang lain melakukan sesuatu)",
            "kanji": "年を取った親にはもう無理をしてほしくない。",
            "hiragana": "とし を とった おや に は もう むり を して ほしく ない 。",
            "arti": "Saya tidak ingin orang tua yang sudah berumur memaksakan diri lagi.",
            "kunci": ["年", "を", "取った", "親", "に", "は", "もう", "無理", "を", "して", "ほしくない", "。"],
            "soal": ["を", "取った", "親", "に", "年", "もう", "して", "は", "無理", "ほしくない", "を", "。"]
        },
        # === BAGIAN 2 ===
        {
            "id": 7,
            "pola": "Bagian 2: ～(さ)せてもらいたい・～(さ)せていただきたい・～(さ)せてほしい (Mengharap diizinkan melakukan sesuatu)",
            "kanji": "昼休みが短いよね。昼ご飯をもっとゆっくり食べさせてもらいたいね。",
            "hiragana": "ひるやすみ が みじかい よね 。 ひるごはん を もっと ゆっくり たべさせ もらいたい ね 。",
            "arti": "Istirahat makan siang pendek ya. Aku ingin diizinkan makan siang dengan lebih santai.",
            "kunci": ["昼休み", "が", "短い", "よね", "。", "昼ご飯", "を", "もっと", "ゆっくり", "食べさせ", "もらいたい", "ね", "。"],
            "soal": ["食べさせ", "もっと", "もらいたい", "が", "昼休み", "昼ご飯", "短い", "よね", "ゆっくり", "ね", "を", "。", "。"]
        },
        {
            "id": 8,
            "pola": "Bagian 2: ～(さ)せてもらいたい・～(さ)せていただきたい・～(さ)せてほしい (Mengharap diizinkan melakukan sesuatu)",
            "kanji": "今日は入管へ行かなければならないので、早く帰らせていただきたいのですが……。",
            "hiragana": "きょう は にゅうかん へ いかなければ ならない ので 、 はやく かえらせて いただきたい の です が …… 。",
            "arti": "Karena hari ini saya harus pergi ke imigrasi, saya ingin meminta izin untuk pulang cepat...",
            "kunci": ["今日", "は", "入管", "へ", "行かなければ", "ならない", "ので", "、", "早く", "帰らせて", "いただきたい", "の", "maxsbagai", "……", "。"],
            "soal": ["帰らせて", "行かなければ", "いただきたい", "今日", "は", "入管", "へ", "ならない", "ので", "早く", "の", "maxsbagai", "……", "、", "。"]
        },
        {
            "id": 9,
            "pola": "Bagian 2: ～(さ)せてもらいたい・～(さ)せていただきたい・～(さ)せてほしい (Mengharap diizinkan melakukan sesuatu)",
            "kanji": "それはさっきも説明したことだよ。何度も同じことを言わさせないで もらいたいよ。",
            "hiragana": "それ は さっき も せつめい した こと だ よ 。 なんど も おなじ こと を いわさせないde もらいたい よ 。",
            "arti": "Itu kan hal yang sudah saya jelaskan tadi. Tolong jangan buat saya mengatakan hal yang sama berulang kali.",
            "kunci": ["それ", "は", "さっき", "も", "説明", "した", "こと", "だよ", "。", "何度も", "同じ", "こと", "を", "言わさせないde", "もらいたい", "よ", "。"],
            "soal": ["説明", "同じ", "もらいたい", "言わさせないde", "さっき", "した", "こと", "も", "何度も", "それ", "だよ", "は", "よ", "を", "。", "。"]
        },
        {
            "id": 10,
            "pola": "Bagian 2: ～(さ)せてもらいたい・～(さ)せていただきたい・～(さ)せてほしい (Mengharap diizinkan melakukan sesuatu)",
            "kanji": "文化祭のポスターはわたしに作らせてほしいなあ。",
            "hiragana": "ぶんかさい の ぽすたー は わたし に つくらせて ほしい なあ 。",
            "arti": "Poster festival budaya, biarkan aku saja yang membuatnya.",
            "kunci": ["文化祭", "の", "ポスター", "は", "わたし", "に", "作らせて", "ほしい", "なあ", "。"],
            "soal": ["ポスター", "は", "作らせて", "文化祭", "わたし", "に", "ほしい", "なあ", "の", "。"]
        },
        {
            "id": 11,
            "pola": "Bagian 2: ～(さ)せてもらいたい・～(さ)せていただきたい・～(さ)せてほしい (Mengharap diizinkan melakukan sesuatu)",
            "kanji": "こんな暑い日に運動場で4時間も練習をさせないでほしいです。",
            "hiragana": "こんな あつい ひ に うんどうじょう で よじかん も れんしゅう を させないで ほしい です 。",
            "arti": "Di hari sepanas ini, saya harap tidak disuruh latihan sampai 4 jam di lapangan olahraga.",
            "kunci": ["こんな", "暑い", "日", "に", "運動場", "で", "4時間", "も", "練習", "を", "させないで", "ほしい", "です", "。"],
            "soal": ["暑い", "練習", "運動場", "4時間", "も", "させないで", "ほしい", "です", "こんな", "日", "に", "で", "を", "。"]
        },
        # === BAGIAN 3 ===
        {
            "id": 12,
            "pola": "Bagian 3: ～といい・～ばいい・～たらいい (Harapan / Saran)",
            "kanji": "このクラスも今日でお別れです。いつかまたみんなで会えるといいですね。",
            "hiragana": "この くらす も きょう で おわかれ です 。 いつか また みんな で あえる と いい です ね 。",
            "arti": "Kelas ini juga akan berpisah hari ini. Semoga suatu saat kita semua bisa bertemu lagi ya.",
            "kunci": ["この", "クラス", "も", "今日", "で", "お別れ", "です", "。", "いつか", "また", "みんな", "で", "会えると", "いいですね", "。"],
            "soal":
