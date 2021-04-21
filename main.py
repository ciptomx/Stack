import os

class Stack:
  def __init__(self):
    self.items = []
  def isEmpty(self):
    return self.items == []
  def push(self, item):
    self.items.append(item)
  def pop(self):
    return self.items.pop()
  def peek(self):
    return self.items[len(self.items)-1]
  def size(self):
    return len(self.items)

  #menu 
  def menu(self):
      pilih = "6"
      while (pilih == "6"):
          os.system("clear")
          print ("MENU UTAMA")
          print ("---------------------")
          print ("1. Push data")
          print ("2. Peek data")
          print ("3. Pop data")
          print ("4. Cek isi data Kosong")
          print ("5. Cek Panjang data")
          print ("6. Keluar")
          print ("---------------------")
          pilihan=str(input(("Silahkan pilih nomor menu : ")))
          if (pilihan=="1"):
            os.system("clear")
            data=str(input("Masukan data yang ingin ditambahkan : "))
            self.push(data)
            print ("Data "+data+" telah ditambahkan")
            x = input ("")
          elif(pilihan=="2"):
            os.system("clear")
            print ("Data terakhir adalah "+self.peek())
            x = input ("")
          elif(pilihan=="3"):
            os.system("clear")
            print ("Data "+self.pop()+" Sudah dihapus")
            x = input ("")
          elif(pilihan=="4"):
            os.system("clear")
            print (self.isEmpty())
            x = input ("")
          elif(pilihan=="5"):
            os.system("clear")
            print ("Jumlah data dalam stack adalah "+str(self.size()))
            x = input ("")
          else:
                pilih = "n"
if __name__ == "__main__":
  s=Stack()
  s.menu()