import streamlit as st
from sklearn.linear_model import LinearRegression
import feedparser
import numpy as np

st.title("🎧 Entertainment and Health App")

menu = st.selectbox("📂 Chọn chức năng bạn muốn dùng:", [
    "🎤 Favorite music artist",
    "💤 Guessing sleeping hours",
    "📰 News",
    "💰 Gold price",
    "❤️ Health check",
    "🫀 Heartbeat",
    "💧 Lượng nước cần uống",
    "🚶‍♀️ Bước chân mỗi ngày",
    "🧠 DISC Test",
    "📈 Stock",
    "👌 Tư duy & Nội lực",
])

if menu == "🎤 Favorite music artist":
    st.sidebar.title("🎶 Music artist list")
    selected_artist = st.sidebar.radio("Choose a music artist:", ["Đen Vâu", "Hà Anh Tuấn", "Sơn Tùng M-TP"])

    videos = {
        "Đen Vâu": [
            ("Bữa ăn cho em", "https://www.youtube.com/watch?v=ukHK1GVyr0I"),
            ("Mang tiền về cho mẹ", "https://www.youtube.com/watch?v=UVbv-PJXm14"),
            ("Trời hôm nay nhiều mây cực!", "https://www.youtube.com/watch?v=MBaF0l-PcRY"),
            ("Hai triệu năm", "https://www.youtube.com/watch?v=LSMDNL4n0kM"),
            ("Trung Quân Idol", "https://www.youtube.com/watch?v=7MMiwZv0HzE&list=RD7MMiwZv0HzE&index=1")
        ],
        "Hà Anh Tuấn": [
            ("Tuyết rơi mùa hè", "https://www.youtube.com/watch?v=pTh3KCD7Euc"),
            ("Nước ngoài", "https://www.youtube.com/watch?v=pU3O9Lnp-Z0"),
            ("Tháng tư là lời nói dối của em", "https://www.youtube.com/watch?v=UCXao7aTDQM"),
            ("Xuân thì", "https://www.youtube.com/watch?v=3s1r_g_jXNs")
        ],
        "Sơn Tùng M-TP": [
            ("Lạc trôi", "https://www.youtube.com/watch?v=Llw9Q6akRo4"),
            ("Chúng ta không thuộc về nhau", "https://www.youtube.com/watch?v=qGRU3sRbaYw"),
            ("Muộn rồi mà sao còn", "https://www.youtube.com/watch?v=xypzmu5mMPY"),
            ("Hãy trao cho anh", "https://www.youtube.com/watch?v=knW7-x7Y7RE")
        ]
    }

    st.header(f"{selected_artist}'s music 🎵")
    for title, url in videos[selected_artist]:
        st.subheader(title)
        st.video(url)

elif menu == "💤 Guessing sleeping hours":
    st.title("🕘 Guessing the sleeping hours")
    x = [[10, 8, 1], [20, 6, 5], [25, 3, 8], [30, 2, 6], [50, 2, 2], [15, 9, 2], [40, 4, 3]]
    y = [10, 8, 6, 6, 5, 7, 9.5]
    model = LinearRegression()
    model.fit(x, y)
    st.write("Please enter your info:")
    age = st.number_input("Your age:", min_value=5, max_value=100, value=25)
    activity = st.slider("Physical activity level (1 = few, 10 = energetic)", 1, 10, 5)
    screen_time = st.number_input("Screen usage per day (hour)", min_value=0, max_value=24, value=6)
    if st.button("🥱 Guess the sleeping time"):
        input_data = [[age, activity, screen_time]]
        result = model.predict(input_data)[0]
        st.success(f"You should sleep {result:.1f} hour per night")
        if result < 6.5:
            st.warning("Maybe you need to sleep much to recover your health")
        elif result > 9:
            st.info("Maybe you are having physical activity hard - Sleep well is necessary to recover your body")
        else:
            st.success("Perfect sleeping time. Keep it going")

elif menu == "📰 News":
    st.header("The latest news from VnExpress")
    feed = feedparser.parse("https://vnexpress.net/rss/tin-moi-nhat.rss")
    for entry in feed.entries[:10]:
        st.subheader(entry.title)
        st.write(entry.published)
        st.write(entry.link)

elif menu == "💰 Gold price":
    st.header("💰 Cập nhật giá vàng từ Vietnamnet")
    feed = feedparser.parse("https://vietnamnet.vn/rss/kinh-doanh.rss")
    gold_news = [entry for entry in feed.entries if "vàng" in entry.title.lower() or "giá vàng" in entry.summary.lower()]
    if gold_news:
        for entry in gold_news[:5]:
            st.subheader(entry.title)
            st.write(entry.published)
            st.write(entry.link)
    else:
        st.warning("Không tìm thấy bản tin giá vàng gần đây.")

