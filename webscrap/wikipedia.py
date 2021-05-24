class WikiPedia(object):
    url = ''

    def __str__(self):
        return self.url

    @staticmethod
    def main():
        while 1:
            menu = int(input("0.Exit 1.Insert 2.print"))
            if menu == 0:
                break
            elif menu == 1:
                Wiki = WikiPedia(input("insert:"))
            elif menu == 2:
                print(f"insert print:{Wiki}")
            else:
                print("wrong number")
                continue
WikiPedia.main()