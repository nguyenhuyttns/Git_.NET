from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from SuyDienTien import *


# Tạo cửa sổ chương trình
win = Tk()
win.title("HỆ THỐNG SUY DIỄN NGÀNH THI")
win['bg'] = 'white'

# Kích thước cửa sổ
window_width = 962
window_height = 598
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
win.geometry(f'{window_width}x{window_height}+{x}+{y}')

# Đường dẫn đến file ảnh JFIF của bạn
image_path = "MainPicture.jfif"

# Mở và chuyển đổi ảnh sang định dạng hỗ trợ (ví dụ: PNG)
jfif_image = Image.open(image_path)
png_image = jfif_image.convert("RGB")
# Lưu ảnh dưới định dạng PNG
png_image.save("converted_image.png", format="PNG")  

# Tạo canvas để chứa hình ảnh nền
canvas = Canvas(win, width=window_width, height=window_height, bg='white')
canvas.pack()

# Tạo đối tượng PhotoImage từ ảnh đã chuyển đổi
background_image = ImageTk.PhotoImage(png_image)
canvas.create_image(window_width // 4, window_height // 1.6, image=background_image)

# Tạo header Label
header_text = "HỆ THỐNG SUY DIỄN NGÀNH THI"
header_label = Label(win, text=header_text, font=("Arial", 25), bg="white")
header_label.place(relx=0.5, rely=0.1, anchor=CENTER)

# Tạo một frame để chứa các button và combobox
border_frame = Frame(win, bg='white', highlightthickness=1, highlightbackground="black")
border_frame.place(relx=0.9, rely=0.3, anchor=NE)

# Thêm Label "Sở Thích Của Bạn" và Combobox vào border_frame
label_sothich_text = Label(border_frame, text="Sở Thích Của Bạn", bg='white')
label_sothich_text.grid(row=0, column=0, padx=5, pady=5, sticky=W)

sothich_options = [
    "Sáng tạo", 
    "Ứng dụng kỹ thuật",
    "Chơi nhạc", 
    "Đọc sách", 
    "Động vật",
    "Quản lý doanh nghiệp",
    "Đi du lịch",
    "Nấu ăn",
    "Học ngoại ngữ",
    "Giúp đỡ mọi người",
    "Làm việc với các con số",
    "Máy tính",
    "Ô tô",
    "Tranh luận",
    "Vẽ"
]

combo_sothich = ttk.Combobox(border_frame, values=sothich_options, width=30)
combo_sothich.grid(row=0, column=1, padx=5, pady=5, sticky=W)

# Thêm Label "Hoc luc cua ban" và Combobox vào border_frame
label_hocluc_text = Label(border_frame, text="Học lực của bạn", bg='white')
label_hocluc_text.grid(row=1, column=0, padx=5, pady=5, sticky=W)

hoc_luc_options = [
    "TB",
    "Khá",
    "Giỏi"
]

combo_hocluc = ttk.Combobox(border_frame, values=hoc_luc_options, width=30)
combo_hocluc.grid(row=1, column=1, padx=5, pady=5, sticky=W)

# Thêm Label "Chọn khối bạn muốn thi" và Combobox vào border_frame
label_khoi_text = Label(border_frame, text="Chọn khối bạn muốn thi", bg='white')
label_khoi_text.grid(row=2, column=0, padx=5, pady=5, sticky=W)

khoi_options = [
"Khối A",
"Khối A1",
"Khối B", 
"Khối C",
"Khối D",
"Các khối năng khiếu"
]

combo_khoi = ttk.Combobox(border_frame, values=khoi_options, width=30)
combo_khoi.grid(row=2, column=1, padx=5, pady=5, sticky=W)

# Thêm Label "Chọn nhom nghanh mong muon" và Combobox vào border_frame
label_nganh_text = Label(border_frame, text="Chọn nhóm ngành mong muốn", bg='white')
label_nganh_text.grid(row=3, column=0, padx=5, pady=5, sticky=W)

nganh_options = [
   "Pháp luật",
   "Nghệ thuật",
   "Báo chí và thông tin",
   "Kinh doanh và quản lý",
   "Khoa học tự nhiên",
   "Máy tính và công nghệ thông tin",
   "Công nghệ kỹ thuật",
   "Kiến trúc và xây dựng",
   "Nông, lâm nghiệp và thuỷ sản",
   "Sức khoẻ"
]

combo_nganh = ttk.Combobox(border_frame, values=nganh_options, width=30)
combo_nganh.grid(row=3, column=1, padx=5, pady=5, sticky=W)


# Thêm Button "Tư Vấn" và "Hủy" vào border_frame
def advice_action():
    pass

def reset_action():
    # Xóa lựa chọn trong các combobox
    combo_sothich.set('')
    combo_hocluc.set('')
    combo_khoi.set('')
    combo_nganh.set('')

button_advice = Button(border_frame, text="Tư Vấn", command=advice_action, width=12)
button_advice.grid(row=5, column=1, padx=(5, 20), pady=5, sticky=W)

button_reset = Button(border_frame, text="Reset", command=reset_action, width=12)
button_reset.grid(row=5, column=1, padx=(20, 5), pady=5, sticky=E)



# Tạo Label "KẾT QUẢ"
label_ketqua_text = Label(border_frame,text="KẾT QUẢ", font=("Arial", 18), bg="white")
label_ketqua_text.grid(row=6, column=0, padx=5, pady=5, sticky=W)

# Tạo ô văn bản
result_text = Text(border_frame, width=50, height=10)
result_text.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky=W)

