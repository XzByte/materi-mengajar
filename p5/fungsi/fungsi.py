# cara buat function

# Deklarasikan dulu nama function seperti dibawah
def function_name():
    # lalu masukkan kode yang ingin dijalankan
    print("Hello, World!")
    
# lalu panggil function tersebut
function_name()


# kalo pake input, hampir sama, tinggal kasih parameter aja kayak dibawah
def function_name_with_input(input):
    print("Inputan kamu adalah : {}".format(input))
    
function_name_with_input("Hello, World!")


# kalo mau return value, tinggal tambahin return di functionnya
def function_name_with_return(input):
    return "Inputan kamu adalah : {}".format(input)
#panggil pake deklarasi print, input, ato di passing ke baris code sesuai kebutuhan
print(function_name_with_return("Hello, World!"))
