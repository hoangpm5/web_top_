import streamlit as st

st.set_page_config(page_title='Vương quốc mô hình', page_icon=':sparkles:')

with st.sidebar:
    st.title('Vương quốc mô hình')
    st.header('Chào mừng bạn đến Vương quốc mô hình!')
    st.image('https://www.ffcollectibles.com.au/cdn/shop/products/G5STUDIOHIGHENDCUSTOMSERIESTHELIFEOFNARUTOUZUMAKI_2.jpg?v=1689176734&width=823')
    st.write('Chúng tôi chuyên bán các mô hình nhân vật hoạt hình chất lượng. Luôn cập nhật và đa dạng sản phẩm. Cam kết sự hài lòng của khách hàng với dịch vụ chuyên nghiệp. Hãy đến và khám phá thế giới mô hình tại Vương quốc mô hình!')
    st.write(':house: Địa chỉ cửa hàng:')
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
        st.image('https://down-vn.img.susercontent.com/file/vn-11134207-7r98o-lsdslu36a36h7f',
                 caption='Goku Ultra Instinct - Mã số: 001')
    with col5:
        st.image('https://down-vn.img.susercontent.com/file/vn-11134207-7r98o-loh3k7kzcann52',
                 caption='Vegeta Super Saiyan - Mã số: 002')
    with col6:
        st.image('https://cf.shopee.vn/file/95ea723ffda3f1e0ea26bb626b9fdf13', caption='Picolo - Mã số: 003')
if b3:
    st.header('Danh sách mô hình One Piece')
    col4, col5, col6 = st.columns(3)
    with col4:
        st.image('https://www.animehouse.co.nz/cdn/shop/products/one-piece-luffy_952x952.png?v=1657677405', caption='Monkey D. Luffy - Mã số: 001')
    with col5:
        st.image('https://www.cyrenanime.com/storage/product-photos/59/roronoa-zoro-859.jpg', caption='Roronoa Zoro - Mã số: 002')
    with col6:
        st.image('https://image.made-in-china.com/202f0j00kvwhFcTIlofO/New-Arrived-2-Gk-Fight-Vinsmoke-Sanji-One-Piece-Wholesale-Japanese-Anime-Figure-Toy-Model.webp', caption='Vinsmoke Sanji - Mã số: 003')
st.header('Đặt hàng')
with st.form('Đơn đặt hàng'):

    topics = ('Dragon Ball', 'Naruto', 'One Piece')
    option_topic = st.selectbox('Chủ đề mô hình', topics)

    codes = ('001', '002', '003')
    option_code = st.selectbox('Mã số mô hình', codes)

    nums = st.slider('Số lượng bạn muốn đặt:', 0, 10, 0)

    name = st.text_input('Họ và tên')

    phone = st.text_input('Số điện thoại nhà riêng')
    address = st.text_input('Địa chỉ giao hàng')

    bill = {'Loại mô hình:': option_topic, 'Mã số:': option_code, 'Số lượng:': nums,
            'Họ tên khách hàng:': name, 'Số điện thoại liên hệ:': phone, 'Địa chỉ giao hàng:': address}

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