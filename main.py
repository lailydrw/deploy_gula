import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive

# gauth=GoogleAuth()
# gauth.LocalWebserverAuth()

st.set_page_config(
    page_title = 'Analisis Harga Gula'
    # ,layout='wide'
)

st.title("Analisis Perubahan Harga Gula di Indonesia")
st.markdown("Oleh : **Laily Dwi Retno Wahyuningtias**")
st.markdown("20 Februari 2024")
from PIL import Image

# image = Image.open("./folder_datasets/Capture.PNG")
# st.image(
#     image,
#     caption="Gula"
# )

st.write("""Harga gula menjadi perhatian utama di pasar global akhir tahun 2023. Kenaikan harga yang signifikan telah menjadi topik hangat di kalangan pelaku industri dan konsumen. Bahkan dalam [berita](https://www.cnbcindonesia.com/news/20231107154758-4-487099/siap-siap-harga-gula-terbang-ke-rp18000-ini-biang-keroknya) yang dilansir dalam lama CNBC dikatakan bahwa harga gula akan mencapai angka Rp18.000,00. Tren naik ini tidak hanya mencerminkan dinamika pasar gula yang kompleks, tetapi juga memiliki dampak yang luas pada berbagai sektor ekonomi dan kehidupan sehari-hari.""")
st.write("""Grafik kurva harga gula nasional memberikan pandangan terhadap tren pergerakan harga gula di Jawa Timur, yang merupakan penghasil gula terbesar di Indonesia. Melalui data yang diperoleh dari siskaperbapo.jatimprov.go.id, dapat ditunjukkan gambaran tentang fluktuasi harga gula nasional sebagai berikut.""")

# harga_gula = r'C:\Users\hp\dqlab\belajar_streamlit\harga.csv'
harga = pd.read_csv('./folder_datasets/harga.csv')

plt.plot(harga['tanggal'], harga['harga_gula_nasional'])
plt.xlabel('tanggal')
plt.ylabel('Rp')
plt.xticks(rotation=90)
plt.title("Grafik Perubahan Harga Gula Nasional")
st.pyplot(plt)
st.markdown("*sumber : siskaperbapo.jatimprov.go.id*")

st.write("""Kenaikan harga gula bisa dipicu oleh berbagai faktor kompleks. Beberapa diantaranya yaitu perubahan kondisi cuaca dan kondisi ekonomi global. Perubahan kondisi cuaca ekstrem seperti kekeringan atau banjir dapat mengganggu produksi tebu. Berikut adalah grafik curah hujan (mm) yang terjadi antara bulan Oktober dan November tahun 2023 silam.""")

# cuaca_malang = r'C:\Users\hp\dqlab\belajar_streamlit\cuaca_malang.csv'
cuaca = pd.read_csv('./folder_datasets/cuaca_malang.csv')

st.markdown("**Grafik Curah Hujan di Kabupaten Malang**")

fig=plt.figure()
plt.plot(cuaca['tanggal'], cuaca['curah_hujan'])
plt.xlabel('tanggal')
plt.ylabel('mm')
plt.xticks(rotation=90)
st.pyplot(fig)

st.markdown("*sumber : dataonline.bmkg.go.id*")

# harga_cuaca = r'C:\Users\hp\dqlab\belajar_streamlit\harga_cuaca.csv'
# gabungan_harga_cuaca = pd.read_csv('./folder_datasets/harga_cuaca.csv')

st.write("""Grafik di atas menunjukkan bahwa curah hujan yang terjadi pada awal bulan November menjadi salah satu faktor penyebab naiknya harga gula. Jika terjadi banjir maka mengakibatkan produksi gula terganggu, terutama jika daerah pertanian tebu atau gula terkena dampaknya. Gangguan ini dapat mengurangi pasokan gula di pasar dan meningkatkan harga.""")

st.write("""Tidak hanya kondisi cuaca ekstrim yang menjadi faktor naiknya harga gula, tetapi kondisi ekonomi global juga berpengaruh. Kenaikan harga gula di Indonesia dan kenaikan harga gula di pasar internasional juga memiliki hubungan yang sangat kompleks dan saling terkait. Walaupun Jawa Timur adalah penghasil gula terbesar di Indonesia, namun Indonesia tetap menjadi salah satu negara yang cukup bergantung pada import gula untuk memenuhi kebutuhan domestiknya. Jika harga gula di pasar internasional naik, maka dapat berdampak langsung pada harga gula di Indonesia karena biaya import menjadi lebih tinggi.""")

col1, col2 = st.columns(2)

with col1:
    fig=plt.figure()
    plt.plot(harga['tanggal'], harga['harga_gula_nasional'])
    plt.xlabel('tanggal')
    plt.ylabel('Rp')
    plt.xticks(rotation=90)
    plt.title("Grafik Perubahan Harga Gula Nasional")
    st.pyplot(fig)   

with col2:
    fig=plt.figure()
    plt.plot(harga['tanggal'], harga['harga_gula_internasional'])
    plt.xlabel('tanggal')
    plt.ylabel('USD/ton')
    plt.xticks(rotation=90)
    plt.title("Grafik Perubahan Harga Gula Internasional")
    st.pyplot(fig)

st.write("""Berdasarkan grafik di atas, dapat dikatakan bahwa kenaikan harga gula di Indonesia dan kenaikan harga gula di pasar internasional saling berdampak, dan dapat mempengaruhi stabilitas harga gula di dalam negeri.""")
st.subheader("Saran dan Kesimpulan")
st.write("Berdasarkan pembahasan di atas dapat diberikan saran sebagai berikut:")
st.markdown("""
    * Pemerintah dan pelaku industri gula dapat mempertimbangkan diversifikasi sumber gula untuk mengurangi ketergantungan pada impor gula. Ini dapat dilakukan dengan mempromosikan pengembangan sumber gula alternatif atau meningkatkan efisiensi produksi gula dalam negeri.
    * Investasi dalam infrastruktur pertanian, termasuk irigasi dan sistem perlindungan tanaman, serta penerapan teknologi modern dalam produksi gula dapat membantu mengurangi dampak buruk dari kondisi cuaca ekstrem dan meningkatkan produktivitas.
    * Pemerintah dapat mengadopsi kebijakan yang bertujuan untuk menjaga stabilitas harga gula dalam negeri, termasuk mekanisme subsidi atau intervensi pasar untuk mencegah lonjakan harga yang tiba-tiba.
""")
st.write("**Kesimpulan**")
st.write("""Fluktuasi harga gula merupakan masalah kompleks yang dipengaruhi oleh berbagai faktor, termasuk kondisi cuaca, kondisi ekonomi global, dan ketergantungan pada impor. Kenaikan harga gula tidak hanya mempengaruhi pelaku industri, tetapi juga masyarakat umum dalam kehidupan sehari-hari. Oleh karena itu, diperlukan kerja sama antara pemerintah, pelaku industri, dan masyarakat untuk menghadapi tantangan ini dengan cara yang efektif, termasuk melalui diversifikasi sumber gula, penguatan infrastruktur, dan kebijakan harga yang stabil.""")

st.markdown("**Referensi**")
st.markdown("""
    1. siskaperbapo.jatimprov.go.id
    2. dataonline.bmkg.go.id
    3. databoks.katadata.co.id
    4. https://www.cnbcindonesia.com/news/20231107154758-4-487099/siap-siap-harga-gula-terbang-ke-rp18000-ini-biang-keroknya
""")