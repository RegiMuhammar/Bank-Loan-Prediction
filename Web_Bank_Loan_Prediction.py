import streamlit as st
from PIL import Image
import pickle

# Load Model
model = pickle.load(open('LRmodel.pkl', 'rb'))

def run():
    img1 = Image.open('bankloan.png')
    st.image(img1,use_column_width=False)
    st.title("Prediksi Pinjaman Bank dengan Algoritma Logistic Regression")

    ## Form Nomor Akun
    account_no = st.text_input('Nomor Akun')

    ## Form Nama Lengkap
    fn = st.text_input('Nama Lengkap')

    ## Form Jenis Kelamin
    gen_display = ('Perempuan','Laki-Laki')
    gen_options = list(range(len(gen_display)))
    gen = st.selectbox("Jenis Kelamin",gen_options, format_func=lambda x: gen_display[x])

    ## Form Status Pernikahan
    mar_display = ('Tidak','Ya')
    mar_options = list(range(len(mar_display)))
    mar = st.selectbox("Status Pernikahan", mar_options, format_func=lambda x: mar_display[x])

    ## Form Tanggungan
    dep_display = ('Tidak ada','1','2','Lebih dari 2')
    dep_options = list(range(len(dep_display)))
    dep = st.selectbox("Tanggungan",  dep_options, format_func=lambda x: dep_display[x])

    ## Form Status Pendidikan
    edu_display = ('Belum lulus','lulus')
    edu_options = list(range(len(edu_display)))
    edu = st.selectbox("Status Pendidikan",edu_options, format_func=lambda x: edu_display[x])

    ## Form Status Pekerjaan
    emp_display = ('Kerja','Berbisnis')
    emp_options = list(range(len(emp_display)))
    emp = st.selectbox("Status Kerja",emp_options, format_func=lambda x: emp_display[x])

    ## For Property status
    prop_display = ('Pedesaan','Semi-Kota','Kota')
    prop_options = list(range(len(prop_display)))
    prop = st.selectbox("Area Properti",prop_options, format_func=lambda x: prop_display[x])

    ## Form Credit Score
    cred_display = ('Antara 300 to 500','Above 500')
    cred_options = list(range(len(cred_display)))
    cred = st.selectbox("Credit Score",cred_options, format_func=lambda x: cred_display[x])

    ## Form Pendapatan Bulanan Pemohon($)
    mon_income = st.number_input("Pendapatan Bulanan Pemohon($)",value=0)

    ## Form Tambahan Pendapatan Bulanan Pemohon($)
    co_mon_income = st.number_input("Tambahan Pendapatan Bulanan Pemohon($)",value=0)

    ## Form Jumlah Pinjaman
    loan_amt = st.number_input("Jumlah Pinjaman",value=0)

    ## form durasi peminjaman
    dur_display = ['2 Bulan','6 Bulan','8 Bulan','1 Tahun','16 Bulan']
    dur_options = range(len(dur_display))
    dur = st.selectbox("Loan Duration",dur_options, format_func=lambda x: dur_display[x])

    if st.button("Submit"):
        duration = 0
        if dur == 0:
            duration = 60
        if dur == 1:
            duration = 180
        if dur == 2:
            duration = 240
        if dur == 3:
            duration = 360
        if dur == 4:
            duration = 480
        features = [[gen, mar, dep, edu, emp, mon_income, co_mon_income, loan_amt, duration, cred, prop]]
        print(features)
        prediction = model.predict(features)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        if ans == 0:
            st.error(
                "Halo: " + fn +" || "
                "Nomor Akun: "+account_no +' || '
                'Berdasarkan Kalkulasi kami, Kamu tidak akan mendapatkan pinjaman dari Bank'
            )
        else:
            st.success(
                "Halo: " + fn +" || "
                "Nomor Akun: "+account_no +' || '
                'Selamat!! Kamu akan mendapatkan pinjaman dari Bank'
            )

run()
