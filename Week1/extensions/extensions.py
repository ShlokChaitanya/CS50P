def main():
    usr_inp = input("File name: ").strip()
    print(get_media_type(usr_inp))


def get_media_type(file_name):
    media_types = {
        '.gif': 'image/gif',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.pdf': 'application/pdf',
        '.txt': 'text/plain',
        '.zip': 'application/zip'
    }
    file_extension = file_name.lower().split('.')[-1]
    return media_types.get('.' + file_extension, 'application/octet-stream')


main()