elif menu == "❤️ Health check":
    st.header("Kiểm tra chỉ số BMI của bạn ")
    can_nang = st.number_input("Nhập cân nặng của bạn  (kg)", min_value=10.0, max_value=200.0, value=60.0, step=0.1)
    chieu_cao = st.number_input("Nhập chiều cao của bạn (m)", min_value=1.0, max_value=2.5, value=1.7, step=0.01)
    if st.button("Tính BMI"):
        bmi = can_nang/(chieu_cao ** 2)
        st.success(f"chỉ số bmi của bạn là: {bmi: .2f}")
        if bmi < 18.5:
            st.warning("Bạn đang thiếu cân, nên ăn uống đầy đủ và dinh dưỡng hơn.")
        elif 18.5 <= bmi < 25:
            st.info("Bạn có cân nặng bình thường. Hãy tiếp tục duy trì lối sống lành mạnh.")
        elif 25 <= bmi < 30:
            st.warning("Bạn đang thừa cân. Nên cân đối chế độ ăn và tập thể dục.")
        else:
            st.error("Bạn đang béo phì. Nên gặp chuyên gia dinh dưỡng hoặc bác sĩ để được tư vấn.")

elif menu == "🫀 Heartbeat":
    st.header("Heartbeat check, are you need to meet a doctor?")
    x = np.array([[100, 2, 12], [95, 4, 15], [90, 6, 18], [85, 9, 20], [80, 12, 25],
                  [75, 20, 50], [72, 30, 65], [70, 40, 70], [68, 50, 75], [66, 58, 78],
                  [70, 65, 70], [75, 70, 68], [80, 75, 65], [85, 80, 60], [90, 85, 58]])
    y = np.array([1.2, 1.3, 1.5, 1.6, 1.7, 2.0, 2.3, 2.7, 3.0, 3.2, 3.5, 3.8, 4.0, 4.3, 4.6])
    model = LinearRegression()
    model.fit(x, y)
    st.subheader("Enter health information")
    hr = st.number_input("Heartbeat (bpm)", min_value=40, max_value=200, value=75)
    age = st.number_input("Age", min_value=1, max_value=120, value=30)
    weight = st.number_input("Weight (kg)", min_value=10.0, max_value=200.0, value=60.0)
    if st.button("Check"):
        score = model.predict([[hr, age, weight]])[0]
        st.success(f"chỉ số rủi ro: **{score: .2f}**")
        if score < 1.5:
            st.info("You're good. No need to meet a doctor.")
        elif score < 2.5:
            st.warning("Need to wait for a bit more time, rest and check again later.")
        elif score < 3.5:
            st.warning("You have some unusual points. Need some advice from the doctor.")
        else:
            st.error("High risk! Meet a doctor as soon as possible!")

elif menu == "💧 Lượng nước cần uống":
    st.title("Khuyến nghị lượng nước uống mỗi ngày")
    tuoi = st.number_input("Nhập tuổi của bạn:", min_value=1, max_value=100, value=18, step=1)
    if st.button("Kiểm tra lượng nước cần uống"):
        if tuoi < 4:
            st.info("Khuyến nghị: 1.3 lít/ngày")
        elif 4 <= tuoi <= 8:
            st.info("Khuyến nghị: 1.7 lít/ngày")
        elif 9 <= tuoi <= 13:
            st.info("Khuyến nghị: 2.1 đến 2.4 lít/ngày")
        elif 14 <= tuoi <= 18:
            st.info("Khuyến nghị: 2.3 đến 3.3 lít/ngày")
        elif 19 <= tuoi <= 50:
            st.info("Khuyến nghị: 2.7 lít/ngày đối với nữ, 3.7 lít/ngày đối với nam")
        elif tuoi > 50:
            st.info("Khuyến nghị: Khoảng 2.5 đến 3.0 lít/ngày (phụ thuộc vào sức khỏe và mức độ vận động)")
        else:
            st.warning("Vui lòng nhập độ tuổi hợp lệ.")

elif menu == "🚶‍♀️ Bước chân mỗi ngày":
    st.header("🚶‍♀️ Kiểm tra số bước đi phù hợp mỗi ngày")
    age2 = st.number_input("Nhập tuổi của bạn:", min_value=0.0, max_value=130.0, value=18.0, step=1.0)
    if st.button("Kiểm tra số bước"):
        st.success(f"Tuổi của bạn: {age2:.0f}")
        if age2 < 18:
            st.info("🔹 Bạn nên đi **12.000–15.000 bước** mỗi ngày.")
        elif 17 < age2 <= 39:
            st.info("🔹 Bạn nên đi **8.000–10.000 bước** mỗi ngày.")
        elif 39 < age2 <= 64:
            st.warning("🔸 Bạn nên đi **7.000–9.000 bước** mỗi ngày.")
        elif age2 > 64:
            st.warning("🔸 Bạn nên đi **6.000–8.000 bước** mỗi ngày.")
        else:
            st.error("⚠️ Có lỗi xảy ra. Vui lòng kiểm tra lại thông tin.")

