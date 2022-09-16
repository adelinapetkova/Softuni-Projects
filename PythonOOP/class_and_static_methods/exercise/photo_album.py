class PhotoAlbum:
    def __init__(self, pages:int):
        self.pages=pages
        self.photos=[[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        if not photos_count%4==0:
            pages=photos_count//4 + 1
        else:
            pages=photos_count//4

        return cls(pages)

    def add_photo(self, label: str):
        for page in range(self.pages):
            if not len(self.photos[page])==4:
                self.photos[page].append(label)
                return f"{label} photo added successfully on page {page+1} slot {len(self.photos[page])}"

        return "No more free slots"

    def display(self):
        info="-----------"
        for page in range(self.pages):
            current_page=[]
            for i in range(len(self.photos[page])):
                current_page.append('[]')
            while len(current_page)<4:
                current_page.append(" ")
            if "[]" not in current_page:
                info+='\n'
            else:
                info += f"\n{' '.join(current_page)}"
            info+="\n-----------"

        return info


album = PhotoAlbum(3)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.add_photo("prom"))
print(album.add_photo("prom"))
print(album.display())