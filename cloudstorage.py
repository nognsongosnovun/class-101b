import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token = 'sl.BBNyUswxRCBHq0hLDJ5O8-l9zPT-9llWJ_xww1g4CgPXt9PkqLL7iqtapfkIaLMkHcMtFcFeNZ0JdBHF7GP4TASzyj1lTqUn_7BG9fn-jbqF8tkW92IaDhoJUJL8CI2sLOJiJmk'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the full path to upload to dropbox: ")

    transferData.upload_file(file_from,file_to)
    print("File has been moved !!!!!!!")

main()
           