elif menu == "🧠 DISC Test":
    st.header("Kiểm tra tính cách theo DISC")
    st.markdown("Chọn một mô tả đúng nhất và một mô tả ít đúng nhất trong từng nhóm")
    groups = [
        {"D": "Tôi quyết đoán và thích kiểm soát", "I": "Tôi thích thân thiện và nói chuyện dễ dàng", "S": "Tôi kiên nhẫn và đáng tin cậy", "C": "Tôi chính xác và có hệ thống"},
        {"D": "Tôi thích thử thách và hành động nhanh", "I": "Tôi tràn đầy năng lượng và lạc quan", "S": "Tôi ổn định và hỗ trợ người khác", "C": "Tôi làm việc theo quy tắc rõ ràng"},
        {"D": "Tôi thích kiểm soát kết quả", "I": "Tôi thích được công nhận", "S": "Tôi ưu tiên sự hài hòa", "C": "Tôi chú ý đến việc chi tiết và phân tích"}
    ]
    scores = {"D": 0, "I": 0, "S": 0, "C": 0}
    for idx, group in enumerate(groups):
        st.markdown(f"### nhóm {idx + 1}")
        options = list(group.values())
        most = st.radio("Mô tả đúng nhất với bạn ", options, key=f"most_{idx}")
        least = st.radio("Mô tả ít đúng nhất với bạn ", options, key=f"least_{idx}")
        for key, val in group.items():
            if val == most:
                scores[key] += 1
            if val == least:
                scores[key] -= 1
    if st.button("Xem kết quả DISC"):
        st.header(" Kết quả của bạn ")
        max_type = max(scores, key=scores.get)
        for style, score in scores.items():
            st.write(f"{style}: {score} điểm ")
        st.markdown(f"Tính nổi bật nhất của bạn là: {max_type}**")
        descriptions = {
            "D": "Quyết đoán, định hướng kết quả và thích kiểm soát",
            "I": "Giao tiếp tốt, tràn đầy năng lượng và truyền cảm hứng",
            "S": "Kiên nhẫn, đáng tin cậy và hỗ trợ người khác",
            "C": "Chính xác, tuân thủ quy trình và thích phân tích logic"
        }
        st.info(descriptions[max_type])
        st.markdown("-----")
        st.markdown("Mô tả chi tiết các nhóm DISC")
        st.markdown("""
            - **D (Dominance)**: Người lãnh đạo, chủ động, thích cạnh tranh. Ví dụ: CEO, nhà sáng lập.  
            - **I (Influence)**: Người truyền cảm hứng, thích giao tiếp, có sức hút. Ví dụ: người làm marketing, diễn giả.  
            - **S (Steadiness)**: Người hỗ trợ, trung thành, kiên nhẫn. Ví dụ: giáo viên, điều dưỡng.  
            - **C (Conscientiousness)**: Người phân tích, tỉ mỉ, theo quy trình. Ví dụ: kế toán, kỹ sư.
        """)
        st.caption("Đây chỉ là bài tham khảo về chỉ số DISC")
elif menu == "📈 Stock":
    st.header("📈 Kinh tế vĩ mô & Giá hàng hóa")

    st.markdown("### 🌐 Tỷ giá & Lãi suất (Việt Nam)")
    st.markdown("[Vietstock - Tỷ giá & Lãi suất](https://finance.vietstock.vn/du-lieu-vi-mo/53-64/ty-gia-lai-suat.htm)")

    st.markdown("### 🏗️ Giá thép")
    st.markdown("[TradingEconomics - Steel](https://tradingeconomics.com/commodity/steel)")

    st.markdown("### ⛽ Baltic Clean Tanker Index (vận tải dầu)")
    st.markdown("[Investing - Baltic Clean Tanker Index](https://vn.investing.com/indices/baltic-clean-tanker-chart)")

    st.markdown("### 📦 Baltic Dry Index (vận tải hàng rời)")
    st.markdown("[TradingEconomics - Baltic Exchange Dry Index](https://tradingeconomics.com/commodity/baltic)")
elif menu == "👌 Tư duy & Nội lực":
    st.header("Tư duy & Nội lực")

    items = [
        ("Khi nội lực chưa đủ", "nhìn đâu cũng thấy khó khăn."),
        ("Nóng nảy", "là do sức lực không đủ."),
        ("Sợ hãi", "là do tưởng tượng quá nhiều."),
        ("Lo lắng", "là do tư duy mập mờ."),
        ("Áp lực", "là do tầm nhìn hạn hẹp."),
        ("Hoảng loạn", "là do chuẩn bị không đủ."),
        ("Nhẹ dạ", "là do thiếu sự rèn luyện."),
    ]

    st.markdown("### Nhận định")
    for cause, effect in items:
        st.markdown(f"- **{cause}** → {effect}")

    st.divider()
    st.caption("Góc nhìn tham khảo nhằm tự nhận thức và rèn luyện bản thân.")    



