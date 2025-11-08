---
title: "Anggota & Peran"
source: "https://docs.cursor.com/id/account/teams/members"
language: "id"
language_name: "Indonesian"
---

# Anggota & Peran
Source: https://docs.cursor.com/id/account/teams/members

Kelola anggota tim dan peran

Tim Cursor punya tiga jenis peran:

<div id="roles">
  ## Peran
</div>

**Member** adalah peran default dengan akses ke fitur Pro-nya Cursor.

* Akses penuh ke fitur Pro Cursor
* Nggak punya akses ke pengaturan penagihan atau dashboard admin
* Bisa lihat pemakaian sendiri dan sisa budget berbasis penggunaan

**Admin** ngatur manajemen tim dan pengaturan keamanan.

* Akses penuh ke fitur Pro
* Tambah/hapus member, ubah peran, setup SSO
* Atur harga berbasis penggunaan dan batas pengeluaran
* Akses ke analitik tim

**Unpaid Admin** nge-manage tim tanpa pakai seat berbayar — ideal buat staf IT atau finance yang nggak butuh akses ke Cursor.

* Nggak ditagih, nggak dapat fitur Pro
* Kapabilitas administratif sama seperti Admin

<Info>Unpaid Admin butuh minimal satu user berbayar di tim.</Info>

<div id="role-comparison">
  ## Perbandingan Peran
</div>

<div className="full-width-table">
  | Kemampuan                | Member | Admin | Admin Tanpa Biaya |
  | ------------------------ | :----: | :---: | :---------------: |
  | Pakai fitur Cursor       |    ✓   |   ✓   |                   |
  | Undang member            |    ✓   |   ✓   |         ✓         |
  | Hapus member             |        |   ✓   |         ✓         |
  | Ubah peran pengguna      |        |   ✓   |         ✓         |
  | Dasbor admin             |        |   ✓   |         ✓         |
  | Konfigurasi SSO/Keamanan |        |   ✓   |         ✓         |
  | Kelola penagihan         |        |   ✓   |         ✓         |
  | Lihat analitik           |        |   ✓   |         ✓         |
  | Kelola akses             |        |   ✓   |         ✓         |
  | Atur kontrol penggunaan  |        |   ✓   |         ✓         |
  | Perlu kursi berbayar     |    ✓   |   ✓   |                   |
</div>

<div id="managing-members">
  ## Mengelola anggota
</div>

Semua anggota tim bisa mengundang orang lain. Saat ini undangan belum dibatasi.

<div id="add-member">
  ### Tambah anggota
</div>

Tambah anggota dengan tiga cara:

1. **Undangan email**

   * Klik `Invite Members`
   * Masukkan alamat email
   * Pengguna akan menerima undangan lewat email

2. **Tautan undangan**

   * Klik `Invite Members`
   * Salin `Invite Link`
   * Bagikan ke anggota tim

3. **SSO**
   * Konfigurasi SSO di [admin dashboard](/id/account/teams/sso)
   * Pengguna otomatis bergabung saat login menggunakan email SSO

<Warning>
  Tautan undangan memiliki masa berlaku yang panjang — siapa pun yang memiliki tautan tersebut bisa bergabung.
  Cabut tautannya atau gunakan [SSO](/id/account/teams/sso)
</Warning>

<div id="remove-member">
  ### Hapus anggota
</div>

Admin bisa menghapus anggota kapan saja lewat menu konteks → "Remove". Jika anggota sudah memakai kredit apa pun, kursinya tetap terpakai sampai akhir siklus penagihan.

<div id="change-role">
  ### Ubah peran
</div>

Admin bisa mengubah peran anggota lain dengan mengklik menu konteks lalu memilih opsi "Change role".<br />

Harus selalu ada setidaknya satu Admin dan satu anggota berbayar dalam tim.

## Keamanan & SSO

SAML 2.0 Single Sign-On (SSO) tersedia di paket Team. Fitur utamanya meliputi:

* Mengonfigurasi koneksi SSO ([pelajari lebih lanjut](/id/account/teams/sso))
* Menyiapkan verifikasi domain
* Pendaftaran pengguna otomatis
* Opsi penegakan SSO
* Integrasi penyedia identitas (Okta, dll.)

<Note>
  <p className="!mb-0">Verifikasi domain wajib untuk mengaktifkan SSO.</p>
</Note>

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=76608c26daf1f9ab2bbc2c4ccb156c0e" style={{ padding: `32px 64px`, backgroundColor: "#0c0c0c" }} data-og-width="802" width="802" data-og-height="440" height="440" data-path="images/account/sso-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=334dc1fc107338d19ec7b0052e7ea0e4 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=543b3d868c19960a5fb4c526d9895bd3 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a06655178ba10f6a72919e9f7d598191 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e280fc911306fe8d3b8e90b7221b0c11 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffd8f2c0168e2ac4f95431062b226021 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/sso-settings.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=1c17e4eac666b663d676ce874f1c4ba5 2500w" />
</Frame>

<div id="usage-controls">
  ## Kontrol Penggunaan
</div>

Buka pengaturan penggunaan buat:

* Mengaktifkan penagihan berbasis penggunaan
* Mengaktifkan model premium
* Mengatur perubahan khusus admin
* Menetapkan batas pengeluaran bulanan
* Memantau penggunaan seluruh tim

<Frame>
  <img src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e8149f830c27308af1bcc329c25e38b5" style={{ backgroundColor: "#0c0c0c" }} data-og-width="1668" width="1668" data-og-height="1160" height="1160" data-path="images/account/usage-based-pricing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bc308a967251694ad7b03189c1083c61 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ddc293e19fa993e65be8c09ced649b4f 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=3a4df7d48d75c6166ab215550a641ca6 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f9051947c802ae54fd964196c50a3701 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ed775e3e98611ead1b938aedaf917f11 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/account/usage-based-pricing.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b26f86bce94dc981d3cf71853a965374 2500w" />
</Frame>

<div id="billing">
  ## Penagihan
</div>

Saat nambah anggota tim:

* Setiap member atau admin nambah satu kursi berbayar (lihat [pricing](https://cursor.com/pricing))
* Member baru dikenai biaya pro-rata untuk sisa waktu di periode penagihan
* Kursi admin yang Unpaid nggak dihitung

Penambahan di tengah bulan cuma ditagih untuk hari yang dipakai. Kalau ngehapus member yang udah pakai kredit, kursinya tetap kepakai sampai akhir siklus penagihan — nggak ada refund pro-rata.

Perubahan role (mis., Admin ke Unpaid Admin) ngubah penagihan mulai dari tanggal perubahan. Pilih penagihan bulanan atau tahunan.

Perpanjangan bulanan/tahunan terjadi di tanggal pendaftaran awal, terlepas dari perubahan member.

<div id="switch-to-yearly-billing">
  ### Beralih ke penagihan tahunan
</div>

Hemat **20%** dengan beralih dari bulanan ke tahunan:

1. Buka [Dashboard](https://cursor.com/dashboard)
2. Di bagian akun, klik "Advanced" lalu "Upgrade to yearly billing"

<Note>
  Kamu cuma bisa beralih dari bulanan ke tahunan lewat dashboard. Untuk beralih dari
  tahunan ke bulanan, hubungi [hi@cursor.com](mailto:hi@cursor.com).
</Note>

---

← Previous: [Pengaturan Enterprise](./pengaturan-enterprise.md) | [Index](./index.md) | Next: [SCIM](./scim.md) →