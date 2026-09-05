import streamlit as st


st.set_page_config(page_title='Vương quốc mô hình', page_icon=':sparkles:')

with st.sidebar:
    st.title('Vương quốc mô hình')
    st.header('Chào mừng bạn đến Vương quốc mô hình!')
    st.image('https://static0.gamerantimages.com/wordpress/wp-content/uploads/2024/04/dragon-ball-super-season-2.jpg')
    st.write(
        'Chúng tôi chuyên bán các mô hình nhân vật hoạt hình chất lượng. '
        'Luôn cập nhật và đa dạng sản phẩm. '
        'Cam kết sự hài lòng của khách hàng với dịch vụ chuyên nghiệp. '
        'Hãy đến và khám phá thế giới mô hình tại Vương quốc mô hình!'
    )
    st.write(':house: Địa chỉ của hàng:')
    st.write(':phone: Điện thoại liên hệ')


st.title('Vương quốc mô hình')

col1, col2, col3 = st.columns(3)

with col1:
    b1 = st.button('Dragon Ball')
with col2:
    b2 = st.button('Naruto')
with col3:
    b3 = st.button('One Piece')

if b1:
    st.header('Danh sách mô hình Dragon Ball')
    col4, col5, col6 = st.columns(3)

    with col4:
        st.image(
            'https://wallpapers.com/images/hd/goku-blue-saiyan-form-dbz-4k-dnivqds6brxseuth.jpg',
            caption='Goku Ultra Instinct – Mã số: 001'
        )
    with col5:
        st.image(
            'https://wallpapercave.com/wp/wp2944958.png',
            caption='Vegeta Super Saiyan – Mã số: 002'
        )
    with col6:
        st.image(
            'https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/672266c8-4109-43f0-bab0-cf7674a30d15/width=1200/672266c8-4109-43f0-bab0-cf7674a30d15.jpeg',
            caption='Picolo – Mã số: 003'
        )


if b2:
    st.header('Danh sách mô hình Naruto')
    col4, col5, col6 = st.columns(3)

    with col4:
        st.image(
            'https://images5.alphacoders.com/413/413842.jpg',
            caption='Uzumaki Naruto – Mã số: 001'
        )
    with col5:
        st.image(
            'https://tse1.mm.bing.net/th/id/OIP.eBomVRyXor7E6AhwTdU24QHaEK?r=0&rs=1&pid=ImgDetMain&o=7&rm=3',
            caption='Uchiha Sasuke – Mã số: 002'
        )
    with col6:
        st.image(
            'https://motionbgs.com/media/5096/kakashi-hatake-naruto.jpg',
            caption='Hatake Kakashi – Mã số: 003'
        )

if b3:
    st.header('Danh sách mô hình One Piece')
    col4, col5, col6 = st.columns(3)

    with col4:
        st.image(
            'https://i.pinimg.com/originals/50/a8/bd/50a8bda8e3b4825cfdb6977c4d453515.jpg',
            caption='Monkey D. Luffy – Mã số: 001'
        )
    with col5:
        st.image(
            'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/0fac42de-c74e-4ac8-a1f0-fdc7dfcd7cf0/dg4zl0h-fd378982-446f-4a39-b721-04873098d5aa.jpg/v1/fill/w_1920,h_3400,q_75,strp/fanart_roronoa_zoro_painting_by_zlatanovitch_dg4zl0h-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzBmYWM0MmRlLWM3NGUtNGFjOC1hMWYwLWZkYzdkZmNkN2NmMFwvZGc0emwwaC1mZDM3ODk4Mi00NDZmLTRhMzktYjcyMS0wNDg3MzA5OGQ1YWEuanBnIiwiaGVpZ2h0IjoiPD0zNDAwIiwid2lkdGgiOiI8PTE5MjAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uud2F0ZXJtYXJrIl0sIndtayI6eyJwYXRoIjoiXC93bVwvMGZhYzQyZGUtYzc0ZS00YWM4LWExZjAtZmRjN2RmY2Q3Y2YwXC96bGF0YW5vdml0Y2gtNC5wbmciLCJvcGFjaXR5Ijo5NSwicHJvcG9ydGlvbnMiOjAuNDUsImdyYXZpdHkiOiJjZW50ZXIifX0.vT8KcM2amI6n9c3mAj345PMNvsGdFSPzRynZcCoDf44',
            caption='Roronoa Zoro – Mã số: 002'
        )
    with col6:
        st.image(
            'https://motionbgs.com/media/1115/sanji-smoking-one-piece.jpg',
            caption='Vinsmoke Sanji – Mã số: 003'
        )
st.header('Đặt hàng')

with st.form('Đơn đặt hàng'):
    
    topics = ('Dragon Ball', 'Naruto', 'One Piece')
    option_topic = st.selectbox('Chủ đề mô hình', topics)

    codes = ('001', '002', '003')
    option_code = st.selectbox('Mã số mô hình', codes)

    nums = st.slider('Số lượng bạn muốn đặt:', 0, 10, 0)

    name = st.text_input('Họ và tên')
    phone = st.text_input('Số điện thoại nhà riêng')

    submitted = st.form_submit_button('Xác nhận đặt hàng')

    if submitted:
        st.success(
            f"Bạn đã đặt {nums} mô hình {option_topic} (Mã số: {option_code}). "
            f"Khách hàng: {name}, SĐT: {phone}"
        )
    address = st.text_input('Địa chỉ giao hàng')

    bill = {
    'Loại mô hình:': option_topic,
    'Mã số:': option_code,
    'Số lượng:': nums,
    'Họ tên khách hàng:': name,
    'Số điện thoại liên hệ:': phone,
    'Địa chỉ giao hàng:': address
}

    submitted = st.form_submit_button("Xác nhận")

    if submitted:
        st.header('Bạn đã chọn:')
        for x, y in bill.items():
            st.write(x, y)
    
print_bill = st.checkbox('In hoá đơn')

if print_bill:
    ans = ''
    for x in bill:
        ans += str(x) + ' ' + str(bill[x]) + '\n'

    st.download_button('In hoá đơn', ans)