# Tạo từ điển ánh xạ giữa giá trị và mã tương ứng
mapping_dict = {
    #Mã quy đổi sở thích
    "Sáng tạo"                : "ST1",
    "Ứng dụng kỹ thuật"       : "ST2",
    "Chơi nhạc"               : "ST3",
    "Đọc sách"                : "ST4",
    "Động vật"                : "ST5",
    "Quản lý doanh nghiệp"    : "ST6",
    "Đi du lịch"              : "ST7",
    "Nấu ăn"                  : "ST8",
    "Học ngoại ngữ"           : "ST9",
    "Giúp đỡ mọi người"       : "ST10",
    "Làm việc với các con số" : "ST11",
    "Máy tính"                : "ST12",
    "Ô tô"                    : "ST13",
    "Tranh luận"              : "ST14",
    "Vẽ"                      : "ST15",

    #Mã quy đổi khối thi
    "Khối A"                  : "K1",
    "Khối A1"                 : "K2",
    "Khối B"                  : "K3",
    "Khối C"                  : "K4",
    "Khối D"                  : "K5",
    "Các khối năng khiếu"     : "K6",

    #Mã quy đổi học lực
    "TB"                      : "HL2",
    "Khá"                     : "HL3",
    "Giỏi"                    : "HL4",

    #Mã quy đổi ngành nghề
    "Pháp luật"                         : "N1",
    "Nghệ thuật"                        : "N2",
    "Báo chí và thông tin"              : "N3",
    "Kinh doanh và quản lý"             : "N4",
    "Khoa học tự nhiên"                 : "N5",
    "Máy tính và công nghệ thông tin"   : "N6",
    "Công nghệ kỹ thuật"                : "N7",
    "Kiến trúc và xây dựng"             : "N8",
    "Nông, lâm nghiệp và thuỷ sản"      : "N9",
    "Sức khoẻ"                          : "N10",

    #Mã quy đổi ngành nghề kêt luận
    "Luật sư"                           : "KL1",
    "Mỹ thuật"                          : "KL2",
    "Diễn viên"                         : "KL3",
    "Thanh nhạc"                        : "KL4",
    "Nhiếp ảnh"                         : "KL5",
    "Báo chí"                           : "KL6",
    "Công nghệ truyền thông"            : "KL7",
    "Quản trị kinh doanh"               : "KL8",
    "Marketing"                         : "KL9",
    "Ngân hàng"                         : "KL10",
    "Kế toán"                           : "KL11",
    "Thiên văn học"                     : "KL12",
    "Vật lý học"                        : "KL13",
    "Hóa học"                           : "KL14",
    "Công nghệ thông tin"               : "KL15",
    "Công nghệ kĩ thuật cơ khí"         : "KL16",
    "Công nghệ kĩ thuật ô tô"           : "KL17",
    "Công nghệ kĩ thuật điện, điện tử"  : "KL18",
    "Kiến trúc"                         : "KL19",
    "Xây dựng"                          : "KL20",
    "Nông nghiệp"                       : "KL21",
    "Lâm nghiệp"                        : "KL22",
    "Thủy sản"                          : "KL23",
    "Y học"                             : "KL24"
}

def display_selected_info():
    sothich_selected = combo_sothich.get()
    hocluc_selected = combo_hocluc.get()
    khoi_selected = combo_khoi.get()
    nganh_selected = combo_nganh.get()

    if not (sothich_selected || hocluc_selected || khoi_selected || nganh_selected):
        messagebox.showwarning("Cảnh báo", "Bạn chưa chọn đủ thông tin.")
    else:
        sothich_mapped = mapping_dict.get(sothich_selected, sothich_selected)
        hocluc_mapped = mapping_dict.get(hocluc_selected, hocluc_selected)
        khoi_mapped = mapping_dict.get(khoi_selected, khoi_selected)
        nganh_mapped = mapping_dict.get(nganh_selected, nganh_selected)

        result_text.delete(1.0, END)
        result_text.insert(END, f"Sở thích: {sothich_mapped}\n")
        result_text.insert(END, f"Học lực: {hocluc_mapped}\n")
        result_text.insert(END, f"Khối thi: {khoi_mapped}\n")
        result_text.insert(END, f"Nhóm ngành muốn thi: {nganh_mapped}\n")

# Thêm button "Tư Vấn" và gọi hàm display_selected_info khi click
button_advice = Button(border_frame, text="Tư Vấn", command=display_selected_info, width=12)
button_advice.grid(row=5, column=1, padx=(5, 20), pady=5, sticky=W)



win.mainloop()
